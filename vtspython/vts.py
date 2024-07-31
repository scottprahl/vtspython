import os
import clr
import sys

# Path to the DLLs
dll_path = os.path.join(os.path.dirname(__file__), 'dlls')

# Add reference to all DLLs in the directory
for dll in os.listdir(dll_path):
    if dll.endswith('.dll'):
        clr.AddReference(os.path.join(dll_path, dll))

# Get the current module object
vts_module = sys.modules[__name__]

# Iterate over all loaded assemblies
for assembly in clr.References:
    # Get all types (classes, methods, etc.) in the assembly
    for typ in assembly.GetTypes():
        # Dynamically set attributes in the module with the types' names
        setattr(vts_module, typ.Name, typ)

def main():
    print("VTS Module Loaded")
    # Example usage (replace 'ClassName' and 'MethodName' with actual names from the DLLs)
    # result = ClassName.MethodName()
    # print(result)
