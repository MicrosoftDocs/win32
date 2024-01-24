---
description: Adhere to these guidelines to facilitate the localization of Windows Installer packages.
ms.assetid: f00b44b4-e8ec-46d2-b329-00728a83275b
title: Preparing a Windows Installer Package for Localization
ms.topic: article
ms.date: 05/31/2018
---

# Preparing a Windows Installer Package for Localization

Localization of a Windows Installer package into multiple languages can be greatly facilitated by doing the following:

-   Author a base installation database that is code page neutral. See [Creating a database with a neutral code page](creating-a-database-with-a-neutral-code-page.md). The code page of the localized database can then be set by importing a text archive table with a non-neutral code page into the base database. See [Setting the code page of a database](setting-the-code-page-of-a-database.md).
-   Organize files requiring localization into separate components and install these files into separate directories. This ensures that two localized packages never install identically named files into the same directory.

For example, a worldwide application using the following resources may have three components.



| Component | Resource                   |
|-----------|----------------------------|
| WORLD     | worldwide.exe              |
| WORLD     | worldwide registry entries |
| WORLD     | worldwide shortcut         |
| ENG       | engui.dll                  |
| ENG       | readme.txt                 |
| FRA       | fraui.dll                  |
| FRA       | readme.txt                 |



 

The files that need to be localized may be installed into the following directory locations:

-   \[ProgramFilesFolder\]\\World\\worldwide.exe
-   \[ProgramFilesFolder\]\\World\\English\\engui.dll
-   \[ProgramFilesFolder\]\\World\\English\\readme.txt
-   \[ProgramFilesFolder\]\\World\\French\\fraui.dll
-   \[ProgramFilesFolder\]\\World\\French\\readme.txt

 

 



