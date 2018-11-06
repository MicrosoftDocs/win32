---
title: WM_CUT message
description: An application sends a WM\_CUT message to an edit control or combo box to delete (cut) the current selection, if any, in the edit control and copy the deleted text to the clipboard in CF\_TEXT format.
ms.assetid: 6ac45589-3e34-491c-9562-e072ddc478f9
keywords:
- WM_CUT message Data Exchange
topic_type:
- apiref
api_name:
- WM_CUT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: article
ms.date: 05/31/2018
---

# WM\_CUT message

An application sends a **WM\_CUT** message to an edit control or combo box to delete (cut) the current selection, if any, in the edit control and copy the deleted text to the clipboard in [**CF\_TEXT**](standard-clipboard-formats.md) format.


```C++
#define WM_CUT                          0x0300
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

The deletion performed by the **WM\_CUT** message can be undone by sending the edit control an [**EM\_UNDO**](https://msdn.microsoft.com/library/Bb761670(v=VS.85).aspx) message.

To delete the current selection without placing the deleted text on the clipboard, use the [**WM\_CLEAR**](wm-clear.md) message.

When sent to a combo box, the **WM\_CUT** message is handled by its edit control. This message has no effect when sent to a combo box with the [**CBS\_DROPDOWNLIST**](https://msdn.microsoft.com/library/Bb775796(v=VS.85).aspx) style.

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

[**WM\_PASTE**](wm-paste.md)
</dt> <dt>

[**WM\_UNDO**](https://msdn.microsoft.com/library/windows/desktop/bb761693)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Clipboard](clipboard.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**EM\_UNDO**](https://msdn.microsoft.com/library/Bb761670(v=VS.85).aspx)
</dt> </dl>

 

 





