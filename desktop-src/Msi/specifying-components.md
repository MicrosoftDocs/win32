---
description: The Windows Installer installs and removes blocks of resources referred to as Windows Installer Components. For more information, see Core Tables Group and Components and Features.
ms.assetid: e51dffed-d1cb-4a12-8615-0c0f612f993b
title: Specifying Components
ms.topic: article
ms.date: 05/31/2018
---

# Specifying Components

The Windows Installer installs and removes blocks of resources referred to as [Windows Installer Components](windows-installer-components.md). For more information, see [Core Tables Group](core-tables-group.md) and [Components and Features](components-and-features.md).

In this section you add information about the components used by the Notepad example to the [Component Table](component-table.md) you created in [Importing a Blank Database](importing-a-blank-database.md). For more information, see [Organizing Applications into Components](organizing-applications-into-components.md) and [Defining Installer Components](defining-installer-components.md).

The Notepad sample uses eight components to control resources.



| Component | Resources                                                                                                             |
|-----------|-----------------------------------------------------------------------------------------------------------------------|
| Baseball  | Baseball.txt, sBaseball                                                                                               |
| Concert   | Concert.txt, sConcert                                                                                                 |
| Dance     | Dance.txt, sDance                                                                                                     |
| Football  | Football.txt, sFootball                                                                                               |
| Help      | Help.txt, sHelp                                                                                                       |
| January   | January.txt, sJanuary                                                                                                 |
| NewYears  | NewYears.txt, sNewYears                                                                                               |
| Notepad   | Redpark.exe, Readme.txt, sReadme, sNotepad, **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Notepad Sample** |



 

Every component should be identified with a unique component ID [GUID](guid.md). If you are reproducing the sample, do not reuse the same component ID GUIDs in the following table. Instead use a utility such as Guidgen.exe to generate new GUIDs for your components.

Be sure that you use a GUID string consistent with the Windows Installer GUID data type. For more information, see [Changing the Component Code](changing-the-component-code.md) and [What happens if the component rules are broken?](what-happens-if-the-component-rules-are-broken.md)

Use Orca or another database editor to enter the following data into the blank [Component Table](component-table.md) of MNP2000.msi. Do not reuse the GUIDs shown below in the ComponentId column in your sample.



| Component | ComponentId                            | Directory\_ | Attributes | Condition | Keypath      |
|-----------|----------------------------------------|-------------|------------|-----------|--------------|
| Baseball  | {F54ABAC0-33F2-11D3-91D7-00C04FD70856} | SPORTDIR    | 2          |           | Baseball.txt |
| Concert   | {76FA7A80-33F6-11D3-91D8-00C04FD70856} | ARTSDIR     | 2          |           | Concert.txt  |
| Dance     | {CCF834A1-33F8-11D3-91D8-00C04FD70856} | ARTSDIR     | 2          |           | Dance.txt    |
| Football  | {CCF834A0-33F8-11D3-91D8-00C04FD70856} | SPORTDIR    | 2          |           | Football.txt |
| Help      | {AD10EB50-33C1-11D3-91D6-00C04FD70856} | NOTEPADDIR  | 2          |           | Help.txt     |
| January   | {CF0BC690-33C9-11D3-91D6-00C04FD70856} | MONDIR      | 2          |           | January.txt  |
| NewYears  | {A42D9140-33D8-11D3-91D6-00C04FD70856} | HOLDIR      | 2          |           | NewYears.txt |
| Notepad   | {19BED232-30AB-11D3-91D3-00C04FD70856} | NOTEPADDIR  | 2          |           | Redpark.exe  |



 

The source and target directories for each component is specified by the value entered into the Directory\_ column. The installer resolves the location of this directory using the information in the Directory table. The installer uses the key path files specified in the KeyPath column to detect each component. The remote execution attributes are set in the sample so that the components can be run-from-source or run-locally.

[Continue](specifying-files-and-file-attributes.md)

 

 



