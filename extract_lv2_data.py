#!/usr/bin/env python3

import lilv
import json
import shutil
import os

world = lilv.World()
modgui = lilv.Namespace(world, "http://moddevices.com/ns/modgui#")
world.load_all()

plugins = []

def get_first(list):
	for i in list:
		return i
	return None

def get_first_value(p, ns):
	return get_first(p.get_value(ns))

def to_str(s):
	if s is None:
		return None
#	return str(str(s).encode('utf-8'))
	return str(s)

def to_version(minor, micro):
	if minor is None or micro is None:
		return '0.0'
	return '%s.%s' % (to_str(minor), to_str(micro))

plugin_type_map = {}
plugin_type_map["DelayPlugin"]      = "Delay"
plugin_type_map["DistortionPlugin"] = "Distortion"
plugin_type_map["WaveshaperPlugin"] = "Distortion"
plugin_type_map["DynamicsPlugin"]   = "Dynamics"
plugin_type_map["AmplifierPlugin"]  = "Dynamics"
plugin_type_map["CompressorPlugin"] = "Dynamics"
plugin_type_map["ExpanderPlugin"]   = "Dynamics"
plugin_type_map["GatePlugin"]       = "Dynamics"
plugin_type_map["LimiterPlugin"]    = "Dynamics"
plugin_type_map["FilterPlugin"]     = "Filter"
plugin_type_map["AllpassPlugin"]    = "Filter"
plugin_type_map["BandpassPlugin"]   = "Filter"
plugin_type_map["CombPlugin"]       = "Filter"
plugin_type_map["EQPlugin"]         = "Filter"
plugin_type_map["MultiEQPlugin"]    = "Filter"
plugin_type_map["ParaEQPlugin"]     = "Filter"
plugin_type_map["HighpassPlugin"]   = "Filter"
plugin_type_map["LowpassPlugin"]    = "Filter"
plugin_type_map["GeneratorPlugin"]  = "Generator"
plugin_type_map["ConstantPlugin"]   = "Generator"
plugin_type_map["InstrumentPlugin"] = "Generator"
plugin_type_map["OscillatorPlugin"] = "Generator"
plugin_type_map["ModulatorPlugin"]  = "Modulator"
plugin_type_map["ChorusPlugin"]     = "Modulator"
plugin_type_map["FlangerPlugin"]    = "Modulator"
plugin_type_map["PhaserPlugin"]     = "Modulator"
plugin_type_map["ReverbPlugin"]     = "Reverb"
plugin_type_map["SimulatorPlugin"]  = "Simulator"
plugin_type_map["SpatialPlugin"]    = "Spatial"
plugin_type_map["SpectralPlugin"]   = "Spectral"
plugin_type_map["PitchPlugin"]      = "Spectral"
plugin_type_map["UtilityPlugin"]    = "Utility"
plugin_type_map["AnalyserPlugin"]   = "Utility"
plugin_type_map["ConverterPlugin"]  = "Utility"
plugin_type_map["FunctionPlugin"]   = "Utility"
plugin_type_map["MixerPlugin"]      = "Utility"

def map_plugin_category(cat):
	if cat in plugin_type_map:
		return plugin_type_map[cat]
	return None

def get_category(p):
	for n in p.get_value(world.ns.rdf.type):
		cat = to_str(n)
		if cat.startswith('http://lv2plug.in/ns/lv2core#'):
			cat = cat[29:]
			if cat == "Plugin":
				continue
			if not cat:
				continue
			return map_plugin_category(cat)
	return None

def get_author_homepage(p):
	homepage = p.get_author_homepage()
	if homepage is not None:
		return homepage

	maintainer = get_first_value(p, world.ns.doap.maintainer)
	if maintainer is not None:
		return world.get(maintainer, world.ns.foaf.homepage, None)

	return None

def figure_out_class(p):
	s = to_str(p.get_uri())
	for c in p.get_children():
		s += ", " + figure_out_class(c)
	return s

def get_screenshot(p):
	screenshot = str(world.get(get_first_value(p, modgui.gui), modgui.screenshot, None))

	if screenshot is None:
		return None

	abs_path = screenshot[7:]

	dst = 'screenshots/' + os.path.basename(abs_path)

	shutil.copyfile(abs_path, dst)

	return dst

if not os.path.isdir('screenshots'):
	os.mkdir('screenshots')

n = 0

screenshots = {}

for i in world.get_all_plugins():
	p = {}
	p["uri"] = to_str(i.get_uri())
	p["name"] = to_str(i.get_name())
	p["author"] = to_str(i.get_author_name())
	p["homepage"] = to_str(get_author_homepage(i))
	p["description"] = to_str(get_first_value(i, world.ns.rdfs.comment))
	p["version"] = to_version(get_first_value(i, world.ns.lv2.minorVersion), get_first_value(i, world.ns.lv2.microVersion))
	p["category"] = get_category(i)
	p["screenshot"] = get_screenshot(i)
	if p["screenshot"] in screenshots:
		screenshots[p["screenshot"]] += 1
	else:
		screenshots[p["screenshot"]] = 1
	plugins.append(p)
	n = n + 1

print(json.dumps(plugins, indent=4, separators=(',', ': ')))
print(n)

for s,n in screenshots.items():
	if n > 1:
		print(s)
