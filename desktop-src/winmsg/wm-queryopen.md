---
Description: Sent to an icon when the user requests that the window be restored to its previous size and position.
ms.assetid: 6e14d5fd-6598-4d2e-a463-2b153c9c2aa3
title: WM_QUERYOPEN message
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WM\_QUERYOPEN message

Sent to an icon when the user requests that the window be restored to its previous size and position.

A window receives this message through its [**WindowProc**](https://msdn.microsoft.com/en-us/library/ms633573(v=VS.85).aspx) function.


```C++
#define WM_QUERYOPEN                    0x0013
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

This parameter is not used.

</dd> <dt>

*lParam* 
</dt> <dd>

This parameter is not used.

</dd> </dl>

## Return value

Type: **LRESULT**

If the icon can be opened, an application that processes this message should return **TRUE**; otherwise, it should return **FALSE** to prevent the icon from being opened.

## Remarks

By default, the [**DefWindowProc**](https://msdn.microsoft.com/en-us/library/ms633572(v=VS.85).aspx) function returns **TRUE**.

While processing this message, the application should not perform any action that would cause an activation or focus change (for example, creating a dialog box).

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

[**DefWindowProc**](https://msdn.microsoft.com/en-us/library/ms633572(v=VS.85).aspx)
</dt> <dt>

**Conceptual**
</dt> <dt>

[Windows](windows.md)
</dt> </dl>

 

 




