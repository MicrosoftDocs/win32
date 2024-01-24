---
description: The Microsoft Installer enables users to install and remove blocks of application functionality that is referred to as Windows Installer Features.
ms.assetid: 88268c5c-57c5-49f8-92df-1ad8f30a70c2
title: Specifying Features
ms.topic: article
ms.date: 05/31/2018
---

# Specifying Features

The Microsoft Installer enables users to install and remove blocks of application functionality that is referred to as [Windows Installer Features](windows-installer-features.md). In this section you add information to the installation database about the features that are available for the Notepad sample. For more information, see [Core Tables Group](core-tables-group.md) and [Components and Features](components-and-features.md).

The Notepad sample installs features in a hierarchy of parent and child features. In the following list, child features are indented relative to their parent feature. The features should display in this order in the [SelectionTree Control](selectiontree-control.md) of the user interface (UI).

Notepad

-   Readme
-   Help

Gate

-   January
    -   NewYears

Sport

-   Baseball
-   Football

Arts

-   Concert
-   Dance

Use a database editor to open MNP2000.msi and enter the following data into the empty [Feature Table](feature-table.md).



| Feature  | Feature\_Parent | Title         | Description                | Display | Level | Directory\_ | Attributes |
|----------|-----------------|---------------|----------------------------|---------|-------|-------------|------------|
| Arts     |                 | Arts          | Arts events at Red Park.   | 20      | 3     | NOTEPADDIR  | 0          |
| Baseball | Sport           | Baseball      | Baseball Games             | 17      | 3     | SPORTDIR    | 32         |
| Concert  | Arts            | Concert       | Concert events at Red Park | 21      | 3     | ARTSDIR     | 2          |
| Dance    | Arts            | Dance         | Dance events at Red Park   | 23      | 3     | ARTSDIR     | 2          |
| Football | Sport           | Football      | Football Games             | 19      | 3     | SPORTDIR    | 2          |
| Gate     |                 | Gate          | Red Park's Admissions      | 6       | 3     | NOTEPADDIR  | 0          |
| Help     | Notepad         | Help          | Help file.                 | 5       | 3     | NOTEPADDIR  | 1          |
| January  | Gate            | January       | January Admissions         | 10      | 3     | MONDIR      | 2          |
| NewYears | January         | New Years Day | New Years Day Admissions   | 11      | 3     | HOLDIR      | 2          |
| Notepad  |                 | Notepad       | Notepad Editor             | 1       | 3     | NOTEPADDIR  | 0          |
| Readme   | Notepad         | Readme        | Readme File                | 3       | 3     | NOTEPADDIR  | 0          |
| Sport    |                 | Sport Events  | Sport Events at Red Park   | 14      | 3     | NOTEPADDIR  | 0          |



 

[Continue](specifying-feature-component-relationships.md)

 

 



