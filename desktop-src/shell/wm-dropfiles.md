---
description: Sent when the user drops a file on the window of an application that has registered itself as a recipient of dropped files.
ms.assetid: 07dc2df7-4699-4e9c-b1a5-4ce877116268
title: WM_DROPFILES message (Winuser.h)
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_DROPFILES message

Sent when the user drops a file on the window of an application that has registered itself as a recipient of dropped files.


```C++
PostMessage(
    (HWND) hWndControl,   // handle to destination control
    (UINT) WM_DROPFILES,  // message ID
    (WPARAM) wParam,      // = (WPARAM) (HDROP) hDrop;
    (LPARAM) lParam       // = 0; not used, must be zero 
);          
```



## Parameters

<dl> <dt>

*hDrop* 
</dt> <dd>

A handle to an internal structure describing the dropped files. Pass this handle [**DragFinish**](/windows/desktop/api/Shellapi/nf-shellapi-dragfinish), [**DragQueryFile**](/windows/desktop/api/Shellapi/nf-shellapi-dragqueryfilea), or [**DragQueryPoint**](/windows/desktop/api/Shellapi/nf-shellapi-dragquerypoint) to retrieve information about the dropped files.

</dd> <dt>

*lParam* 
</dt> <dd>

Must be zero.

</dd> </dl>

## Return value

An application should return zero if it processes this message.

## Remarks

The HDROP handle is declared in Shellapi.h. You must include this header in your build to use **WM\_DROPFILES**. For further discussion of how to use drag-and-drop to transfer Shell data, see [Transferring Shell Data Using Drag-and-Drop or the Clipboard](dragdrop.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Winuser.h</dt> </dl> |



## See also

<dl> <dt>

[**PostMessage**](/windows/win32/api/winuser/nf-winuser-postmessagea)
</dt> <dt>

[**DragAcceptFiles**](/windows/desktop/api/Shellapi/nf-shellapi-dragacceptfiles)
</dt> </dl>

 

 
