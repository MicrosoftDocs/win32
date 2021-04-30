---
description: A Component table is required in every merge module.
ms.assetid: ef4a0678-bf6b-47c9-89e8-40e12da52d9b
title: Authoring Merge Module Component Tables
ms.topic: article
ms.date: 05/31/2018
---

# Authoring Merge Module Component Tables

A [Component table](component-table.md) is required in every merge module. This table contains a record for each component delivered by the merge module to the target .msi file. Note that each of these components must also be specified in the [ModuleComponents table](modulecomponents-table.md) described in [Authoring ModuleComponents Tables](authoring-modulecomponents-tables.md).

Use the standard naming convention when entering names into the Component column to ensure that the identifier for each component is unique for all merge modules and installation databases. For more information, see [Naming Primary Keys in Merge Module Databases](naming-primary-keys-in-merge-module-databases.md).

Complete the remaining fields in each record as described for an installation database in [Component table](component-table.md). The components added to a package by a merge module must adhere to the guidelines for valid Windows Installer Components described in the following sections:

-   [Windows Installer Components](windows-installer-components.md)
-   [Organizing Applications into Components](organizing-applications-into-components.md)

 

 



