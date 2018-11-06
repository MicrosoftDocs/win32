---
Description: Contains an object for each interface exposed by the component to which the collection is related.
ms.assetid: ee755693-e3ff-4bb1-9fde-a2bfee9c3d29
title: InterfacesForComponent collection
ms.topic: interface
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InterfacesForComponent
api_type: 
- COM
api_location: 
---

# InterfacesForComponent collection

Contains an object for each interface exposed by the component to which the collection is related.

This collection does not support the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) and [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **InterfacesForComponent** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**MethodsForInterface**](methodsforinterface.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)
-   [**RolesForInterface**](rolesforinterface.md)

You can navigate to this collection from the following collections:

-   [**Components**](components.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [CLSID](#clsid)
-   [Description](#description)
-   [IID](#iid)
-   [Name](#name)
-   [QueuingEnabled](#queuingenabled)
-   [QueueingSupported](#queueingsupported)

### CLSID



|                |                           |
|----------------|---------------------------|
| Description    | A GUID for the component. |
| Access         | ReadOnly                  |
| Type           | String                    |
| Default        | N/A                       |
| Minimum system | Windows 2000              |



 

### Description



|                |                                  |
|----------------|----------------------------------|
| Description    | A description for the interface. |
| Access         | ReadWrite                        |
| Type           | String                           |
| Default        | ""                               |
| Minimum system | Windows 2000                     |



 

### IID



|                |                                                                                                                                                           |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A GUID for the interface. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                  |
| Type           | String                                                                                                                                                    |
| Default        | N/A                                                                                                                                                       |
| Minimum system | Windows 2000                                                                                                                                              |



 

### Name



|                |                                                                                                                                                             |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A name for the interface. This property is returned when the [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                    |
| Type           | String                                                                                                                                                      |
| Default        | N/A                                                                                                                                                         |
| Minimum system | Windows 2000                                                                                                                                                |



 

### QueuingEnabled



|                |                                                                                                                                                                                                                                    |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Marks the interface as queuable and can be set by using the Admin SDK or Component Services administrative tool. However, only an interface that has the **Queuing Supported** flag set can have the **Queuing Enabled** flag set. |
| Access         | ReadWrite                                                                                                                                                                                                                          |
| Type           | Bool                                                                                                                                                                                                                               |
| Default        | False                                                                                                                                                                                                                              |
| Minimum system | Windows 2000                                                                                                                                                                                                                       |



 

### QueueingSupported



|                |                                                                                                                                                                        |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Interface supports queuing. For an interface to support queuing, all methods should have only in parameters. **Queuing Supported** is exposed as a read-only property. |
| Access         | ReadOnly                                                                                                                                                               |
| Type           | Bool                                                                                                                                                                   |
| Default        | False                                                                                                                                                                  |
| Minimum system | Windows 2000                                                                                                                                                           |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



