---
description: Package authors should ensure that the names of any custom tables, properties, or actions defined in their package will not conflict with the names of standard tables, properties, or actions that are native to the Windows Installer.
ms.assetid: f86b51c5-161a-4218-987d-f17116e4f668
title: Naming Custom Tables, Properties, and Actions
ms.topic: article
ms.date: 05/31/2018
---

# Naming Custom Tables, Properties, and Actions

Package authors should ensure that the names of any custom tables, properties, or actions defined in their package will not conflict with the names of standard tables, properties, or actions that are native to the Windows Installer.

Package authors should adhere to the following guidelines for custom table, property, or action names.

-   Make names for custom tables, properties, or actions that have a prefix that identifies your application.
-   Never use a name with Msi as the prefix. Starting with Windows Installer 2.0, all new native Windows Installer properties, actions, and tables are given names prefixed by Msi. This prefix is not case sensitive, for example MsiNewInternalTable. Because the prefix is not case sensitive, authors should avoid all cases of the Msi prefix.

For more information, see [Table Names](table-names.md).

 

 



