---
description: The Windows Installer keeps all information about the installation in a relational database. You can modify this database, and therefore the installation, by using transforms and merges.
ms.assetid: 32163e06-d03d-4b65-b744-62f306f2100d
title: Merges and Transforms
ms.topic: article
ms.date: 05/31/2018
---

# Merges and Transforms

The Windows Installer keeps all information about the installation in a relational database. You can modify this database, and therefore the installation, by using transforms and merges.

## Transforms

A [database transform](database-transforms.md) adds or replaces elements in the original database. For example, a transform can change all of the text in an application's user interface from French to English.

Primary uses for transforms include:

-   Customization of base installation packages for particular groups of users.

    Transforms can be used to encapsulate the various customizations of a single base package that are required by different groups of users. For example, this is useful in organizations where the finance and staff support departments require different installations of a particular product. A product's base package can be available to everyone at one administrative installation point with appropriate customizations distributed to each group of users separately.

-   Synchronization of applications across languages.

    Transforms are useful for keeping packages authored at widely separated locations synchronized during authoring. For example, if an upgrade is first developed for an English version of an application that exists in English and French, a transform can be applied to the upgraded English version that converts it into an upgraded French version.

    Multiple transforms can be applied to a base package and then applied on-the-fly during installation. This extends the capabilities of the installer to create custom packages and provides a mechanism for efficiently assigning the most appropriate installations to different groups of users.

-   Patching applications.

    Transforms can be used to apply a minor fix to an application that does not warrant a major upgrade. For more information about patches, see [Patch Packages](patch-packages.md).

## Merges

A merge combines two databases into one database, and adds, rather than replaces, information. If the same information exists in both databases, a merge conflict occurs. Merges are useful to development teams because they allow a large application to be divided into parts that can be recombined later. For example, the database elements for the installation of a new component can be developed separately and later merged into the main installation database. For more information, see [Merge Modules](merge-modules.md).

A development team might apply a merge operation in the following way:

1.  Separate into groups and work simultaneously on different components of a large application.
2.  Each development group then populates a database with installation information for its own component, without being concerned with the other components of the application.
3.  After the development of a component is complete, that component's database can be merged into the main installation database for the entire application.

 

 



