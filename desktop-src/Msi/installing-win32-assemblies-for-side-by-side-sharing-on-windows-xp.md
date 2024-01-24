---
description: The following describes how to create a Windows Installer package to install a Win32 assembly.
ms.assetid: 1234e904-fc7f-4eb7-8c50-0c959bbf5261
title: Installing Win32 Assemblies for Side-by-Side Sharing
ms.topic: article
ms.date: 05/31/2018
---

# Installing Win32 Assemblies for Side-by-Side Sharing

The following describes how to create a Windows Installer package to install a Win32 assembly. The package installs a side-by-side assembly in the Winsxs folder for the shared use of the application. After installing the package, the shared assembly is globally available to any application that specifies a dependence on the assembly in an assembly manifest file. The installer does not globally register the side-by-side assembly on the system.

Note that you may install shared side-by-side assemblies using [merge modules](merge-modules.md).

Before continuing you should understand how to author a Windows Installer package without assemblies. For an example of how to author a simple installation, see [An Installation Example](an-installation-example.md).

**To install a shared assembly side-by-side**

1.  Define a Windows Installer component that includes the Win32 assembly. This component may contain other resources that should always be installed or removed with the assembly. All the other components of the application can be authored just as for an installation without assemblies. Add a row to the [Component table](component-table.md) for the component containing the Win32 assembly. Enter a valid Windows Installer [GUID](guid.md) for this component code. Do not use the manifest file as the key path for this component.
2.  Add a row to the [FeatureComponents table](featurecomponents-table.md) tying the component to a Windows Installer feature. For information see, [Components and Features](components-and-features.md). A Windows Installer feature should be a piece of the application's functionality that is recognizable to a user. The assembly is activated when this feature is selected by a user or faulted in by an application. If the assembly defines an additional feature, then add an additional row to the [Feature table](feature-table.md) for the feature's attributes. This step is not needed when authoring a merge module.
3.  For side-by-side assemblies, binding and activation information, such as COM classes, interfaces, and type libraries, is stored in manifest files rather than the registry. Shared assemblies store this information in an assembly manifest. On systems that support side-by-side assemblies, the installer skips processing any information about the component entered in the [Extension table](extension-table.md), [Verb table](verb-table.md), [TypeLib table](typelib-table.md), [MIME table](mime-table.md), [Class table](class-table.md), [ProgId table](progid-table.md), and [AppId table](appid-table.md). Binding and activation information may be entered into these tables for use by systems that do not support side-by-side assembly sharing.
4.  Side-by-side installation does not globally register the assembly, the installer skips self-registering the component if any self-registration information has been entered in the [SelfReg table](selfreg-table.md). Self-registration information may be entered into the SelfReg table for self-registration of the component on systems that do not support side-by-side assembly sharing.
5.  Add any other registry information, exclusive of binding and activation or self-registration of the component, to the [Registry table](registry-table.md), [RemoveRegistry table](removeregistry-table.md), and [Environment table](environment-table.md).
6.  Because this is a shared assembly do not generate a .local file. Do not include information for this component in the [IsolatedComponent table](isolatedcomponent-table.md). The installer skips the IsolatedComponent table for this component on operating systems that support side-by-side sharing. Add information to the IsolatedComponent table if you would like the assembly to be private on systems that support .local files.
7.  To enable side-by-side sharing, the Win32 assembly must be installed into the Winsxs folder. This is accomplished by leaving the File\_Application column of the [MsiAssembly table](msiassembly-table.md) null for the assembly. This tells the installer to install the assembly to the WinSxS folder, instead of to the folder of the component. Add a row to the [MsiAssembly table](msiassembly-table.md) for the component that contains the Win32 assembly. Enter a value of 1 in the Attributes field of the MsiAssembly table to specify that this is a Win32 assembly. For a shared assembly, leave the File\_Application field empty. Add the [MsiPublishAssemblies action](msipublishassemblies-action.md) to the [InstallExecuteSequence table](installexecutesequence-table.md) or [AdvtExecuteSequence table](advtexecutesequence-table.md). Add the [MsiUnpublishAssemblies action](msiunpublishassemblies-action.md) to the InstallExecuteSequence table.
8.  Add rows to the [MsiAssemblyName table](msiassemblyname-table.md) for the component. Add one row for each name and value pair specified in the assemblyIdentity section of the manifest. For an example, see [MsiAssemblyName table](msiassemblyname-table.md).

 

 



