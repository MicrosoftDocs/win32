---
title: WM\_CAPTURECHANGED message
description: Sent to the window that is losing the mouse capture.
ms.assetid: '79c8f65e-31fa-4bdb-9e88-0160a52b5b7d'
keywords: ["WM_CAPTURECHANGED message Keyboard and Mouse Input"]
topic_type:
- apiref
api_name:
- WM_CAPTURECHANGED
api_location:
- Winuser.h
api_type:
- HeaderDef
---

# WM\_CAPTURECHANGED message

Sent to the window that is losing the mouse capture.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.


```C++
#define WM_CAPTURECHANGED               0x0215
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

A handle to the window gaining the mouse capture.

</dd> </dl>

## Return value

An application should return zero if it processes this message.

## Remarks

A window receives this message even if it calls [**ReleaseCapture**](releasecapture.md) itself. An application should not attempt to set the mouse capture in response to this message.

When it receives this message, a window should redraw itself, if necessary, to reflect the new mouse-capture state.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**ReleaseCapture**](releasecapture.md)
</dt> <dt>

[**SetCapture**](setcapture.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Mouse Input](mouse-input.md)
</dt> </dl>

 

 





