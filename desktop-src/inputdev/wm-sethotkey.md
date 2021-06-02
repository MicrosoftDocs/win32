---
title: WM_SETHOTKEY message (Winuser.h)
description: Sent to a window to associate a hot key with the window. When the user presses the hot key, the system activates the window.
ms.assetid: b2c7e6ca-da71-440b-a05e-17f2da419d18
keywords:
- WM_SETHOTKEY message Keyboard and Mouse Input
topic_type:
- apiref
api_name:
- WM_SETHOTKEY
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_SETHOTKEY message

Sent to a window to associate a hot key with the window. When the user presses the hot key, the system activates the window.


```C++
#define WM_SETHOTKEY                    0x0032
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The low-order word specifies the virtual-key code to associate with the window.

The high-order word can be one or more of the following values from CommCtrl.h.

Setting *wParam* to **NULL** removes the hot key associated with a window.



| Value                                                                                                                                                                                                                         | Meaning                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| <span id="HOTKEYF_ALT"></span><span id="hotkeyf_alt"></span><dl> <dt>**HOTKEYF\_ALT**</dt> <dt>0x04</dt> </dl>             | ALT key<br/>      |
| <span id="HOTKEYF_CONTROL"></span><span id="hotkeyf_control"></span><dl> <dt>**HOTKEYF\_CONTROL**</dt> <dt>0x02</dt> </dl> | CTRL key<br/>     |
| <span id="HOTKEYF_EXT"></span><span id="hotkeyf_ext"></span><dl> <dt>**HOTKEYF\_EXT**</dt> <dt>0x08</dt> </dl>             | Extended key<br/> |
| <span id="HOTKEYF_SHIFT"></span><span id="hotkeyf_shift"></span><dl> <dt>**HOTKEYF\_SHIFT**</dt> <dt>0x01</dt> </dl>       | SHIFT key<br/>    |



 

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

The return value is one of the following.



| Return value                                                                  | Description                                                                             |
|-------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <dl> <dt>-1</dt> </dl> | The function is unsuccessful; the hot key is invalid.<br/>                        |
| <dl> <dt>0</dt> </dl>  | The function is unsuccessful; the window is invalid.<br/>                         |
| <dl> <dt>1</dt> </dl>  | The function is successful, and no other window has the same hot key.<br/>        |
| <dl> <dt>2</dt> </dl>  | The function is successful, but another window already has the same hot key.<br/> |



 

## Remarks

A hot key cannot be associated with a child window.

**VK\_ESCAPE**, **VK\_SPACE**, and **VK\_TAB** are invalid hot keys.

When the user presses the hot key, the system generates a [**WM\_SYSCOMMAND**](/windows/desktop/menurc/wm-syscommand) message with *wParam* equal to **SC\_HOTKEY** and *lParam* equal to the window's handle. If this message is passed on to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca), the system will bring the window's last active popup (if it exists) or the window itself (if there is no popup window) to the foreground.

A window can only have one hot key. If the window already has a hot key associated with it, the new hot key replaces the old one. If more than one window has the same hot key, the window that is activated by the hot key is random.

These hot keys are unrelated to the hot keys set by [**RegisterHotKey**](/windows/win32/api/winuser/nf-winuser-registerhotkey).

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

[**WM\_GETHOTKEY**](wm-gethotkey.md)
</dt> <dt>

[**WM\_SYSCOMMAND**](/windows/desktop/menurc/wm-syscommand)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Input](keyboard-input.md)
</dt> </dl>

 

