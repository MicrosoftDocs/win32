---
title: TB_SETBUTTONSIZE message (Commctrl.h)
description: Sets the size of buttons on a toolbar.
ms.assetid: ef6beed7-a3d6-4379-b9c1-c64a5e33ce78
keywords:
- TB_SETBUTTONSIZE message Windows Controls
topic_type:
- apiref
api_name:
- TB_SETBUTTONSIZE
api_location:
- Commctrl.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# TB\_SETBUTTONSIZE message

Sets the size of buttons on a toolbar.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) specifies the width, in pixels, of the buttons. The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) specifies the height, in pixels, of the buttons.

</dd> </dl>

## Return value

Returns **TRUE** if successful, or **FALSE** otherwise.

## Remarks

**TB\_SETBUTTONSIZE** should generally be called after adding buttons.

Use [**TB\_SETBUTTONWIDTH**](tb-setbuttonwidth.md) to set the maximum and minimum allowed widths for buttons before they are added. Use **TB\_SETBUTTONSIZE** to set the actual size of buttons.

## Examples

The following example code sets the width of buttons to 80 pixels and the height to 30 pixels.


```C++
// hWndToolbar is a handle to the toolbar window.
SendMessage(hWndToolbar, TB_SETBUTTONSIZE, 0, MAKELPARAM(80, 30);
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Commctrl.h</dt> </dl> |



 

