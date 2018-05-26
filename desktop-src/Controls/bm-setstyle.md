---
title: BM\_SETSTYLE message
description: Sets the style of a button. You can send this message explicitly or use the Button\_SetStyle macro.
ms.assetid: 6439e68f-87fc-4a4a-8025-facc3c0e03e2
keywords:
- BM_SETSTYLE message Windows Controls
topic_type:
- apiref
api_name:
- BM_SETSTYLE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BM\_SETSTYLE message

Sets the style of a button. You can send this message explicitly or use the [**Button\_SetStyle**](/windows/win32/Windowsx/nf-windowsx-button_setstyle?branch=master) macro.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The button style. This parameter can be a combination of button styles. For a table of button styles, see [Button Styles](button-styles.md).

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](https://msdn.microsoft.com/library/windows/desktop/ms632659) of *lParam* is a **BOOL** that specifies whether the button is to be redrawn. A value of **TRUE** redraws the button; a value of **FALSE** does not redraw the button.

</dd> </dl>

## Return value

This message always returns zero.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



 

 





