---
title: WM_ASKCBFORMATNAME message (Winuser.h)
description: Sent to the clipboard owner by a clipboard viewer window to request the name of a CF\_OWNERDISPLAY clipboard format.
ms.assetid: eee026ec-58db-41b3-9705-30a17eebbd70
keywords:
- WM_ASKCBFORMATNAME message Data Exchange
topic_type:
- apiref
api_name:
- WM_ASKCBFORMATNAME
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_ASKCBFORMATNAME message

Sent to the clipboard owner by a clipboard viewer window to request the name of a [**CF\_OWNERDISPLAY**](standard-clipboard-formats.md) clipboard format.

A window receives this message through its [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)) function.


```C++
#define WM_ASKCBFORMATNAME              0x030C
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The size, in characters, of the buffer pointed to by the *lParam* parameter.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to the buffer that is to receive the clipboard format name.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

In response to this message, the clipboard owner should copy the name of the owner-display format to the specified buffer, not exceeding the buffer size specified by the *wParam* parameter.

A clipboard viewer window sends this message to the clipboard owner to determine the name of the [**CF\_OWNERDISPLAY**](standard-clipboard-formats.md) format   for example, to initialize a menu listing available formats.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Clipboard Overview](clipboard.md)
</dt> </dl>

 

