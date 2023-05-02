<h1 align="center">Python and Folium Map</h1>
<p align="center">
  <a href="https://github.com/gpalve/python-folium-map/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/gpalve/python-folium-map"></a>
  <a href="https://github.com/gpalve/python-folium-map/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/gpalve/python-folium-map"></a>
  <a href="https://github.com/gpalve/python-folium-map/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/gpalve/python-folium-map"></a>
  <a href="https://github.com/gpalve/python-folium-map/blob/master/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/gpalve/python-folium-map"></a>
</p>

<p align="center">
  <strong>Python and Folium Map</strong> is a basic building block for Python and Folium map project.
</p>

<h2>Installation</h2>

<ol>
  <li>Clone the repository:</li>
</ol>

<pre><code>git clone https://github.com/gpalve/python-folium-map.git</code></pre>

<ol start="2">
  <li>Install the required Python packages:</li>
</ol>

<pre><code>pip install -r requirements.txt</code></pre>

<h2>Usage</h2>

<ol>
  <li>Import the <code>folium</code> module:</li>
</ol>

<pre><code>import folium</code></pre>

<ol start="2">
  <li>Create a <code>Map</code> object:</li>
</ol>

<pre><code>map = folium.Map(location=[37.7749, -122.4194], zoom_start=12)</code></pre>

<ol start="3">
  <li>Add markers to the map:</li>
</ol>

<pre><code>folium.Marker(location=[37.7749, -122.4194], tooltip='San Francisco').add_to(map)</code></pre>

<p>You can customize the marker icon and tooltip text by passing additional parameters to the <code>Marker</code> method. For example, to use a custom icon:</p>

<pre><code>icon_url = 'https://www.iconsdb.com/icons/preview/red/marker-2-xxl.png'
icon = folium.features.CustomIcon(icon_url, icon_size=(50, 50))
folium.Marker(location=[37.7749, -122.4194], tooltip='San Francisco', icon=icon).add_to(map)</code></pre>

<p>To add a line between two points on the map:</p>

<pre><code>points = [[37.7749, -122.4194], [37.3382, -121.8863]]
folium.PolyLine(points, color='red', weight=5, opacity=0.7).add_to(map)</code></pre>

<p>You can also add other types of markers and shapes to the map, such as circles, polygons, and GeoJSON layers. Refer to the <a href="https://python-visualization.github.io/folium/">Folium documentation</a> for more information.</p>

<h2>License</h2>

<p>Python and Folium Map is distributed



<img src="https://raw.githubusercontent.com/gpalve/python-folium-map/main/folium-map.png" />
