---
Description: Contains an object for each transient publisher property for the parent TransientSubscriptions collection. Transient subscriptions can be created on the fly for running object instances, and they vanish when the object is destroyed.
ms.assetid: 63921caa-5c22-4203-b1a3-f143928f4742
title: TransientPublisherProperties collection
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TransientPublisherProperties collection

Contains an object for each transient publisher property for the parent [**TransientSubscriptions**](transientsubscriptions.md) collection. Transient subscriptions can be created on the fly for running object instances, and they vanish when the object is destroyed.

This collection supports the [**Add**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-add?branch=master) and [**Remove**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-remove?branch=master) methods of the [**COMAdminCatalogCollection**](/windows/win32/ComAdmin/?branch=master) object.

## Members

The **TransientPublisherProperties** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**TransientSubscriptions**](transientsubscriptions.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](/windows/win32/ComAdmin/?branch=master) object within the collection:

-   [Name](#name)
-   [Value](#value)

### Name



|                |                                                                                                                                                                                                                                                                        |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The name of the property. Extra spaces at the beginning and end of the string are stripped out. This property is returned when the [**Key**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_key?branch=master) or [**Name**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_name?branch=master) property method is called on an object of this collection. |
| Access         | WriteOnce                                                                                                                                                                                                                                                              |
| Type           | String                                                                                                                                                                                                                                                                 |
| Default        | "New Property"                                                                                                                                                                                                                                                         |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                           |



 

### Value



|                |                           |
|----------------|---------------------------|
| Description    | A value for the property. |
| Access         | ReadWrite                 |
| Type           | Variant                   |
| Default        | N/A                       |
| Minimum system | Windows 2000              |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



