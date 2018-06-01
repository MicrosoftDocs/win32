---
title: Admin Helper API and Scripts
description: Admin Helper API and Scripts
ms.assetid: 20e64aa7-724c-4045-9365-cc8e5df364b7
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Admin Helper API and Scripts

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The [Admin Helper API](https://www.bing.com/search?q=Admin Helper API) provides the [**AdminIndexServer**](iadminindexserver.md), [**CatAdm**](icatadm.md), and [**ScopeAdm**](iscopeadm.md) objects for managing the tasks, catalogs, and scopes of Indexing Service. A script can use these objects, for example, to start, pause, or stop Indexing Service; set, get, or add a catalog; and set, get, or add a scope for a catalog.

The following table shows how to create in scripts an [**AdminIndexServer**](iadminindexserver.md) object, shows one way to create a [**CatAdm**](icatadm.md) object, and shows one way to create a [**ScopeAdm**](iscopeadm.md) object. For additional ways of creating **CatAdm** objects, see the methods of the **AdminIndexServer** object. For additional ways of creating **ScopeAdm** objects, see the methods of the **CatAdm** object.



| Object                                    | Creation in VBScript                                       | Creation in JScript                                  |
|-------------------------------------------|------------------------------------------------------------|------------------------------------------------------|
| [AdminIndexServer](iadminindexserver.md) | `Set objAdminIS = WScript.CreateObject("Microsoft.ISAdm")` | `objAdminIS = new ActiveXObject("Microsoft.ISAdm");` |
| [CatAdm](icatadm.md)                     | `Set objCatAdm = objAdminIS.GetCatalog( )`                 | `objCatAdm = new objAdminIS.GetCatalog( );`          |
| [ScopeAdm](iscopeadm.md)                 | `Set objScopeAdm = objCatAdm.GetScope( )`                  | `objScopeAdm = new objCatAdm.GetScope( );`           |



 

The Ciodm.dll file contains the objects of the Admin Helper API.

 

 




