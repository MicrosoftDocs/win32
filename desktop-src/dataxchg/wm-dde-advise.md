---
title: WM_DDE_ADVISE message (Dde.h)
description: A Dynamic Data Exchange (DDE) client application posts the WM\_DDE\_ADVISE message to a DDE server application to request the server to supply an update for a data item whenever the item changes.
ms.assetid: b00db740-36a7-4487-abbf-d74b12f5212a
keywords:
- WM_DDE_ADVISE message Data Exchange
topic_type:
- apiref
api_name:
- WM_DDE_ADVISE
api_location:
- Dde.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_DDE\_ADVISE message

A Dynamic Data Exchange (DDE) client application posts the **WM\_DDE\_ADVISE** message to a DDE server application to request the server to supply an update for a data item whenever the item changes.

To post this message, call the [**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea) function with the following parameters.


```C++
#define WM_DDE_ADVISE      0x03E2
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the client window posting the message.

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word is a handle to a global memory object containing a [**DDEADVISE**](/windows/desktop/api/Dde/ns-dde-ddeadvise) structure that specifies how the data is to be sent.

The high-order word contains an atom that identifies the requested data item.

</dd> </dl>

## Remarks

If a client application supports more than one clipboard format for a single topic and item, it can post multiple **WM\_DDE\_ADVISE** messages for the topic and item, specifying a different clipboard format with each message. Note that a server can support multiple formats only for hot data links, not warm data links.

### Posting

The client application posts the **WM\_DDE\_ADVISE** message by calling the [**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea) function, not the [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) function.

The client application allocates the global memory object using the [**GlobalAlloc**](/windows/desktop/api/winbase/nf-winbase-globalalloc) function. It allocates the atom using the [**GlobalAddAtom**](/windows/desktop/api/Winbase/nf-winbase-globaladdatoma) function.

The client application must create or reuse the **WM\_DDE\_ADVISE** *lParam* parameter by calling the [**PackDDElParam**](/windows/desktop/api/Dde/nf-dde-packddelparam) function or the [**ReuseDDElParam**](/windows/desktop/api/Dde/nf-dde-reuseddelparam) function.

If the receiving (server) application responds with a negative [**WM\_DDE\_ACK**](wm-dde-ack.md) message, the posting application must delete the object.

The **fRelease** flag is not used in **WM\_DDE\_ADVISE** messages, but their data-freeing behavior is similar to that of [**WM\_DDE\_DATA**](wm-dde-data.md) and [**WM\_DDE\_POKE**](wm-dde-poke.md) messages where **fRelease** is **TRUE**.

### Receiving

The server application posts the [**WM\_DDE\_ACK**](wm-dde-ack.md) message to respond positively or negatively. When posting **WM\_DDE\_ACK**, the application can reuse the atom or delete it and create a new one. If the **WM\_DDE\_ACK** message is positive, the application should delete the global memory object; otherwise, the application should not delete the object.

The server must create or reuse the [**WM\_DDE\_ACK**](wm-dde-ack.md) *lParam* parameter by calling the [**PackDDElParam**](/windows/desktop/api/Dde/nf-dde-packddelparam) function or the [**ReuseDDElParam**](/windows/desktop/api/Dde/nf-dde-reuseddelparam) function.

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

[**DDEADVISE**](/windows/desktop/api/Dde/ns-dde-ddeadvise)
</dt> <dt>

[**FreeDDElParam**](/windows/desktop/api/Dde/nf-dde-freeddelparam)
</dt> <dt>

[**GlobalAddAtom**](/windows/desktop/api/Winbase/nf-winbase-globaladdatoma)
</dt> <dt>

[**PackDDElParam**](/windows/desktop/api/Dde/nf-dde-packddelparam)
</dt> <dt>

[**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea)
</dt> <dt>

[**ReuseDDElParam**](/windows/desktop/api/Dde/nf-dde-reuseddelparam)
</dt> <dt>

[**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage)
</dt> <dt>

[**UnpackDDElParam**](/windows/desktop/api/Dde/nf-dde-unpackddelparam)
</dt> <dt>

[**WM\_DDE\_ACK**](wm-dde-ack.md)
</dt> <dt>

[**WM\_DDE\_DATA**](wm-dde-data.md)
</dt> <dt>

[**WM\_DDE\_POKE**](wm-dde-poke.md)
</dt> <dt>

[**WM\_DDE\_REQUEST**](wm-dde-request.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[About Dynamic Data Exchange](about-dynamic-data-exchange.md)
</dt> </dl>

 

