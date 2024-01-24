---
title: WM_NOTIFY message (Winuser.h)
description: Sent by a common control to its parent window when an event has occurred or the control requires some information.
ms.assetid: 'vs|controls|~\controls\common\messages\wm_notify.htm'
keywords:
- WM_NOTIFY message Windows Controls
topic_type:
- apiref
api_name:
- WM_NOTIFY
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_NOTIFY message

Sent by a common control to its parent window when an event has occurred or the control requires some information.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The identifier of the common control sending the message. This identifier is not guaranteed to be unique. An application should use the **hwndFrom** or **idFrom** member of the [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure (passed as the *lParam* parameter) to identify the control.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure that contains the notification code and additional information. For some notification messages, this parameter points to a larger structure that has the **NMHDR** structure as its first member.

</dd> </dl>

## Return value

The return value is ignored except for notification messages that specify otherwise.

## Remarks

The destination of the message must be the **HWND** of the parent of the control. This value can be obtained by using [**GetParent**](/windows/desktop/api/winuser/nf-winuser-getparent), as shown in the following example, where *m\_controlHwnd* is the **HWND** of the control itself.


```
NMHDR nmh;
nmh.code = CUSTOM_SELCHANGE;    // Message type defined by control.
nmh.idFrom = GetDlgCtrlID(m_controlHwnd);
nmh.hwndFrom = m_controlHwnd;
SendMessage(GetParent(m_controlHwnd), 
    WM_NOTIFY, 
    nmh.idFrom, 
    (LPARAM)&nmh);
```



Applications handle the message in the window procedure of the parent window, as shown in the following example, which handles the notification message sent by the custom control in the previous example.


```
INT_PTR CALLBACK DlgProc(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {
    case WM_NOTIFY:
        switch (((LPNMHDR)lParam)->code)
        {
        case CUSTOM_SELCHANGE:
            if (((LPNMHDR)lParam)->idFrom == IDC_CUSTOMLISTBOX1)
            {
                ...   // Respond to message.
                return TRUE;
            }
            break; 
        ... // More cases on WM_NOTIFY switch.
        break;
        }
    ...  // More cases on message switch.
    }
    return FALSE;
}
```



Some notifications, chiefly those that have been in the API for a long time, are sent as [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) messages. For more information, see [Control Messages](control-messages.md).

If the message handler is in a dialog box procedure, you must use the [**SetWindowLong**](/windows/desktop/api/winuser/nf-winuser-setwindowlonga) function with DWL\_MSGRESULT to set a return value.

For Windows Vista and later systems, the **WM\_NOTIFY** message cannot be sent between processes.

Many notifications are available in both ANSI and Unicode formats. The window sending the **WM\_NOTIFY** message uses the [**WM\_NOTIFYFORMAT**](wm-notifyformat.md) message to determine which format should be used. See **WM\_NOTIFYFORMAT** for further discussion.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl> |



## See also

<dl> <dt>

[**WM\_NOTIFYFORMAT**](wm-notifyformat.md)
</dt> </dl>

 

