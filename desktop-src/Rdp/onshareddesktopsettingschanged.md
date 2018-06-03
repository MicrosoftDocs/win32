---
title: OnSharedDesktopSettingsChanged event
description: Called when a shared desktop setting changes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c7f7365d-f7d6-4dfe-b473-fbf576f94bc9
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnSharedDesktopSettingsChanged event RDP
topic_type:
- apiref
api_name:
- OnSharedDesktopSettingsChanged
api_location:
- RdpEncom.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OnSharedDesktopSettingsChanged event

Called when a shared desktop setting changes.

## Syntax


```C++
void OnSharedDesktopSettingsChanged(
  [in] long width,
  [in] long height,
  [in] long colordepth
);
```



## Parameters

<dl> <dt>

*width* \[in\]
</dt> <dd>

The control's remote desktop width, in pixels.

</dd> <dt>

*height* \[in\]
</dt> <dd>

The control's remote desktop height, in pixels.

</dd> <dt>

*colordepth* \[in\]
</dt> <dd>

The color depth for the control's connection.

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

 

 





