---
title: DeviceEvent object
description: Describes an EventID Constants that can be used when calling RegisterEvent or RegisterPersistentEvent on a DeviceManager object.
ms.assetid: 'f91ab3be-c046-4a2f-acae-e8cbe013105d'
keywords: ["DeviceEvent object WIA Automation", "DeviceEvent object WIA Automation , described"]
topic_type:
- apiref
api_name:
- DeviceEvent
api_location:
- Wiaaut.h
api_type:
- COM
---

# DeviceEvent object

Describes an [**EventID Constants**](-wiaaut-consts-eventid.md) that can be used when calling [**RegisterEvent**](-wiaaut-idevicemanager-registerevent.md) or [**RegisterPersistentEvent**](-wiaaut-idevicemanager-registerpersistentevent.md) on a [**DeviceManager**](-wiaaut-devicemanager.md) object.

## Members

The **DeviceEvent** object has these types of members:

-   [Properties](#properties)

### Properties

The **DeviceEvent** object has these properties.



| Property                                                                         | Access type          | Description                                                                                            |
|:---------------------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------|
| [**Description (DeviceEvent)**](-wiaaut-ideviceevent-description.md)<br/> | Read-only<br/> | Retrieves the **DeviceEvent** description.<br/>                                                  |
| [**EventID**](-wiaaut-ideviceevent-eventid.md)<br/>                       | Read-only<br/> | Retrieves the [**EventID Constants**](-wiaaut-consts-eventid.md) for this **DeviceEvent**.<br/> |
| [**Name (DeviceEvent)**](-wiaaut-ideviceevent-name.md)<br/>               | Read-only<br/> | Retrieves the **DeviceEvent** name.<br/>                                                         |
| [**Type (DeviceEvent)**](-wiaaut-ideviceevent-type.md)<br/>               | Read-only<br/> | Retrieves the type of this **DeviceEvent**.<br/>                                                 |



 

## Remarks

Note that while the most common event IDs are provided as constants, not all [**EventID Constants**](-wiaaut-consts-eventid.md) are supported for all imaging devices.

For example code, see [Enumerate all the Supported Events for the Selected Device](-wiaaut-shared-samples.md#enumerate-all-the-supported-events-for-the-selected-device) in Shared Samples.

### Creation\\Access Functions

Use any of the following to retrieve a reference to the object:



[**Item (DeviceEvents)**](-wiaaut-ideviceevents-item.md)



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



 

 





