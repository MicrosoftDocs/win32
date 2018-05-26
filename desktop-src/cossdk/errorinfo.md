---
Description: Retrieves extended error information regarding methods that deal with multiple objects, such as Populate and SaveChanges on the COMAdminCatalogCollection object, and methods to install, import, or export applications or components on the COMAdminCatalog object.
ms.assetid: cf612fc4-55dd-4706-8c41-2654ca922b9a
title: ErrorInfo collection
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ErrorInfo collection

Retrieves extended error information regarding methods that deal with multiple objects, such as [**Populate**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-populate?branch=master) and [**SaveChanges**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-savechanges?branch=master) on the [**COMAdminCatalogCollection**](/windows/win32/ComAdmin/?branch=master) object, and methods to install, import, or export applications or components on the [**COMAdminCatalog**](/windows/win32/ComAdmin/?branch=master) object.

Use the [**GetCollection**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-getcollection?branch=master) method on a [**COMAdminCatalogCollection**](/windows/win32/ComAdmin/?branch=master) to access the **ErrorInfo** collection associated with the original collection that has an error.

You must call [**GetCollection**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-getcollection?branch=master) on **ErrorInfo** immediately after an error occurs; otherwise, the error information is lost.

This collection does not support the [**Add**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-add?branch=master) and [**Remove**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-remove?branch=master) methods of the [**COMAdminCatalogCollection**](/windows/win32/ComAdmin/?branch=master) object.

## Members

The **ErrorInfo** collection inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from every collection except for **ErrorInfo**, [**InprocServers**](inprocservers.md), [**PropertyInfo**](propertyinfo.md), [**RelatedCollectionInfo**](relatedcollectioninfo.md), [**Root**](root.md), and [**WOWInprocServers**](wowinprocservers.md).

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](/windows/win32/ComAdmin/?branch=master) object within the collection:

-   [ErrorCode](#errorcode)
-   [MajorRef](#majorref)
-   [MinorRef](#minorref)
-   [Name](#name)

### ErrorCode



|                |                                        |
|----------------|----------------------------------------|
| Description    | The error code for the object or file. |
| Access         | ReadOnly                               |
| Type           | String                                 |
| Default        | None                                   |
| Minimum system | Windows 2000                           |



 

### MajorRef



|                |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The [**Key**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_key?branch=master) property value for the object that has an error. For example, if a [**SaveChanges**](/windows/win32/ComAdmin/nf-comadmin-icatalogcollection-savechanges?branch=master) call for a collection fails on a particular object in the collection, the **Key** property value for that object is reported as the MajorRef value. Use this property to look at the item that fails to update or to find the component or DLL that fails to install. |
| Access         | ReadOnly                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Type           | String                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Default        | None                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                                                                                                                                                                         |



 

### MinorRef



|                |                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A precise specification of the item that has an error, such as a property name. If multiple errors occur or in contexts in which this doesn't apply, MinorRef is &lt;Invalid&gt;. |
| Access         | ReadOnly                                                                                                                                                                          |
| Type           | String                                                                                                                                                                            |
| Default        | None                                                                                                                                                                              |
| Minimum system | Windows 2000                                                                                                                                                                      |



 

### Name



|                |                                                                                                                                                                                                                          |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The name of the object or file that has an error. This property is returned when the [**Key**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_key?branch=master) or [**Name**](/windows/win32/ComAdmin/nf-comadmin-icatalogobject-get_name?branch=master) property method is called on an object of this collection. |
| Access         | ReadOnly                                                                                                                                                                                                                 |
| Type           | String                                                                                                                                                                                                                   |
| Default        | None                                                                                                                                                                                                                     |
| Minimum system | Windows 2000                                                                                                                                                                                                             |



 

## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 



