---
description: When the installation of an existing application is moved to Windows Installer from another setup technology, the setup developer may start authoring a Windows Installer package using the source and target file images of the existing installation.
ms.assetid: 8b0fb473-e19f-4427-b2a1-d0721cde9d38
title: Planning the Installation
ms.topic: article
ms.date: 05/31/2018
---

# Planning the Installation

When the installation of an existing application is moved to Windows Installer from another setup technology, the setup developer may start authoring a Windows Installer package using the source and target file images of the existing installation. A detailed plan of how the files and other resources are organized at the source and target is also a good starting point for developing a package for a new application.

The sample installation package takes the following files that are stored at the source location for the application and installs them to the target on the user's computer.



| File         | Description                               | Path to source                                    | Path to target                                          |
|--------------|-------------------------------------------|---------------------------------------------------|---------------------------------------------------------|
| Redpark.exe  | Text editor executable file.              | C:\\Sample\\Notepad\\Redpark.exe                  | \[ProgramFilesFolder\]\\Red\_Park\\Redpark.exe          |
| Readme.txt   | An informational file.                    | C:\\Sample\\Notepad\\Readme.txt                   | \[ProgramFilesFolder\]\\Red\_Park\\Readme.txt           |
| Help.txt     | Help manual                               | C:\\Sample\\Notepad\\Help.txt                     | Not installed. Always run-from-source.                  |
| Baseball.txt | Baseball game schedule for year 2000.     | C:\\Sample\\Notepad\\Events\\Baseball.txt         | \[ProgramFilesFolder\]\\Red\_Park\\Sports\\Baseball.txt |
| Football.txt | Football game schedule for year 2000.     | C:\\Sample\\Notepad\\Events\\Football.txt         | \[ProgramFilesFolder\]\\Red\_Park\\Sports\\Football.txt |
| Dance.txt    | Dance performances for year 2000.         | C:\\Sample\\Notepad\\Events\\Dance.txt            | \[ProgramFilesFolder\]\\Red\_Park\\Arts\\Dance.txt      |
| Concert.txt  | Music performances for year 2000.         | C:\\Sample\\Notepad\\Events\\Concert.txt          | \[ProgramFilesFolder\]\\Red\_Park\\Arts\\Concert.txt    |
| January.txt  | Admissions in January of year 2000.       | C:\\Sample\\Notepad\\Gate\\January.txt            | \[ProgramFilesFolder\]\\Red\_Park\\Gate\\January.txt    |
| NewYears.txt | Admissions on New Years Day of year 2000. | C:\\Sample\\Notepad\\Gate\\Holidays\\NewYears.txt | \[ProgramFilesFolder\]\\Red\_Park\\Gate\\NewYears.txt   |



 

The sample writes the following values in the user's registry under **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Notepad Sample**.



| Name             | Value    |
|------------------|----------|
| lfCharSet        | 0        |
| lfClipPrecision  | 2        |
| lfFaceName       | FixedSys |
| lfItalic         | 0        |
| lfOrientation    | 0        |
| lfOutPrecision   | 1        |
| fSavePageSetting | 0        |
| lfPitchAndFamily | 49       |
| iPointSize       | 120      |
| lfQuality        | 2        |
| lfStrikeOut      | 0        |
| lfWeight         | 400      |
| fWrap            | 0        |



 

The sample installs the following shortcuts. One of these shortcuts may be selected during setup as an advertised shortcut so that the user can install-on-demand the Baseball feature.



| Name      | Shortcut location                         | Shortcut target                                         |
|-----------|-------------------------------------------|---------------------------------------------------------|
| sNotepad  | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Redpark.exe          |
| sReadme   | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Readme.txt           |
| sHelp     | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Sample\\Notepad\\Help.txt       |
| sBaseball | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Sports\\Baseball.txt |
| sFootball | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Sports\\Football.txt |
| sDance    | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Arts\\Dance.txt      |
| sConcert  | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Arts\\Concert.txt    |
| sJanuary  | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Gate\\January.txt    |
| sNewYears | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Gate\\NewYears.txt   |



 

To reproduce the sample, begin by creating the source directory structure given in the first table. You can make a copy of your system's Notepad.exe file and then rename this copy Redpark.exe. Use the Notepad editor to create the remaining text files. The directory structure of the target, the registry values, and the shortcuts are added by authoring the installation database.

[Continue](importing-a-blank-database.md)

 

 



