---
title: WM\_TOUCHHITTESTING message
description: Sent to a window on a touch down in order to determine the most probable touch target.
ms.assetid: 741F9D67-A914-46CF-91A3-EF40447E7438
keywords:
- WM_TOUCHHITTESTING message Input Messages and Notifications
topic_type:
- apiref
api_name:
- WM_TOUCHHITTESTING
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

# WM\_TOUCHHITTESTING message

Sent to a window on a touch down in order to determine the most probable touch target.

> \[!Important\]  
> Desktop apps should be DPI aware. If your app is not DPI aware, screen coordinates contained in pointer messages and related structures might appear inaccurate due to DPI virtualization. DPI virtualization provides automatic scaling support to applications that are not DPI aware and is active by default (users can turn it off). For more information, see [Writing High-DPI Win32 Applications](https://msdn.microsoft.com/library/windows/desktop/dd464660).

 


```C++
#define WM_TOUCHHITTESTING       0x024D
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Unused.

</dd> <dt>

*lParam* 
</dt> <dd>

Pointer to the [**TOUCH\_HIT\_TESTING\_INPUT**](https://msdn.microsoft.com/library/windows/desktop/hh437254) structure that holds the touch contact area data.

</dd> </dl>

## Return value

If one or more elements are within the touch contact area, an application should return the result of [**PackTouchHitTestingProximityEvaluation**](https://msdn.microsoft.com/library/windows/desktop/hh437250).

If no elements are within the touch contact area, an application should set the value of **score** in [**TOUCH\_HIT\_TESTING\_PROXIMITY\_EVALUATION**](https://msdn.microsoft.com/library/windows/desktop/hh437256) to [**TOUCH\_HIT\_TESTING\_PROXIMITY\_FARTHEST**](https://msdn.microsoft.com/library/windows/desktop/hh437249) and call [**PackTouchHitTestingProximityEvaluation**](https://msdn.microsoft.com/library/windows/desktop/hh437250) to get the LRESULT return value.

If the application does not process this message, it must call [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572).

## Remarks

This message is sent to windows that register through the [**RegisterTouchHitTestingWindow**](https://msdn.microsoft.com/library/windows/desktop/hh437252) function.

## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                     |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Messages](messages.md)
</dt> <dt>

[**Touch Hit Testing Scores**](https://msdn.microsoft.com/library/windows/desktop/hh437249)
</dt> </dl>

 

 





