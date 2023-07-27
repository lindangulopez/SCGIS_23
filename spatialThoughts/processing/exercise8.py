layer = iface.activeLayer()
fields = layer.fields()
field_names = [field.name() for field in fields]

print("Original field names:", field_names)

# Shorten the field names to 3 letters
new_field_names = [field_name[:3] for field_name in field_names]

print("Modified field names:", new_field_names)
