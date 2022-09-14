---
description: Exposed properties for the WOWLegacyServers collection are intended to be identical to the LegacyServers collection except that the WOWLegacyServers collection is drawn from the 32-bit registry on 64-bit computers.
ms.assetid: 72380276-214c-4f12-b575-deb975d846d3
title: WOWLegacyServers collection
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WOWLegacyServers
api_type: 
- COM
api_location: 
---

# WOWLegacyServers collection

Exposed properties for the **WOWLegacyServers** collection are intended to be identical to the [**LegacyServers**](legacyservers.md) collection except that the **WOWLegacyServers** collection is drawn from the 32-bit registry on 64-bit computers.

This collection does not support the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) and [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **WOWLegacyServers** collection inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**Root**](root.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [ClassName](#classname)
-   [CLSID](#clsid)
-   [InprocServer32](#inprocserver32)
-   [LocalServer32](#localserver32)
-   [ProgID](#progid)

### ClassName



| Entry | Value |
|----------------|------------------------|
| Description    | The name of the class. |
| Access         | ReadOnly               |
| Type           | String                 |
| Default        | N/A                    |
| Minimum system | Windows XP             |



 

### CLSID



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A GUID for the component. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                  |
| Type           | String                                                                                                                                                    |
| Default        | N/A                                                                                                                                                       |
| Minimum system | Windows XP                                                                                                                                                |



 

### InprocServer32



| Entry | Value |
|----------------|----------------------------------|
| Description    | The file path for the component. |
| Access         | ReadOnly                         |
| Type           | String                           |
| Default        | N/A                              |
| Minimum system | Windows XP                       |



 

### LocalServer32



| Entry | Value |
|----------------|---------------------------------------------------------------|
| Description    | Specifies the full path to a 32-bit local server application. |
| Access         | ReadOnly                                                      |
| Type           | String                                                        |
| Default        | N/A                                                           |
| Minimum system | Windows XP                                                    |



 

### ProgID



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A name identifying the component. This property is returned when the [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                            |
| Type           | String                                                                                                                                                              |
| Default        | N/A                                                                                                                                                                 |
| Minimum system | Windows XP                                                                                                                                                          |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 
