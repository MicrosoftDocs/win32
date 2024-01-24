---
description: The sample upgrade package updates shortcuts to the new files and features.
ms.assetid: 5a12932d-053d-49c3-9f06-0c122ca293d0
title: Updating Shortcuts for an Upgrade
ms.topic: article
ms.date: 05/31/2018
---

# Updating Shortcuts for an Upgrade

The sample upgrade package updates shortcuts to the new files and features.

Use your database editor to open MNP2001.msi and enter the following data into the [Shortcut table](shortcut-table.md).



| Shortcut    | Directory\_ | Name           | Component\_ | Target               | Arguments | Description | Hotkey | Icon\_         | IconIndex | ShowCmd | WkDir |
|-------------|-------------|----------------|-------------|----------------------|-----------|-------------|--------|----------------|-----------|---------|-------|
| sBaseball   | MENUDIR     | Baseba01.txt   | Baseball    | Baseball             |           |             |        | orca\_icon.exe |           |         |       |
| sConcert    | MENUDIR     | Concer01.txt   | Concert     | \[\#Concer01.txt\]   |           |             |        |                |           |         |       |
| sDancell    | MENUDIR     | Dance01.txt    | Dance       | \[\#Dance01.txt\]    |           |             |        |                |           |         |       |
| sFootball   | MENUDIR     | Footba01.txt   | Football    | \[\#Footba01.txt\]   |           |             |        |                |           |         |       |
| sHelp       | MENUDIR     | Help.txt       | Help        | \[\#Help.txt\]       |           |             |        |                |           |         |       |
| sJanuary    | MENUDIR     | Januar01.txt   | January     | \[\#Januar01.txt\]   |           |             |        |                |           |         |       |
| sNewYears   | MENUDIR     | NewYea01.txt   | NewYears    | \[\#NewYea01.txt\]   |           |             |        |                |           |         |       |
| sNotepad    | MENUDIR     | Redpark.exe    | Notepad     | \[\#Redpark.exe\]    |           |             |        |                |           |         |       |
| sReadme     | MENUDIR     | Readme.txt     | Notepad     | \[\#Readme.txt\]     |           |             |        |                |           |         |       |
| sMemorial   | MENUDIR     | Memori01.txt   | Memorial    | \[\#Memori01.txt\]   |           |             |        |                |           |         |       |
| sBasketball | MENUDIR     | Basketba01.txt | Basketball  | \[\#Basketba01.txt\] |           |             |        |                |           |         |       |
| sOpera      | MENUDIR     | Opera01.txt    | Opera       | \[\#Opera01.txt\]    |           |             |        |                |           |         |       |



 

[Continue](updating-upgrade-table-for-an-upgrade.md)

 

 



