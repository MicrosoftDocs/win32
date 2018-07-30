---
title: WM\_PASTE message
description: An application sends a WM\_PASTE message to an edit control or combo box to copy the current content of the clipboard to the edit control at the current caret position. Data is inserted only if the clipboard contains data in CF\_TEXT format.
ms.assetid: 6830b511-986f-46ef-a977-7adedffe86ea
keywords:
- WM_PASTE message Data Exchange
topic_type:
- apiref
api_name:
- WM_PASTE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_PASTE message

An application sends a **WM\_PASTE** message to an edit control or combo box to copy the current content of the clipboard to the edit control at the current caret position. Data is inserted only if the clipboard contains data in [**CF\_TEXT**](standard-clipboard-formats.md) format.


```C++
#define WM_PASTE                        0x0302
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> </dl>

## Return value

This message does not return a value.

## Remarks

When sent to a combo box, the **WM\_PASTE** message is handled by its edit control. This message has no effect when sent to a combo box with the [**CBS\_DROPDOWNLIST**](https://msdn.microsoft.com/library/Bb775796(v=VS.85).aspx) style.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**WM\_CLEAR**](wm-clear.md)
</dt> <dt>

[**WM\_COPY**](wm-copy.md)
</dt> <dt>

[**WM\_CUT**](wm-cut.md)
</dt> <dt>

[**WM\_UNDO**](https://msdn.microsoft.com/library/windows/desktop/bb761693)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Clipboard](clipboard.md)
</dt> </dl>

 

 





