---
title: Service object
description: The Service object represents an individual service on the device and provides access to the properties, methods, and events that are exposed by the service and its content.
ms.assetid: 035edd34-75e9-4edd-8785-66021380070c
keywords:
- Service object WPD Automation
- Service object WPD Automation , described
topic_type:
- apiref
api_name:
- Service
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Service object

The **Service** object represents an individual service on the device and provides access to the properties, methods, and events that are exposed by the service and its content.

A **Service** object can be retrieved in the following ways: by a zero-based numeric index, by Persistent Unique ID (PUID), or by service type, as shown in the following code.


```JScript
// Retrieve a service object by index.
var serviceObject = deviceObject.Services[Index];

// Retrieve a service object by PUID.
var serviceObject = deviceObject.Services[PUID];

// Retrieve a service object by service type.
var coolServices = deviceObject.GetServicesByType("{123456678-AAAA-BBBB-CCCC-DDDDEEEEFFFF}");
var serviceObject = coolServices[Index];
```



## Members

The **Service** object has these types of members:

-   [Events](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **Service** object has these events.



| Event                                                                          | Description                                                                                                                                                                         |
|:-------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**onAddChildComplete**](service-onaddchildcomplete.md)                       | Occurs when a [**Service.AddChild**](service-addchild.md) operation is completed.<br/>                                                                                       |
| [**onGetChildrenByFormatComplete**](service-ongetchildrenbyformatcomplete.md) | Occurs when a [**Service.GetChildrenByFormat**](service-getchildrenbyformat.md) operation is completed.<br/>                                                                 |
| [**on*Method*Complete**](service-onmethodcomplete.md)                         | Occurs after a service-defined method is completed.<br/>                                                                                                                      |
| [**onObjectAdded**](onobjectadded.md)                                         | Occurs after an object is added to this **Service** object.<br/>                                                                                                              |
| [**onObjectRemoved**](onobjectremoved.md)                                     | Occurs after an object is removed from this **Service** object.<br/>                                                                                                          |
| [**onObjectUpdated**](onobjectupdated.md)                                     | Occurs after an object is updated on this **Service** object.<br/>                                                                                                            |
| [**onRemoveChildComplete**](service-onremovechildcomplete.md)                 | Occurs when a [**Service.RemoveChild**](service-removechild.md) operation is completed.<br/>                                                                                 |
| [**on*ServiceEventName***](onserviceeventname.md)                             | The name of this event is defined by the service. For example, if a service defines an event called *MySuperEvent*, the event handler property will be *onMySuperEvent*.<br/> |



 

### Methods

The **Service** object has these methods.



| Method                                                     | Description                                                                                                                                                  |
|:-----------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddChild**](service-addchild.md)                       | Adds a **WPDObject**, obtained from the [**Service.CreateNewObject**](service-createnewobject.md) method, as a child of this **Service** object.<br/> |
| [**CreateNewObject**](service-createnewobject.md)         | Creates and initializes a **WPDObject** to the specified data format.<br/>                                                                             |
| [**GetChildrenByFormat**](service-getchildrenbyformat.md) | Returns a collection of the immediate children of this **Service** object filtered by one or more formats.<br/>                                        |
| [***Method***](service-method.md)                         | Invokes a service-defined method.<br/>                                                                                                                 |
| [**RemoveChild**](service-removechild.md)                 | Deletes a child object from this **Service** object.<br/>                                                                                              |



 

### Properties

The **Service** object has these properties.



| Property                                                        | Access type           | Description                                                                               |
|:----------------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------------|
| [**AbstractServices**](service-abstractservices.md)<br/> | Read-only<br/>  | Gets a collection of the abstract service GUIDs that this service implements.<br/>  |
| [**Children**](service-children.md)<br/>                 | Read-only<br/>  | Gets a collection of all of the immediate children of this **Service** object.<br/> |
| [***ServiceProperty***](service-serviceproperty.md)<br/> | Read/write<br/> | Gets or sets a service-defined property of this **Service** object.<br/>            |
| [***WpdProperty***](service-wpdproperty.md)<br/>         | Read/write<br/> | Gets or sets a predefined WPD property for this **Service** object.<br/>            |



 

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[About the Service Object](about-the-service-object.md)
</dt> <dt>

[**Device Object**](device-object.md)
</dt> <dt>

[WPD Automation Reference](wpd-automation-reference.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





