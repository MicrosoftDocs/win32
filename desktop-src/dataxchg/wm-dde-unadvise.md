---
title: WM\_DDE\_UNADVISE message
description: A Dynamic Data Exchange (DDE) client application posts a WM\_DDE\_UNADVISE message to inform a DDE server application that the specified item or a particular clipboard format for the item should no longer be updated.
ms.assetid: '9a5f9a86-e6fa-450e-b8bf-f20042c7e6d1'
keywords: ["WM_DDE_UNADVISE message Data Exchange"]
topic_type:
- apiref
api_name:
- WM_DDE_UNADVISE
api_location:
- Dde.h
api_type:
- HeaderDef
---

# WM\_DDE\_UNADVISE message

A Dynamic Data Exchange (DDE) client application posts a **WM\_DDE\_UNADVISE** message to inform a DDE server application that the specified item or a particular clipboard format for the item should no longer be updated. This terminates the warm or hot data link for the specified item.

To post this message, call the [**PostMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644944) function with the following parameters.


```C++
#define WM_DDE_UNADVISE        0x03E3
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

A handle to the client window sending the message.

</dd> <dt>

*lParam* 
</dt> <dd>

The low-order word specifies the clipboard format of the item for which the update request is being retracted. If this is **NULL**, all active [**WM\_DDE\_ADVISE**](wm-dde-advise.md) conversations for the item are to be terminated.

The high-order word contains a global atom that identifies the item for which the update request is being retracted. If this is **NULL**, all active [**WM\_DDE\_ADVISE**](wm-dde-advise.md) links associated with the conversation are to be terminated.

</dd> </dl>

## Remarks

The client application allocates the high-order word of *lParam* by calling the [**GlobalAddAtom**](globaladdatom.md) function.

The server application posts the [**WM\_DDE\_ACK**](wm-dde-ack.md) message to respond positively or negatively. When posting **WM\_DDE\_ACK**, the server can either reuse the atom, or it can delete the atom and create a new one.

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

**Conceptual**
</dt> <dt>

[About Dynamic Data Exchange](about-dynamic-data-exchange.md)
</dt> </dl>

 

 





