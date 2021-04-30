---
title: WM_CHANGEUISTATE message (Winuser.h)
description: An application sends the WM\_CHANGEUISTATE message to indicate that the UI state should be changed.
ms.assetid: d8dfc2fe-c64f-4e7e-b021-127aa85d5dd6
keywords:
- WM_CHANGEUISTATE message Menus and Other Resources
topic_type:
- apiref
api_name:
- WM_CHANGEUISTATE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_CHANGEUISTATE message

An application sends the **WM\_CHANGEUISTATE** message to indicate that the UI state should be changed.


```C++
#define WM_CHANGEUISTATE                0x0127
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The low-order word specifies the action to be taken. This member can be one of the following values.



| Value                                                                                                                                                                                                                   | Meaning                                                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="UIS_CLEAR"></span><span id="uis_clear"></span><dl> <dt>**UIS\_CLEAR**</dt> <dt>2</dt> </dl>                | The UI state flags specified by the high-order word should be cleared.<br/>                                                                  |
| <span id="UIS_INITIALIZE"></span><span id="uis_initialize"></span><dl> <dt>**UIS\_INITIALIZE**</dt> <dt>3</dt> </dl> | The UI state flags specified by the high-order word should be changed based on the last input event. For more information, see Remarks.<br/> |
| <span id="UIS_SET"></span><span id="uis_set"></span><dl> <dt>**UIS\_SET**</dt> <dt>1</dt> </dl>                      | The UI state flags specified by the high-order word should be set.<br/>                                                                      |



 

The high-order word specifies which UI state elements are affected or the style of the control. This member can be one or more of the following values.



| Value                                                                                                                                                                                                                     | Meaning                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <span id="UISF_ACTIVE"></span><span id="uisf_active"></span><dl> <dt>**UISF\_ACTIVE**</dt> <dt>0x4</dt> </dl>          | A control should be drawn in the style used for active controls.<br/> |
| <span id="UISF_HIDEACCEL"></span><span id="uisf_hideaccel"></span><dl> <dt>**UISF\_HIDEACCEL**</dt> <dt>0x2</dt> </dl> | Keyboard accelerators are hidden.<br/>                                |
| <span id="UISF_HIDEFOCUS"></span><span id="uisf_hidefocus"></span><dl> <dt>**UISF\_HIDEFOCUS**</dt> <dt>0x1</dt> </dl> | Focus indicators are hidden.<br/>                                     |



 

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used and must be 0.

</dd> </dl>

## Remarks

A window should send this message to itself or its parent when it must change the UI state elements of all windows in the same hierarchy. The window procedure must let [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) process this message so that the entire window tree has a consistent UI state. When the top-level window receives the **WM\_CHANGEUISTATE** message, it sends a [**WM\_UPDATEUISTATE**](wm-updateuistate.md) message with the same parameters to all child windows. When the system processes the **WM\_UPDATEUISTATE** message, it makes the change in the UI state.

If the low-order word of *wParam* is UIS\_INITIALIZE, the system will send the [**WM\_UPDATEUISTATE**](wm-updateuistate.md) message with a UI state based on the last input event. For example, if the last input came from the mouse, the system will hide the keyboard cues. And, if the last input came from the keyboard, the system will show the keyboard cues. If the state that results from processing **WM\_CHANGEUISTATE** is the same as the old state, [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) does not send this message.

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

[**WM\_QUERYUISTATE**](wm-queryuistate.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Accelerators](keyboard-accelerators.md)
</dt> </dl>

 

