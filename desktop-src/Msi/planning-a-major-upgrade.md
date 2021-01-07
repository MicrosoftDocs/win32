---
description: If Windows Installer is used for the installation and setup of an application, later upgrades of that application can be handled by installing an upgrade package.
ms.assetid: 69ad4928-e750-47c2-8668-c9e3deff8066
title: Planning a Major Upgrade
ms.topic: article
ms.date: 05/31/2018
---

# Planning a Major Upgrade

If Windows Installer is used for the installation and setup of an application, later upgrades of that application can be handled by installing an upgrade package. Setup developers may choose to author an upgrade package by modifying the original installation package. This approach is illustrated by the following upgrade example.

The installation of the original product, MNP2000, followed by the installation of the upgrade package provides the user with the following files required by the product MNP2001.



| File          | Description                                                    | Path to source                                    | Path to target                                          |
|---------------|----------------------------------------------------------------|---------------------------------------------------|---------------------------------------------------------|
| Redpark.exe   | Text editor executable file. Unchanged from previous products. | C:\\Sample\\Notepad\\Redpark.exe                  | \[ProgramFilesFolder\]\\Red\_Park\\Redpark.exe          |
| Readme.txt    | An information file. Unchanged from previous products.         | C:\\Sample\\Notepad\\Readme.txt                   | \[ProgramFilesFolder\]\\Red\_Park\\Readme.txt           |
| Help.txt      | Help manual. Unchanged from previous products.                 | C:\\Sample\\Notepad\\Help.txt                     | Not installed. Always run-from-source.                  |
| Baseba01.txt  | Baseball game schedule for year 2001.                          | C:\\Sample\\Notepad\\Events\\Baseba01.txt         | \[ProgramFilesFolder\]\\Red\_Park\\Sports\\Baseball.txt |
| Footba01.txt  | Football game schedule for year 2001.                          | C:\\Sample\\Notepad\\Events\\Footba01.txt         | \[ProgramFilesFolder\]\\Red\_Park\\Sports\\Football.txt |
| Basket01.txt  | Basketball game schedule for year 2001.                        | C:\\Sample\\Notepad\\Events\\Basket01.txt         | \[ProgramFilesFolder\]\\Red\_Park\\Sports\\Basket01.txt |
| Dance01.txt   | Dance performances for year 2001.                              | C:\\Sample\\Notepad\\Events\\Dance01.txt          | \[ProgramFilesFolder\]\\Red\_Park\\Arts\\Dance.txt      |
| Concert01.txt | Music performances for year 2001.                              | C:\\Sample\\Notepad\\Events\\Concer01.txt         | \[ProgramFilesFolder\]\\Red\_Park\\Arts\\Concert.txt    |
| Opera01.txt   | Opera performances for year 2001.                              | C:\\Sample\\Notepad\\Events\\Opera01.txt          | \[ProgramFilesFolder\]\\Red\_Park\\Arts\\Opera01.txt    |
| Januar01.txt  | Admissions in January of year 2001.                            | C:\\Sample\\Notepad\\Gate\\Januar01.txt           | \[ProgramFilesFolder\]\\Red\_Park\\Gate\\January.txt    |
| NewYea01.txt  | Admissions on New Years Day of year 2001.                      | C:\\Sample\\Notepad\\Gate\\Holidays\\NewYea01.txt | \[ProgramFilesFolder\]\\Red\_Park\\Gate\\NewYears.txt   |
| Memori01.txt  | Admissions on Memorial Day of year 2001.                       | C:\\Sample\\Notepad\\Gate\\Holidays\\Memori01.txt | \[ProgramFilesFolder\]\\Red\_Park\\Gate\\Memori01.txt   |



 

Installation of the upgrade package removes all the features installed with the original product that are not being used by the upgraded product.

For example, when upgrading from MNP2000, installation of the upgrade removes the following files from the user's computer:

-   Baseball.txt
-   Football.txt
-   Dance.txt
-   Concert.txt
-   January.txt
-   NewYears.txt

Installation of the upgrade package writes the following values in the user's registry under:

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Notepad Sample**



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



 

The upgrade updates old shortcuts to the following shortcuts. One of these shortcuts may be selected during setup as an advertised shortcut so that the user can install-on-demand the Baseball feature.



| Name        | Shortcut location                         | Shortcut target                                           |
|-------------|-------------------------------------------|-----------------------------------------------------------|
| sNotepad    | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Redpark.exe            |
| sReadme     | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Readme.txt             |
| sHelp       | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Sample\\Notepad\\Help.txt         |
| sBaseball   | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Sports\\Baseba01.txt   |
| sFootball   | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Sports\\Footba01.txt   |
| sBasketball | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Sports\\Basketba01.txt |
| sDance      | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Arts\\Dance01.txt      |
| sConcert    | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Arts\\Concer01.txt     |
| sOpera      | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Arts\\Opera01.txt      |
| sJanuary    | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Gate\\Januar01.txt     |
| sNewYears   | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Gate\\NewYea01.txt     |
| sMemorial   | \[ProgramFilesFolder\]\\Red\_Park\\Menu\\ | \[ProgramFilesFolder\]\\Red\_Park\\Gate\\Memori01.txt     |



 

When a user uninstalls the upgrade package, Windows Installer completely removes all versions of the product from the user's computer. The user is not left with any parts of MNP2000 or MNP2001.

[Continue](importing-original-installation-database.md)

 

 



