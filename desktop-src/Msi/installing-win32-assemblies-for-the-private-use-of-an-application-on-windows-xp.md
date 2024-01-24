---
description: The procedure in this topic identifies how to create a Windows Installer package to install a Win32 assembly.
ms.assetid: 2d4bc2be-cce6-45e6-b6a7-7ff96d28eb96
title: Installing Win32 Assemblies for the Private Use of an Application on Windows XP
ms.topic: article
ms.date: 05/31/2018
---

# Installing Win32 Assemblies for the Private Use of an Application on Windows XP

The procedure in this topic identifies how to create a Windows Installer package to install a Win32 assembly. The package installs the assembly and an application manifest file into an authored folder that the application uses. The application manifest specifies the dependence of the application on the private assembly. After installing the package, the private assembly is available for the exclusive use of the application. The assembly dependence that is specified in the application manifest overrides (for this application) any other global assembly dependencies that are specified in assembly manifest files.

Before you continue, it is a good idea to understand how to author a Windows Installer package without assemblies. For more information, see [An Installation Example](an-installation-example.md).

**To install a private assembly on Windows XP**

1.  Define a Windows Installer component that includes the Win32 assembly and the application manifest file. This component can contain other resources that should always be installed or removed with the assembly. The remaining steps of this procedure describe how to author the installation database to install this component.
2.  Add a row to the [Component table](component-table.md) for the component that contains the Win32 assembly and application manifest file. Enter a valid Windows Installer [GUID](guid.md) for this component code. For more information, see [Changing the Component Code](changing-the-component-code.md) and [What happens if the component rules are broken?](what-happens-if-the-component-rules-are-broken.md)
3.  The installer copies the assembly manifest file into the folder that contains the file specified in the File\_Application field of the [MsiAssembly table](msiassembly-table.md).
4.  Add a row to the [FeatureComponents table](featurecomponents-table.md) tying the component to a Windows Installer feature. For more information, see [Components and Features](components-and-features.md). A Windows Installer feature should be a piece of the application functionality that a user can recognize. The assembly is activated when this feature is selected by a user or faulted in by an application. If the assembly defines an additional feature, then add an additional row to the [Feature table](feature-table.md) for the feature attributes. This step is not required if authoring a merge module.
5.  For side-by-side assemblies, binding and activation information, for example, COM classes, interfaces, and type libraries, is stored in manifest files rather than the registry. Private assemblies store this information in an assembly manifest. On systems that support side-by-side assemblies, the installer skips processing any information about the component that is entered in the [Extension table](extension-table.md), [Verb table](verb-table.md), [TypeLib table](typelib-table.md), [MIME table](mime-table.md), [Class table](class-table.md), [ProgId table](progid-table.md), and [AppId table](appid-table.md). Binding and activation information can be entered into the tables for use by systems that do not support side-by-side assembly sharing.
6.  Side-by-side installation does not register the assembly globally. The installer skips self-registering the component if any self-registration information is entered in the [SelfReg table](selfreg-table.md). Self-registration information can be entered into the SelfReg table for self-registration of the component on systems that do not support side-by-side assembly sharing.
7.  Add any other registry information, exclusive of binding and activation or self-registration of the component, to the [Registry table](registry-table.md), [RemoveRegistry table](removeregistry-table.md), and [Environment table](environment-table.md).
8.  The installer skips the [IsolatedComponent table](isolatedcomponent-table.md) for this component on operating systems that support side-by-side sharing. Enter information into this table if you want the assembly to be private on systems that support local files.
9.  Add a row to the [MsiAssembly table](msiassembly-table.md) for the component that contains the Win32 assembly. Enter a value of 1 in the Attributes field of the MsiAssembly table to specify that this is a Win32 assembly. Enter the file key of the private assembly in the File\_Application field of the [MsiAssembly table](msiassembly-table.md). Add the [MsiPublishAssemblies action](msipublishassemblies-action.md) to the [InstallExecuteSequence table](installexecutesequence-table.md) or [AdvtExecuteSequence table](advtexecutesequence-table.md). Add the [MsiUnpublishAssemblies action](msiunpublishassemblies-action.md) to the InstallExecuteSequence table. Author a folder for the assembly and manifest file into the [Directory table](directory-table.md). This folder should be in the application's root directory and contain the file specified in the File\_Application field of the [MsiAssembly table](msiassembly-table.md). During the installation of the application, the installer resolves the [Directory table](directory-table.md) for the path to this folder. For more information, see [Using the Directory Table](using-the-directory-table.md).
10. Add rows to the [MsiAssemblyName table](msiassemblyname-table.md) for the component. Add one row for each name and value pair specified in the assemblyIdentity section of the manifest. For more information, see [MsiAssemblyName table](msiassemblyname-table.md).

 

 



