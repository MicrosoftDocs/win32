---
title: OnControlLevelChangeRequest event
description: Called when a viewer requests control.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 24021ff3-6dde-40c4-9dac-279442bd085d
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnControlLevelChangeRequest event RDP
topic_type:
- apiref
api_name:
- OnControlLevelChangeRequest
api_location:
- RdpEncom.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# OnControlLevelChangeRequest event

Called when a viewer requests control.

## Syntax


```C++
void OnControlLevelChangeRequest(
  [in] IDispatch  *pAttendee,
  [in] CTRL_LEVEL RequestedLevel
);
```



## Parameters

<dl> <dt>

*pAttendee* \[in\]
</dt> <dd>

Attendee that requests control. Query the **IDispatch** interface for the [**IRDPSRAPIAttendee**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiattendee?branch=master) interface that you use to retrieve information about the attendee.

</dd> <dt>

*RequestedLevel* \[in\]
</dt> <dd>

Level of control requested by the attendee. For possible values, see the [**CTRL\_LEVEL**](/windows/win32/Rdpencomapi/ne-rdpencomapi-__midl___midl_itf_rdpencomapi_0000_0000_0001?branch=master) enumeration.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

Any authenticated attendee can request a control level change.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps \| UWP apps\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps \| UWP apps\]<br/>                                |
| Header<br/>                   | <dl> <dt>RdpEncomAPI.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>RdpEncomAPI.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>RdpEncomAPI.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RdpEncom.dll</dt> </dl>    |



## See also

<dl> <dt>

[**\_IRDPSessionEvents**](/windows/win32/RdpEncomAPI/?branch=master)
</dt> </dl>

 

 





