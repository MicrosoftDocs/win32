---
title: WM\_RENDERFORMAT message
description: Sent to the clipboard owner if it has delayed rendering a specific clipboard format and if an application has requested data in that format.
ms.assetid: '81638109-4c5e-4b4c-b2db-4208b6ee83cc'
keywords: ["WM_RENDERFORMAT message Data Exchange"]
topic_type:
- apiref
api_name:
- WM_RENDERFORMAT
api_location:
- Winuser.h
api_type:
- HeaderDef
---

# WM\_RENDERFORMAT message

Sent to the clipboard owner if it has delayed rendering a specific clipboard format and if an application has requested data in that format. The clipboard owner must render data in the specified format and place it on the clipboard by calling the [**SetClipboardData**](setclipboarddata.md) function.


```C++
#define WM_RENDERFORMAT                 0x0305
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [clipboard format](standard-clipboard-formats.md) to be rendered.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

When responding to a **WM\_RENDERFORMAT** message, the clipboard owner must not open the clipboard before calling [**SetClipboardData**](setclipboarddata.md).

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

[**SetClipboardData**](setclipboarddata.md)
</dt> <dt>

[**WM\_RENDERALLFORMATS**](wm-renderallformats.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Clipboard](clipboard.md)
</dt> </dl>

 

 





