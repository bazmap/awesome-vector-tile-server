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
            <th>Usage</th>
        </tr>
    </thead>
    <tbody>\n"""


    tile_server_data.sort(key=lambda item: (item["provider"], item["name"]))


    for tile_server in tile_server_data:

        if (
            not tile_server.get("name")
            or not tile_server.get("server-url")
            or not tile_server.get("server-url").get("url")
        ):
            continue

        # Provider
        srv_provider = tile_server.get("provider")

        # Name
        srv_name = tile_server.get("name")

        # Description + Metadata URL + attribution
        srv_desc = tile_server.get("description", "")

        if (
            tile_server.get("metadata-url")
            and tile_server.get("metadata-url").get("url")
        ):
            if srv_desc != "":
                srv_desc += "<br />"

            srv_desc += "<a href='" + tile_server.get("metadata-url").get("url") + "' title='" + tile_server.get("metadata-url").get("url") + "' target='_blank'>ℹ️ Metadata" + "</a>"

        if tile_server.get("attribution"):
            if srv_desc != "":
                srv_desc += "<br />"

            srv_desc += "Attribution : <code>" + tile_server.get("attribution") + "</code>"

        # URL
        srv_url = "<a href='" + tile_server.get("server-url").get("url") + "' title='Tile server url"

        if "active" not in tile_server["server-url"]:
            srv_url += " (url not tested)"
        elif tile_server["server-url"]["active"]:
            srv_url += " (url is active)"
        else:
            srv_url += " (url is not active)"

        srv_url += "' target='_blank'>" + tile_server.get("server-url").get("url")

        srv_url += "</a>"

        if "active" not in tile_server["server-url"]:
            srv_url += "⚫"
        elif tile_server["server-url"]["active"]:
            srv_url += "🟢"
        else:
            srv_url += "🔴"


        # Styles
        srv_styles = "<ul>"
        if tile_server.get("styles"):
            for style in tile_server["styles"]:
                if (
                    style.get("style-url")
                    and style.get("style-url").get("url")
                ):
                    srv_styles += "<li><a href='" + style.get("style-url").get("url") + "' title='Tile style url"

                    if "active" not in style["style-url"]:
                        srv_styles += " (url not tested)"
                    elif style["style-url"]["active"]:
                        srv_styles += " (url is active)"
                    else:
                        srv_styles += " (url is not active)"

                    srv_styles += "' target='_blank'>" + style.get("name", "N/A")

                    srv_styles += "</a>"

                    if "active" not in style["style-url"]:
                        srv_styles += "⚫"
                    elif style["style-url"]["active"]:
                        srv_styles += "🟢"
                    else:
                        srv_styles += "🔴"

                    if (
                        style.get("metadata-url")
                        and style.get("metadata-url").get("url")
                    ):
                        srv_styles += " - <a href='" + style.get("metadata-url").get("url") + "' title='" + style.get("metadata-url").get("url") + "' target='_blank'>ℹ️ Infos" + "</a>"

                    srv_styles += "</li>"

        srv_styles += "</ul>"

        # Coverage
        srv_coverage = tile_server.get("coverage")

        # Usage
        srv_usage = tile_server.get("usage")



        # Generate table row
        html_table += "        <tr>\n"
        html_table += f"            <td>{srv_provider}</td>\n"
        html_table += f"            <td>{srv_name}</td>\n"
        html_table += f"            <td>{srv_desc}</td>\n"
        html_table += f"            <td>{srv_url}</td>\n"
        html_table += f"            <td>{srv_styles}</td>\n"
        html_table += f"            <td>{srv_coverage}</td>\n"
        html_table += f"            <td>{srv_usage}</td>\n"
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
    list_file = os.path.join(current_directory, '../../', list_file)
    readme_file = os.path.join(current_directory, '../../', readme_file)



    with open(list_file, "r", encoding='utf-8') as f:
        tile_server_data = json.load(f)

    with open(readme_file, "r", encoding='utf-8') as f:
        readme_data = f.read()

    table_list = create_html_table(tile_server_data)

    modified_readme = modify_readme(readme_data, table_list)

    with open(readme_file, "w", encoding='utf-8') as f:
        f.write(modified_readme)