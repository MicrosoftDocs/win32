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

<!--

# Modernize your desktop applications

The Windows 10 October 2018 Update introduces many new features that enable you to deliver a modern experience in your desktop applications. This includes:

* **MSIX packages**. This is a modern application package format that is available for any desktop application.
* **XAML Islands**. Certain UWP controls are now available as a set of building blocks that you can adopt in WPF, Windows Forms, and C/C++ Win32 applications.
* UWP controls that are optimized for desktop applications.

-- categorize everything by: features available to any desktop application, features for .NET and Win32, and features for UWP targeted at desktop

-->

The UWP platform is being made available as a set of "building blocks" that you can adopt in your desktop applications without having to rewrite your application for UWP. There's no need to learn a whole new stack to modernize. You can enhance existing investments in-place by choosing which parts of the platform to adopt.

This guide describes UWP platform features that you can use in your desktop applications right now.

<!-- categorize everything by: features available to any desktop application, features for .NET and Win32, and features for UWP targeted at desktop
-->

## MSIX packages

MSIX is a modern Windows app package format that provides a universal packaging experience for all Windows applications, including UWP, WPF, Windows Forms and Win32 applications. MSIX brings together the best aspects of MSI, .appx, App-V and ClickOnce installation technologies and is built to be safe, secure, and reliable.

Packaging your desktop Windows applications in MSIX packages gets you access to a robust installation and updating experience, a managed security model with a flexible capability system, support for the Microsoft Store, enterprise management, and many custom distribution models.

To learn more, see the [MSIX documentation](https://docs.microsoft.com/windows/msix).

## UWP controls in desktop applications (developer preview)

Starting with the Windows 10 October 2018 Update, you can add [UWP XAML controls](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/controls-by-function) to the user interfaces of non-UWP desktop applications. This means that you can use the latest UWP features such as the [Fluent Design System](https://docs.microsoft.com/windows/uwp/design/fluent-design-system/index) and [Windows Ink](https://docs.microsoft.com/windows/uwp/design/input/pen-and-stylus-interactions) in your existing WPF, Windows Forms, and C++ Win32 applications. This developer scenario is sometimes called *XAML islands*.

> [!NOTE]
> The APIs and controls that enable XAML islands are currently available as a developer preview. Although we encourage you to try them out in your own prototype code now, we do not recommend that you use them in production code at this time. These APIs and controls will continue to mature and stabilize in future Windows releases. Microsoft makes no warranties, express or implied, with respect to the information provided here.

We provide several ways to use XAML islands in your desktop applications, depending on the technology or framework you are using. For complete details, see [UWP controls in desktop applications](https://docs.microsoft.com/windows/uwp/xaml-platform/xaml-host-controls)

### Wrapped controls (WPF and Windows Forms only)

WPF and Windows Forms applications can use a selection of wrapped UWP controls in the [Windows Community Toolkit](https://docs.microsoft.com/windows/uwpcommunitytoolkit/). You can add these controls directly to the design surface of your WPF or Windows Forms project and then use like any other WPF or Windows Forms control in your designer. We refer to these controls as *wrapped controls* because they wrap the interface and functionality of a specific UWP control.

For more information, see [Wrapped controls](https://docs.microsoft.com/windows/uwp/xaml-platform/xaml-host-controls#wrapped-controls).

### Host controls (WPF and Windows Forms only)

For scenarios beyond those covered by the available wrapped controls, WPF and Windows Forms applications can also use the [WindowsXamlHost](https://docs.microsoft.com/windows/communitytoolkit/controls/wpf-winforms/windowsxamlhost) control in the [Windows Community Toolkit](https://docs.microsoft.com/windows/uwpcommunitytoolkit/). This control can host any UWP control that derives from [**Windows.UI.Xaml.UIElement**](https://docs.microsoft.com/uwp/api/windows.ui.xaml.uielement), including any [UWP controls](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/controls-by-function) provided by the Windows SDK as well as custom user controls.

### UWP XAML hosting API

If you have a C++ Win32 application, you can use the *UWP XAML hosting API* to host any UWP control that derives from [**Windows.UI.Xaml.UIElement**](https://docs.microsoft.com/uwp/api/windows.ui.xaml.uielement) in any UI element in your application that has an associated window handle (HWND). For more information about using this API, see [Using the XAML hosting API in a desktop application](https://docs.microsoft.com/en-us/windows/uwp/xaml-platform/using-the-xaml-hosting-api).

> [!NOTE]
> C++ Win32 desktop applications must use the UWP XAML hosting API to host UWP controls. Wrapped controls and host controls are not available for these types of applications. For WPF and Windows Forms applications, we recommend that you use the wrapped controls and host controls in the Windows Community Toolkit instead of the UWP XAML hosting API. These controls use the UWP XAML hosting API internally and provide a simpler development experience. However, you can use the UWP XAML hosting API directly in WPF and Windows Forms applications if you choose.

<a id="desktop-uwp-controls"/>

## UWP controls optimized for desktop applications

Here's some new UWP controls that you can use to create desktop-optimized experiences with the [Fluent Design System](https://docs.microsoft.com/windows/uwp/design/fluent-design-system/index).

| Control |  Description |
|------ |--------------|
| [MenuBar](https://docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/menus#create-a-menu-bar) | Provides a quick and simple way to expose a set of commands for apps that might need more organization or grouping then a **CommandBar** allows. |
| [DropDownButton](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/buttons#create-a-drop-down-button) | Shows a chevron as a visual indicator that it has an attached flyout that contains more options.  |
| [SplitButton](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/buttons#create-a-split-button) | Provides a button has two parts that can be invoked separately. One part behaves like a standard button and invokes an immediate action. The other part invokes a flyout that contains additional options that the user can choose from.|
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
