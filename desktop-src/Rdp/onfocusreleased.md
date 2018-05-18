---
title: OnFocusReleased event
description: This event is raised when the user wants to release the focus out of the viewer ActiveX control.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e77cc6d7-3e11-4ee1-bee5-525451396ae8'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["OnFocusReleased event RDP"]
topic_type:
- apiref
api_name:
- OnFocusReleased
api_location:
- RdpEncom.dll
api_type:
- COM
---

# OnFocusReleased event

This event is raised when the user wants to release the focus out of the viewer ActiveX control.

## Syntax


```C++
void OnFocusReleased(
  [in] int iDirection
);
```



## Parameters

<dl> <dt>

*iDirection* \[in\]
</dt> <dd>

The direction that the user intends to move the focus out of the control. A value of -1 indicates left. A value of 1 indicates right.

</dd> </dl>

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

 

 





