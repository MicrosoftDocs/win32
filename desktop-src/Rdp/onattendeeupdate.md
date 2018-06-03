---
title: OnAttendeeUpdate event
description: Called when one of the property values for an attendee changes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 18cd01cb-bf39-4dee-af94-409ce3f76637
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnAttendeeUpdate event RDP
topic_type:
- apiref
api_name:
- OnAttendeeUpdate
api_location:
- RdpEncom.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OnAttendeeUpdate event

Called when one of the property values for an attendee changes.

## Syntax


```C++
void OnAttendeeUpdate(
  [in] IDispatch *pAttendee
);
```



## Parameters

<dl> <dt>

*pAttendee* \[in\]
</dt> <dd>

The attendee whose property values changed. Query the **IDispatch** interface for the [**IRDPSRAPIAttendee**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiattendee) interface that you use to retrieve information about the attendee.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

You should query all the properties of the attendee and update the user interface accordingly.

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

[**\_IRDPSessionEvents**](/windows/desktop/api/RdpEncomAPI/)
</dt> </dl>

 

 





