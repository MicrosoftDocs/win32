---
title: OnSharedRectChanged event
description: Called when the size of the shared top-level window of the application changes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a361bb88-0540-4264-8b46-510d29058fca
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnSharedRectChanged event RDP
topic_type:
- apiref
api_name:
- OnSharedRectChanged
api_location:
- RdpEncom.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OnSharedRectChanged event

Called when the size of the shared top-level window of the application changes.

## Syntax


```C++
void OnSharedRectChanged(
  [in] long left,
  [in] long top,
  [in] long right,
  [in] long bottom
);
```



## Parameters

<dl> <dt>

*left* \[in\]
</dt> <dd>

Left edge of the window, in pixels.

</dd> <dt>

*top* \[in\]
</dt> <dd>

Top edge of the window, in pixels.

</dd> <dt>

*right* \[in\]
</dt> <dd>

Right edge of the window, in pixels.

</dd> <dt>

*bottom* \[in\]
</dt> <dd>

Bottom edge of the window, in pixels.

</dd> </dl>

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
</dt> </dl>

 

 





