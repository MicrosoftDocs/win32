---
title: WM_NOTIFYFORMAT message (Winuser.h)
description: Determines if a window accepts ANSI or Unicode structures in the WM\_NOTIFY notification message. WM\_NOTIFYFORMAT messages are sent from a common control to its parent window and from the parent window to the common control.
ms.assetid: 45ddef45-3300-448d-b609-5fe931b08336
keywords:
- WM_NOTIFYFORMAT message Windows Controls
topic_type:
- apiref
api_name:
- WM_NOTIFYFORMAT
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_NOTIFYFORMAT message

Determines if a window accepts ANSI or Unicode structures in the [**WM\_NOTIFY**](wm-notify.md) notification message. **WM\_NOTIFYFORMAT** messages are sent from a common control to its parent window and from the parent window to the common control.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the window that is sending the **WM\_NOTIFYFORMAT** message. If *lParam* is NF\_QUERY, this parameter is the handle to a control. If *lParam* is NF\_REQUERY, this parameter is the handle to the parent window of a control.

</dd> <dt>

*lParam* 
</dt> <dd>

The command value that specifies the nature of the **WM\_NOTIFYFORMAT** message. This will be one of the following values:



| Value                                                                                                                                                | Meaning                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="NF_QUERY"></span><span id="nf_query"></span><dl> <dt>**NF\_QUERY**</dt> </dl>       | The message is a query to determine whether ANSI or Unicode structures should be used in [**WM\_NOTIFY**](wm-notify.md) messages. This command is sent from a control to its parent window during the creation of a control and in response to an NF\_REQUERY command.<br/>                                                                                                         |
| <span id="NF_REQUERY"></span><span id="nf_requery"></span><dl> <dt>**NF\_REQUERY**</dt> </dl> | The message is a request for a control to send an NF\_QUERY form of this message to its parent window. This command is sent from the parent window. The parent window is asking the control to requery it about the type of structures to use in [**WM\_NOTIFY**](wm-notify.md) messages. If *lParam* is NF\_REQUERY, the return value is the result of the requery operation.<br/> |



 

</dd> </dl>

## Return value

Returns one of the following values.



| Return code                                                                                 | Description                                                                                                    |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**NFR\_ANSI**</dt> </dl>    | ANSI structures should be used in [**WM\_NOTIFY**](wm-notify.md) messages sent by the control.<br/>     |
| <dl> <dt>**NFR\_UNICODE**</dt> </dl> | Unicode structures should be used in [**WM\_NOTIFY**](wm-notify.md) messages sent by the control. <br/> |
| <dl> <dt>**0**</dt> </dl>            | An error occurred.<br/>                                                                                  |



 

## Remarks

When a common control is created, the control sends a **WM\_NOTIFYFORMAT** message to its parent window to determine the type of structures to use in [**WM\_NOTIFY**](wm-notify.md) messages. If the parent window does not handle this message, the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function responds according to the type of the parent window. That is, if the parent window is a Unicode window, **DefWindowProc** returns NFR\_UNICODE, and if the parent window is an ANSI window, **DefWindowProc** returns NFR\_ANSI. If the parent window is a dialog box and does not handle this message, the [**DefDlgProc**](/windows/desktop/api/winuser/nf-winuser-defdlgprocw) function similarly responds according to the type of the dialog box (Unicode or ANSI).

A parent window can change the type of structures a common control uses in [**WM\_NOTIFY**](wm-notify.md) messages by setting *lParam* to NF\_REQUERY and sending a **WM\_NOTIFYFORMAT** message to the control. This causes the control to send an NF\_QUERY form of the **WM\_NOTIFYFORMAT** message to the parent window.

All common controls will send **WM\_NOTIFYFORMAT** messages. However, the standard Windows controls (edit controls, combo boxes, list boxes, buttons, scroll bars, and static controls) do not.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl> |



 

