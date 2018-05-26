---
title: WM\_GESTURENOTIFY message
description: Gives you a chance to set the gesture configuration.
ms.assetid: 83c23928-86ce-421d-bb84-5c41a770bf60
keywords:
- WM_GESTURENOTIFY message Windows Touch
topic_type:
- apiref
api_name:
- WM_GESTURENOTIFY
api_location:
- winuser.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WM\_GESTURENOTIFY message

Gives you a chance to set the gesture configuration.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

Unused.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**GESTURENOTIFYSTRUCT**](/windows/win32/winuser/ns-winuser-taggesturenotifystruct?branch=master).

</dd> </dl>

## Return value

A value should be returned from [DefWindowProc](http://go.microsoft.com/fwlink/p/?linkid=136637).

## Remarks

When the **WM\_GESTURENOTIFY** message is received, the application can use [**SetGestureConfig**](/windows/win32/winuser/nf-winuser-setgestureconfig?branch=master) to specify the gestures to receive. This message should always be bubbled up using the [DefWindowProc](http://go.microsoft.com/fwlink/p/?linkid=136637) function.

> [!Note]  
> Handling the **WM\_GESTURENOTIFY** message will change the gesture configuration for the lifetime of the Window, not just for the next gesture.

 

## Examples

The following example shows how to enable all gestures. For more examples, see [**SetGestureConfig**](/windows/win32/winuser/nf-winuser-setgestureconfig?branch=master).


```C++
    switch (message)
    {
    case WM_GESTURENOTIFY:
        GESTURECONFIG gc = {0,GC_ALLGESTURES,0};
        BOOL bResult = SetGestureConfig(hWnd,0,1,&amp;gc,sizeof(GESTURECONFIG));
            
        if(!bResult)
        {
            // an error
        }
        return DefWindowProc(hWnd, WM_GESTURENOTIFY, wParam, lParam);
    }
      
```



## Requirements



|                                     |                                                                                                          |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                  |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Notifications](notifications.md)
</dt> <dt>

[Windows Touch Gestures Programming Guide](guide-multi-touch-gestures.md)
</dt> <dt>

[**GESTURENOTIFYSTRUCT**](/windows/win32/winuser/ns-winuser-taggesturenotifystruct?branch=master)
</dt> <dt>

[**SetGestureConfig**](/windows/win32/winuser/nf-winuser-setgestureconfig?branch=master)
</dt> </dl>

 

 





