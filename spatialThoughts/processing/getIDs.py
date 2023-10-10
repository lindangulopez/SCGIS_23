layer = iface.activeLayer()
features = layer.getFeatures()
ids = []
for f in features:
  id = f.id()
  ids.append(id)

print(ids)