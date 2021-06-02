---
title: WM_UPDATEUISTATE message (Winuser.h)
description: An application sends the WM\_UPDATEUISTATE message to change the UI state for the specified window and all its child windows.
ms.assetid: cbdeeddd-59b2-4a73-bfe9-17647d32bcf3
keywords:
- WM_UPDATEUISTATE message Menus and Other Resources
topic_type:
- apiref
api_name:
- WM_UPDATEUISTATE
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_UPDATEUISTATE message

An application sends the **WM\_UPDATEUISTATE** message to change the UI state for the specified window and all its child windows.


```C++
#define WM_UPDATEUISTATE                0x0128
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The low-order word specifies the action to be performed. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                   | Meaning                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="UIS_CLEAR"></span><span id="uis_clear"></span><dl> <dt>**UIS\_CLEAR**</dt> <dt>2</dt> </dl>                | The UI state element specified by the high-order word should be hidden.<br/>                                                                   |
| <span id="UIS_INITIALIZE"></span><span id="uis_initialize"></span><dl> <dt>**UIS\_INITIALIZE**</dt> <dt>3</dt> </dl> | The UI state element specified by the high-order word should be changed based on the last input event. For more information, see Remarks.<br/> |
| <span id="UIS_SET"></span><span id="uis_set"></span><dl> <dt>**UIS\_SET**</dt> <dt>1</dt> </dl>                      | The UI state element specified by the high-order word should be visible.<br/>                                                                  |



 

The high-order word specifies which UI state elements are affected or the style of the control. This parameter can be one or more of the following values.



| Value                                                                                                                                                                                                                     | Meaning                                                                     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <span id="UISF_ACTIVE"></span><span id="uisf_active"></span><dl> <dt>**UISF\_ACTIVE**</dt> <dt>0x4</dt> </dl>          | A control should be drawn in the style used for active controls.<br/> |
| <span id="UISF_HIDEACCEL"></span><span id="uisf_hideaccel"></span><dl> <dt>**UISF\_HIDEACCEL**</dt> <dt>0x2</dt> </dl> | Keyboard accelerators.<br/>                                           |
| <span id="UISF_HIDEFOCUS"></span><span id="uisf_hidefocus"></span><dl> <dt>**UISF\_HIDEFOCUS**</dt> <dt>0x1</dt> </dl> | Focus indicators.<br/>                                                |



 

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Remarks

A window should send this message to change the UI state of all its child windows. In contrast to the [**WM\_CHANGEUISTATE**](wm-changeuistate.md) message, which is a notification, when [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) processes the **WM\_UPDATEUISTATE** message it changes the UI state and propagates the changes to all child windows.

The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function updates the UI state according to the *wParam* value. If the UI state is modified, the function sends the message to all the immediate child windows. **DefWindowProc** also sends this message when it receives a [**WM\_CHANGEUISTATE**](wm-changeuistate.md) message notifying the system that a child window intends to modify the UI state.

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

[**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca)
</dt> <dt>

[**WM\_CHANGEUISTATE**](wm-changeuistate.md)
</dt> <dt>

[**WM\_QUERYUISTATE**](wm-queryuistate.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Keyboard Accelerators](keyboard-accelerators.md)
</dt> </dl>

 

