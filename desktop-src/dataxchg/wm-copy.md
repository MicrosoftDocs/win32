---
title: WM_COPY message (Winuser.h)
description: An application sends the WM\_COPY message to an edit control or combo box to copy the current selection to the clipboard in CF\_TEXT format.
ms.assetid: dcac3ad3-1e70-4b71-accd-261587224e60
keywords:
- WM_COPY message Data Exchange
topic_type:
- apiref
api_name:
- WM_COPY
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_COPY message

An application sends the **WM\_COPY** message to an edit control or combo box to copy the current selection to the clipboard in [**CF\_TEXT**](standard-clipboard-formats.md) format.


```C++
#define WM_COPY                         0x0301
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

Returns nonzero value on success, else zero.

## Remarks

When sent to a combo box, the **WM\_COPY** message is handled by its edit control. This message has no effect when sent to a combo box with the [**CBS\_DROPDOWNLIST**](../controls/combo-box-styles.md) style.

## Requirements



| Requirement | Value |
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

[**WM\_CUT**](wm-cut.md)
</dt> <dt>

[**WM\_PASTE**](wm-paste.md)
</dt> <dt>

[**WM\_UNDO**](/windows/desktop/Controls/wm-undo)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Clipboard](clipboard.md)
</dt> </dl>

 

