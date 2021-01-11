---
description: Navigating the COM+ Collection Hierarchy
ms.assetid: bd72effe-898f-40a6-973c-a26e7fe2478f
title: Navigating the COM+ Collection Hierarchy
ms.topic: article
ms.date: 05/31/2018
---

# Navigating the COM+ Collection Hierarchy

Some collections you can retrieve easily by using the [**GetCollection**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-getcollection) method on the [**COMAdminCatalog**](comadmincatalog.md) object. This method retrieves a "top-level" collection; that is, a collection such as [**Applications**](applications.md), which stands on its own and which is unique and not logically subsumed under another collection.

Many collections, however, are logically subsumed under another collection because they contain elements that are part of some larger structure. For example, the [**Components**](components.md) collection is subsumed, or related, to the [**Applications**](applications.md) collection because it contains the components installed in a particular COM+ application, which itself corresponds to an item in the **Applications** collection. Related collections such as this are not unique; there is a **Components** collection for each distinct application.

Therefore, collections are arranged in a hierarchical structure that corresponds naturally to the logical relationships between the items they contain. A diagram of the collection hierarchy can be found at [COM+ Administration Collections](com--administration-collections.md). For many of the elements that you want to configure using the COMAdmin objects, you need to navigate through some portion of the collection hierarchy to retrieve the appropriate item.

What this means in practice is that if you want to get an item in a related collection, you need to go through all the necessary higher level, subsuming collections first. And to retrieve a related collection, you need to retrieve the specific item in the parent collection to which the child collection is related. For example, if you want to configure an item corresponding to a component in a particular COM+ application, you must perform the following steps:

1.  Get the [**Applications**](applications.md) collection and populate it.
2.  Enumerate through the contents of the [**Applications**](applications.md) collection until you get to the item corresponding to the correct COM+ application.
3.  Get and populate the [**Components**](components.md) collection for that particular COM+ application.
4.  Enumerate through the contents of the [**Components**](components.md) collection until you get to the item corresponding to the correct component.

The following Microsoft Visual Basic example shows how to perform the preceding steps:


```VB
On Error GoTo My_Error_Handler

Dim Catalog As COMAdminCatalog 
Set Catalog = CreateObject("COMAdmin.COMAdminCatalog")

' Get the Applications collection and populate it.
Dim Applications As COMAdminCatalogCollection 
Set Applications = Catalog.GetCollection("Applications") 
Applications.Populate

' Get the correct application, "My Application".
Dim AppObject As COMAdminCatalogObject 
For Each AppObject in Applications 
    If AppObject.Name = "My Application" Then 
        Exit For 
    End If
Next 

' Get and populate the Components collection for "My Application".
Dim Components As COMAdminCatalogCollection 
Set Components = Applications.GetCollection("Components", AppObject.Key) 
Components.Populate

' Get the correct component, "My Component".
Dim CompObject As COMAdminCatalogObject 
For Each CompObject in Components 
    If CompObject.Name = "My Component" Then 
        Exit For 
    End If
Next 

```



Two distinct **GetCollection** methods are used in the preceding example. The first is exposed by [**COMAdminCatalog**](comadmincatalog.md) and is used to get a top-level collection—in this case, "Applications". The second is exposed by [**COMAdminCatalogCollection**](comadmincatalogcollection.md) and is used to get a collection related to the present collection; you indicate precisely which collection you want by passing in the name "Components" and the Key property value of the parent object. The Key property value is often a name or a GUID that uniquely identifies the object; this value is identified in the documentation for each collection.

In the most general case, you need to get related collections iteratively down the collection hierarchy until you retrieve the collection you want. The steps you would take follow the same general model, repetitively. For a complete list of collections, see [COM+ Administration Collections](com--administration-collections.md).

In some cases, you might want to use a shortcut method the second time you follow a path through the collection hierarchy. You can use this method only after you have already cached all the intervening Key values. For details, see [**ICOMAdminCatalog::GetCollectionByQuery**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-getcollectionbyquery).

## Related topics

<dl> <dt>

[Populating COM+ Collections](populating-com--collections.md)
</dt> <dt>

[Querying for Available Related Collections](querying-for-available-related-collections.md)
</dt> <dt>

[Retrieving Collections on the COM+ Catalog](retrieving-collections-on-the-com--catalog.md)
</dt> </dl>

 

 



