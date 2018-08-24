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

## MSIX packages: Safe, secure, and reliable deployment

MSIX is a new containerization package format that applies to all Windows applications including Win32, Windows Forms, WPF, and UWP. This new format inherits great features from UWP:

* Robust installation and updating.

* Managed security model with a flexible capability system.

* Support for the Microsoft Store, enterprise management, and many custom distribution models.

* Use DAC or command-line. Visual Studio support coming.

* If you've got apps without source code, use IT Pro tool.

See [MSIX](https://review.docs.microsoft.com/en-us/windows/msix/landing-page-test?branch=master)


## XAML Islands: Fluent controls in your desktop application UIs

Add [Fluent controls](https://docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/controls-by-function) to the user interfaces of your desktop application by using XAML Islands.

A XAML island acts as a wrapper for Fluent controls. How you create A XAML island in your desktop application depends on what type of desktop application you have. The following table summarizes your options.

| XAML Island Technology            |  Windows Forms | WPF | C++ Win32 |
|------------------------------|----------------|-----|-------|
| XAML Islands Wrapped controls|  ✔             |  ✔ |       |
| XAML Islands Host Control    |  ✔             |  ✔ |       |
| XAML Islands API             |  ✔             |  ✔ |  ✔    |

If you have a C++ Win32 application, you can add a XAML island by using the XAML Islands API.

If you have a Windows Forms or WPF application, You can drag a special control (called a XAML Island host control) to the surface of your designer. This control abstracts away the complexities of a XAML island so that all you have to do is assign that control to your favorite Fluent control.

There are several Fluent controls that you can add directly to your design surfaces without even having to first use a host control. These are called **Wrapped Controls**. They go one step further by abstracting away the host control.

### XAML Island host control

>[!NOTE]
>This feature is in preview only.

* Host control is convenient way to add a XAML Island to Windows Forms and WPF apps.

  * Show simple example with screenshot.

See [Host UWP controls in WPF and Windows Forms applications](https://docs.microsoft.com/en-us/windows/uwp/xaml-platform/xaml-host-controls)

See [WindowsXAMLHostControl](https://docs.microsoft.com/en-us/windows/communitytoolkit/controls/WindowsXAMLHost)  * Link to host control doc on Community Toolkit Page.

### XAML Island wrapped controls

>[!NOTE]
>This feature is in preview only.

* Wrapped controls that you can use directly on design surfaces.

* Complete list going out with next refresh of the Toolkit is currently TBD.

#### WebView

* Code snippet of XAML Island assigned to WebView.

* Screenshot of WebView in win32 application.

See [WebView controls for Windows Forms and WPF applications](https://docs.microsoft.com/en-us/windows/communitytoolkit/controls/webview)

#### InkCanvas

* Code snippet of XAML Island assigned to WebView.

* Screenshot of WebView in win32 application.

* Link to WebView doc.

#### InkToolbar

* Code snippet of XAML Island assigned to WebView.

* Screenshot of WebView in win32 application.

* Link to WebView doc.

#### MediaPlayerElement

* Code snippet of XAML Island assigned to WebView.

* Screenshot of WebView in win32 application.

* Link to WebView doc.

#### WebViewCompatible

* Code snippet of XAML Island assigned to WebView.

* Screenshot of WebView in win32 application.

* Link to WebView doc.

### XAML Island API

>[!NOTE]
>This feature is in preview only.

* Win32 API for Win32 apps.

  * Show simple example with screenshot.

  * Link to code-first sample.

See [Using the UWP XAML hosting API in a desktop application](https://review.docs.microsoft.com/en-us/windows/uwp/xaml-platform/using-the-xaml-hosting-api?branch=mcleans-xamlhosting).

### Fluent controls made for the desktop

* Add any Fluent control to your XAML Islands.

See [Controls by function](https://docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/controls-by-function)

* There's several new desktop-grade controls available with Fluent.

* These controls render as expected on large desktop screens.

#### MenuBar

* Code snippet of XAML Island assigned to MenuBar.

* Screenshot of MenuBar in win32 application.

See [Menus and context menus](https://review.docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/menus?branch=jimwalk%2Frs5-menu-bar).

#### DropDownButton

* Code snippet of XAML Island assigned to DropDownButton.

* Screenshot of DropDownButton in win32 application.

See [Create a drop down button](https://docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/buttons#create-a-drop-down-button)

#### SplitButtonMenuBar

* Code snippet of XAML Island assigned to SplitButtonMenuBar.

* Screenshot of SplitButtonMenuBar in win32 application.

See [Create a split button](https://docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/buttons#create-a-split-button)

#### CommandBarFlyout

* Code snippet of XAML Island assigned to CommandBarFlyout.

* Screenshot of CommandBarFlyout in win32 application.

See [Command bar flyout](https://review.docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/command-bar-flyout?branch=jimwalk%2Frs5-command-bar-flyout).

#### EditableComboBox

* Code snippet of XAML Island assigned to EditableComboBox.

* Screenshot of EditableComboBox in win32 application.

See [Make a combo box editable](https://review.docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/combo-box?branch=rs5#make-a-combo-box-editable)

#### DataGridView

* Code snippet of XAML Island assigned to DataGridView.

* Screenshot of DataGridView in win32 application.

See [DataGrid XAML control](https://docs.microsoft.com/en-us/windows/communitytoolkit/controls/datagrid)

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
