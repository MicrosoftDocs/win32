---
title: WM_DDE_REQUEST message (Dde.h)
description: A Dynamic Data Exchange (DDE) client application posts a WM\_DDE\_REQUEST message to a DDE server application to request the value of a data item. To post this message, call the PostMessage function with the following parameters.
ms.assetid: 922452d2-455c-43e1-a8a8-e3c52b0fab51
keywords:
- WM_DDE_REQUEST message Data Exchange
topic_type:
- apiref
api_name:
- WM_DDE_REQUEST
api_location:
- Dde.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_DDE\_REQUEST message

A Dynamic Data Exchange (DDE) client application posts a **WM\_DDE\_REQUEST** message to a DDE server application to request the value of a data item.

To post this message, call the [**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea) function with the following parameters.


```C++
#define WM_DDE_REQUEST     0x03E6
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the client window sending the message.

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word specifies a standard or registered clipboard format.

The high-order word contains an atom that identifies the data item requested from the server.

</dd> </dl>

## Remarks

### Posting

The client application allocates the atom by calling the [**GlobalAddAtom**](/windows/desktop/api/Winbase/nf-winbase-globaladdatoma) function.

### Receiving

If the receiving (server) application can satisfy the request, it responds with a [**WM\_DDE\_DATA**](wm-dde-data.md) message containing the requested data. Otherwise, it responds with a negative [**WM\_DDE\_ACK**](wm-dde-ack.md) message.

When responding with either a [**WM\_DDE\_DATA**](wm-dde-data.md) or [**WM\_DDE\_ACK**](wm-dde-ack.md) message, the server application can either reuse the atom or it can delete the atom and create a new one.

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

**Conceptual**
</dt> <dt>

[About Dynamic Data Exchange](about-dynamic-data-exchange.md)
</dt> </dl>

 

