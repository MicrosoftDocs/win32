---
Description: Add modern XAML user interfaces, create MSIX packages, and incorporate other modern components into your desktop application in an "alacart" fashion.
title: Desktop guide to the modern platform
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 08/21/2018
---

# Desktop guide to the modern platform

* The modern platform is being made available as stand-alone building blocks that you can adopt in your desktop applications ala cart without having to completely rewrite applications in UWP.

* Enhance existing investments in-place. No re-write required. No need to learn a whole new stack to modernize.

* Choose which stack to invest in (modern front-ends, MSIX deployment + opt-into security level, UWP APIs etc.).

* Add UWP XAML controls to  

## MSIX packages

MSIX is a new containerization package format that applies to all Windows applications including Win32, Windows Forms, WPF, and UWP. This new format inherits great features from UWP:

* Robust installation and updating.

* Managed security model with a flexible capability system.

* Support for the Microsoft Store, enterprise management, and many custom distribution models.

* Use DAC or command-line. Visual Studio support coming.

* If you've got apps without source code, use IT Pro tool.

See [MSIX](https://review.docs.microsoft.com/en-us/windows/msix/landing-page-test?branch=master)

## XAML Islands (Preview)

You can add [UWP XAML controls](https://docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/controls-by-function) to the user interfaces of your desktop application by using XAML Islands.

A XAML island acts as a wrapper for UWP XAML controls. If you have a Windows Forms or WPF application, You can drag a special control, called a XAML Island host control, to the surface of your designer. This control abstracts away the complexities of a XAML island so that all you have to do is assign that control to your favorite UWP XAML control.

There are several Fluent controls that you can add directly to your design surfaces without even having to first use a host control. These are called **Wrapped Controls**. They go one step further by abstracting away the host control.

If you have a C++ Win32 application, you can add a XAML island by using the XAML Islands API.

| XAML Island Technology            |  Windows Forms | WPF | C++ Win32 |
|------------------------------|----------------|-----|-------|
| XAML Island Host Control    |  ✔             |  ✔ |       |
| XAML Island Wrapped controls|  ✔             |  ✔ |       |
| XAML Island API             |  ✔             |  ✔ |  ✔    |

To learn more about XAML Islands, see [Host UWP controls in WPF and Windows Forms applications](https://docs.microsoft.com/en-us/windows/uwp/xaml-platform/xaml-host-controls).

### XAML Island Host Control (Preview)

>[!NOTE]
>This feature is in preview only.

You can drag a XAML Island Host control directly to the design surface of your Windows Forms or WPF application. Then, you can set that host control to any UWP XAML control that you want. See  [WindowsXAMLHostControl](https://docs.microsoft.com/en-us/windows/communitytoolkit/controls/WindowsXAMLHost).

For a catalog of UWP XAML controls, See [Controls by function](https://docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/controls-by-function).

Here's some new UWP XAML controls that you can use to create desktop-optimized experiences with a modern Fluent design.

| Control |  Description |
|------ |--------------|
| [Menus and context menus](https://review.docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/menus?branch=jimwalk%2Frs5-menu-bar) | MenuBar |
| [Create a drop down button](https://docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/buttons#create-a-drop-down-button) | DropDownButton |
| [Create a split button](https://docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/buttons#create-a-split-button) | SplitButtonMenuBar |
| [Command bar flyout](https://review.docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/command-bar-flyout?branch=jimwalk%2Frs5-command-bar-flyout) |  CommandBarFlyout |
| [Make a combo box editable](https://review.docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/combo-box?branch=rs5#make-a-combo-box-editable) | EditableComboBox |
| [DataGrid XAML control](https://docs.microsoft.com/en-us/windows/communitytoolkit/controls/datagrid) |   DataGridView |

### XAML Island Wrapped Controls (Preview)

Wrapped controls that you can use directly on design surfaces. They e

| Guide |  Description |
|------ |--------------|
| [WebView](https://docs.microsoft.com/en-us/windows/communitytoolkit/controls/webview) |   Description |
| [InkCanvas]() | Description |
| [InkToolbar]() | Description |
| [MediaPlayerElement]() | Description |
| [WebViewCompatible]() | Description  |

### XAML Island API (Preview)

>[!NOTE]
>This feature is in preview only.

For C++ win32 apps, use the XAML Island API to incorporate UWP XAML controls into your desktop application UIs.

See [Using the UWP XAML hosting API in a desktop application](https://review.docs.microsoft.com/en-us/windows/uwp/xaml-platform/using-the-xaml-hosting-api?branch=mcleans-xamlhosting).

Here's some new UWP XAML controls that you can use to create desktop-optimized experiences with a modern Fluent design.

| Control |  Description |
|------ |--------------|
| [Menus and context menus](https://review.docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/menus?branch=jimwalk%2Frs5-menu-bar) | MenuBar |
| [Create a drop down button](https://docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/buttons#create-a-drop-down-button) | DropDownButton |
| [Create a split button](https://docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/buttons#create-a-split-button) | SplitButtonMenuBar |
| [Command bar flyout](https://review.docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/command-bar-flyout?branch=jimwalk%2Frs5-command-bar-flyout) |  CommandBarFlyout |
| [Make a combo box editable](https://review.docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/combo-box?branch=rs5#make-a-combo-box-editable) | EditableComboBox |
| [DataGrid XAML control](https://docs.microsoft.com/en-us/windows/communitytoolkit/controls/datagrid) |   DataGridView |

## Windows UI library: Windows version-independent Fluent controls

* Value prop and example.

See [Windows UI Library (Preview version)](https://docs.microsoft.com/en-us/uwp/toolkits/winui/)

## Access to WinRT APIs from desktop application code

* Some sort of stake in the ground that clarifies that desktop applications have access to UWP APIs.

See [Enhance your desktop application for Windows 10](https://docs.microsoft.com/en-us/windows/uwp/porting/desktop-to-uwp-enhance)

## Other Interesting technologies

* [.NET Core 3](https://blogs.msdn.microsoft.com/dotnet/2018/05/07/net-core-3-and-support-for-windows-desktop-applications/)
* [Microsoft Graph](https://developer.microsoft.com/en-us/graph)
* [Adaptive Cards](https://adaptivecards.io/)
* [High DPI support in Windows Forms](https://docs.microsoft.com/en-us/dotnet/framework/winforms/high-dpi-support-in-windows-forms)
