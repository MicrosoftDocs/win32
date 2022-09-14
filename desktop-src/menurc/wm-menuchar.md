---
title: WM_MENUCHAR message (Winuser.h)
description: Sent when a menu is active and the user presses a key that does not correspond to any mnemonic or accelerator key. This message is sent to the window that owns the menu.
ms.assetid: de6c91bb-80fd-44b2-8d96-d016477a6547
keywords:
- WM_MENUCHAR message Menus and Other Resources
topic_type:
- apiref
api_name:
- WM_MENUCHAR
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_MENUCHAR message

Sent when a menu is active and the user presses a key that does not correspond to any mnemonic or accelerator key. This message is sent to the window that owns the menu.


```C++
#define WM_MENUCHAR                     0x0120
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The low-order word specifies the character code that corresponds to the key the user pressed.

The high-order word specifies the active menu type. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                 | Meaning                                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <span id="MF_POPUP"></span><span id="mf_popup"></span><dl> <dt>**MF\_POPUP**</dt> <dt>0x00000010L</dt> </dl>       | A drop-down menu, submenu, or shortcut menu.<br/> |
| <span id="MF_SYSMENU"></span><span id="mf_sysmenu"></span><dl> <dt>**MF\_SYSMENU**</dt> <dt>0x00002000L</dt> </dl> | The window menu.<br/>                             |



 

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the active menu.

</dd> </dl>

## Return value

An application that processes this message should return one of the following values in the high-order word of the return value.



| Return code/value                                                                                                                                  | Description                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**MNC\_CLOSE**</dt> <dt>1</dt> </dl>   | Informs the system that it should close the active menu.<br/>                                                                                                                      |
| <dl> <dt>**MNC\_EXECUTE**</dt> <dt>2</dt> </dl> | Informs the system that it should choose the item specified in the low-order word of the return value. The owner window receives a [**WM\_COMMAND**](wm-command.md) message.<br/> |
| <dl> <dt>**MNC\_IGNORE**</dt> <dt>0</dt> </dl>  | Informs the system that it should discard the character the user pressed and create a short beep on the system speaker.<br/>                                                       |
| <dl> <dt>**MNC\_SELECT**</dt> <dt>3</dt> </dl>  | Informs the system that it should select the item specified in the low-order word of the return value. <br/>                                                                       |



 

## Remarks

The low-order word is ignored if the high-order word contains 0 or 1.

An application should process this message when an accelerator is used to select a menu item that displays a bitmap.

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

[**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85))
</dt> <dt>

[**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85))
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Accelerators](keyboard-accelerators.md)
</dt> </dl>

 

