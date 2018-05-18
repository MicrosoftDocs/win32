---
title: OnChannelDataReceived event
description: Called when data is received from an attendee.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '6bd71aad-66a0-46e4-8e0e-c59cae694de7'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["OnChannelDataReceived event RDP"]
topic_type:
- apiref
api_name:
- OnChannelDataReceived
api_location:
- RdpEncom.dll
api_type:
- COM
---

# OnChannelDataReceived event

Called when data is received from an attendee.

## Syntax


```C++
void OnChannelDataReceived(
  [in] IUnknown *pChannel,
  [in] long     lAttendeeId,
  [in] BSTR     bstrData
);
```



## Parameters

<dl> <dt>

*pChannel* \[in\]
</dt> <dd>

Channel that received the data.

</dd> <dt>

*lAttendeeId* \[in\]
</dt> <dd>

Identifies the attendee who sent the data. To get the attendee, use the identifier when accessing the [**Item Property of IRDPSRAPIAttendeeManager**](irdpsrapiattendeemanager-item.md).

</dd> <dt>

*bstrData* \[in\]
</dt> <dd>

Data received.

</dd> </dl>

## Return value

This event does not return a value.

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

 

 





