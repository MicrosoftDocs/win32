---
description: The VBScript file WiGenXfm.vbs is provided in the Windows SDK Components for Windows Installer Developers. This sample script can generate a transform from two Windows Installer databases. For more information see Database Transforms.
ms.assetid: bfa918b8-8d90-4e14-8a06-6c3d5b5dc13b
title: Generate a Transform
ms.topic: article
ms.date: 05/31/2018
---

# Generate a Transform

The VBScript file WiGenXfm.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample script can generate a transform from two Windows Installer databases. For more information see [Database Transforms](database-transforms.md).

The sample demonstrates the use of:

[**OpenDatabase method (Installer Object)**](installer-opendatabase.md)

[**LastErrorRecord method**](installer-lasterrorrecord.md) of the [**Installer object**](installer-object.md)

[**GenerateTransform method**](database-generatetransform.md) of the [**Database object**](database-object.md)

You'll require the CScript.exe or WScript.exe version of Windows Script Host to use this sample. To use CScript.exe to run this sample, type a command line at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[*path to file*\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiGenXfm.vbs \[path to original database\]\[path to revised database\]\[path to transform file\]**

Specify the path to the original Windows Installer database. Specify the path to the revised database. Specify the path to the transform file to be created. If the path to the transform file is omitted, the two databases are only compared.

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host, see [Windows Installer Development Tools](windows-installer-development-tools.md).

Note that [A Localization Example](a-localization-example.md) demonstrates [Generating a Customization Transform](generating-a-customization-transform.md).

 

 



