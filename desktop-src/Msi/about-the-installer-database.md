---
description: The Windows Installer database consists of many interrelated tables that together comprise a relational database of the information necessary to install a group of applications.
ms.assetid: 3352dd8f-c082-4c4b-98be-5823c8b28f07
title: About the Installer Database
ms.topic: article
ms.date: 05/31/2018
---

# About the Installer Database

The Windows Installer database consists of many interrelated tables that together comprise a relational database of the information necessary to install a group of applications. Because the database is relational, the tables are linked through the data in the primary and foreign key values. This provides an efficient method for changing the installation process and means that users can more easily customize a large application or group of applications. The database tables reflect the general layout of the entire group of applications, including:

-   Available features
-   Components
-   Relationship between features and components
-   Necessary registry settings
-   User interface for the application

To create an installation database, you must populate the tables with all the information about the applications and the installation process. Manually authoring all these tables becomes a large task even for a moderate size installation; therefore some third-party tools are available to assist with building the installer database. The following sections describe groups of related database tables.

[Core Tables Group](core-tables-group.md)

[File Tables Group](file-tables-group.md)

[Registry Tables Group](registry-tables-group.md)

[System Tables Group](system-tables-group.md)

[Locator Tables Group](locator-tables-group.md)

[Program Information Tables Group](program-information-tables-group.md)

[Installation Procedure Tables Group](installation-procedure-tables-group.md)

[Entity Relationship Diagram Legend](entity-relationship-diagram-legend.md)

[Text Archive Files](text-archive-files.md)

For a complete list of all tables in an installation database, see [Database Tables](database-tables.md).

## Related topics

<dl> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> </dl>

 

 



