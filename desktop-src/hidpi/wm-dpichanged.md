---
title: WM_DPICHANGED message (WinUser.h)
description: Sent when the effective dots per inch (dpi) for a window has changed.
ms.assetid: 97C458F2-89CD-45FF-ABEE-F158A3BCE0B8
keywords:
- WM_DPICHANGED message High DPI
topic_type:
- apiref
api_name:
- WM_DPICHANGED
api_location:
- WinUser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# WM\_DPICHANGED message

Sent when the effective dots per inch (dpi) for a window has changed. The DPI is the scale factor for a window. There are multiple events that can cause the DPI to change. The following list indicates the possible causes for the change in DPI.

-   The window is moved to a new monitor that has a different DPI.
-   The DPI of the monitor hosting the window changes.

The current DPI for a window always equals the last DPI sent by **WM\_DPICHANGED**. This is the scale factor that the window should be scaling to for threads that are aware of DPI changes.


```C++
#define WM_DPICHANGED       0x02E0
```



## Parameters

<dl> <dt>

*wParam* 
</dt> <dd>

The [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) of the *wParam* contains the Y-axis value of the new dpi of the window. The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) of the *wParam* contains the X-axis value of the new DPI of the window. For example, 96, 120, 144, or 192. The values of the X-axis and the Y-axis are identical for Windows apps.

</dd> <dt>

*lParam* 
</dt> <dd>

A pointer to a [**RECT**](/windows/desktop/api/windef/ns-windef-rect) structure that provides a suggested size and position of the current window scaled for the new DPI. The expectation is that apps will reposition and resize windows based on the suggestions provided by *lParam* when handling this message.

</dd> </dl>

## Return value

If an application processes this message, it should return zero.

## Remarks

This message is only relevant for **PROCESS\_PER\_MONITOR\_DPI\_AWARE** applications or **DPI\_AWARENESS\_PER\_MONITOR\_AWARE** threads. It may be received on certain DPI changes if your top-level window or process is running as **DPI unaware** or **system DPI aware**, but in those situations it can be safely ignored. For more information about the different types of awareness, see [**PROCESS\_DPI\_AWARENESS**](/windows/desktop/api/ShellScalingApi/ne-shellscalingapi-process_dpi_awareness) and [**DPI\_AWARENESS**](/windows/desktop/api/windef/ne-windef-dpi_awareness). Older versions of Windows required DPI awareness to be tied at the level of an application. Those apps use **PROCESS\_DPI\_AWARENESS**. Currently, DPI awareness is tied to threads and individual windows rather than the entire application. These apps use **DPI\_AWARENESS**.

You only need to use either the X-axis or the Y-axis value when scaling your application since they are the same.

In order to handle this message correctly, you will need to resize and reposition your window based on the suggestions provided by *lParam* and using [**SetWindowPos**](/windows/desktop/api/winuser/nf-winuser-setwindowpos). If you do not do this, your window will grow or shrink with respect to everything else on the new monitor. For example, if a user is using multiple monitors and drags your window from a 96 DPI monitor to a 192 DPI monitor, your window will appear to be half as large with respect to other items on the 192 DPI monitor.

The base value of DPI is defined as **USER\_DEFAULT\_SCREEN\_DPI** which is set to 96. To determine the scaling factor for a monitor, take the DPI value and divide by **USER\_DEFAULT\_SCREEN\_DPI**. The following table provides some sample DPI values and associated scaling factors.



| DPI value | Scaling percentage |
|-----------|--------------------|
| 96        | 100%               |
| 120       | 125%               |
| 144       | 150%               |
| 192       | 200%               |



 

The following example provides a sample DPI change handler.


```C++
    case WM_DPICHANGED:
    {
        g_dpi = HIWORD(wParam);
        UpdateDpiDependentFontsAndResources();

        RECT* const prcNewWindow = (RECT*)lParam;
        SetWindowPos(hWnd,
            NULL,
            prcNewWindow ->left,
            prcNewWindow ->top,
            prcNewWindow->right - prcNewWindow->left,
            prcNewWindow->bottom - prcNewWindow->top,
            SWP_NOZORDER | SWP_NOACTIVATE);
        break;
    }
```



The following code linearly scales a value from 100% (96 DPI) to an arbitrary DPI defined by *g\_dpi*.


```C++
    INT iBorderWidth100 = 5;
    iBorderWidth = MulDiv(iBorderWidth100, g_dpi, USER_DEFAULT_SCREEN_DPI);
```



An alternative way to scale a value is to convert the DPI value into a scale factor and use that.


```C++
    INT iBorderWidth100 = 5;
    FLOAT fscale = (float) g_dpi / USER_DEFAULT_SCREEN_DPI;
    iBorderWidth = iBorderWidth100 * fscale;
```



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                              |
| Header<br/>                   | <dl> <dt>WinUser.h</dt> </dl> |



## See also

<dl> <dt>

[**DPI\_AWARENESS**](/windows/desktop/api/windef/ne-windef-dpi_awareness)
</dt> <dt>

[**PROCESS\_DPI\_AWARENESS**](/windows/desktop/api/ShellScalingApi/ne-shellscalingapi-process_dpi_awareness)
</dt> </dl>

 

