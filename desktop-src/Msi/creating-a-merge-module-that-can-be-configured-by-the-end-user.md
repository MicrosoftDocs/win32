---
description: To create merge modules, use the general guidelines that are described in the Authoring Merge Modules topic.
ms.assetid: 9d5e60dc-9133-4c6e-9a47-dd341f2757fa
title: Creating a Merge Module that Can Be Configured by the End-User
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Merge Module that Can Be Configured by the End-User

To create merge modules, use the general guidelines that are described in the [Authoring Merge Modules](authoring-merge-modules.md) topic. In addition, you must do the following to create a merge module that may be configured by the end-user of the module:

-   End-users need to have Mergemod.dll version 2.0 to configure your module. Users who have earlier versions of Mergemod.dll can apply the module, but they always get the default settings.
-   Add a [ModuleConfiguration Table](moduleconfiguration-table.md) to the merge module to identify the items that may be configured by an end-user. Add a record in this table for each configurable item. These items are substituted into the templates that are specified in the [ModuleSubstitution Table](modulesubstitution-table.md). Enter a name for each configurable item into the Name field. Enter the format, type, and semantic context for each item in the Format, Type, and ContextData columns. For more information, see [Semantic Types](semantic-types.md). Enter a default value for the item in the DefaultValue field using the [CMSM Special Format](cmsm-special-format.md).
-   Add a [ModuleSubstitution Table](modulesubstitution-table.md) to the merge module. Each record in this table corresponds to a substitution of one or more configurable items into one field of the merge module database. Enter the table, row, and column of the field that receives the substitution. Enter a formatting template for the substitution into the Value column using the [CMSM Special Format](cmsm-special-format.md).
-   Add records to the [Validation Table](-validation-table.md) for the ModuleSubstitution and ModuleConfiguration tables.
-   Add records to the [ModuleIgnoreTable Table](moduleignoretable-table.md) for the [ModuleSubstitution Table](modulesubstitution-table.md) and the [ModuleConfiguration Table](moduleconfiguration-table.md). This ensures that the module is compatible for users who have versions of Mergemod.dll that are earlier than version 2.0.

 

 



