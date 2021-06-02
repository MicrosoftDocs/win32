---
description: The VBScript file WiToAnsi.vbs is provided in the Windows SDK Components for Windows Installer Developers. This sample shows how script is used to rewrite a Unicode text file as an ANSI text file.
ms.assetid: cb22495f-968c-470a-a2f1-d0e068133956
title: Copy a Unicode File to an ANSI File
ms.topic: article
ms.date: 05/31/2018
---

# Copy a Unicode File to an ANSI File

The VBScript file WiToAnsi.vbs is provided in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). This sample shows how script is used to rewrite a Unicode text file as an ANSI text file.

Using this sample requires the CScript.exe or WScript.exe version of Windows Script Host. To use CScript.exe to run this sample, type a command line at the command prompt using the following syntax. Help is displayed if the first argument is /? or if too few arguments are specified. To redirect the output to a file, end the command line with VBS > \[*path to file*\]. The sample returns a value of 0 for success, 1 if help is invoked, and 2 if the script fails.

**cscript WiToAnsi.vbs \[path to Unicode file\]\[path to ANSI file\]**

Specify the Unicode text file that is being converted. Specify the ANSI text file that is being created. If no ANSI file is specified, the Unicode file is replaced.

For additional scripting examples, see [Windows Installer Scripting Examples](windows-installer-scripting-examples.md). For sample utilities that do not require Windows Script Host see [Windows Installer Development Tools](windows-installer-development-tools.md).

 

 



