---
description: The installer keeps information about the installation directory structure in the Directory Table.
ms.assetid: 31390138-b1d0-4f0b-9304-6e7c69e6a736
title: Specifying Directory Structure
ms.topic: article
ms.date: 05/31/2018
---

# Specifying Directory Structure

The installer keeps information about the installation directory structure in the [Directory Table](directory-table.md). See the [Core Tables Group](core-tables-group.md). In this section you add directory structure information for the Notepad sample to the empty database you created in [Importing a Blank Database](importing-a-blank-database.md). Use the database editor Orca that is provided with the SDK, or another editor, to open the Directory Table in MNP2000.msi. Use the editor to enter the following data into the blank Directory table.

[Directory Table](directory-table.md)



| Directory                                        | Directory\_Parent                                | DefaultDir        |
|--------------------------------------------------|--------------------------------------------------|-------------------|
| [**TARGETDIR**](targetdir.md)                   |                                                  | SourceDir         |
| [**ProgramFilesFolder**](programfilesfolder.md) | [**TARGETDIR**](targetdir.md)                   | .                 |
| ARTSDIR                                          | NOTEPADDIR                                       | Arts:Events       |
| HOLDIR                                           | MONDIR                                           | .:Holidays        |
| MENUDIR                                          | NOTEPADDIR                                       | Menu              |
| MONDIR                                           | NOTEPADDIR                                       | Gate              |
| NOTEPADDIR                                       | [**ProgramFilesFolder**](programfilesfolder.md) | Red\_Park:Notepad |
| SPORTDIR                                         | NOTEPADDIR                                       | Sports:Events     |



 

Entering this data into the Directory table specifies the source and target directory structures. See the [Directory Table](directory-table.md) and [Using the Directory Table](using-the-directory-table.md) topics. Note that the [**TARGETDIR**](targetdir.md) property must be the name of one root in the Directory table of every installation.

[Continue](specifying-components.md)

 

 



