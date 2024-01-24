---
description: The information in this topic identifies the recommended guidelines for updating assemblies using Windows Installer patches.
ms.assetid: 60c70d48-aae2-4ea5-a880-ac9e2c83c28c
title: Updating Assemblies
ms.topic: article
ms.date: 05/31/2018
---

# Updating Assemblies

The information in this topic identifies the recommended guidelines for updating assemblies using Windows Installer patches.

Authors of assembly updates can use the following guidelines, which apply to all types of assemblies:

-   The recommended method for updating an assembly is to change the strong name of the assembly in the [MsiAssemblyName table](msiassemblyname-table.md). The new assembly version can be provided by a new component or by the same component that provides the old version.
-   If the new assembly version is provided by the same component, do not change the assembly type from a .NET Framework assembly to a Win32 assembly or vice versa.
-   If all applications on the system must use the updated assembly, you should deploy a policy assembly. A policy assembly can redirect applications on the system to use the new assembly version. Policy assemblies should be provided by creating a new component.
-   Windows Installer 3.0 or later is required to uninstall assembly updates. For more information, see [Removing Patches](removing-patches.md).
-   The newer version of the assembly should contain the same or higher versions of files from previously released assemblies.
-   Windows Installer 3.0 can service .NET Framework and Win32 assemblies by a complete file replacement or by a smaller delta update. For more information, see [Reducing Patch Size](reducing-patch-size.md).
-   If your update changes the strong name of the assembly, the [MsiPatchOldAssemblyFile](msipatcholdassemblyfile-table.md) table and [MsiPatchOldAssemblyName](msipatcholdassemblyname-table.md) table are required if the patch package does not have a [MsiPatchSequence](msipatchsequence-table.md) table. The MsiPatchOldAssemblyFile table and MsiPatchOldAssemblyName table are not required if the patch package has patch sequencing information in a MsiPatchSequence table.
-   Before releasing a new patch, test the patch by applying it with all previously released patches.

## Updating Win32 Assemblies

Use the following guidelines when you update Win32 assemblies:

-   Change the strong name of the new assembly that is specified in the [MsiAssemblyName table](msiassemblyname-table.md).
-   If you want your application to always use the new version of the assembly without affecting the assembly version used by other applications on the system, use the same component to contain the new assembly version that you used for the old assembly version. Keep the same ComponentId in the [Component](component-table.md) table. After your application is patched, it only holds a reference to the new version of the assembly. The old version of the assembly can remain with the new version in the global assembly cache. This does not affect other applications on the system that use the old version of the assembly. When the same component is used for both the new and old versions of the assembly, your update can be a smaller delta patch.
-   If the new version of the assembly is not compatible with all the systems that you want to install your application on, you can install the new and old versions of the assembly as side-by-side assemblies. To install both assembly versions side-by-side, create a new component to contain the new assembly version. The ComponentId in the [Component](component-table.md) table for the new component should be different from the ComponentId of the component with the old version. After your application is patched, it holds references to both assembly versions. Then the application can be directed to the compatible version of the assembly by a manifest. When different components are used for the new and old versions of the assembly, your update uses complete file replacement.

## Updating .NET Framework Assemblies

Use the following guidelines when you update .NET Framework assemblies.

-   Change the strong name of the new assembly that is specified in the [MsiAssemblyName table](msiassemblyname-table.md).
-   If you want your application to always use the new version of the assembly without affecting the assembly version used by other applications on the system, change the strong name of the new assembly that is specified in the [MsiAssemblyName table](msiassemblyname-table.md), and use the same component to contain the new assembly version that you used for the old assembly version. Keep the same ComponentId in the [Component](component-table.md) table. After your application is patched, it only holds a reference to the new version of the assembly. The old version of the assembly can remain with the new version in the global cache. This does not affect other applications on the system that use the old version of the assembly. When the same component is used for both the new and old versions of the assembly, your update can be a smaller delta patch.
-   If the new version of the assembly is not compatible with all systems that you want to install your application on, you can install the new and old versions of the assembly as side-by-side assemblies. To install both assembly versions side-by-side, change the strong name of the new assembly that is specified in the [MsiAssemblyName table](msiassemblyname-table.md), and create a new component to contain the new assembly version. The ComponentId in the [Component](component-table.md) table for the new component should be different than the ComponentId of the component with the old version. After your application is patched, it holds references to both assembly versions. The application can then be directed to the compatible version of the assembly by a manifest. When different components are used for the new and old versions of the assembly, your update uses complete file replacement.
-   An in-place update overwrites the copy of a .NET Framework Assembly in the global assembly cache. This type of assembly update does not change the strong name of the assembly. Only the value in the FileVersion field of the [MsiAssemblyName table](msiassemblyname-table.md) is changed. The in-place update of a .NET Framework Assembly requires .NET Framework 1.1 SP1 or greater.
    > [!Note]  
    > The in-place type of update overwrites the copy of the assembly in the global cache, and can break other applications if the new version of the assembly is not completely backward compatible. The recommended method for updating an assembly is to change the strong name of the assembly in the [MsiAssemblyName table](msiassemblyname-table.md).

     

 

 



