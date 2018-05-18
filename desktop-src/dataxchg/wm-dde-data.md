---
title: WM\_DDE\_DATA message
description: A Dynamic Data Exchange (DDE) server application posts a WM\_DDE\_DATA message to a DDE client application to pass a data item to the client or to notify the client of the availability of a data item.
ms.assetid: 'ed6a65d3-b2a3-45f2-9600-291ce2ec8c0a'
keywords: ["WM_DDE_DATA message Data Exchange"]
topic_type:
- apiref
api_name:
- WM_DDE_DATA
api_location:
- Dde.h
api_type:
- HeaderDef
---

# WM\_DDE\_DATA message

A Dynamic Data Exchange (DDE) server application posts a **WM\_DDE\_DATA** message to a DDE client application to pass a data item to the client or to notify the client of the availability of a data item.

To post this message, call the [**PostMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644944) function with the following parameters.


```C++
#define WM_DDE_DATA        0x03E05
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the server window posting the message.

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word is a handle to a global memory object containing a [**DDEDATA**](ddedata.md) structure with the data and additional information. The handle should be set to **NULL** if the server is notifying the client that the data-item value has changed during a warm data link. A warm link is established by the client sending a [**WM\_DDE\_ADVISE**](wm-dde-advise.md) message with the **fDeferUpd** bit set.

The high-order word contains an atom that identifies the data item for which the data or notification is sent.

</dd> </dl>

## Remarks

### Posting

The server application allocates the global memory object using the [**GlobalAlloc**](https://msdn.microsoft.com/library/windows/desktop/aa366574) function. It allocates the atom using the [**GlobalAddAtom**](globaladdatom.md) function.

The server must create or reuse the **WM\_DDE\_DATA** *lParam* parameter by calling the [**PackDDElParam**](packddelparam.md) function or the [**ReuseDDElParam**](reuseddelparam.md) function.

If the receiving (client) application responds with a negative [**WM\_DDE\_ACK**](wm-dde-ack.md) message, the posting (server) application must delete the global memory object; otherwise, the client must delete the object after extracting its contents by calling the [**UnpackDDElParam**](unpackddelparam.md) function.

If the server application sets the **fRelease** member of the [**DDEDATA**](ddedata.md) structure to **FALSE**, the server is responsible for deleting the object upon receiving either a positive or negative acknowledgment.

The server application should not set both the **fAckReq** and **fRelease** members of the [**DDEDATA**](ddedata.md) structure to **FALSE**. If both members are set to **FALSE**, it is impossible for the server to determine when to delete the object.

### Receiving

If **fAckReq** is **TRUE**, the client application should post the [**WM\_DDE\_ACK**](wm-dde-ack.md) message to respond positively or negatively. When posting **WM\_DDE\_ACK**, the client can either reuse the atom, or it can delete it and create a new one.

The client must create or reuse the [**WM\_DDE\_ACK**](wm-dde-ack.md) *lParam* parameter by calling the [**PackDDElParam**](packddelparam.md) function or the [**ReuseDDElParam**](reuseddelparam.md) function.

If **fAckReq** is **FALSE**, the client application should delete the atom.

If the posting application specified global memory object as **NULL**, the receiving application can request the server to send the data by posting a [**WM\_DDE\_REQUEST**](wm-dde-request.md) message.

After processing a **WM\_DDE\_DATA** message in which the global memory object is not **NULL**, the client should free the object, unless one of the following conditions is true:

-   The **fRelease** member is **FALSE**.
-   The **fRelease** member is **TRUE**, but the client application responds with a negative [**WM\_DDE\_ACK**](wm-dde-ack.md) message.

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                 |
| Header<br/>                   | <dl> <dt>Dde.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DDEDATA**](ddedata.md)
</dt> <dt>

[**FreeDDElParam**](freeddelparam.md)
</dt> <dt>

[**GlobalAddAtom**](globaladdatom.md)
</dt> <dt>

[**PackDDElParam**](packddelparam.md)
</dt> <dt>

[**PostMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644944)
</dt> <dt>

[**ReuseDDElParam**](reuseddelparam.md)
</dt> <dt>

[**SendMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644950)
</dt> <dt>

[**UnpackDDElParam**](unpackddelparam.md)
</dt> <dt>

[**WM\_DDE\_ACK**](wm-dde-ack.md)
</dt> <dt>

[**WM\_DDE\_ADVISE**](wm-dde-advise.md)
</dt> <dt>

[**WM\_DDE\_POKE**](wm-dde-poke.md)
</dt> <dt>

[**WM\_DDE\_REQUEST**](wm-dde-request.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[About Dynamic Data Exchange](about-dynamic-data-exchange.md)
</dt> </dl>

 

 





