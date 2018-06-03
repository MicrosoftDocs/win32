---
title: WiaEventFlag enumeration
description: Supplies the bits that make up a DeviceEvent type. You can test a DeviceEvent type by using the AND operation with Type (DeviceEvent) and a member from the WiaEventFlag enumeration.
ms.assetid: 28df53e5-b1e5-4395-9a49-66e4bfcebb25
keywords:
- WiaEventFlag enumeration WIA Automation
- WiaDeviceType enumeration WIA Automation
topic_type:
- apiref
api_name:
- WiaDeviceType
api_location:
- Wiaaut.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# WiaEventFlag enumeration

Supplies the bits that make up a [**DeviceEvent**](-wiaaut-deviceevent.md) type. You can test a **DeviceEvent** type by using the **AND** operation with [**Type (DeviceEvent)**](-wiaaut-ideviceevent-type.md) and a member from the **WiaEventFlag** enumeration.

## Members



| Member                | Description                                                                                                                                        | Value |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| **NotificationEvent** | Indicates that the [**DeviceEvent**](-wiaaut-deviceevent.md) is intended to notify a running application that this event has occurred.<br/> | 0x1   |
| **ActionEvent**       | Indicates that the [**DeviceEvent**](-wiaaut-deviceevent.md) can, if necessary, launch an application if this event occurs.<br/>            | 0x2   |



## Remarks

Because only Action events can have persistent event handlers, it is important to test for this flag before calling [**RegisterPersistentEvent**](-wiaaut-idevicemanager-registerpersistentevent.md).

For example code, see [Determine the Event Type](https://www.bing.com/search?q=Determine the Event Type) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



 

 





