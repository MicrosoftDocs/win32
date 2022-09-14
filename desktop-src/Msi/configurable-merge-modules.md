---
description: Merge modules (.msm files) may be authored to contain attributes that are configurable by the consumer of the merge module.
ms.assetid: 461436f0-3a91-4a49-934a-f975bf13df40
title: Configurable Merge Modules
ms.topic: article
ms.date: 05/31/2018
---

# Configurable Merge Modules

Merge modules (.msm files) may be authored to contain attributes that are configurable by the consumer of the merge module. This enables the merge module to be configured at the time the installation package and module are merged and installed by the end-user. Configurable merge modules require Mergemod.dll version 2.0 but can run on any version of the Windows Installer.

The implementation of configurable merge modules consists of two parts. First, when creating the merge module (.msm file), the merge module author adds information to the module database that specifies which items can be modified and how these items can be configured by the module user. The author adds entries to the [Merge Module Database Tables](merge-module-database-tables.md) that are reserved for configurable information ([ModuleConfiguration table](moduleconfiguration-table.md) and [ModuleSubstitution table](modulesubstitution-table.md)), updates the [\_Validation table](-validation-table.md), and adds entries for the configurable merge module tables to the [ModuleIgnoreTable table](moduleignoretable-table.md). The additions to the ModuleIgnore table are required to make the module compatible with Mergemod.dll versions earlier than 2.0.

Second, when merging the module into an installation package (.msi file), the end-user of the module uses a merge tool. The merge tool calls Mergemod.dll to expose the configuration information in the module to a client configuration tool. The configuration tool may interact with the end-user but is not required to expose all possible configuration options. If the user declines to provide a selection for a configurable item, the module may provide a default value. After the user gives the configuration tool his selections, the merge tool calls Mergemod.dll to perform the merge.

Configurable merge modules are fully compatible with tools earlier than Mergemod.dll version 2.0. In these cases, the tool uses the default values in the module.

For more information, see [Using Configurable Merge Modules](using-configurable-merge-modules.md).

 

 



