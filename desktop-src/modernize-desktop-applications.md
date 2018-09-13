---
Description: Add modern XAML user interfaces, create MSIX packages, and incorporate other modern components into your desktop application in an "alacart" fashion.
title: Desktop guide to the modern platform
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 09/11/2018
---

# Desktop guide to the modern platform

The UWP platform is being made available as a set of "building blocks" that you can adopt in your desktop applications without having to rewrite your application for UWP. There's no need to learn a whole new stack to modernize. You can enhance existing investments in-place by choosing which parts of the platform to adopt.

This guide describes UWP platform features that you can use in your desktop applications right now.

<!-- categorize everything by: features available to any desktop application, features for .NET and Win32, and features for UWP targeted at desktop
-->

## MSIX packages

MSIX is a new containerization package format that applies to all Windows applications including Win32, Windows Forms, WPF, and UWP. This new format inherits great features from UWP and provides robust installation and updating, managed security model with a flexible capability system, and support for the Microsoft Store, enterprise management, and many custom distribution models.

To learn more, see [MSIX](https://docs.microsoft.com/windows/msix).

## XAML Islands (Preview)

You can add [UWP XAML controls](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/controls-by-function) to the user interfaces of your desktop application by using XAML Islands.

A XAML island acts as a wrapper for UWP XAML controls. If you have a Windows Forms or WPF application, You can drag a special control, called a XAML Island host control, to the surface of your designer. This control abstracts away the complexities of a XAML island so that all you have to do is assign that control to your favorite UWP XAML control.

There are several UWP XAML controls that you can add directly to your design surfaces without even having to first use a host control. These are called **Wrapped Controls**. They go one step further by abstracting away the host control.

If you have a C++ Win32 application, you can add a XAML island by using the XAML Islands API.

This table summarizes the options.

| XAML Island Technology            |  Windows Forms | WPF | C++ Win32 |
|------------------------------|----------------|-----|-------|
| XAML Island Host Control    |  ✔             |  ✔ |       |
| XAML Island Wrapped controls|  ✔             |  ✔ |       |
| XAML Island API             |  ✔             |  ✔ |  ✔    |

To learn more about XAML Islands, see [Host UWP controls in WPF and Windows Forms applications](https://docs.microsoft.com/windows/uwp/xaml-platform/xaml-host-controls).

### XAML Island Host Control (Preview)

>[!NOTE]
>This feature is in preview only.

You can drag a XAML Island Host control directly to the design surface of your Windows Forms or WPF application. Then, you can set that host control to any UWP XAML control that you want. See  [WindowsXAMLHostControl](https://docs.microsoft.com/windows/communitytoolkit/controls/WindowsXAMLHost).

To look at the complete list of UWP XAML controls, see [Controls by function](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/controls-by-function).

### XAML Island Wrapped Controls (Preview)

Add wrapped controls directly to the design surface of your desktop application. Here's what's available today:

| Control |  Description |
|------ |--------------|
| [WebView](https://docs.microsoft.com/windows/communitytoolkit/controls/webview) |   Shows richly formatted HTML content from a remote web server, dynamically generated files, or content files by using the Microsoft Edge rendering engine. |
| [InkCanvas]() | Renders pen input as either an ink stroke (using default settings for color and thickness) or an erase stroke.  |
| [InkToolbar]() | Contains a customizable and extensible collection of buttons that activate ink-related features in an associated InkCanvas. |
| [MediaPlayerElement]() | Used to view and listen to video and audio. |
| [WebViewCompatible]() | Need to find out what this is.  |

We'll update this guide with new controls as they are released.

### XAML Island API (Preview)

>[!NOTE]
>This feature is in preview only.

For C++ win32 apps, use the XAML Island API to incorporate UWP XAML controls into your desktop application UIs.

See [Using the UWP XAML hosting API in a desktop application](https://review.docs.microsoft.com/windows/uwp/xaml-platform/using-the-xaml-hosting-api?branch=mcleans-xamlhosting).

To look at the complete list of UWP XAML controls, see [Controls by function](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/controls-by-function).

<a id="desktop-uwp-controls"/>

## UWP XAML controls optimized for desktop applications

Here's some new UWP XAML controls that you can use to create desktop-optimized experiences with a modern Fluent design.

| Control |  Description |
|------ |--------------|
| [MenuBar](https://review.docs.microsoft.com/windows/uwp/design/controls-and-patterns/menus?branch=jimwalk%2Frs5-menu-bar) | provides a quick and simple way to expose a set of commands for apps that might need more organization or grouping then a CommandBar allows. |
| [DropDownButton](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/buttons#create-a-drop-down-button) | Shows a chevron as a visual indicator that it has an attached flyout that contains more options.  |
| [SplitButton](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/buttons#create-a-split-button) | A [SplitButton](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/buttons#create-a-split-button) has two parts that can be invoked separately. One part behaves like a standard button and invokes an immediate action. The other part invokes a flyout that contains additional options that the user can choose from.|
| [CommandBarFlyout](https://review.docs.microsoft.com/windows/uwp/design/controls-and-patterns/command-bar-flyout?branch=jimwalk%2Frs5-command-bar-flyout) |  Has **PrimaryCommands** and **SecondaryCommands** properties you can use to add commands. You can place commands in either collection, or both. When and how the primary and secondary commands are displayed depends on the display mode. |
| [EditableComboBox](https://review.docs.microsoft.com/windows/uwp/design/controls-and-patterns/combo-box?branch=rs5#make-a-combo-box-editable) | Need description. |
| [DataGridView](https://docs.microsoft.com/windows/communitytoolkit/controls/datagrid) |   Provides a flexible way to display a collection of data in rows and columns.  |

## Windows UI library

The Windows UI library contains new platform controls that haven't yet shipped as part of the Windows platform. It also contains updated versions of existing controls.

Perhaps the best aspect of this library is that it ships controls as NuGet packages. Therefore, you can safely adopt new controls as they are released without having to worry about whether your users are running a compatible version of Windows 10.  That let's you keep your UIs on the cutting edge without having to wait for the rest of the company to catch up on Windows releases and you don't have to include version checks or conditional XAML to hedge against compatibility issues.

See [Windows UI Library (Preview version)](https://docs.microsoft.com/uwp/toolkits/winui/)

## Other UWP Features

After you've added a few file references to your desktop application project, you can use UWP APIs to add modern experiences that light up for Windows 10 users such toast notifications.

![Toast](images/toast.png)

See [Enhance your desktop application for Windows 10](https://docs.microsoft.com/windows/uwp/porting/desktop-to-uwp-enhance)

## Other Interesting technologies

* [.NET Core 3](https://blogs.msdn.microsoft.com/dotnet/2018/05/07/net-core-3-and-support-for-windows-desktop-applications/)
* [Microsoft Graph](https://developer.microsoft.com/graph)
* [Adaptive Cards](https://adaptivecards.io/)
* [High DPI support in Windows Forms](https://docs.microsoft.com/dotnet/framework/winforms/high-dpi-support-in-windows-forms)
