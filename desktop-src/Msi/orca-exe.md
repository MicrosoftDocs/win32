---
Description: Orca.exe is a database table editor for creating and editing Windows Installer packages and merge modules.
ms.assetid: 4dddc262-1271-4e00-a986-53380b957b17
title: Orca.exe
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Orca.exe

Orca.exe is a database table editor for creating and editing Windows Installer packages and merge modules. The tool provides a graphical interface for validation, highlighting the particular entries where validation errors or warnings occur.

This tool is only available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). It is provided as an Orca.msi file. After installing the Windows SDK Components for Windows Installer Developers, double click Orca.msi to install the Orca.exe file.

## Syntax

**orca** *\[<options&gt;\]\[<source file&gt;\]*

## Command Line Options

Orca.exe uses the following case-insensitive command line options. A slash delimiter may also be used in place of a dash.



| Option | Description                                                 |
|--------|-------------------------------------------------------------|
| -q     | Quiet mode                                                  |
| -s     | <*database*&gt; Schema database \["orca.dat" - default\] |
| -?     | Help dialog                                                 |



 

Orca.exe uses the following case-insensitive command line options with merge modules. A slash delimiter may also be used in place of a dash. When performing a merge the -f, -m and <*sourcefile*&gt; are all required.



| Option     | Description                                                                |
|------------|----------------------------------------------------------------------------|
| -c         | Commit merge to database if no errors.                                     |
| -!         | Commit merge to a database even if there are errors.                       |
| -m         | <*module*&gt; Merge Module to merge into database.                      |
| -f         | Feature\[:Feature2\] Feature(s) to connect to Merge Module.                |
| -r         | <*directory id*&gt; Directory entry for the module root redirection.    |
| -x         | <*directory*&gt; Extract files to an image under the directory.         |
| -g         | <*language*&gt; Language used to open a module.                         |
| -l         | <*log file*&gt; File to use as a log, append if it already exists.      |
| -i         | <*directory*&gt; Extract files to the source image under the directory. |
| -cab       | <*filename*&gt; Extract the MSM cabinet to file.                        |
| -lfn       | Use Long File Names during the extraction.                                 |
| -configure | <*filename*&gt; Configure the module using data from a file.            |



 

## Related topics

<dl> <dt>

[Windows Installer Development Tools](windows-installer-development-tools.md)
</dt> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> </dl>

 

 



