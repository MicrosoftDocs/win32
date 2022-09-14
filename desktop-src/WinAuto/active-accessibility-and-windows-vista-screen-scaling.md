---
title: Active Accessibility and Windows Vista Screen Scaling
description: Windows Vista enables users to change the dots-per-inch (dpi) setting so that most UI elements on the screen appear larger.
ms.assetid: c781fefd-09f0-4340-b3d3-f4e57308f392
ms.topic: article
ms.date: 05/31/2018
---

# Active Accessibility and Windows Vista Screen Scaling

Windows Vista enables users to change the dots-per-inch (dpi) setting so that most UI elements on the screen appear larger. Although this feature has long been available in Microsoft Windows, in previous versions the scaling had to be implemented by applications. In Windows Vista, the Desktop Window Manager performs default scaling for all applications that do not handle their own scaling. Microsoft Active Accessibility client applications must take this feature into account.

## Scaling in Windows Vista

The default dpi setting is 96, which means that 96 pixels occupy a width or height of one notional inch. The exact measure of an "inch" depends on the size and physical resolution of the monitor. For example, on a monitor 12 inches wide, at a horizontal resolution of 1280 pixels, a horizontal line of 96 pixels extends about 9/10 of an inch.

Changing the dpi setting is not the same as changing the screen resolution. With dpi scaling, the number of physical pixels on the screen remains the same. However, scaling is applied to the size and location of UI elements. This scaling can be performed automatically by the Desktop Window Manager (DWM) for the desktop and for applications that do not explicitly ask not to be scaled.

In effect, when the user sets the scale factor to 120 dpi, a vertical or horizontal inch on the screen becomes bigger by 25 percent. All dimensions are scaled accordingly. The offset of a window from the top and left edges of the screen increases by 25 percent. The size of the window increases in the same proportion, along with the offsets and sizes of all UI elements it contains.

By default, the DWM does not perform scaling for non-dpi-aware applications when the user sets the dpi to 120, but does perform it when the dpi is set to a custom value of 144 or higher. However, the user can override the default behavior.

Screen scaling creates new challenges for applications that are concerned in any way with screen coordinates. The screen now contains two coordinate systems: physical and logical. The physical coordinates of a point are the actual offset in pixels from the top left of the origin. The logical coordinates are the offsets as they would be if the pixels themselves were scaled.

Suppose you design a dialog box with a button at coordinates (100, 48). When this dialog box is displayed at the default 96 dpi, the button is located at physical coordinates of (100, 48). At 120 dpi, it is located at physical coordinates of (125, 60). But the logical coordinates are the same at any dpi setting: (100, 48).

Logical coordinates are important, because they make the behavior of the operating system and applications consistent regardless of the dpi setting. For example, **System.Windows.Forms.Cursor.Position** normally returns the logical coordinates. If you move the cursor over an element in a dialog box, the same coordinates are returned regardless of the dpi setting. If you draw a control at (100, 100), it is drawn to those logical coordinates, and will occupy the same relative position at any dpi setting.

## Scaling in Active Accessibility Clients

Microsoft Active Accessibility does not use logical coordinates. The following methods and functions either return physical coordinates or take them as parameters.

-   [**IAccessible::accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)
-   [**IAccessible::accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)
-   [**AccessibleObjectFromPoint**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfrompoint)

By default, an Microsoft Active Accessibility client application running in a non-96-dpi environment will not be able to obtain correct results from these calls. For example, because the cursor position is in logical coordinates, the client cannot simply pass these coordinates to [**AccessibleObjectFromPoint**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfrompoint) to obtain the element that is under the cursor.

In addition, an application that creates a window outside its client area, such as an accessibility application that highlights focused UI elements, will not create the window at the correct screen location, because the window will be placed at the logical coordinates, not the physical coordinates returned by [**IAccessible::accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation).

The solution is in two parts:

-   Make the client application "dpi-aware". To do this, call the [**SetProcessDPIAware**](/windows/win32/api/winuser/nf-winuser-setprocessdpiaware) function at startup. This function makes the entire process dpi-aware, meaning that all windows that belong to the process are unscaled.
-   Use functions that are dpi-aware. For example, to get cursor coordinates, call the [**GetPhysicalCursorPos**](/windows/win32/api/winuser/nf-winuser-getphysicalcursorpos) function. Do not use [**GetCursorPos**](/windows/win32/api/winuser/nf-winuser-getcursorpos); its behavior in dpi-aware applications is undefined.

If your application performs direct cross-process communication with non-dpi-aware applications, you may have convert between logical and physical coordinates by using the [**PhysicalToLogicalPoint**](/windows/win32/api/winuser/nf-winuser-physicaltologicalpoint) and [**LogicalToPhysicalPoint**](/windows/win32/api/winuser/nf-winuser-logicaltophysicalpoint) functions.

 

 