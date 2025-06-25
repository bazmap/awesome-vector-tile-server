import os
import json
import re


def create_html_table(tile_server_data):
    html_table = """<table>
    <thead>
        <tr>
            <th>Provider</th>
            <th>Name</th>
            <th>Description</th>
            <th>URL</th>
            <th>Styles</th>
            <th>Coverage</th>
        </tr>
    </thead>
    <tbody>\n"""


    tile_server_data.sort(key=lambda item: (item["provider"], item["name"]))


    for tile_server in tile_server_data:

        if (
            tile_server["name"] is None
            or tile_server["name"] == ""
            or tile_server["metadata-url"]["url"] is None
            or tile_server["metadata-url"]["url"] == ""
        ):
            continue

        # Provider
        srv_provider = tile_server.get("provider", "N/A")

        # Name
        srv_name = tile_server.get("name", "N/A")

        # Description + Metadata URL + attribution
        srv_desc = tile_server.get("description", "N/A")
        if tile_server["metadata-url"]["url"] is not None:
            srv_desc += "<br /><a href='" + tile_server.get("metadata-url").get("url") + "' title='" + tile_server.get("metadata-url").get("url")

            if tile_server["metadata-url"]["active"]:
                srv_desc += " (url is active)"
            else:
                srv_desc += " (url is not active)"

            srv_desc += "' target='_blank'>Metadata "

            if tile_server["metadata-url"]["active"]:
                srv_desc += "🟢"
            else:
                srv_desc += "🔴"

            srv_desc += "</a>"

        if tile_server["attribution"] is not None:
            srv_desc += "<br />Attribution : <code>" + tile_server.get("attribution") + "</code>"

        # URL
        srv_url = ""
        if tile_server["server-url"]["url"] is not None:
            srv_url += "<a href='" + tile_server.get("server-url").get("url") + "' title='Tile server url"

            if tile_server["server-url"]["active"]:
                srv_url += " (url is active)"
            else:
                srv_url += " (url is not active)"

            srv_url += "' target='_blank'>" + tile_server.get("server-url").get("url")

            if tile_server["server-url"]["active"]:
                srv_url += "🟢"
            else:
                srv_url += "🔴"

            srv_url += "</a>"

        # Styles
        srv_styles = "<ul>"
        if tile_server["styles"] is not None:
            for style in tile_server["styles"]:
                if style["style-url"] is not None:
                    srv_styles += "<li><a href='" + style.get("style-url").get("url") + "' title='Tile server url"

                    if style["style-url"]["active"]:
                        srv_styles += " (url is active)"
                    else:
                        srv_styles += " (url is not active)"

                    srv_styles += "' target='_blank'>" + style.get("name", "N/A")

                    if style["style-url"]["active"]:
                        srv_styles += "🟢"
                    else:
                        srv_styles += "🔴"

                    srv_styles += "</a></li>"

        srv_styles += "</ul>"

        # Coverage
        srv_coverage = tile_server.get("coverage", "N/A")



        # Generate table row
        html_table += "        <tr>\n"
        html_table += f"            <td>{srv_provider}</td>\n"
        html_table += f"            <td>{srv_name}</td>\n"
        html_table += f"            <td>{srv_desc}</td>\n"
        html_table += f"            <td>{srv_url}</td>\n"
        html_table += f"            <td>{srv_styles}</td>\n"
        html_table += f"            <td>{srv_coverage}</td>\n"
        html_table += "        </tr>\n"


    html_table += "    </tbody>\n</table>"

    return html_table



def modify_readme(readme_file, table_list):
    pattern = r'(<!--START of the curated list-->)(.*?)(<!--END of the curated list-->)'
    replacement = r'\1\n' + table_list + r'\n\3'
    return re.sub(pattern, replacement, readme_data, flags=re.DOTALL)



if __name__ == "__main__":

    # File
    list_file = "vector-tile-server-list.json"
    readme_file = "readme.md"

    # Current script place
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Path to the file
    list_file = os.path.join(current_directory, '../', list_file)
    readme_file = os.path.join(current_directory, '../', readme_file)



    with open(list_file, "r", encoding='utf-8') as f:
        tile_server_data = json.load(f)

    with open(readme_file, "r", encoding='utf-8') as f:
        readme_data = f.read()

    table_list = create_html_table(tile_server_data)

    modified_readme = modify_readme(readme_data, table_list)

    with open(readme_file, "w", encoding='utf-8') as f:
        f.write(modified_readme)