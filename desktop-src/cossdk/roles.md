---
description: The Roles collection is always related to an object in the Applications collection. It holds an object for each role assigned to the application to which it is related.
ms.assetid: '87f39c2a-ad66-4390-9220-06751dcebd95'
title: Roles collection
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Roles
api_type: 
- COM
api_location: 
---

# Roles collection

The **Roles** collection is always related to an object in the [**Applications**](applications.md) collection. It holds an object for each role assigned to the application to which it is related.

This collection supports the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) and [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **Roles** collection inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)
-   [**UsersInRole**](usersinrole.md)

You can navigate to this collection from the following collections:

-   [**Applications**](applications.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [Description](#description)
-   [Name](#name)

### Description



| Entry | Value |
|----------------|----------------------------|
| Description    | A description of the role. |
| Access         | ReadWrite                  |
| Type           | String                     |
| Default        | ""                         |
| Minimum system | Windows 2000               |



 

### Name



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The role name. Extra spaces at the beginning and end of the string are stripped out. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) or [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | WriteOnce                                                                                                                                                                                                                                                   |
| Type           | String                                                                                                                                                                                                                                                      |
| Default        | "New Role"                                                                                                                                                                                                                                                  |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 
