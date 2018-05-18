---
title: Enable and Control DWM Composition
description: The Desktop Window Manager (DWM) composition APIs provides several functions for setting and querying for basic information that is used by the DWM.
ms.assetid: VS|winui|~\winui\desktopwindowmanager\overviews\dwm_composition_ovw.htm
keywords: ["Desktop Window Manager (DWM),composition", "DWM (Desktop Window Manager),composition", "composition", "desktop composition", "colorization", "non-client region rendering", "Desktop Window Manager (DWM),colorization", "DWM (Desktop Window Manager),colorization", "Desktop Window Manager (DWM),non-client region rendering", "DWM (Desktop Window Manager),non-client region rendering", "Desktop Window Manager (DWM),messaging", "DWM (Desktop Window Manager),messaging", "messaging"]
---

# Enable and Control DWM Composition

The Desktop Window Manager (DWM) composition APIs provides several functions for setting and querying for basic information that is used by the DWM. These APIs enable you to query and change the composition state. Additionally, you can set and query the rendering policy for different DWM window attributes.

This topic contains the following sections:

-   [Disabling DWM Composition](#disabling-dwm-composition)
-   [Retrieving the Colorization Information](#retrieving-the-colorization-information)
-   [Controlling Non-Client Region Rendering](#controlling-non-client-region-rendering)
-   [Messaging](#messaging)

## Disabling DWM Composition

> [!Note]  
> As of Windows 8, the information in this section is no longer valid. DWM can no longer be programmatically disabled, nor is it disabled when an application attempts to draw to the primary display surface. The following information applies to only Windows 7 and earlier systems.

 

Because DWM uses the graphics processing unit (GPU) for desktop composition, certain applications might have to disable DWM for compatibility. Applications that take full control of the desktop, such as games that run in full-screen mode, must determine whether the DWM is enabled and if it is, disable it. To do this, two functions are needed: [**DwmIsCompositionEnabled**](dwmiscompositionenabled.md) and [**DwmEnableComposition**](dwmenablecomposition.md).

A call to [**DwmEnableComposition**](dwmenablecomposition.md) with *fEnable* set to **DWM\_EC\_DISABLECOMPOSITION** disables DWM composition until either the calling process has shut down or composition has been re-enabled by calling **DwmEnableComposition**, with *fEnable* set to **DWM\_EC\_ENABLECOMPOSITION**. DWM composition restarts automatically as soon as all applications that have disabled composition have shut down or manually re-enabled composition by calling **DwmEnableComposition**.

> [!Note]  
> The DWM will automatically disable composition when an application attempts to draw directly to the primary display surface. Composition will be disabled until the primary device surface is released by that application.

 

## Retrieving the Colorization Information

The color of the non-client region of windows is handled by the current system color theme. The colorization value is provided through the DWM APIs to enable applications to match client UI with the system color theme.

To access this colorization value and monitor the color change, use the [**DwmGetColorizationColor**](dwmgetcolorizationcolor.md) function and the [**WM\_DWMCOLORIZATIONCOLORCHANGED**](wm-dwmcolorizationcolorchanged.md) message.

The following example demonstrates how to monitor the color change and access the new color.


```
...
case WM_DWMCOLORIZATIONCOLORCHANGED:
{
    g_currColor = (DWORD)wParam;
    g_opacityblend = (BOOL)lParam; 
}
break;
...
```



## Controlling Non-Client Region Rendering

Two of the visual effects DWM enables are transparency of the non-client region of a window and transition effects. Some applications might have to disable or re-enable these effects for styling or compatibility reasons. The following functions are used to manage transparency and transition effect behavior:

-   [**DwmGetWindowAttribute**](dwmgetwindowattribute.md)
-   [**DwmSetWindowAttribute**](dwmsetwindowattribute.md)

To retrieve the current non-client rendering state for an application's window, use [**DwmGetWindowAttribute**](dwmgetwindowattribute.md) with the **DWMWA\_NCRENDERING\_ENABLED** attribute. The following example shows a typical **DwmGetWindowAttribute** call.

``` syntax
BOOL enabled = FALSE;
HRESULT hr = DwmGetWindowAttribute(hwnd, DWMWA_NCRENDERING_ENABLED, &enabled, sizeof(enabled));
```

> [!Note]  
> Each [**DWMWINDOWATTRIBUTE**](dwmwindowattribute.md) has an implied type associated with it. Refer to each enumeration member for detailed information.

 

[**DwmSetWindowAttribute**](dwmsetwindowattribute.md) enables applications to set the non-client area rendering policy. It also determines how the application should handle DWM transition effects.

The following example disables non-client area rendering.


```
HRESULT DisableNCRendering(HWND hwnd)
{
    HRESULT hr = S_OK;

    DWMNCRENDERINGPOLICY ncrp = DWMNCRP_DISABLED;

    // Disable non-client area rendering on the window.
    hr = DwmSetWindowAttribute(hwnd, DWMWA_NCRENDERING_POLICY, &amp;ncrp, sizeof(ncrp));
    if (SUCCEEDED(hr))
    {
        // ...
    }
   
    return hr;
}
```



In addition to controlling the non-client area rendering, [**DwmSetWindowAttribute**](dwmsetwindowattribute.md) can also control DWM transition effects. Transition behavior can be set by using **DWMWA\_TRANSITIONS\_FORCEDISABLED** as the *dwAttribute* parameter.

## Messaging

The following messages provide notification of DWM events. These messages can be used to monitor changes such as composition state changes and system color theme changes.

-   [**WM\_DWMCOLORIZATIONCOLORCHANGED**](wm-dwmcolorizationcolorchanged.md)
-   [**WM\_DWMCOMPOSITIONCHANGED**](wm-dwmcompositionchanged.md)
-   [**WM\_DWMNCRENDERINGCHANGED**](wm-dwmncrenderingchanged.md)
-   [**WM\_DWMWINDOWMAXIMIZEDCHANGE**](wm-dwmwindowmaximizedchange.md)

 

 




