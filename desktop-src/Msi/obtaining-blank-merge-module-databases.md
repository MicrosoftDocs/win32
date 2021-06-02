---
description: Obtain a blank merge module database. You can use the file Schema.msm provided with the Windows Installer SDK as a starting database for your merge module. For more information, see Windows SDK Components for Windows Installer Developers.
ms.assetid: 8408e892-adc6-4ef5-ad36-4d04c021c899
title: Obtaining Blank Merge Module Databases
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining Blank Merge Module Databases

Obtain a blank merge module database. You can use the file Schema.msm provided with the Windows Installer SDK as a starting database for your merge module. For more information, see [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

Developers should author merge modules using the simplest database schema that installs their components. The use of a simple schema ensures the greatest compatibility for the merge module. Merging a merge module into an installation package with a different database schema usually results in merge conflicts.

For a complete list of all the required and optional tables in merge modules, see [Merge Module Database Tables](merge-module-database-tables.md).

 

 



