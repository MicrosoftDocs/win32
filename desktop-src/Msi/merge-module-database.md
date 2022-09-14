---
description: The database of a merge module contains all the installation properties and setup logic for the module.
ms.assetid: 72e42392-54e6-4be8-9a43-04158552be3d
title: Merge Module Database
ms.topic: article
ms.date: 05/31/2018
---

# Merge Module Database

The database of a merge module contains all the installation properties and setup logic for the module. It is essentially a simplified [installer database](installer-database.md) or .msi file. Standard merge module database files are indicated by an .msm extension. For a list of all database tables that can exist in merge modules, see [Merge Module Database Tables](merge-module-database-tables.md). The following tables are required in the database of every .msm file:

[Component](component-table.md)

[Directory](directory-table.md)

[FeatureComponents](featurecomponents-table.md)

[File](file-table.md)

[ModuleSignature](modulesignature-table.md)

[ModuleComponents](modulecomponents-table.md)

Note that the Component, Directory, FeatureComponents, and File tables are also present in all .msi files. A merge module database does not contain a [Feature table](feature-table.md) and so the .msm file cannot be installed alone. To install a merge module, it must first be merged by using a merge tool into an .msi file.

The [ModuleSignature Table](modulesignature-table.md) is only present in .msi files that has been merged with at least one .msm file. If this table is present in an .msi file, it contains one record for each merge module that has been previously merged into the installation database.

Merge modules may contain optional MergeModule Sequence tables. These tables occur only in .msm files. When the .msm files are merged into an .msi file, these tables modify the action [*sequence tables*](s-gly.md) of the .msi file.

Merge modules may contain custom tables. These tables are used by [custom actions](custom-actions.md) defined in the merge module.

Merge modules rarely require user interface tables. These tables need to be present only in rare cases where the merge module requires input from the user during installation. For more information, see [Authoring User Interfaces in Merge Modules](authoring-user-interfaces-in-merge-modules.md).

 

 



