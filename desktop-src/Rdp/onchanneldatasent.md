---
title: OnChannelDataSent event
description: Called when data is sent to the client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4f01145a-16ac-452a-839b-24d01a094a42'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["OnChannelDataSent event RDP"]
topic_type:
- apiref
api_name:
- OnChannelDataSent
api_location:
- RdpEncom.dll
api_type:
- COM
---

# OnChannelDataSent event

Called when data is sent to the client.

## Syntax


```C++
void OnChannelDataSent(
  [in] IUnknown *pChannel,
  [in] long     lAttendeeId,
  [in] long     BytesSent
);
```



## Parameters

<dl> <dt>

*pChannel* \[in\]
</dt> <dd>

Channel that sent the data.

</dd> <dt>

*lAttendeeId* \[in\]
</dt> <dd>

Identifies the attendee who is sending the data. To get the attendee, use the identifier when accessing the [**Item Property of IRDPSRAPIAttendeeManager**](irdpsrapiattendeemanager-item.md).

</dd> <dt>

*BytesSent* \[in\]
</dt> <dd>

Size, in bytes, of the channel data.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

Applications use this notification to determine when to send data to the clients. After a call to [**IRDPSRAPIVirtualChannel::SendData**](irdpsrapivirtualchannel-senddata.md) fails with **E\_PENDING**, applications should stop sending data until they receive this notification.

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

 

 





