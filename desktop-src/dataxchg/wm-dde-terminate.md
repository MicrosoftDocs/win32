---
title: WM_DDE_TERMINATE message (Dde.h)
description: A Dynamic Data Exchange (DDE) application (client or server) posts a WM\_DDE\_TERMINATE message to terminate a conversation. To post this message, call the PostMessage function with the following parameters.
ms.assetid: 4fc162c0-ccc2-44e3-9c07-d49d7426af8b
keywords:
- WM_DDE_TERMINATE message Data Exchange
topic_type:
- apiref
api_name:
- WM_DDE_TERMINATE
api_location:
- Dde.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_DDE\_TERMINATE message

A Dynamic Data Exchange (DDE) application (client or server) posts a **WM\_DDE\_TERMINATE** message to terminate a conversation.

To post this message, call the [**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea) function with the following parameters.


```C++
#define WM_DDE_TERMINATE       0x03E1
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the client or server window posting the message.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Remarks

### Posting

While waiting for confirmation of the termination, the posting application should not post any other messages to the receiving application. If the sending application receives messages (other than **WM\_DDE\_TERMINATE**) from the receiving application, it should delete any atoms or shared memory objects accompanying the messages, except global memory objects associated with [**WM\_DDE\_POKE**](wm-dde-poke.md) or [**WM\_DDE\_DATA**](wm-dde-data.md) messages that do not have the **fRelease** member set.

### Receiving

The client or server application should respond by posting a **WM\_DDE\_TERMINATE** message.

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

[**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea)
</dt> <dt>

[**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage)
</dt> <dt>

[**WM\_DDE\_DATA**](wm-dde-data.md)
</dt> <dt>

[**WM\_DDE\_POKE**](wm-dde-poke.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[About Dynamic Data Exchange](about-dynamic-data-exchange.md)
</dt> </dl>

 

