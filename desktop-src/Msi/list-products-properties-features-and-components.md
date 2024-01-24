---
description: The VBScript file WiLstPrd.vbs is provided in the Windows SDK Components for Windows Installer Developers. The sample script connects to an Installer object and enumerates registered products and product information.
ms.assetid: 13615dc2-ebc7-4536-9dd8-9bb1dbf3cfaf
title: List Products, Properties, Features, and Components
ms.topic: article
ms.date: 05/31/2018
---

# List Products, Properties, Features, and Components

The VBScript file WiLstPrd.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). The sample script connects to an [**Installer**](installer-object.md) object and enumerates registered products and product information.

This sample demonstrates the use of:

-   [**ProductInfo property**](installer-productinfo.md)
-   [**ProductState property (Installer object)**](installer-productstate-property.md)
-   [**Products property**](installer-products.md)
-   [**Features property**](installer-features.md)
-   [**FeatureParent property**](installer-featureparent.md)
-   [**FeatureState property**](installer-featurestate.md)
-   [**Components property**](installer-components.md)
-   [**ComponentClients property**](installer-componentclients.md)
-   [**ComponentPath property**](installer-componentpath.md)
-   [**LastErrorRecord method**](installer-lasterrorrecord.md)
-   [**RegistryValue method**](installer-registryvalue.md) of the [**Installer object**](installer-object.md)

You'll require the CScript.exe or WScript.exe version of Windows Script Host to use this sample. To use CScript.exe to run this sample, type a command line at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[path to file\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiLstPrd.vbs \[Product Name\] \[options\]**

Specify the case-insensitive product name or the product ID GUID of the installed or advertised product. If no product or options are specified, the installer lists all the products installed or advertised on the system.

Note that these options are not switches so you should not prefix them with a slash (/) on the commandline. The following options may be combined by concatenating the letters. For example, "pc" to list both the products' properties and installed components.



| Option               | Description                                                                                                                           |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| no options specified | List the products' properties.                                                                                                        |
| p                    | List the products' properties.                                                                                                        |
| f                    | List the products' features, feature parents, and installation states                                                                 |
| c                    | List the products' installed components.                                                                                              |
| d                    | List the value under **HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\SharedDlls** for the key files of the products' component. |



 

For more information, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md) for additional scripting examples. For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 



