---
title: Storage object
description: The Storage object represents an individual legacy storage on the device and provides access to the properties that are exposed by the storage.
ms.assetid: '85ab290a-16f5-49cd-9ee4-ee640604f855'
keywords: ["Storage object WPD Automation", "Storage object WPD Automation , described"]
topic_type:
- apiref
api_name:
- Storage
api_type:
- COM
---

# Storage object

The **Storage** object represents an individual legacy storage on the device and provides access to the properties that are exposed by the storage.

A **Storage** object is retrieved by using a zero-based numeric index into [**Device.Storages**](device-storages.md), which is a collection of all the storages on the device.


```JScript
var storageObject = deviceObject.Storages[0];
```



## Members

The **Storage** object has these types of members:

-   [Events](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **Storage** object has these events.



| Event                                                                          | Description                                                                                                                 |
|:-------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| [**onAddChildComplete**](storage-onaddchildcomplete.md)                       | Occurs when a [**Storage.AddChild**](storage-addchild.md) operation has completed.<br/>                              |
| [**onGetChildrenByFormatComplete**](storage-ongetchildrenbyformatcomplete.md) | Occurs when a [**Storage.GetChildrenByFormat**](storage-getchildrenbyformat.md) method operation has completed.<br/> |
| [**onObjectAdded**](storage-onobjectadded.md)                                 | Occurs after an object has been added to this **Storage** object.<br/>                                                |
| [**onObjectRemoved**](storage-onobjectremoved.md)                             | Occurs after an object has been removed from this **Storage** object.<br/>                                            |
| [**onObjectUpdated**](storage-onobjectupdated.md)                             | Occurs after an object has been updated on this **Storage** object.<br/>                                              |
| [**onRemoveChildComplete**](storage-onremovechildcomplete.md)                 | Occurs when a [**Storage.RemoveChild**](storage-removechild.md) operation has completed.<br/>                        |



 

### Methods

The **Storage** object has these methods.



| Method                                                     | Description                                                                                                                                                 |
|:-----------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddChild**](storage-addchild.md)                       | Adds a **WPDObject** obtained from the [**Storage.CreateNewObject**](storage-createnewobject.md) method, as a child of this **Storage** object.<br/> |
| [**CreateNewObject**](storage-createnewobject.md)         | Creates and initializes a **WPDObject** to the specified data format.<br/>                                                                            |
| [**GetChildrenByFormat**](storage-getchildrenbyformat.md) | Returns a collection of the immediate children of this **Storage** object filtered by one or more formats.<br/>                                       |
| [**RemoveChild**](storage-removechild.md)                 | Removes a child object from this **Storage** object.<br/>                                                                                             |



 

### Properties

The **Storage** object has these properties.



| Property                                                | Access type           | Description                                                                               |
|:--------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------------|
| [**Children**](storage-children.md)<br/>         | Read-only<br/>  | Gets a collection of all of the immediate children of this **Storage** object.<br/> |
| [***WpdProperty***](storage-wpdproperty.md)<br/> | Read/write<br/> | Gets or sets a predefined WPD property on this **Storage** object.<br/>             |



 

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[About the Storage Object](about-the-storage-object.md)
</dt> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[WPD Automation Reference](wpd-automation-reference.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





