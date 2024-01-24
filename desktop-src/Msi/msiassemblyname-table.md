---
description: The MsiAssembly Table and MsiAssemblyName Table specify Windows Installer settings for common language runtime assemblies and Win32 assemblies.
ms.assetid: cfe9a0a3-e40f-4c59-b2e4-ad7654528e3b
title: MsiAssemblyName Table
ms.topic: article
ms.date: 05/31/2018
---

# MsiAssemblyName Table

The [MsiAssembly Table](msiassembly-table.md) and MsiAssemblyName Table specify Windows Installer settings for common language runtime assemblies and Win32 assemblies. For information see, [Installation of Assemblies to the Global Assembly Cache](installation-of-assemblies-to-the-global-assembly-cache.md) and [Installation of Win32 Assemblies](installation-of-win32-assemblies.md).

The MsiAssemblyName Table specifies the schema for the elements of a strong assembly cache name for a .NET Framework or Win32 assembly. The name is constructed by appending all elements with the same Component\_ key. See the following example.

Windows Installer can install Win32 assemblies as [side-by-side assemblies](side-by-side-assemblies.md). For more information, see the [Side-by-Side Assembly API](../sbscs/side-by-side-assembly-api.md).

The MsiAssemblyName Table has the following columns.



| Column      | Type                         | Key | Nullable |
|-------------|------------------------------|-----|----------|
| Component\_ | [Identifier](identifier.md) | Y   | N        |
| Name        | [Text](text.md)             | Y   | N        |
| Value       | [Text](text.md)             | N   | N        |



 

## Columns

<dl> <dt>

<span id="Component_"></span><span id="component_"></span><span id="COMPONENT_"></span>Component\_
</dt> <dd>

Key into the [Component Table](component-table.md) that specifies the Windows Installer component that contains this assembly.

</dd> <dt>

<span id="Name"></span><span id="name"></span><span id="NAME"></span>Name
</dt> <dd>

Name of the attribute associated with the value specified in the Value column.

</dd> <dt>

<span id="Value"></span><span id="value"></span><span id="VALUE"></span>Value
</dt> <dd>

Value associated with the name specified in the Name column.

</dd> </dl>

## Remarks

The information authored into the MsiAssemblyName Table must match the information in the manifest file of the assembly. If the information in the manifest and MsiAssemblyName Table do not match, removal of the application can leave the assembly on the computer.

For Win32 assemblies there must be a row in the MsiAssemblyName Table for each of the following entries in the Name field: type, name, version, language, publicKeyToken and processorArchitecture. The corresponding value for each name can be entered into the Value field. The name-value pairs in MsiAssemblyName Table must match the type, name, version, language, publicKeyToken and processorArchitecture attributes in the manifest of the assembly.

For private common language runtime assemblies (.NET Frameworkversions 1.0 and 1.1), the MsiAssemblyName Table must include a row for each of the following entries in the Name field: Name, Version, and Culture. The corresponding value for each Name can be entered into the Value field.

For global common language runtime assemblies (.NET Framework versions 1.0 and 1.1), the MsiAssemblyName Table must include a row for each of the following entries in the Name field: Name, Version, Culture, and PublicKeyToken. The corresponding value for each Name can be entered into the Value field.

The .NET Framework version 1.1 is the minimum version that can be used to perform an in-place update of a global common language runtime assembly. You can check the [**MsiNetAssemblySupport**](msinetassemblysupport.md) property for the version. The MsiAssemblyName Table must also have a FileVersion field because this type of assembly update only changes the FileVersion. For more information, see [Updating Assemblies](updating-assemblies.md).

For example, the assembly manifest for ComponentA might have an assemblyIdentity section as follows for a Win32 assembly.

``` syntax
<assemblyIdentity type="win32" name="ms-sxstest-simple" version="1.0.0.0" language="en" publicKeyToken="1111111111222222" processorArchitecture="x86"/>
```

In this case, populate the MsiAssemblyName Table as follows.



| Component  | Name                  | Value             |
|------------|-----------------------|-------------------|
| ComponentA | type                  | win32             |
| ComponentA | name                  | ms-sxstest-simple |
| ComponentA | version               | 1.0.0.0           |
| ComponentA | language              | en                |
| ComponentA | publicKeyToken        | 1111111111222222  |
| ComponentA | processorArchitecture | x86               |



 

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE66](ice66.md)  
[ICE83](ice83.md)  
</dl>

 

 
