---
Description: Contains a list of the in-process servers registered with the system. It contains an object for each component that is registered as an in-process server.
ms.assetid: 10434de7-c5e3-4fb0-8472-2a581607fcc0
title: InprocServers collection
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InprocServers collection

Contains a list of the in-process servers registered with the system. It contains an object for each component that is registered as an in-process server.

This collection supports the [**Remove**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-remove?branch=master) method of the [**COMAdminCatalogCollection**](/windows/win32/ComAdmin/?branch=master) object, but not the [**Add**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-add?branch=master) method. To install or import components into an application, use methods on the [**COMAdminCatalog**](/windows/win32/ComAdmin/?branch=master) object.

## Members

The **InprocServers** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**Root**](root.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](/windows/win32/ComAdmin/?branch=master) object within the collection:

-   [CLSID](#clsid)
-   [InprocServer32](#inprocserver32)
-   [ProgID](#progid)

### CLSID



|                |                                                                                                                                                           |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A GUID for the component. This property is returned when the [**Key**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_key?branch=master) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                  |
| Type           | String                                                                                                                                                    |
| Default        | N/A                                                                                                                                                       |
| Minimum system | Windows 2000                                                                                                                                              |



 

### InprocServer32



|                |                                  |
|----------------|----------------------------------|
| Description    | The file path for the component. |
| Access         | ReadOnly                         |
| Type           | String                           |
| Default        | N/A                              |
| Minimum system | Windows 2000                     |



 

### ProgID



|                |                                                                                                                                                                     |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A name identifying the component. This property is returned when the [**Name**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_name?branch=master) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                            |
| Type           | String                                                                                                                                                              |
| Default        | N/A                                                                                                                                                                 |
| Minimum system | Windows 2000                                                                                                                                                        |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



