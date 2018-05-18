---
title: DeviceEvents object
description: Contains a collection of all the supported DeviceEvent objects for an imaging device. See the Events property of the Device object for more details on determining the collection of supported device events.
ms.assetid: '68c6aeac-9e60-4387-be89-d7f507da04e6'
keywords: ["DeviceEvents object WIA Automation", "DeviceEvents object WIA Automation , described"]
topic_type:
- apiref
api_name:
- DeviceEvents
api_location:
- Wiaaut.h
api_type:
- COM
---

# DeviceEvents object

Contains a collection of all the supported [**DeviceEvent**](-wiaaut-deviceevent.md) objects for an imaging device. See the [**Events**](-wiaaut-idevice-events.md) property of the [**Device**](-wiaaut-device.md) object for more details on determining the collection of supported device events.

## Members

The **DeviceEvents** object has these types of members:

-   [Properties](#properties)

### Properties

The **DeviceEvents** object has these properties.



| Property                                                               | Access type          | Description                                                                             |
|:-----------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------|
| [**Count (DeviceEvents)**](-wiaaut-ideviceevents-count.md)<br/> | Read-only<br/> | Retrieves the number of members in the **DeviceEvents** collection.<br/>          |
| [**Item (DeviceEvents)**](-wiaaut-ideviceevents-item.md)<br/>   | Read-only<br/> | Retrieves the specified item in the **DeviceEvents** collection by position.<br/> |



 

## Remarks

Note that the supported events vary from one imaging device to the next.

For example code, see [Enumerate all the Supported Events for the Selected Device](-wiaaut-shared-samples.md#enumerate-all-the-supported-events-for-the-selected-device) in Shared Samples.

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**Events**](-wiaaut-idevice-events.md)



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

[**Events**](-wiaaut-idevice-events.md)
</dt> </dl>

 

 





