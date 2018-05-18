---
title: OnAttendeeConnected event
description: Called when an attendee connects to the session.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cf3c41c9-d572-433a-ba80-960d38296749'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["OnAttendeeConnected event RDP"]
topic_type:
- apiref
api_name:
- OnAttendeeConnected
api_location:
- RdpEncom.dll
api_type:
- COM
---

# OnAttendeeConnected event

Called when an attendee connects to the session.

## Syntax


```C++
void OnAttendeeConnected(
  [in] IDispatch *pAttendee
);
```



## Parameters

<dl> <dt>

*pAttendee* \[in\]
</dt> <dd>

The attendee that connected to the session. Query the **IDispatch** interface for the [**IRDPSRAPIAttendee**](irdpsrapiattendee.md) interface that you use to retrieve information about the attendee.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

This event means that the attendee has gone through the connection sequence and the client is ready to receive graphics data. The client is already authenticated based on the ticket and password sent in the security data. The client though is not able to view or control the session at this point because its [**control level property**](irdpsrapiattendee-controllevel.md) is set to CTRL\_LEVEL\_NONE.

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

 

 





