---
title: Enable and control DWM composition
description: The Desktop Window Manager (DWM) composition APIs provide several functions for setting and querying for basic information that is used by the DWM.
ms.assetid: VS|winui|~\winui\desktopwindowmanager\overviews\dwm_composition_ovw.htm
keywords:
- Desktop Window Manager (DWM),composition
- DWM (Desktop Window Manager),composition
- composition
- desktop composition
- colorization
- non-client region rendering
- Desktop Window Manager (DWM),colorization
- DWM (Desktop Window Manager),colorization
- Desktop Window Manager (DWM),non-client region rendering
- DWM (Desktop Window Manager),non-client region rendering
- Desktop Window Manager (DWM),messaging
- DWM (Desktop Window Manager),messaging
- messaging
ms.topic: article
ms.date: 05/30/2019
---

# Enable and control DWM composition

The Desktop Window Manager (DWM) composition APIs provide several functions for setting and querying for basic information that is used by the DWM. These APIs enable you to query and change the composition state. Additionally, you can set and query the rendering policy for different DWM window attributes.

## Retrieving colorization information

The color of the non-client region of a window is determined by the current system color theme. The colorization value is provided through the DWM APIs to enable your application to match client UI with the system color theme.

To access this colorization value, and monitor the color change, use the [**DwmGetColorizationColor**](/windows/desktop/api/dwmapi/nf-dwmapi-dwmgetcolorizationcolor) function and the [**WM_DWMCOLORIZATIONCOLORCHANGED**](wm-dwmcolorizationcolorchanged.md) message.

This example demonstrates how to handle the color changed message and access the new color.

```cpp
...
case WM_DWMCOLORIZATIONCOLORCHANGED:
{
    DWORD newColorizationColor{ (DWORD)wParam };
    BOOL isBlendedWithOpacity{ (BOOL)lParam };
}
break;
...
```

## Controlling non-client region rendering

Two of the visual effects that DWM enables are transparency of the non-client region of a window, and transition effects. Your application might have to disable or re-enable these effects for styling or compatibility reasons. The following functions are used to manage transparency and transition effect behavior.

- [**DwmGetWindowAttribute**](/windows/desktop/api/dwmapi/nf-dwmapi-dwmgetwindowattribute)
- [**DwmSetWindowAttribute**](/windows/desktop/api/dwmapi/nf-dwmapi-dwmsetwindowattribute)

To retrieve the current non-client rendering state for an application's window, call [**DwmGetWindowAttribute**](/windows/desktop/api/dwmapi/nf-dwmapi-dwmgetwindowattribute) with *dwAttribute* set to [**DWMWA_NCRENDERING_ENABLED**](/windows/desktop/api/dwmapi/ne-dwmapi-dwmwindowattribute). As you can see from the documentation for [**DWMWA_NCRENDERING_ENABLED**](/windows/desktop/api/dwmapi/ne-dwmapi-dwmwindowattribute), when you pass that flag to **DwmGetWindowAttribute**, the retrieved attribute value is of type **BOOL**. Different flags cause **DwmGetWindowAttribute** to return values of different types. Here's a code example.

```cpp
BOOL isNCRenderingEnabled{ FALSE };
HRESULT hr = ::DwmGetWindowAttribute(hWnd,
    DWMWA_NCRENDERING_ENABLED,
    &isNCRenderingEnabled,
    sizeof(isNCRenderingEnabled));
```

This next example shows how to use the [**DWMWA_EXTENDED_FRAME_BOUNDS**](/windows/desktop/api/dwmapi/ne-dwmapi-dwmwindowattribute) flag with **DwmGetWindowAttribute** to retrieve the extended frame bounds rectangle of a window. The documentation for that flag tells us that the retrieved attribute value is of type **RECT**.

```cpp
RECT extendedFrameBounds{ 0,0,0,0 };
HRESULT hr = ::DwmGetWindowAttribute(hWnd,
    DWMWA_EXTENDED_FRAME_BOUNDS,
    &extendedFrameBounds,
    sizeof(extendedFrameBounds));
```

> [!NOTE]
> Follow the same programming pattern shown above when you call [**DwmGetWindowAttribute**](/windows/desktop/api/dwmapi/nf-dwmapi-dwmgetwindowattribute) with flags for different attributes. The [**DWMWINDOWATTRIBUTE**](/windows/desktop/api/Dwmapi/ne-dwmapi-dwmwindowattribute) enumeration topic indicates, in the row for each flag, what type of value you should pass a pointer to in the *pvAttribute* parameter for **DwmGetWindowAttribute**. The *cbAttribute* parameter contains the size, in bytes, of that object.

[**DwmSetWindowAttribute**](/windows/desktop/api/dwmapi/nf-dwmapi-dwmsetwindowattribute) enables your application to set the non-client area rendering policy. That function also determines how your application should handle DWM transition effects.

This next example disables non-client area rendering. This causes any previous calls to [DwmEnableBlurBehindWindow](/windows/desktop/api/dwmapi/nf-dwmapi-dwmenableblurbehindwindow) or to [DwmExtendFrameIntoClientArea](/windows/desktop/api/dwmapi/nf-dwmapi-dwmextendframeintoclientarea) to be disabled.

```
HRESULT DisableNCRendering(HWND hWnd)
{
    HRESULT hr = S_OK;

    DWMNCRENDERINGPOLICY ncrp = DWMNCRP_DISABLED;

    // Disable non-client area rendering on the window.
    hr = ::DwmSetWindowAttribute(hWnd,
        DWMWA_NCRENDERING_POLICY,
        &ncrp,
        sizeof(ncrp));

    if (SUCCEEDED(hr))
    {
        // ...
    }

    return hr;
}
```

In addition to controlling the non-client area rendering, [**DwmSetWindowAttribute**](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmsetwindowattribute) can also control DWM transition effects. You can set transition behavior by using **DWMWA\_TRANSITIONS\_FORCEDISABLED** as the *dwAttribute* parameter.

## Messages

The following messages provide notification of DWM events. These messages can be used to monitor changes such as composition state changes and system color theme changes.

- [**WM\_DWMCOLORIZATIONCOLORCHANGED**](wm-dwmcolorizationcolorchanged.md)
- [**WM\_DWMCOMPOSITIONCHANGED**](wm-dwmcompositionchanged.md)
- [**WM\_DWMNCRENDERINGCHANGED**](wm-dwmncrenderingchanged.md)
- [**WM\_DWMWINDOWMAXIMIZEDCHANGE**](wm-dwmwindowmaximizedchange.md)

## Disabling DWM composition (Windows 7 and earlier)

> [!WARNING]
> The info in this section applies only to Windows 7 and earlier systems.

Because DWM uses the graphics processing unit (GPU) for desktop composition, your application might have to disable DWM for compatibility. Applications that take full control of the desktop, such as games that run in full-screen mode, must determine whether the DWM is enabled and if it is, disable it. To do this, two functions are needed.

- [**DwmIsCompositionEnabled**](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmiscompositionenabled)
- [**DwmEnableComposition**](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmenablecomposition)

A call to [**DwmEnableComposition**](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmenablecomposition) with *fEnable* set to **DWM\_EC\_DISABLECOMPOSITION** disables DWM composition until either the calling process has shut down, or composition has been re-enabled by calling **DwmEnableComposition** with *fEnable* set to **DWM\_EC\_ENABLECOMPOSITION**. DWM composition restarts automatically as soon as all applications that have disabled composition have either shut down or have manually re-enabled composition by calling **DwmEnableComposition**.

> [!NOTE]  
> The DWM automatically disables composition when an application attempts to draw directly to the primary display surface. Composition will be disabled until the primary device surface is released by that application.
