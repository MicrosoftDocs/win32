---
title: TTM_GETTEXT message (Commctrl.h)
description: Retrieves the information a tooltip control maintains about a tool.
ms.assetid: f2afa706-4209-4761-a981-df3d5b938c88
keywords:
- TTM_GETTEXT message Windows Controls
topic_type:
- apiref
api_name:
- TTM_GETTEXT
- TTM_GETTEXTA
- TTM_GETTEXTW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_GETTEXT message

Retrieves the information a tooltip control maintains about a tool.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>The number of **TCHARs**, including the terminating **NULL**, to copy to the buffer pointed to by **lpszText**. </dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa) structure. Set the **cbSize** member of this structure to `sizeof(TOOLINFO)` before sending this message. Set the **hwnd** and **uId** members to identify the tool for which to retrieve information. Allocate a buffer of size specified by *wParam*. Set the **lpszText** member to point to the buffer to receive the tool text.

</dd> </dl>

## Return value

No return value.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TTM\_GETTEXTW** (Unicode) and **TTM\_GETTEXTA** (ANSI)<br/>                   |



 

 





