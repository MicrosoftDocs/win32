---
title: PGM_SETSCROLLINFO message (Commctrl.h)
description: Sets the scrolling parameters of the pager control, including the timeout value, the lines per timeout, and the pixels per line. You can send this message explicitly or by using the Pager\_SetScrollInfo macro.
ms.assetid: e02450b8-f2b5-45b2-9395-d7412119849c
keywords:
- PGM_SETSCROLLINFO message Windows Controls
topic_type:
- apiref
api_name:
- PGM_SETSCROLLINFO
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# PGM\_SETSCROLLINFO message

\[Intended for internal use; not recommended for use in applications. This message may not be supported in future versions of Windows.\]

Sets the scrolling parameters of the pager control, including the timeout value, the lines per timeout, and the pixels per line. You can send this message explicitly or by using the [**Pager\_SetScrollInfo**](/windows/desktop/api/Commctrl/nf-commctrl-pager_setscrollinfo) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A **UINT** that specifies the timeout value for the scroll, in milliseconds.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) is a **UINT** that specifies the number of lines to scroll per timeout. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) is a **UINT** that specifies the number of pixels per line.

</dd> </dl>

## Return value

The return value is not used.

## Security Considerations

Using this message might compromise the security of your program.

## Remarks

The *wParam* timeout value controls the rate at which the pager control generates scrolling events when the control has captured the mouse input and the left mouse button is pressed. Smaller values result in faster scrolling; larger values result in slower scrolling. The default value is one-eighth of the double-click time. For more information, see [**GetDoubleClickTime**](/windows/desktop/api/winuser/nf-winuser-getdoubleclicktime).

By default, with each scrolling event the pager control scrolls an amount equal to the entire width or height of the control, depending on whether the pager control has a horizontal or vertical orientation. The values in *lParam* are used to override the default scrolling amount. If nonzero values are provided, the scrolling amount is the product of the two values (LOWORD(*lParam*) \* HIWORD(*lParam*)).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



## See also

<dl> <dt>

[**Pager\_SetScrollInfo**](/windows/desktop/api/Commctrl/nf-commctrl-pager_setscrollinfo)
</dt> </dl>

 

