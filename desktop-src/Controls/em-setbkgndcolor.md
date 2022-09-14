---
title: EM_SETBKGNDCOLOR message (Richedit.h)
description: The EM\_SETBKGNDCOLOR message sets the background color for a rich edit control.
ms.assetid: 0ad191cd-6370-493e-bfe2-5aa8d81ed999
keywords:
- EM_SETBKGNDCOLOR message Windows Controls
topic_type:
- apiref
api_name:
- EM_SETBKGNDCOLOR
api_location:
- Richedit.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EM\_SETBKGNDCOLOR message

The **EM\_SETBKGNDCOLOR** message sets the background color for a rich edit control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Specifies whether to use the system color. If this parameter is a nonzero value, the background is set to the window background system color. Otherwise, the background is set to the specified color.

</dd> <dt>

*lParam* 
</dt> <dd>

A [**COLORREF**](/windows/desktop/gdi/colorref) structure specifying the color if *wParam* is zero. To generate a **COLORREF**, use the [**RGB**](/windows/desktop/api/wingdi/nf-wingdi-rgb) macro.

</dd> </dl>

## Return value

This message returns the original background color.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Richedit.h</dt> </dl> |



## See also

<dl> <dt>

**Other Resources**
</dt> <dt>

[**COLORREF**](/windows/desktop/gdi/colorref)
</dt> <dt>

[**RGB**](/windows/desktop/api/wingdi/nf-wingdi-rgb)
</dt> </dl>

 

