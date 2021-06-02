---
description: Contains an object for each method on the interface to which the collection is related.
ms.assetid: e64b007f-e44d-4b6b-97b2-1e017c5a7dbe
title: MethodsForInterface collection
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MethodsForInterface
api_type: 
- COM
api_location: 
---

# MethodsForInterface collection

Contains an object for each method on the interface to which the collection is related.

This collection does not support the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) and [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **MethodsForInterface** collection inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)
-   [**RolesForMethod**](rolesformethod.md)

You can navigate to this collection from the following collections:

-   [**InterfacesForComponent**](interfacesforcomponent.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [AutoComplete](#autocomplete)
-   [CLSID](#clsid)
-   [Description](#description)
-   [IID](#iid)
-   [Index](#index)
-   [Name](#name)

### AutoComplete



| Entry | Value |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Determines whether the object is automatically deactivated when the method completes, without SetComplete or SetAbort necessarily being called. This affects only the default setting of the JIT Activation "Done" bit at method start; this bit can be reset (as with SetComplete or SetAbort) within the method to override the default. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                  |
| Type           | Bool                                                                                                                                                                                                                                                                                                                                       |
| Default        | False                                                                                                                                                                                                                                                                                                                                      |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                                                                               |



 

### CLSID



| Entry | Value |
|----------------|---------------------------|
| Description    | A GUID for the component. |
| Access         | ReadOnly                  |
| Type           | String                    |
| Default        | N/A                       |
| Minimum system | Windows 2000              |



 

### Description



| Entry | Value |
|----------------|------------------------------|
| Description    | A description of the method. |
| Access         | ReadWrite                    |
| Type           | String                       |
| Default        | ""                           |
| Minimum system | Windows 2000                 |



 

### IID



| Entry | Value |
|----------------|---------------------------|
| Description    | A GUID for the interface. |
| Access         | ReadOnly                  |
| Type           | String                    |
| Default        | N/A                       |
| Minimum system | Windows 2000              |



 

### Index



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The method dispatch identifier. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                        |
| Type           | **DWORD**                                                                                                                                                       |
| Default        | N/A                                                                                                                                                             |
| Minimum system | Windows 2000                                                                                                                                                    |



 

### Name



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The method name. This property is returned when the [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                           |
| Type           | String                                                                                                                                             |
| Default        | N/A                                                                                                                                                |
| Minimum system | Windows 2000                                                                                                                                       |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 
