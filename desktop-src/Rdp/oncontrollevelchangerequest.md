---
title: OnControlLevelChangeRequest event
description: Called when a viewer requests control.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '24021ff3-6dde-40c4-9dac-279442bd085d'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["OnControlLevelChangeRequest event RDP"]
topic_type:
- apiref
api_name:
- OnControlLevelChangeRequest
api_location:
- RdpEncom.dll
api_type:
- COM
---

# OnControlLevelChangeRequest event

Called when a viewer requests control.

## Syntax


```C++
void OnControlLevelChangeRequest(
  [in] IDispatch  *pAttendee,
  [in] CTRL_LEVEL RequestedLevel
);
```



## Parameters

<dl> <dt>

*pAttendee* \[in\]
</dt> <dd>

Attendee that requests control. Query the **IDispatch** interface for the [**IRDPSRAPIAttendee**](irdpsrapiattendee.md) interface that you use to retrieve information about the attendee.

</dd> <dt>

*RequestedLevel* \[in\]
</dt> <dd>

Level of control requested by the attendee. For possible values, see the [**CTRL\_LEVEL**](ctrl-level.md) enumeration.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

Any authenticated attendee can request a control level change.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>RdpEncomAPI.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>RdpEncomAPI.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>RdpEncomAPI.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RdpEncom.dll</dt> </dl>    |



## See also

<dl> <dt>

[**\_IRDPSessionEvents**](-irdpsessionevents.md)
</dt> </dl>

 

 





