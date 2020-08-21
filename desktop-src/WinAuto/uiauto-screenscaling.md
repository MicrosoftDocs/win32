---
title: Understanding Screen Scaling Issues
description: Windows Vista and later versions of the operating system enable users to change the dots per inch (dpi) setting so that most UI elements on the screen appear larger.
ms.assetid: 27dc49e7-2466-4ea3-a6d9-5ea86d6b4c60
keywords:
- clients,UI Automation screen scaling
- clients,screen scaling
- clients,scaling
- UI Automation,screen scaling
- UI Automation,scaling
- screen scaling
ms.topic: article
ms.date: 05/31/2018
---

# Understanding Screen Scaling Issues

Windows Vista and later versions of the operating system enable users to change the dots per inch (dpi) setting so that most UI elements on the screen appear larger. In earlier versions of Windows, the scaling had to be implemented by applications. In Windows Vista and later, the Desktop Window Manager (DWM) performs default scaling for all applications that do not handle their own scaling. Microsoft UI Automation client applications must take this feature into account.

This topic contains the following sections:

-   [Scaling in Windows Vista and Later](#scaling-in-windows-vista-and-later)
-   [Scaling in UI Automation Clients](#scaling-in-ui-automation-clients)

## Scaling in Windows Vista and Later

The default dpi setting is 96, which means that 96 pixels occupy a width or height of one notional inch. The exact measure of an "inch" depends on the size and physical resolution of the monitor. For example, on a monitor 12 inches wide, at a horizontal resolution of 1280 pixels, a horizontal line of 96 pixels extends about 9/10 of an inch.

Changing the dpi setting is not the same as changing the screen resolution. With dpi scaling, the number of physical pixels on the screen remains the same. However, scaling is applied to the size and location of UI elements. This scaling can be performed automatically by the DWM for the desktop and for applications that do not explicitly ask not to be scaled.

In effect, when the user sets the scale factor to 120 dpi, a vertical or horizontal inch on the screen becomes bigger by 25 percent. All dimensions are scaled accordingly. The offset of an application window from the top edge and left edge of the screen increases by 25 percent. If application scaling is enabled and the application is not dpi-aware, the size of the window increases in the same proportion, along with the offsets and sizes of all UI elements it contains.

> [!Note]  
> By default, the DWM does not perform scaling for non-dpi-aware applications when the user sets the dpi to 120, but does perform scaling when the dpi is set to a custom value of 144 or higher. However, the user can override the default behavior.

 

Screen scaling creates new challenges for applications that are concerned in any way with screen coordinates. The screen now contains two coordinate systems: physical and logical. The physical coordinates of a point are the actual offset in pixels from the upper-left of the origin point. The logical coordinates are the offsets as they would be if the pixels themselves were scaled.

Suppose you design a dialog box with a button at coordinates (100, 48). When this dialog box is displayed at the default 96 dpi, the button is located at physical coordinates of (100, 48). At 120 dpi, it is located at physical coordinates of (125, 60). But the logical coordinates are the same at any dpi setting: (100, 48).

Logical coordinates are important, because they make the behavior of the operating system and applications consistent, regardless of the dpi setting. For example, typically, the [**GetCursorPos**](/windows/desktop/api/winuser/nf-winuser-getcursorpos) function returns the logical coordinates. If you move the cursor over an element in a dialog box, the same coordinates are returned, regardless of the dpi setting. If you draw a control at (100, 100), it is drawn to those logical coordinates, and will occupy the same relative position at any dpi setting.

## Scaling in UI Automation Clients

The UI Automation API does not use logical coordinates. The following methods and properties return physical coordinates or take physical coordinates as parameters.

-   [**IUIAutomation::ElementFromPoint**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfrompoint)
-   [**IUIAutomation::ElementFromPointBuildCache**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfrompointbuildcache)
-   [**IUIAutomationElement::GetClickablePoint**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getclickablepoint)
-   [**IUIAutomationElement::CurrentBoundingRectangle**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentboundingrectangle)
-   [**IUIAutomationElement::CachedBoundingRectangle**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_cachedboundingrectangle)
-   [**IRawElementProviderFragment::BoundingRectangle**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementproviderfragment-get_boundingrectangle)

By default, UI Automation applications that are running in an environment that is not set to 96 dpi will not obtain correct results from these methods and properties. For example, because the cursor position is in logical coordinates, the client cannot pass these coordinates to [**IUIAutomation::ElementFromPoint**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfrompoint) to obtain the element that is under the cursor. In addition, the application will not be able to correctly place windows outside its client area.

The solution has two parts.

First, make the client application dpi-aware. To do this, call the [**SetProcessDPIAware**](/windows/desktop/api/winuser/nf-winuser-setprocessdpiaware) function at startup. This function makes the entire process dpi-aware, meaning that all windows that belong to the process are unscaled.

Second, to get cursor coordinates, call the [**GetPhysicalCursorPos**](/windows/desktop/api/winuser/nf-winuser-getphysicalcursorpos) function.

 

 