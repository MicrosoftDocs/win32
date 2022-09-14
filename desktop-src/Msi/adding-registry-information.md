---
description: The Registry table, and related tables, of the installation database holds the registry information the application needs written in the system registry.
ms.assetid: e4695018-e9c3-400c-b4bb-6160e154d2cf
title: Adding Registry Information
ms.topic: article
ms.date: 05/31/2018
---

# Adding Registry Information

The [Registry table](registry-table.md), and related tables, of the installation database holds the registry information the application needs written in the system registry. See the [Registry Tables Group](registry-tables-group.md). In this section you add the information that is to be registered on the user's computer by the Notepad sample.

Use your database editor to open MNP2000.msi and enter the following data into the empty Registry table.

[Registry Table](registry-table.md)



| Registry       | Root | Key                                 | Name             | Value    | Component\_ |
|----------------|------|-------------------------------------|------------------|----------|-------------|
| CharSet        | 2    | SOFTWARE\\Microsoft\\Notepad Sample | lfCharSet        | \#0      | Notepad     |
| ClipPrecision  | 2    | SOFTWARE\\Microsoft\\Notepad Sample | lfClipPrecision  | \#2      | Notepad     |
| Escapement     | 2    | SOFTWARE\\Microsoft\\Notepad Sample | lfFaceName       | FixedSys | Notepad     |
| Italic         | 2    | SOFTWARE\\Microsoft\\Notepad Sample | lfItalic         | \#0      | Notepad     |
| Orientation    | 2    | SOFTWARE\\Microsoft\\Notepad Sample | lfOrientation    | \#0      | Notepad     |
| OutPrecision   | 2    | SOFTWARE\\Microsoft\\Notepad Sample | lfOutPrecision   | \#1      | Notepad     |
| PageSettings   | 2    | SOFTWARE\\Microsoft\\Notepad Sample | fSavePageSetting | \#0      | Notepad     |
| PitchAndFamily | 2    | SOFTWARE\\Microsoft\\Notepad Sample | lfPitchAndFamily | \#49     | Notepad     |
| PointSize      | 2    | SOFTWARE\\Microsoft\\Notepad Sample | iPointSize       | \#120    | Notepad     |
| Quality        | 2    | SOFTWARE\\Microsoft\\Notepad Sample | lfQuality        | \#2      | Notepad     |
| StrikeOut      | 2    | SOFTWARE\\Microsoft\\Notepad Sample | lfStrikeOut      | \#0      | Notepad     |
| Weight         | 2    | SOFTWARE\\Microsoft\\Notepad Sample | lfWeight         | \#400    | Notepad     |
| Wrap           | 2    | SOFTWARE\\Microsoft\\Notepad Sample | fWrap            | \#0      | Notepad     |



 

[Continue](specifying-shortcuts.md)

 

 



