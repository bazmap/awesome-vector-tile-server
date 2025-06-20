const map = new maplibregl.Map({
	container: 'map',
	style: 'https://openmaptiles.data.gouv.fr/styles/fiord-color/style.json',
	center: [6.14997, 46.20222],
	zoom: 14,
	hash: true
});



const inspectControl = new MaplibreInspect({
	showInspectMap: false,
	showMapPopup: false,
	showMapInspectButton: false // on utilise notre propre bouton
});

map.addControl(inspectControl, 'top-right');

const nav = new maplibregl.NavigationControl({
	visualizePitch: true,
	visualizeRoll: true,
	showZoom: true,
	showCompass: true
});

map.addControl(nav, 'top-left');