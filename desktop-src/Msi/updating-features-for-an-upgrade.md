---
description: The sample Windows Installer upgrade package adds new features to the original product.
ms.assetid: cbc4c2ff-e08b-4ebb-a306-a80f9a6e4360
title: Updating Features for an Upgrade
ms.topic: article
ms.date: 05/31/2018
---

# Updating Features for an Upgrade

The sample upgrade package adds three new features to the original product:

-   Basketball, a new child feature of the Sport feature.
-   Opera, a new child feature of the Arts feature.
-   Memorial, a new child feature of the Gate feature.

Use your database editor to open MNP2001.msi and enter the following data into the [Feature table](feature-table.md).

[Feature Table](feature-table.md)



| Feature    | Feature\_Parent | Title         | Description                | Display | Level | Directory\_ | Attributes |
|------------|-----------------|---------------|----------------------------|---------|-------|-------------|------------|
| Arts       |                 | Arts          | Arts events at Red Park.   | 18      | 3     | NOTEPADDIR  | 0          |
| Baseball   | Sport           | Baseball      | Baseball Games             | 17      | 3     | SPORTDIR    | 32         |
| Concert    | Arts            | Concert       | Concert events at Red Park | 19      | 3     | ARTSDIR     | 2          |
| Dance      | Arts            | Dance         | Dance events at Red Park   | 21      | 3     | ARTSDIR     | 2          |
| Football   | Sport           | Football      | Football Games             | 13      | 3     | SPORTDIR    | 2          |
| Gate       |                 | Gate          | Red Park's Admissions      | 6       | 3     | NOTEPADDIR  | 0          |
| Help       | Notepad         | Help          | Help file.                 | 5       | 3     | NOTEPADDIR  | 1          |
| January    | Gate            | January       | January Admissions         | 7       | 3     | MONDIR      | 2          |
| NewYears   | January         | New Years Day | New Years Day Admissions   | 9       | 3     | HOLDIR      | 2          |
| Notepad    |                 | Notepad       | Notepad Editor             | 1       | 3     | NOTEPADDIR  | 0          |
| Readme     | Notepad         | Readme        | Readme File                | 3       | 3     | NOTEPADDIR  | 0          |
| Sport      |                 | Sport Events  | Sport Events at Red Park   | 12      | 3     | NOTEPADDIR  | 0          |
| Basketball | Sport           | Basketball    | Basketball Games           | 15      | 3     | SPORTDIR    | 2          |
| Opera      | Arts            | Opera         | Opera Performances         | 23      | 3     | ARTSDIR     | 2          |
| Memorial   | Gate            | Memorial Day  | Memorial Day Admissions    | 11      | 3     | HOLDIR      | 2          |



 

Use your database editor to open MNP2001.msi and enter the following data into the empty [FeatureComponents Table](featurecomponents-table.md).



| Feature\_  | Component\_ |
|------------|-------------|
| Baseball   | Baseball    |
| Concert    | Concert     |
| Dance      | Dance       |
| Football   | Football    |
| Help       | Help        |
| January    | January     |
| NewYears   | NewYears    |
| Notepad    | Notepad     |
| Readme     | Notepad     |
| Basketball | Basketball  |
| Opera      | Opera       |
| Memorial   | Memorial    |



 

[Continue](updating-shortcuts-for-an-upgrade.md)

 

 



