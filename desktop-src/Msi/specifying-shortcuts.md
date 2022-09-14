---
description: The Shortcut table and related tables of the installation database hold information needed to install shortcuts. See the Program Information Tables Group and Editing Installer Shortcuts.
ms.assetid: 0f3adf78-e650-414f-b85d-b53b986eafda
title: Specifying Shortcuts
ms.topic: article
ms.date: 05/31/2018
---

# Specifying Shortcuts

The [Shortcut table](shortcut-table.md) and related tables of the installation database hold information needed to install shortcuts. See the [Program Information Tables Group](program-information-tables-group.md) and [Editing Installer Shortcuts](editing-installer-shortcuts.md).

In this section you add information that specifies advertised and non-advertised shortcuts for the Notepad sample.

Use your database editor to open MNP2000.msi and enter the following data into the Shortcut table.

[Shortcut Table](shortcut-table.md)



| Shortcut  | Directory\_ | Name         | Component\_ | Target             | Arguments | Description | Hotkey | Icon\_         | IconIndex | ShowCmd | WkDir |
|-----------|-------------|--------------|-------------|--------------------|-----------|-------------|--------|----------------|-----------|---------|-------|
| sBaseball | MENUDIR     | Baseball.txt | Baseball    | Baseball           |           |             |        | orca\_icon.exe |           |         |       |
| sConcert  | MENUDIR     | Concert.txt  | Concert     | \[\#Concert.txt\]  |           |             |        |                |           |         |       |
| sDance    | MENUDIR     | Dance.txt    | Dance       | \[\#Dance.txt\]    |           |             |        |                |           |         |       |
| sFootball | MENUDIR     | Football.txt | Football    | \[\#Football.txt\] |           |             |        |                |           |         |       |
| sHelp     | MENUDIR     | Help.txt     | Help        | \[\#Help.txt\]     |           |             |        |                |           |         |       |
| sJanuary  | MENUDIR     | January.txt  | January     | \[\#January.txt\]  |           |             |        |                |           |         |       |
| sNewYears | MENUDIR     | NewYears.txt | NewYears    | \[\#NewYears.txt\] |           |             |        |                |           |         |       |
| sNotepad  | MENUDIR     | Redpark.exe  | Notepad     | \[\#Redpark.exe\]  |           |             |        |                |           |         |       |
| sReadme   | MENUDIR     | Readme.txt   | Notepad     | \[\#Readme.txt\]   |           |             |        |                |           |         |       |



 

The sample installation needs to enable installation of an advertised shortcut for the Baseball feature. This requires specifying a key to the Icon table in the Icon\_ column of the Shortcut table. For the purposes of this example you may copy the icon for the Orca database editor provided with the Windows Installer SDK. Export the [Icon table](icon-table.md) from Orca.msi and then merge this table into the MNP2000.msi database using Orca or another merge tool. Orca also creates a directory named Icon in the directory containing MNP2000.msi, and adds the icon binary data file orca\_icon.exe.ibd. See the Data column in Icon table. The completed Icon table should look as follows when viewed in Orca.

[Icon Table](icon-table.md)



| Name           | Data            |
|----------------|-----------------|
| orca\_icon.exe | \[Binary Data\] |



 

[Continue](specifying-properties.md)

## Related topics

<dl> <dt>

[Editing Installer Shortcuts](editing-installer-shortcuts.md)
</dt> </dl>

 

 



