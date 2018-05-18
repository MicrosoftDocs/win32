---
Description: 'Contains an object for each method on the interface to which the collection is related.'
ms.assetid: 'e64b007f-e44d-4b6b-97b2-1e017c5a7dbe'
title: MethodsForInterface collection
---

# MethodsForInterface collection

Contains an object for each method on the interface to which the collection is related.

This collection does not support the [**Add**](icatalogcollection-add.md) and [**Remove**](icatalogcollection-remove.md) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **MethodsForInterface** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

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



|                |                                                                                                                                                                                                                                                                                                                                            |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Determines whether the object is automatically deactivated when the method completes, without SetComplete or SetAbort necessarily being called. This affects only the default setting of the JIT Activation "Done" bit at method start; this bit can be reset (as with SetComplete or SetAbort) within the method to override the default. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                  |
| Type           | Bool                                                                                                                                                                                                                                                                                                                                       |
| Default        | False                                                                                                                                                                                                                                                                                                                                      |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                                                                               |



 

### CLSID



|                |                           |
|----------------|---------------------------|
| Description    | A GUID for the component. |
| Access         | ReadOnly                  |
| Type           | String                    |
| Default        | N/A                       |
| Minimum system | Windows 2000              |



 

### Description



|                |                              |
|----------------|------------------------------|
| Description    | A description of the method. |
| Access         | ReadWrite                    |
| Type           | String                       |
| Default        | ""                           |
| Minimum system | Windows 2000                 |



 

### IID



|                |                           |
|----------------|---------------------------|
| Description    | A GUID for the interface. |
| Access         | ReadOnly                  |
| Type           | String                    |
| Default        | N/A                       |
| Minimum system | Windows 2000              |



 

### Index



|                |                                                                                                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The method dispatch identifier. This property is returned when the [**Key**](icatalogobject-key.md) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                        |
| Type           | **DWORD**                                                                                                                                                       |
| Default        | N/A                                                                                                                                                             |
| Minimum system | Windows 2000                                                                                                                                                    |



 

### Name



|                |                                                                                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The method name. This property is returned when the [**Name**](icatalogobject-name.md) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                           |
| Type           | String                                                                                                                                             |
| Default        | N/A                                                                                                                                                |
| Minimum system | Windows 2000                                                                                                                                       |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



