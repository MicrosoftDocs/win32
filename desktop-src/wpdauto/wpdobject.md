---
title: WPDObject object
description: The WPDObject represents a generic object on the device.
ms.assetid: c22d0cc3-2a63-4ece-8d96-0d8aa89e95f2
keywords:
- WPDObject object WPD Automation
- WPDObject object WPD Automation , described
topic_type:
- apiref
api_name:
- WPDObject
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# WPDObject object

The **WPDObject** represents a generic object on the device. The **Service** object and the **Storage** object both inherit their functionality from **WPDObject**.

Examples of how to use the methods, properties, and events listed here for **WPDObject** can be found in the corresponding pages of the [**Service Object**](service-object.md) and [**Storage Object**](storage-object.md) sections.

## Members

The **WPDObject** object has these types of members:

-   [Events](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **WPDObject** object has these events.



| Event                                                  | Description                                                        |
|:-------------------------------------------------------|:-------------------------------------------------------------------|
| [**onAddChildComplete**](onaddchildcomplete.md)       | Occurs when an **AddChild** operation has completed.<br/>    |
| [**onRemoveChildComplete**](onremovechildcomplete.md) | Occurs when an **RemoveChild** operation has completed.<br/> |



 

### Methods

The **WPDObject** object has these methods.



| Method                                                       | Description                                                                                                                                                                                                                  |
|:-------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddChild**](wpdobject-addchild.md)                       | Adds a **WPDObject** obtained from the [**Service.CreateNewObject()**](service-createnewobject.md) method or the [**Storage.CreateNewObject()**](storage-createnewobject.md) method, as a child of this object.<br/> |
| [**GetChildrenByFormat**](wpdobject-getchildrenbyformat.md) | Returns a collection of the immediate children of this object filtered by one or more data formats.<br/>                                                                                                               |
| [**RemoveChild**](wpdobject-removechild.md)                 | Deletes a child object from this object.<br/>                                                                                                                                                                          |



 

### Properties

The **WPDObject** object has these properties.



| Property                                                          | Access type           | Description                                                               |
|:------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------|
| [**Children**](wpdobject-children.md)<br/>                 | Read-only<br/>  | Gets a collection of all of the immediate children of this object.        |
| [**Parent**](wpdobject-parent.md)<br/>                     | Read-only<br/>  | Gets the immediate parent of this object.                                 |
| [**Resource**](wpdobject-resource.md)<br/>                 | Read/write<br/> | Provides read/write access to this object's resource.<br/>          |
| [**Service**](wpdobject-service.md)<br/>                   | Read-only<br/>  | Gets the **Service** object that contains this **WPDObject**.             |
| [***ServiceProperty***](wpdobject-serviceproperty.md)<br/> | Read/write<br/> | Gets or sets a service-defined property for this object.<br/>       |
| [**Storage**](wpdobject-storage.md)<br/>                   | Read-only<br/>  | Gets the **Storage** object that contains this **WPDObject**. <br/> |
| [***WpdProperty***](wpdobject-wpdproperty.md)<br/>         | Read/write<br/> | Gets or sets a pre-defined WPD property for this object.<br/>       |



 

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[About the WPDObject](about-the-wpdobject-.md)
</dt> <dt>

[**childrenCollection Object**](childrencollection-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[WPD Automation Reference](wpd-automation-reference.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





