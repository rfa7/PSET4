ab = importlib.util.spec_from_file_location("module.name","F:\\Dev\\Py\\goo.py")
xy = importlib.util.module_from_spec(ab)
spec.loader.exec_module(xy)