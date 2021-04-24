---
title: TTM_ENUMTOOLS message (Commctrl.h)
description: Retrieves the information that a tooltip control maintains about the current tool \ 8212;that is, the tool for which the tooltip is currently displaying text.
ms.assetid: c470db71-c24c-45f4-b497-e59811017eee
keywords:
- TTM_ENUMTOOLS message Windows Controls
topic_type:
- apiref
api_name:
- TTM_ENUMTOOLS
- TTM_ENUMTOOLSA
- TTM_ENUMTOOLSW
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TTM\_ENUMTOOLS message

Retrieves the information that a tooltip control maintains about the current tool that is, the tool for which the tooltip is currently displaying text.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Zero-based index of the tool for which to retrieve information.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to a [**TOOLINFO**](/windows/win32/api/commctrl/ns-commctrl-tttoolinfoa) structure that receives information about the tool. Set the **cbSize** member of this structure to sizeof(TOOLINFO) before sending this message. Allocate a buffer. Set the **lpszText** member to point to the buffer to receive the tool text. There is no way to determine the required buffer size. However, tool text, as returned at the **lpszText** member of the **TOOLINFO** structure, has a maximum length of 80 **TCHARs**, including the terminating **NULL**. If the text exceeds this length, it is truncated.

</dd> </dl>

## Return value

Returns **FALSE** whether or not a tool is enumerated.

## Remarks

**Security Warning:** Using this message might compromise the security of your program. This message does not provide a way for the message receiver to know the size of the buffer or to specify the size of the buffer. You should review the [Security Considerations: Microsoft Windows Controls](sec-comctls.md) before continuing.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **TTM\_ENUMTOOLSW** (Unicode) and **TTM\_ENUMTOOLSA** (ANSI)<br/>               |



 

 





