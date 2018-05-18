---
title: OnConnectionAuthenticated event
description: Called when the connection is authenticated.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '951545a9-367f-4516-9c32-dae967284427'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["OnConnectionAuthenticated event RDP"]
topic_type:
- apiref
api_name:
- OnConnectionAuthenticated
api_location:
- RdpEncom.dll
api_type:
- COM
---

# OnConnectionAuthenticated event

Called when the connection is authenticated.

## Syntax


```C++
void OnConnectionAuthenticated();
```



## Parameters

This event has no parameters.

## Return value

This event does not return a value.

## Remarks

If the authentication fails, the client will be disconnected and the [**OnConnectionTerminated**](onconnectionterminated.md) event may include an extended code of 0x0300.

This event occurs after the [**OnConnectionEstablished**](onconnectionestablished.md) event.

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

 

 





