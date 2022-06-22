---
title: High-contrast mode
description: High-contrast mode
ms.assetid: 817F2BBD-3744-4D34-927F-EBF9F7894CC0
ms.topic: article
ms.date: 05/31/2018
---

# High-contrast mode

## Platforms

 **Clients** - Windows 8  
**Servers** - Windows Server 2012  



## Description

In previous Windows operating systems, high-contrast mode was limited to themes running under classic themes, which were not visually styled. In Windows 8 and Windows Server 2012, classic mode has been removed and replaced with visually styled high contrast themes. One of the main benefits for you of this change is the removal of a separate code path for apps running in classic mode.

Developers still need to be educated in how high-contrast mode can affect their app and how to develop an app that is truly style-agnostic. This is important because while the incorrect use or assumption of theme colors can cause apps to behave correctly under a visual style such as Aero, those same apps respond incorrectly under high contrast. For instance, in Aero, text is always black and the highlight color is a light blue. In high-contrast black, however, the highlight color is black. If you assume black text, as has been the case in many in-box apps prior to Windows 8, and use the system default for highlighting, the user will see black text on a black background. It’s necessary in these situations to understand how to use themes and system metrics correctly so the app looks correct across styles.

## Manifestations

-   Theming is not enabled in the client area of apps that do not contain a Windows 8 &lt;supportedOS&gt; tag in their app manifest. Therefore, the apps must render the client area, using the code path required to render in high-contrast mode of the classic theme.
-   Theming is not enabled in both the non-client and client areas of apps in high-contrast themes. It is also not enabled in apps that do not contain a Windows 8 &lt;supportedOS&gt; tag in their app manifest and that draw in the non-client area of a window using the DwnIsCompositionEnabled() API. The entire app renders in the high-contrast mode of the classic theme.
-   Apps that add support for Windows 8 in their manifest, but do not use visual styles for rendering, that is, they hardcode colors or images in their apps, might not render correctly in high-contrast themes. Text might be difficult to read or images might not appear as they should in high contrast mode.

## Mitigation

The text colors in the high-contrast themes have been authored to be compliant with the Microsoft Accessibility guidelines. We maintain a 14:1 high-contrast ratio between foreground and background. If the colors that are enabled by default are not suitable to a particular end user, they can easily be customized through the control panel settings for ‘Window Color’ in those high-contrast themes.

These UI components are customizable in high-contrast themes:

-   Window background color
-   Text color
-   Hyperlinks color
-   Disabled text
-   Selected text foreground and background colors
-   Active window title foreground and background colors
-   Inactive window title foreground and background colors
-   Button foreground and background colors

## Solution

If unexpected behavior is seen in apps in high-contrast themes, one of these solutions might help:

-   **Manifesting an app for Windows 8:**

    Apps that don’t contain the Windows 8 &lt;supportedOS&gt; tag in the app manifest will have their client areas rendered without a theme. In-box apps should all contain this entry in the app manifest. Add the 4a2f28e3-53b9-4441-ba9c-d69d4a4a6e38 GUID value for Windows 8.

-   **Using visual styles with owner-drawn UIs:**

    Owner-drawn controls should follow the instructions on [MSDN](/windows/desktop/Controls/using-visual-styles) for correctly rendering control parts and states, including text. Developers should not rely on the text or background color specified in a device context in order to use non-UxTheme methods for rendering. In the case where there is no theme part for the control in question, use GetThemeSysColor with the [appropriate metric](/windows/desktop/api/winuser/nf-winuser-getsyscolor) and draw the text using standard GDI methods. If none of the UxTheme calls are appropriate, use the GetSysColor method to get the appropriate metric.

-   **Selecting text color:**

    Do not use a hardcoded text color, even if it’s assumed to look fine in all common scenarios. The shipping themes are created in a way that supports high visibility with associated metrics. For instance, COLOR\_HIGHLIGHTTEXT is meant to be used with COLOR\_HIGHLIGHT as a background and COLOR\_WINDOWTEXT is meant to be used with COLOR\_WINDOW as a background. If there are exceptions to these associations, work with them in the theme parts and state definitions themselves and not in code. When designing high-contrast UIs, it is crucial that the UI be agnostic to the currently applied high-contrast theme, as high-contrast users can customize their colors.

-   **Responding to WM\_ThemeChange Event:**

    If your app caches the colors retrieved from the theme or applies colors in a nonstandard fashion, add a message handler for WM\_THEMECHANGE that recalculates the stored color values and repaints the UI.

-   **Writing a high-contrast WWA app:**

    Web apps do not have access to the UxTheme APIs, but should still be written with the current system metrics as the basis for the UI. There are a few resources for WWA developers to leverage to ensure a high-contrast compliant app:

    -   The [W3C CSS Color specification](https://www.w3.org/TR/css3-color/) specifies syntax for using system metrics instead of specific colors
    -   Support for high-contrast media queries is being added to Internet Explorer 10
    -   WWAs can leverage the IAccessibilityCapabilities::get\_HighContrast() method to check the state of high contrast

    Windows Store apps don’t have many of the same issues with theme parts that are present in Classic Windows Applications, but you still need to ensure high-contrast compliance. By default, Internet Explorer ignores certain user-defined styles and replaces them with high-contrast compliant values. For example, background-image, background, and color CSS properties are ignored.

    If you don’t want Internet Explorer to ignore any properties you set and you have made sure that the UI is high-contrast compliant, you can set the new M3 CSS property –ms-high-contrast: off on a parent element.

-   **Writing a high-contrast Windows Store app:**

    Windows Store app should use the [SystemColors](/dotnet/api/system.windows.systemcolors) class for determining proper UI element coloring, keeping in mind that certain system metric colors are designed to be used in conjunction, such as SystemColors.WindowColor and SystemColors.WindowTextColor. This facilitates a superior high-contrast experience.

-   **Properly detecting high contrast in previous versions of Windows:**

    Apps running on previous versions of Windows do not have access to the new high-contrast themes even if the manifest specifies compatibility with the version of Windows in question. As such, it might be necessary to insert additional code paths to handle rendering in the classic environment used in previous versions of Windows. The presence of high contrast in this case should be checked by calling the [SystemParametersInfo](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) function with the SPI\_GETHIGHCONTRAST flag. This is the only supported way of checking the presence of high contrast.

## Tests

While testing an app, make sure that it renders correctly in all the in-box themes provided by Windows 8: Aero, Basic, High Contrast 1, High Contrast 2, High Contrast Black, and High Contrast White. Make sure that the text is clearly visible and easy to read in the high-contrast themes.

## Resources

-   [Aero Style Classes, Parts, and States](../controls/aero-style-classes-parts-and-states.md) (the new basic theme and high-contrast themes also use these states)
-   [Parts and States common to all visual styles](../controls/parts-and-states.md)
-   [Using Visual Styles with Custom and Owner-Drawn Controls](../controls/using-visual-styles.md)
-   [GetSysColor function](/windows/win32/api/winuser/nf-winuser-getsyscolor)
-   [W3C CSS Color Module Level 3](https://www.w3.org/TR/css3-color/)
-   [SystemColors Class](/dotnet/api/system.windows.systemcolors)
-   [SystemParametersInfo function](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa)
-   [Microsoft Accessibility](https://www.microsoft.com/enable/)

 

 
