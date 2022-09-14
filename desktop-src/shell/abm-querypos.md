---
description: Requests a size and screen position for an appbar.
ms.assetid: 061a30fb-a68a-464e-ad8c-0bda672b57d9
title: ABM_QUERYPOS message (Shellapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ABM\_QUERYPOS message

Requests a size and screen position for an appbar. When the request is made, the message proposes a screen edge and a bounding rectangle for the appbar. The system adjusts the bounding rectangle so that the appbar does not interfere with the Windows taskbar or any other appbars.


```C++
SHAppBarMessage(ABM_QUERYPOS, pabd); 
```



## Parameters

<dl> <dt>

*pabd* 
</dt> <dd>

A pointer to an [**APPBARDATA**](/windows/desktop/api/Shellapi/ns-shellapi-appbardata) structure. The **uEdge** member specifies a screen edge, and the **rc** member contains the proposed bounding rectangle. When the [**SHAppBarMessage**](/windows/desktop/api/Shellapi/nf-shellapi-shappbarmessage) function returns, **rc** contains the approved bounding rectangle. You must specify the **cbSize**, **hWnd**, **uEdge**, and **rc** members when sending this message; all other members are ignored.

</dd> </dl>

## Return value

Always returns **TRUE**.

## Remarks

An appbar should send this message before sending the [**ABM\_SETPOS**](abm-setpos.md) message.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Shellapi.h</dt> </dl> |



 

 




