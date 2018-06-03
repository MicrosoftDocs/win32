---
title: OnGraphicsStreamResumed event
description: Called when the graphics stream has been resumed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6f0665a1-89b6-4b3d-8773-607207b76397
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnGraphicsStreamResumed event RDP
topic_type:
- apiref
api_name:
- OnGraphicsStreamResumed
api_location:
- RdpEncom.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OnGraphicsStreamResumed event

Called when the graphics stream has been resumed.

## Syntax


```C++
void OnGraphicsStreamResumed();
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

[**IRDPSRAPISharingSession::Resume**](/windows/desktop/api/RdpEncomAPI/nf-rdpencomapi-irdpsrapisharingsession-resume)
</dt> </dl>

 

 





