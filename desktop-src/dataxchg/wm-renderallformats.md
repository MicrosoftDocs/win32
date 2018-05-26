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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_RENDERALLFORMATS message

Sent to the clipboard owner before it is destroyed, if the clipboard owner has delayed rendering one or more clipboard formats. For the content of the clipboard to remain available to other applications, the clipboard owner must render data in all the formats it is capable of generating, and place the data on the clipboard by calling the [**SetClipboardData**](/windows/win32/Winuser/nf-winuser-setclipboarddata?branch=master) function.

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

When responding to a **WM\_RENDERALLFORMATS** message, the clipboard owner must call the [**OpenClipboard**](/windows/win32/Winuser/nf-winuser-openclipboard?branch=master) and [**EmptyClipboard**](/windows/win32/Winuser/nf-winuser-emptyclipboard?branch=master) functions before calling [**SetClipboardData**](/windows/win32/Winuser/nf-winuser-setclipboarddata?branch=master).

When the application returns, the system removes any unrendered formats from the list of available clipboard formats. For information about delayed rendering, see [**SetClipboardData**](/windows/win32/Winuser/nf-winuser-setclipboarddata?branch=master).

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

[**EmptyClipboard**](/windows/win32/Winuser/nf-winuser-emptyclipboard?branch=master)
</dt> <dt>

[**OpenClipboard**](/windows/win32/Winuser/nf-winuser-openclipboard?branch=master)
</dt> <dt>

[**SetClipboardData**](/windows/win32/Winuser/nf-winuser-setclipboarddata?branch=master)
</dt> <dt>

[**WM\_RENDERFORMAT**](wm-renderformat.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Clipboard](clipboard.md)
</dt> </dl>

 

 





