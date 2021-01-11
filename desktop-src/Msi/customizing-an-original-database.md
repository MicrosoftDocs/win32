---
description: Make a copy of the sample Windows Installer installation package MNP2000.msi and rename this copy MNP2000t.msi.
ms.assetid: 1251d377-7143-4a6b-81d0-0915f952be10
title: Customizing an Original Database
ms.topic: article
ms.date: 05/31/2018
---

# Customizing an Original Database

Make a copy of the sample Windows Installer installation package MNP2000.msi and rename this copy MNP2000t.msi. In the following steps you will customize this file using a database table editor such as Orca, which is provided with the SDK, or another database editor.

Include the new resource file for the phone list, Phone.txt, in the Notepad folder with the other source files.



| File      | Description                             | Path to source                 | Path to target                               |
|-----------|-----------------------------------------|--------------------------------|----------------------------------------------|
| phone.txt | A resource for the Phone\_List feature. | C:\\Sample\\Notepad\\phone.txt | \[ProgramFilesFolder\]\\Red\_Park\\phone.txt |



 

Use your database editor to add a record to the [File table](file-table.md) of MNP2000t.msi for the new file.

[File Table](file-table.md)



| File      | Component\_ | FileName  | FileSize | Version | Language | Attributes | Sequence |
|-----------|-------------|-----------|----------|---------|----------|------------|----------|
| Phone.txt | Phone       | Phone.txt | 1000     |         |          | 0          | 1        |



 

As explained in the section: [Using Transforms to Add Resources](using-transforms-to-add-resources.md), the transform should add one or more new components to the installation database to contain the new phone list feature. Use your database editor to add the following record to the [Component table](component-table.md) of MNP2000t.msi.

The Phone component should be identified with a unique component ID [GUID](guid.md). If you are reproducing the sample, do not reuse the same component ID GUID as in the following table. Instead use a utility such as Guidgen.exe to generate a new GUID. Be sure that you use a GUID string consistent with the Windows Installer [GUID](guid.md) data type.

[Component Table](component-table.md)



| Component | ComponentId                            | Directory\_ | Attributes | Condition | Keypath   |
|-----------|----------------------------------------|-------------|------------|-----------|-----------|
| Phone     | {D152A1EC-9F7A-4E45-B0DC-ED6EE5D829F8} | NOTEPADDIR  | 2          |           | Phone.txt |



 

Use your database editor to modify the data in the [Feature table](feature-table.md) of MNP2000t.msi. Enter 0 into the Level column of the Gate feature record. This disables the Gate feature and its child features and hides these features from the UI. Note that because the [**INSTALLLEVEL**](installlevel.md) property is set to 3 in the [Property table](property-table.md), the installer does not install features with a Level of 0. Add a record for the new Phone\_List feature.

[Feature Table](feature-table.md)



| Feature     | Feature\_Parent | Title         | Description                | Display | Level | Directory\_ | Attributes |
|-------------|-----------------|---------------|----------------------------|---------|-------|-------------|------------|
| Arts        |                 | Arts          | Arts events at Red Park.   | 20      | 3     | NOTEPADDIR  | 0          |
| Baseball    | Sport           | Baseball      | Baseball Games             | 17      | 3     | SPORTDIR    | 32         |
| Concert     | Arts            | Concert       | Concert events at Red Park | 21      | 3     | ARTSDIR     | 2          |
| Dance       | Arts            | Dance         | Dance events at Red Park   | 23      | 3     | ARTSDIR     | 2          |
| Football    | Sport           | Football      | Football Games             | 19      | 3     | SPORTDIR    | 2          |
| Gate        |                 | Gate          | Red Park's Admissions      | 6       | 0     | NOTEPADDIR  | 0          |
| Help        | Notepad         | Help          | Help file.                 | 5       | 3     | NOTEPADDIR  | 1          |
| January     | Gate            | January       | January Admissions         | 10      | 3     | MONDIR      | 2          |
| NewYears    | January         | New Years Day | New Years Day Admissions   | 11      | 3     | HOLDIR      | 2          |
| Notepad     |                 | Notepad       | Notepad Editor             | 1       | 3     | NOTEPADDIR  | 0          |
| Readme      | Notepad         | Readme        | Readme File                | 3       | 3     | NOTEPADDIR  | 0          |
| Sport       |                 | Sport Events  | Sport Events at Red Park   | 14      | 3     | NOTEPADDIR  | 0          |
| Phone\_List |                 | Phone List    | Phone List                 | 24      | 3     | NOTEPADDIR  | 0          |



 

Add the following record to the [FeatureComponents table](featurecomponents-table.md) of MNP2000t.msi.

[FeatureComponents Table](featurecomponents-table.md)



| Feature\_   | Component\_ |
|-------------|-------------|
| Phone\_List | Phone       |



 

Add a new record in the [Shortcut table](shortcut-table.md) to create a shortcut to the Phone\_List feature.

[Shortcut Table](shortcut-table.md)



| Shortcut | Directory\_ | Name      | Component\_ | Target          | Arguments | Description | Hotkey | Icon\_ | IconIndex | ShowCmd | WkDir |
|----------|-------------|-----------|-------------|-----------------|-----------|-------------|--------|--------|-----------|---------|-------|
| sPhone   | MENUDIR     | Phone.txt | Phone       | \[\#Phone.txt\] |           |             |        |        |           |         |       |



 

[Continue](generating-a-customization-transform.md)

 

 



