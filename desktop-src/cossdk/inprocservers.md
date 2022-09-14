---
description: Contains a list of the in-process servers registered with the system. It contains an object for each component that is registered as an in-process server.
ms.assetid: 10434de7-c5e3-4fb0-8472-2a581607fcc0
title: InprocServers collection
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InprocServers
api_type: 
- COM
api_location: 
---

# InprocServers collection

Contains a list of the in-process servers registered with the system. It contains an object for each component that is registered as an in-process server.

This collection supports the [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) method of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object, but not the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) method. To install or import components into an application, use methods on the [**COMAdminCatalog**](comadmincatalog.md) object.

## Members

The **InprocServers** collection inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**Root**](root.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [CLSID](#clsid)
-   [InprocServer32](#inprocserver32)
-   [ProgID](#progid)

### CLSID



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A GUID for the component. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                  |
| Type           | String                                                                                                                                                    |
| Default        | N/A                                                                                                                                                       |
| Minimum system | Windows 2000                                                                                                                                              |



 

### InprocServer32



| Entry | Value |
|----------------|----------------------------------|
| Description    | The file path for the component. |
| Access         | ReadOnly                         |
| Type           | String                           |
| Default        | N/A                              |
| Minimum system | Windows 2000                     |



 

### ProgID



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A name identifying the component. This property is returned when the [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                            |
| Type           | String                                                                                                                                                              |
| Default        | N/A                                                                                                                                                                 |
| Minimum system | Windows 2000                                                                                                                                                        |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 
