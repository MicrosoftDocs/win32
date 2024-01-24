---
description: A blank FeatureComponents table is required in every merge module. This empty table provides a schema for the merge tool if the target .msi file does not have its own FeatureComponents table.
ms.assetid: 19463fc7-8362-4943-8907-22c38f66fe25
title: Authoring Merge Module FeatureComponents Tables
ms.topic: article
ms.date: 05/31/2018
---

# Authoring Merge Module FeatureComponents Tables

A blank [FeatureComponents table](featurecomponents-table.md) is required in every merge module. This empty table provides a schema for the merge tool if the target .msi file does not have its own FeatureComponents table.

If, and only if, there is no FeatureComponents table in the target .msi file does the merge tool use the blank table provided in the module. In this case, the merge tool creates a duplicate table in the target .msi file and adds rows that associate the new components in the merge module to the features in the application's installation package.

 

 



