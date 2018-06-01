---
Description: Creating Admin Helper Objects
ms.assetid: 434d8b9a-03a8-4e91-b6ff-c692f77b342d
title: Creating Admin Helper Objects
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating Admin Helper Objects

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The [Admin Helper API](https://www.bing.com/search?q=Admin Helper API) provides the [**AdminIndexServer**](iadminindexserver.md), [**CatAdm**](icatadm.md), and [**ScopeAdm**](iscopeadm.md) objects for managing the tasks, catalogs, and scopes of Indexing Service. An application can use these objects, for example, to start, pause, or stop Indexing Service; set, get, or add a catalog; or set, get, or add a scope for a catalog.

The following table shows how to declare an [**AdminIndexServer**](iadminindexserver.md) object with either early or late binding.



| Object                                                   | Early Binding                                                                                                | Late Binding                          |
|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------|
| [**AdminIndexServer**](iadminindexserver.md)<br/> | `Dim objAdminIS as Microsoft.ISAdm`<br/> Or<br/> `Reference to CIODMLib Type Library`<br/> | `Dim objAdminIS as Object`<br/> |



 

You subsequently can use either of the following statements to create the [**AdminIndexServer**](iadminindexserver.md) object.


```VB
Set objAdminIS = New Microsoft.ISAdm
Set objAdminIS = CreateObject("Microsoft.ISAdm")
```



The following table shows how to declare a [**CatAdm**](icatadm.md) object with either early or late binding. The **CatAdm** object doesn't have a prog ID, so you must use a reference to the CIODMLib type library for early binding.



| Object                    | Early Binding                                   | Late Binding                         |
|---------------------------|-------------------------------------------------|--------------------------------------|
| [**CatAdm**](icatadm.md) | `Reference to CIODMLib Type Library`<br/> | `Dim objCatAdm as Object`<br/> |



 

You subsequently can use the following statement to create the [**CatAdm**](icatadm.md) object.


```VB
Set objCatAdm = objAdminIS.GetCatalog( )
```



For additional ways of creating a [**CatAdm**](icatadm.md) object, see the other methods of the [**AdminIndexServer**](iadminindexserver.md) object.

The following table shows how to declare a [**ScopeAdm**](iscopeadm.md) object with either early or late binding. The **ScopeAdm** object doesn't have a prog ID, so you must use a reference to the CIODMLib type library for early binding.



| Object                                   | Early Binding                                   | Late Binding                           |
|------------------------------------------|-------------------------------------------------|----------------------------------------|
| [**ScopeAdm**](iscopeadm.md)<br/> | `Reference to CIODMLib Type Library`<br/> | `Dim objScopeAdm as Object`<br/> |



 

You subsequently can use the following statement to create the [**ScopeAdm**](iscopeadm.md) object.


```VB
Set objScopeAdm = objCatAdm.GetScope( )
```



For additional ways of creating a [**ScopeAdm**](iscopeadm.md) object, see the other methods of the [**CatAdm**](icatadm.md) object.

 

 




