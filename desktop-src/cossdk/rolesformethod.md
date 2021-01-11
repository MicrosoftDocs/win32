---
description: Contains an object for each role assigned to the method to which the collection is related. The roles must already be assigned at the application level.
ms.assetid: 3a086163-e367-4dd1-996b-821b3e1111b2
title: RolesForMethod collection
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RolesForMethod
api_type: 
- COM
api_location: 
---

# RolesForMethod collection

Contains an object for each role assigned to the method to which the collection is related. The roles must already be assigned at the application level.

This collection supports the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) and [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **RolesForMethod** collection inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**MethodsForInterface**](methodsforinterface.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [Name](#name)

### Name



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The role name. Must already be a role assigned to the application (appearing in the Roles collection). Extra spaces at the beginning and end of the string are stripped out. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) or [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | WriteOnce                                                                                                                                                                                                                                                                                                                                           |
| Type           | String                                                                                                                                                                                                                                                                                                                                              |
| Default        | "New Role"                                                                                                                                                                                                                                                                                                                                          |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                                                                                        |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 
