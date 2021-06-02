---
title: WM_DDE_INITIATE message (Dde.h)
description: A Dynamic Data Exchange (DDE) client application sends a WM\_DDE\_INITIATE message to initiate a conversation with a server application responding to the specified application and topic names.
ms.assetid: d486f584-75a3-4ffd-ba5d-f95f2692cd6c
keywords:
- WM_DDE_INITIATE message Data Exchange
topic_type:
- apiref
api_name:
- WM_DDE_INITIATE
api_location:
- Dde.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_DDE\_INITIATE message

A Dynamic Data Exchange (DDE) client application sends a **WM\_DDE\_INITIATE** message to initiate a conversation with a server application responding to the specified application and topic names. Upon receiving this message, all server applications with names that match the specified application and that support the specified topic are expected to acknowledge it. (For more information, see the [**WM\_DDE\_ACK**](wm-dde-ack.md) message.)


```C++
#define WM_DDE_INITIATE        0x03E0
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the client window sending the message.

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word contains an atom that identifies the application with which a conversation is requested. The application name cannot contain slashes (/) or backslashes (\\). These characters are reserved for network implementations. If this parameter is **NULL**, a conversation with all applications is requested.

The high-order word contains an atom that identifies the topic for which a conversation is requested. If the topic is **NULL**, conversations for all available topics are requested.

</dd> </dl>

## Remarks

If the low-order word of *lParam* is **NULL**, any server application can respond. If the high-order word of *lParam* is **NULL**, any topic is valid. Upon receiving a **WM\_DDE\_INITIATE** request with the high-order word of the *lParam* parameter set to **NULL**, a server must send a [**WM\_DDE\_ACK**](wm-dde-ack.md) message for each of the topics it supports.

### Sending

The client broadcasts the message to all top-level windows by setting the first parameter of [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) to **HWND\_BROADCAST**.

If the client application has already obtained the window handle of the desired server, it can send **WM\_DDE\_INITIATE** directly to the server window by passing the server's window handle as the first parameter of [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage).

The client application allocates atoms by calling the [**GlobalAddAtom**](/windows/desktop/api/Winbase/nf-winbase-globaladdatoma) function.

When [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) returns, the client application must delete the atoms.

### Receiving

To complete the initiation of a conversation, the server application must respond with one or more [**WM\_DDE\_ACK**](wm-dde-ack.md) messages, where each message is for a separate topic. When sending **WM\_DDE\_ACK** message, the server should create new atoms; it should not reuse the atoms sent with **WM\_DDE\_INITIATE**.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>Dde.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**GlobalAddAtom**](/windows/desktop/api/Winbase/nf-winbase-globaladdatoma)
</dt> <dt>

[**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea)
</dt> <dt>

[**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage)
</dt> <dt>

[**WM\_DDE\_ACK**](wm-dde-ack.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[About Dynamic Data Exchange](about-dynamic-data-exchange.md)
</dt> </dl>

 

