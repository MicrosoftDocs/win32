---
title: WM\_RENDERALLFORMATS message
description: Sent to the clipboard owner before it is destroyed, if the clipboard owner has delayed rendering one or more clipboard formats.
ms.assetid: dff9100f-2dba-467d-be74-a9a9c2b2122b
keywords:
- WM_RENDERALLFORMATS message Data Exchange
topic_type:
- apiref
api_name:
- WM_RENDERALLFORMATS
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_RENDERALLFORMATS message

Sent to the clipboard owner before it is destroyed, if the clipboard owner has delayed rendering one or more clipboard formats. For the content of the clipboard to remain available to other applications, the clipboard owner must render data in all the formats it is capable of generating, and place the data on the clipboard by calling the [**SetClipboardData**](/windows/desktop/api/Winuser/nf-winuser-setclipboarddata) function.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633573) function.


```C++
#define WM_RENDERALLFORMATS             0x0306
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used and must be zero.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

When responding to a **WM\_RENDERALLFORMATS** message, the clipboard owner must call the [**OpenClipboard**](/windows/desktop/api/Winuser/nf-winuser-openclipboard) and [**EmptyClipboard**](/windows/desktop/api/Winuser/nf-winuser-emptyclipboard) functions before calling [**SetClipboardData**](/windows/desktop/api/Winuser/nf-winuser-setclipboarddata).

When the application returns, the system removes any unrendered formats from the list of available clipboard formats. For information about delayed rendering, see [**SetClipboardData**](/windows/desktop/api/Winuser/nf-winuser-setclipboarddata).

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**EmptyClipboard**](/windows/desktop/api/Winuser/nf-winuser-emptyclipboard)
</dt> <dt>

[**OpenClipboard**](/windows/desktop/api/Winuser/nf-winuser-openclipboard)
</dt> <dt>

[**SetClipboardData**](/windows/desktop/api/Winuser/nf-winuser-setclipboarddata)
</dt> <dt>

[**WM\_RENDERFORMAT**](wm-renderformat.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Clipboard](clipboard.md)
</dt> </dl>

 

 





