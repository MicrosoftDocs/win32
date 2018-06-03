---
title: OnError event
description: Called when a critical error occurs in the session.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d3475a78-def9-4bd7-8dad-34a39632b542
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnError event RDP
topic_type:
- apiref
api_name:
- OnError
api_location:
- RdpEncom.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OnError event

Called when a critical error occurs in the session.

## Syntax


```C++
void OnError(
  [in] VARIANT ErrorInfo
);
```



## Parameters

<dl> <dt>

*ErrorInfo* \[in\]
</dt> <dd>

An **HRESULT** value of the critical error that occurred. The variant type is **VT\_I4** and the **lVal** member of the **VARIANT** contains the **HRESULT** value.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

If you receive this notification, you should consider the session terminated and should destroy the RDPSession object.

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

 

 





