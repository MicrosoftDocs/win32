---
title: WM_TOUCH message (Winuser.h)
description: Notifies the window when one or more touch points, such as a finger or pen, touches a touch-sensitive digitizer surface.
ms.assetid: 5dee8bab-34fa-4dd9-a65b-35883757ec80
keywords:
- WM_TOUCH message Windows Touch
topic_type:
- apiref
api_name:
- WM_TOUCH
api_location:
- winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_TOUCH message

Notifies the window when one or more touch points, such as a finger or pen, touches a touch-sensitive digitizer surface.

## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The low-order word contains the number of touch points associated with this message. The high-order word is reserved for future use.

</dd> <dt>

*lParam* 
</dt> <dd>

Contains a touch input handle that can be used in a call to [**GetTouchInputInfo**](/windows/desktop/api/winuser/nf-winuser-gettouchinputinfo) to retrieve detailed information about the touch points associated with this message.

This handle is valid only within the current process and should not be passed cross-process except as the **LPARAM** in a **SendMessage** or **PostMessage** call.

When the application no longer requires this handle, the application must call **CloseTouchInputHandle** to free the process memory associated with this handle. Failing to do so can result in an application memory leak.

Note that the touch input handle in this parameter is no longer valid after the message has been passed to [DefWindowProc](/windows/win32/api/winuser/nf-winuser-defwindowproca). [DefWindowProc](/windows/win32/api/winuser/nf-winuser-defwindowproca) will close and invalidate this handle.

Note also that the touch input handle in this parameter is no longer valid after the message has been forwarded using [**PostMessage**](sendmessage--postmessage--and-related-functions.md), **SendMessage**, or one of their variants. These functions will close and invalidate this handle.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

If the application does not process the message, it must call [DefWindowProc](/windows/win32/api/winuser/nf-winuser-defwindowproca). Not doing so causes the application to leak memory because the touch input handle is not closed and associated process memory is not freed.

## Remarks

**WM\_TOUCH** messages do not respect **HTTRANSPARENT** regions of windows. If a window returns **HTTRANSPARENT** in response to a **WM\_NCHITTEST** message, mouse messages go to the parent, and **WM\_TOUCH** messages go directly to the window.

## Examples

The following code is an example of how to obtain detailed touch input information associated with this message.


```C++
UINT cInputs = LOWORD(wParam);
PTOUCHINPUT pInputs = new TOUCHINPUT[cInputs];
if (NULL != pInputs)
{
    if (GetTouchInputInfo((HTOUCHINPUT)lParam,
                          cInputs,
                          pInputs,
                          sizeof(TOUCHINPUT)))
    {
        // process pInputs
        if (!CloseTouchInputHandle((HTOUCHINPUT)lParam))
        {
            // error handling
        }
    }
    else
    {
        // GetLastError() and error handling
    }
    delete [] pInputs;
}
else
{
    // error handling, presumably out of memory
}
return DefWindowProc(hWnd, message, wParam, lParam);
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                                  |
| Header<br/>                   | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Messages](messages.md)
</dt> <dt>

[Manipulations and Inertia Programming Guide](manipulation-and-inertia.md)
</dt> <dt>

[Windows Touch Input Programming Guide](guide-multi-touch-input.md)
</dt> </dl>

 

