---
description: Merge modules rarely require a user interface.
ms.assetid: 53bd2064-09dd-406f-a8ff-7b04f3525b9f
title: Authoring User Interfaces in Merge Modules
ms.topic: article
ms.date: 05/31/2018
---

# Authoring User Interfaces in Merge Modules

Merge modules rarely require a user interface. Releasing a merge module that contains both installable components and a user interface ultimately restricts the flexibility of the module user. Combining both components and UI into one module can prevent developers from using their own UI or from providing silent installations. A better alternative is to release two merge modules, one that silently installs the components and a second optional module that contains the UI. The module with the UI should list the component module in its [ModuleDependency table](moduledependency-table.md). This method enables module authors to provide a UI without forcing it on developers.

When UI tables are used in merge modules they can be merged in the same way as any other tables.

 

 



