---
title: Using Visual Styles with Custom and Owner-Drawn Controls
description: This topic describes how to use the visual styles API to apply visual styles to custom controls or owner-drawn controls.
ms.assetid: 8b06f9ce-702c-48f8-8cf3-2718a09b8d77
ms.topic: article
ms.date: 05/31/2018
---

# Using Visual Styles with Custom and Owner-Drawn Controls

This topic describes how to use the visual styles API to apply visual styles to custom controls or owner-drawn controls.

-   [Drawing Controls with Visual Styles](#drawing-controls-with-visual-styles)
-   [Responding to Theme Changes](#responding-to-theme-changes)
-   [Related topics](#related-topics)

## Drawing Controls with Visual Styles

Visual styles are supported by ComCtrl32.dll version 6 and later. If your application is configured to use ComCtrl32.dll version 6 and later, and if that version is available on the system, the current visual styles are automatically applied to all common controls in your application. However, the current visual styles are not automatically applied to custom controls or owner-drawn controls. Your application must include code that checks whether visual styles are available and, if so, uses the visual styles API to apply the currently selected visual styles to your custom and owner-drawn controls.

To check whether visual styles are available, call the [**IsAppThemed**](/windows/desktop/api/Uxtheme/nf-uxtheme-isappthemed) function. If visual styles are not available, use fallback code to draw the control.

If visual styles are available, you can use visual-styles functions such as [**DrawThemeText**](/windows/desktop/api/Uxtheme/nf-uxtheme-drawthemetext) to render your control. Note that [**DrawThemeTextEx**](/windows/desktop/api/Uxtheme/nf-uxtheme-drawthemetextex) enables you to customize the appearance of text, retaining some properties of the theme font while modifying others.

**To draw a control in the current visual style**

1.  Call [**OpenThemeData**](/windows/desktop/api/Uxtheme/nf-uxtheme-openthemedata), passing the *hwnd* of the control you want to apply visual styles to and a class list that describes the control's type. The classes are defined in Vssym32.h. **OpenThemeData** returns an HTHEME handle, but if the visual styles manager is disabled or the current visual style does not supply specific information for a given control, the function returns **NULL**. If the return value is **NULL**, use non-visual-styles drawing functions.
2.  To draw the control background, call [**DrawThemeBackground**](/windows/desktop/api/Uxtheme/nf-uxtheme-drawthemebackground) or [**DrawThemeBackgroundEx**](/windows/desktop/api/Uxtheme/nf-uxtheme-drawthemebackgroundex).
3.  To determine the location of the content rectangle, call [**GetThemeBackgroundContentRect**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemebackgroundcontentrect).
4.  To render text, use either [**DrawThemeText**](/windows/desktop/api/Uxtheme/nf-uxtheme-drawthemetext) or [**DrawThemeTextEx**](/windows/desktop/api/Uxtheme/nf-uxtheme-drawthemetextex), basing the coordinates on the rectangle returned by [**GetThemeBackgroundContentRect**](/windows/desktop/api/Uxtheme/nf-uxtheme-getthemebackgroundcontentrect). These functions can render text either in the theme's font for a specified control part and state, or in the font currently selected into the device context (DC).
5.  When your control receives a [**WM\_DESTROY**](/windows/desktop/winmsg/wm-destroy) message, call [**CloseThemeData**](/windows/desktop/api/Uxtheme/nf-uxtheme-closethemedata) to release the theme handle that was returned when you called [**OpenThemeData**](/windows/desktop/api/Uxtheme/nf-uxtheme-openthemedata).

The following example code demonstrates one way to draw a button control in the current visual style.


```C++
HTHEME hTheme = NULL;

hTheme = OpenThemeData(hwndButton, L"Button");
// ...
DrawMyControl(hDC, hwndButton, hTheme, iState);
// ...
if (hTheme)
{
    CloseThemeData(hTheme);
}


void DrawMyControl(HDC hDC, HWND hwndButton, HTHEME hTheme, int iState)
{
    RECT rc, rcContent;
    TCHAR szButtonText[255];
    HRESULT hr;
    size_t cch;

    GetWindowRect(hwndButton, &rc);
    GetWindowText(hwndButton, szButtonText,
                  (sizeof(szButtonText) / sizeof(szButtonText[0])+1));
    hr = StringCchLength(szButtonText,
         (sizeof(szButtonText) / sizeof(szButtonText[0])), &cch);
    if (hTheme)
    {
        hr = DrawThemeBackground(hTheme, hDC, BP_PUSHBUTTON, iState, &rc, 0);
        if (SUCCEEDED(hr))
        {
            hr = GetThemeBackgroundContentRect(hTheme, hDC, BP_PUSHBUTTON, 
                    iState, &rc, &rcContent);
        }

        if (SUCCEEDED(hr))
        {
            hr = DrawThemeText(hTheme, hDC, BP_PUSHBUTTON, iState, 
                    szButtonText, cch,
                    DT_CENTER | DT_VCENTER | DT_SINGLELINE,
                    0, &rcContent);
        }

    }
    else
    {
        // Draw the control without using visual styles.
    }
}
```





The following example code is in the [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) message handler for a subclassed button control. The text for the control is drawn in the visual styles font, but the color is application-defined depending on the state of the control.


```C++
// textColor is a COLORREF whose value has been set according to whether the button is "hot".
// paint is the PAINTSTRUCT whose members are filled in by BeginPaint.
HTHEME theme = OpenThemeData(hWnd, L"button");
if (theme)
{
    DTTOPTS opts = { 0 };
    opts.dwSize = sizeof(opts);
    opts.crText = textColor;
    opts.dwFlags |= DTT_TEXTCOLOR;
    WCHAR caption[255];
    size_t cch;
    GetWindowText(hWnd, caption, 255);
    StringCchLength(caption, 255, &cch);
    DrawThemeTextEx(theme, paint.hdc, BP_PUSHBUTTON, CBS_UNCHECKEDNORMAL, 
        caption, cch, DT_CENTER | DT_VCENTER | DT_SINGLELINE, 
        &paint.rcPaint, &opts);
    CloseThemeData(theme);
}
else
{
    // Draw the control without using visual styles.
}
```



You can use parts from other controls and render each part separately. For example, for a calendar control that consists of a grid, you can treat each square formed by the grid as a toolbar button, by obtaining the theme handle as follows:


```C++
OpenThemeData(hwnd, L"Toolbar");
```



You can mix and match control parts by calling [**OpenThemeData**](/windows/desktop/api/Uxtheme/nf-uxtheme-openthemedata) multiple times for a given control and using the appropriate theme handle to draw different parts. In some visual styles, however, certain parts might not be compatible with other parts.

Another approach to rendering controls in the active visual style is to use the system colors. For example, you can use system colors to set the text color when calling the [**DrawThemeTextEx**](/windows/desktop/api/Uxtheme/nf-uxtheme-drawthemetextex) function. Most system colors are set when a visual style file is applied.

## Responding to Theme Changes

When your control receives a [**WM\_THEMECHANGED**](/windows/desktop/winmsg/wm-themechanged) message and is holding a global handle to the theme, it should do the following:

-   Call [**CloseThemeData**](/windows/desktop/api/Uxtheme/nf-uxtheme-closethemedata) to close the existing theme handle.
-   Call [**OpenThemeData**](/windows/desktop/api/Uxtheme/nf-uxtheme-openthemedata) to get the theme handle to the newly loaded visual style.

The following example illustrates the two calls.


```C++
case WM_THEMECHANGED:
     CloseThemeData (g_hTheme);
     g_hTheme = OpenThemeData (hwnd, L"MyClassName");
```



## Related topics

<dl> <dt>

[Enabling Visual Styles](cookbook-overview.md)
</dt> <dt>

[Visual Styles](themes-overview.md)
</dt> </dl>

 

 