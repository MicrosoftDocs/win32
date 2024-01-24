---
description: You can use the installer to add the information in one database into another database by performing a merge.
ms.assetid: c53ef3d2-b3dc-4cd1-bd98-a856a223917f
title: Merging Databases
ms.topic: article
ms.date: 05/31/2018
---

# Merging Databases

You can use the installer to add the information in one database into another database by performing a merge. [Merges and Transforms](merges-and-transforms.md) operate on an entire database, and a merge combines two databases into one. Merges are useful to development teams because they allow the installation database of large application to be divided into smaller parts and then recombined into the complete installation database later.

**To merge several component databases into a single complete database**

1.  Develop the partial component databases separately.
2.  Merge each component database into the main product database by calling the [**MsiDatabaseMerge**](/windows/desktop/api/Msiquery/nf-msiquery-msidatabasemergea) function.

 

 



