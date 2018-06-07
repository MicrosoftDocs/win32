---
title: WM\_CTLCOLORLISTBOX message
description: Sent to the parent window of a list box before the system draws the list box. By responding to this message, the parent window can set the text and background colors of the list box by using the specified display device context handle.
ms.assetid: e128e77f-e966-44c4-9f0e-efcf421b6c82
keywords:
- WM_CTLCOLORLISTBOX message Windows Controls
topic_type:
- apiref
api_name:
- WM_CTLCOLORLISTBOX
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

# WM\_CTLCOLORLISTBOX message

Sent to the parent window of a list box before the system draws the list box. By responding to this message, the parent window can set the text and background colors of the list box by using the specified display device context handle.


```C++
WM_CTLCOLORLISTBOX

    WPARAM wParam;
    LPARAM lParam; 
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Handle to the device context for the list box.

</dd> <dt>

*lParam* 
</dt> <dd>

Handle to the list box.

</dd> </dl>

## Return value

If an application processes this message, it must return a handle to a brush. The system uses the brush to paint the background of the list box.

## Remarks

By default, the [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572) function selects the default system colors for the list box.

The **WM\_CTLCOLORLISTBOX** message is never sent between threads. It is sent only within one thread.

If a dialog box procedure handles this message, it should cast the desired return value to a **INT\_PTR** and return the value directly. If the dialog box procedure returns **FALSE**, then default message handling is performed. The **DWL\_MSGRESULT** value set by the [**SetWindowLong**](https://msdn.microsoft.com/library/windows/desktop/ms633591) function is ignored.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

**Other Resources**
</dt> <dt>

[**RealizePalette**](https://msdn.microsoft.com/library/windows/desktop/dd162896)
</dt> <dt>

[**SelectPalette**](https://msdn.microsoft.com/library/windows/desktop/dd162958)
</dt> <dt>

[**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572)
</dt> </dl>

 

 





