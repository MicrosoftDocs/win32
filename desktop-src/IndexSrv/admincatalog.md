---
title: AdminCatalog
description: AdminCatalog
ms.assetid: 3a3882d1-6d3c-4a01-8abb-a309820721fe
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AdminCatalog

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The AdminCatalog form performs one of several actions on a selected catalog. This form appears when the name of a catalog in the catalog tree view on the [ISAdminForm](isadminform.md) form is right-clicked. The AdminCatalog form contains the following controls.

-   An option button to force a full rescan of all scopes of the catalog.
-   An option button to force a master merge of the catalog.
-   An option button to create a new directory for the catalog.
-   An option button to remove the catalog.
-   A command button to perform the selected action.
-   A command button to cancel the action.

The following topics discuss selected code segments for the AdminCatalog form that perform actions specific to Indexing Service.

-   [Rescanning All Scopes](rescanning-all-scopes.md)
-   [Forcing a Master Merge](forcing-a-master-merge.md)
-   [Removing a Catalog](removing-a-catalog.md)

 

 




