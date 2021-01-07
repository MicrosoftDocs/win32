---
description: When authoring an INF file for a Setup application you should also refer to the INF file format documented in General Guidelines for INF Files and INF File Sections and Directives of the Microsoft Windows 2000 Driver Development Kit.
ms.assetid: f9df95bb-345d-4a70-a27e-0b1bc2a27ada
title: Authoring an INF file
ms.topic: article
ms.date: 05/31/2018
---

# Authoring an INF file

When authoring an INF file for a Setup application you should also refer to the INF file format documented in *General Guidelines for INF Files* and *INF File Sections and Directives* of the Microsoft Windows 2000 Driver Development Kit.

When authoring INF files for a setup application adhere to the following rules.

-   A **Version** section is required in every INF file.
-   Sections must begin with the section name enclosed by square brackets (\[\]).
-   Names of **DestinationDirs**, **SourceDisksFiles**, **SourceDisksNames**, **Strings**, and **Version** sections must be identical to the section type. For example use \[DestinationDirs\]. Authors may specify the names of other types of sections.
-   Names of **SourceDisksNames** and **SourceDisksFiles** sections may be appended with a platform-specific suffix. For example, to show an Intel-specific **SourceDisksNames** section use \[SourceDisksNames.x86\]. If the setup functions find platform-specific **SourceDisksNames** and **SourceDisksFiles** sections matching the user's platform, the functions use the platform-specific sections. Otherwise the setup functions use the non-suffixed **SourceDisksNames** and **SourceDisksFiles** sections. The setup functions can programmatically determine the user's system. See the [INF SourceDisksNames and SourceDisksFiles Sections Example](inf-sourcedisksnames-and-sourcedisksfiles-sections-example.md).
-   Values may be expressed as replaceable strings using the form %*strkey*%. To use a % character in the string, use %%. The strkey must be defined in a **Strings** section of the INF file.

 

 



