---
title: OnConnectionFailed event
description: Called when the client fails to connect to the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e18284cc-9b43-4764-9c4e-d6a86cbd071f'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["OnConnectionFailed event RDP"]
topic_type:
- apiref
api_name:
- OnConnectionFailed
api_location:
- RdpEncom.dll
api_type:
- COM
---

# OnConnectionFailed event

Called when the client fails to connect to the server.

## Syntax


```C++
void OnConnectionFailed();
```



## Parameters

This event has no parameters.

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

 

 





