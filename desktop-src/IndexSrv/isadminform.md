---
title: ISAdminForm
description: ISAdminForm
ms.assetid: d7340a0a-32aa-4b38-afbf-6421c948d980
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISAdminForm

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **ISAdmin** form is the startup form of the application. It contains the following controls.

-   A text box for entry of the name of the computer to manage.
-   Command buttons to connect to, start, and stop Indexing Service on the specified computer.
-   A tree view of the catalog structure on the specified computer.
-   A list view that shows either the status of the catalogs on the specified computer or the scope of the selected catalog. The catalog status is dynamically updated at a regular interval by the timer control.
-   An (invisible) timer control that determines the update interval of the catalog status list view.

The following topics discuss selected code segments for the **ISAdmin** form that perform actions specific to Indexing Service.

-   [Creating the AdminIndexServer Object](creating-the-adminindexserver-object.md)
-   [Populating the Catalog Tree View](populating-the-catalog-tree-view.md)
-   [Getting the Catalog Status](getting-the-catalog-status.md)
-   [Getting the Scopes](getting-the-scopes.md)
-   [Starting and Stopping Indexing Service](starting-and-stopping-indexing-service.md)
-   [Updating the Catalog Status](updating-the-catalog-status.md)

 

 




