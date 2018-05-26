---
Description: Identical to the InprocServers collection except that this collection also includes local servers.
ms.assetid: b185f568-ec97-4710-b744-5d69e71d6f60
title: LegacyServers collection
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LegacyServers collection

Identical to the [**InprocServers**](inprocservers.md) collection except that this collection also includes local servers.

This collection does not support the [**Add**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-add?branch=master) and [**Remove**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-remove?branch=master) methods of the [**COMAdminCatalogCollection**](/windows/win32/ComAdmin/?branch=master) object.

## Members

The **LegacyServers** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**Root**](root.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](/windows/win32/ComAdmin/?branch=master) object within the collection:

-   [ClassName](#classname)
-   [CLSID](#clsid)
-   [InprocServer32](#inprocserver32)
-   [LocalServer32](#localserver32)
-   [ProgID](#progid)

### ClassName



|                |                        |
|----------------|------------------------|
| Description    | The name of the class. |
| Access         | ReadOnly               |
| Type           | String                 |
| Default        | N/A                    |
| Minimum system | Windows XP             |



 

### CLSID



|                |                                                                                                                                                           |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A GUID for the component. This property is returned when the [**Key**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_key?branch=master) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                  |
| Type           | String                                                                                                                                                    |
| Default        | N/A                                                                                                                                                       |
| Minimum system | Windows XP                                                                                                                                                |



 

### InprocServer32



|                |                                  |
|----------------|----------------------------------|
| Description    | The file path for the component. |
| Access         | ReadOnly                         |
| Type           | String                           |
| Default        | N/A                              |
| Minimum system | Windows XP                       |



 

### LocalServer32



|                |                                                               |
|----------------|---------------------------------------------------------------|
| Description    | Specifies the full path to a 32-bit local server application. |
| Access         | ReadOnly                                                      |
| Type           | String                                                        |
| Default        | N/A                                                           |
| Minimum system | Windows XP                                                    |



 

### ProgID



|                |                                                                                                                                                                     |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A name identifying the component. This property is returned when the [**Name**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_name?branch=master) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                            |
| Type           | String                                                                                                                                                              |
| Default        | N/A                                                                                                                                                                 |
| Minimum system | Windows XP                                                                                                                                                          |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



