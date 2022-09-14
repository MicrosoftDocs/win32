---
title: WM_GETHOTKEY message (Winuser.h)
description: Sent to determine the hot key associated with a window.
ms.assetid: 6f527758-e713-47a8-a571-3bf3270f0b33
keywords:
- WM_GETHOTKEY message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_GETHOTKEY
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_GETHOTKEY message

Sent to determine the hot key associated with a window.


```C++
#define WM_GETHOTKEY                    0x0033
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Not used; must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

Not used; must be zero.

</dd> </dl>

## Return value

The return value is the virtual-key code and modifiers for the hot key, or **NULL** if no hot key is associated with the window. The virtual-key code is in the low byte of the return value and the modifiers are in the high byte. The modifiers can be a combination of the following flags from CommCtrl.h.



| Return code/value                                                                                                                                         | Description             |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| <dl> <dt>**HOTKEYF\_ALT**</dt> <dt>0x04</dt> </dl>     | ALT key<br/>      |
| <dl> <dt>**HOTKEYF\_CONTROL**</dt> <dt>0x02</dt> </dl> | CTRL key<br/>     |
| <dl> <dt>**HOTKEYF\_EXT**</dt> <dt>0x08</dt> </dl>     | Extended key<br/> |
| <dl> <dt>**HOTKEYF\_SHIFT**</dt> <dt>0x01</dt> </dl>   | SHIFT key<br/>    |



 

## Remarks

These hot keys are unrelated to the hot keys set by the [**RegisterHotKey**](/windows/win32/api/winuser/nf-winuser-registerhotkey) function.

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

[**RegisterHotKey**](/windows/win32/api/winuser/nf-winuser-registerhotkey)
</dt> <dt>

[**WM\_SETHOTKEY**](wm-sethotkey.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Input](keyboard-input.md)
</dt> </dl>

 

