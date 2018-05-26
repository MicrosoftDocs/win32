---
title: OnAttendeeDisconnected event
description: Called when an attendee disconnects from the session.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4edcd497-8821-46c0-8d44-0b24e4f3f285
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnAttendeeDisconnected event RDP
topic_type:
- apiref
api_name:
- OnAttendeeDisconnected
api_location:
- RdpEncom.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# OnAttendeeDisconnected event

Called when an attendee disconnects from the session.

## Syntax


```C++
void OnAttendeeDisconnected(
  [in] IDispatch *pDisconnectInfo
);
```



## Parameters

<dl> <dt>

*pDisconnectInfo* \[in\]
</dt> <dd>

The attendee that disconnected from the session. Query the **IDispatch** interface for the [**IRDPSRAPIAttendeeDisconnectInfo**](/windows/win32/RdpEncomAPI/nn-rdpencomapi-irdpsrapiattendeedisconnectinfo?branch=master) interface that you use to retrieve information about the disconnect operation.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

Notification is sent when:

-   The client initiated the disconnect request.
-   The server initiated the disconnect request in response to a [**IRDPSRAPIAttendee::TerminateConnection**](/windows/win32/RdpEncomAPI/nf-rdpencomapi-irdpsrapiattendee-terminateconnection?branch=master) call (for example, the user wants to explicitly disconnect the attendee).
-   The server initiated the disconnect request because there was an error in managing the connection with the attendee.

Notification is not sent when the attendees are disconnected because the session is closing.

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

 

 





