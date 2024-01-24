---
description: Windows Installer developers can use the guidelines in this topic to author Windows Installer packages that contain assemblies.
ms.assetid: 60687a4f-aaa4-4264-a3f7-0a16eb1fb336
title: Adding Assemblies to a Package
ms.topic: article
ms.date: 05/31/2018
---

# Adding Assemblies to a Package

Windows Installer developers can use the guidelines in this topic to author Windows Installer packages that contain assemblies.

The following guidelines apply to Win32 assemblies, and assemblies that the common language runtime of the Microsoft .NET Framework uses.

-   A Windows Installer component should contain no more than one assembly.
-   All of the files in the assembly should be in a single component.
-   Each component that contains an assembly should have an entry in the [MsiAssembly](msiassembly-table.md) table.
-   The strong assembly cache name of each assembly should be authored into the [MsiAssemblyName](msiassemblyname-table.md) table.
-   Use the [Registry](registry-table.md) table instead of the [Class](class-table.md) table when you register COM Interop for an assembly.
-   Assemblies that have the same strong name are the same assembly. When the same assembly is installed by different applications, the components that contain the assembly should use the same value for the ComponentId in their [Component](component-table.md) tables.

> [!Note]  
> Product advertisements identify assemblies that can be installed and used by different applications. Product advertisements do not identify private assemblies.

 

## Adding Win32 Assemblies

Use the following guidelines when you include Win32 assemblies:

-   The KeyPath value in the [Component](component-table.md) table for a component that contains a Win32 assembly should not be Null.
-   The KeyPath value in the [Component](component-table.md) table for a component that contains a Win32 policy assembly should be the manifest file.
-   The KeyPath value in the [Component](component-table.md) table for a component that contains a Win32 assembly, that is not a policy assembly, should not be the manifest file or catalog file. It should be a different file in the assembly.
-   Add a row to the [MsiAssemblyName](msiassemblyname-table.md) table for each name and value pair that are listed in the **assemblyIdentity** section of the Win32 assembly's manifest.

## Adding Assemblies used with the .NET Framework

Use the following guidelines when you include assemblies that the common language runtime of the .NET Framework uses.

-   The KeyPath value in the [Component](component-table.md) table for a component that contains the assembly should not be Null.
-   When you install an assembly used by the common language runtime to the global assembly cache, the value in the File\_Application column of the MsiAssembly table must be Null.
-   Add a row to the [MsiAssemblyName](msiassemblyname-table.md) table for each attribute of the assembly's strong name. All assemblies must have the Name, Version, and Culture attributes that are specified in the MsiAssemblyName table. A publicKeyToken attribute is required for a global assembly. The following table is an example of the MsiAssemblyName table for a global assembly for use by the common language runtime.

[MsiAssemblyName Table](msiassemblyname-table.md)



| Component  | Name           | Value            |
|------------|----------------|------------------|
| ComponentA | Name           | simple           |
| ComponentA | version        | 1.0.0.0          |
| ComponentA | Culture        | neutral          |
| ComponentA | publicKeyToken | 9d1ec8380f483f5a |



 

 

 



