---
title: OnApplicationClose event
description: Called when an application closes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1fe853ec-f584-43c4-8980-3ed1884bcfaf'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["OnApplicationClose event RDP"]
topic_type:
- apiref
api_name:
- OnApplicationClose
api_location:
- RdpEncom.dll
api_type:
- COM
---

# OnApplicationClose event

Called when an application closes.

## Syntax


```C++
void OnApplicationClose(
  [in] IDispatch *pApplication
);
```



## Parameters

<dl> <dt>

*pApplication* \[in\]
</dt> <dd>

The application that was closed. Query the **IDispatch** interface for the [**IRDPSRAPIApplication**](irdpsrapiapplication.md) interface that you use to retrieve information about the application.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

An Application object is considered destroyed when its last sharable top-level window is destroyed. Note that this event is sent after the [**OnWindowClose**](onwindowclose.md) event is sent.

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

 

 





