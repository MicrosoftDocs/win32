---
title: OnWindowClose event
description: Called when a sharable top-level window is closed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '68afa225-cba9-4b1a-8547-a404972c7dd9'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["OnWindowClose event RDP"]
topic_type:
- apiref
api_name:
- OnWindowClose
api_location:
- RdpEncom.dll
api_type:
- COM
---

# OnWindowClose event

Called when a sharable top-level window is closed.

## Syntax


```C++
void OnWindowClose(
  [in] IDispatch *pWindow
);
```



## Parameters

<dl> <dt>

*pWindow* \[in\]
</dt> <dd>

The sharable top-level window that closed. Query the **IDispatch** interface for the [**IRDPSRAPIWindow**](irdpsrapiwindow.md) interface that you use to retrieve information about the window.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

If this is the last window corresponding to the application, then this event is immediately followed by the [**OnApplicationClose**](onapplicationclose.md) event.

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

 

 





