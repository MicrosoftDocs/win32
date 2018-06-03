---
title: OnGraphicsStreamPaused event
description: Called when the graphics stream has been paused.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6c18d0d5-fc02-4db2-91ad-6ab6ff34535f
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnGraphicsStreamPaused event RDP
topic_type:
- apiref
api_name:
- OnGraphicsStreamPaused
api_location:
- RdpEncom.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OnGraphicsStreamPaused event

Called when the graphics stream has been paused.

## Syntax


```C++
void OnGraphicsStreamPaused();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

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
</dt> <dt>

[**IRDPSRAPISharingSession::Pause**](/windows/desktop/api/RdpEncomAPI/nf-rdpencomapi-irdpsrapisharingsession-pause)
</dt> </dl>

 

 





