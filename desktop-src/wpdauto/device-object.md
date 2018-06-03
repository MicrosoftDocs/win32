---
title: Device object
description: The Device Object represents the current device instance and is the entry point into WPD Automation.
ms.assetid: a8e64b13-db88-4abb-a0b0-abe340d0632a
keywords:
- Device object WPD Automation
- Device object WPD Automation , described
topic_type:
- apiref
api_name:
- Device
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# Device object

The **Device Object** represents the current device instance and is the entry point into WPD Automation. The **Device Object** provides access and enumeration of device services and storages as well as access to device specific properties, events, and services.

A **Device Object** is created through the following property of a scripting host.


```JScript
var deviceObject = window.external;
```



> [!Note]  
> A **Device Object** is functional only while the physical device that it represents is connected. Any operations performed on a **Device Object** after the physical device is disconnected will return an error and raise a **DISP\_E\_EXCEPTION** exception, with **pExcepInfo** filled out.

 

## Members

The **Device** object has these types of members:

-   [Events](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **Device** object has these events.



| Event                                      | Description                                                                                     |
|:-------------------------------------------|:------------------------------------------------------------------------------------------------|
| [**onDeviceReset**](ondevicereset.md)     | Occurs when the device is about to reset.<br/>                                            |
| [**onDeviceUpdated**](ondeviceupdated.md) | Occurs when the device has been updated, as when a device property has been changed.<br/> |



 

### Methods

The **Device** object has these methods.



| Method                                                | Description                                                                 |
|:------------------------------------------------------|:----------------------------------------------------------------------------|
| [**GetServicesByType**](device-getservicesbytype.md) | Returns a collection of services for the specified service type.<br/> |



 

### Properties

The **Device** object has these properties.



| Property                                               | Access type           | Description                                                                                    |
|:-------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------|
| [**Services**](device-services.md)<br/>         | Read-only<br/>  | Provides read-only access to a collection of all the services on the device.<br/>        |
| [**Storages**](device-storages.md)<br/>         | Read-only<br/>  | Provides read-only access to a collection of all the legacy storages on the device.<br/> |
| [***WpdProperty***](device-wpdproperty.md)<br/> | Read/write<br/> | Gets or sets the value of a device-specific property.<br/>                               |



 

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[About the Device Object](about-the-device-object.md)
</dt> <dt>

[**Service Object**](service-object.md)
</dt> <dt>

[**Storage Object**](storage-object.md)
</dt> <dt>

[WPD Automation Reference](wpd-automation-reference.md)
</dt> <dt>

[**WPDObject**](wpdobject.md)
</dt> </dl>

 

 





