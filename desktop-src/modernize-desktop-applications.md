---
Description: Add modern XAML user interfaces, create MSIX packages, and incorporate other modern components into your desktop application in an "alacart" fashion.
title: Desktop guide to the modern platform
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 09/11/2018
---

# Modernize Your Desktop Applications for Windows 10

Windows 10 and the Universal Windows Platform (UWP) offer many features you can use to deliver a modern experience in your desktop applications. Most of these features are available as modular components that you can adopt in your desktop applications at your own pace without having to rewrite your application for a different platform. You can enhance your existing desktop applications by choosing which parts of Windows 10 and UWP to adopt.

This article describes the Windows 10 and UWP features that you can use in your desktop applications today.

## MSIX packages

MSIX is a modern Windows app package format that provides a universal packaging experience for all Windows applications, including UWP, WPF, Windows Forms and Win32 applications. MSIX brings together the best aspects of MSI, .appx, App-V and ClickOnce installation technologies and is built to be safe, secure, and reliable.

Packaging your desktop Windows applications in MSIX packages gets you access to a robust installation and updating experience, a managed security model with a flexible capability system, support for the Microsoft Store, enterprise management, and many custom distribution models.

To learn more, see the [MSIX documentation](https://docs.microsoft.com/windows/msix).

## Integrate Windows 10 experiences into your desktop application with UWP APIs

You can call some UWP APIs directly in your WPF, Windows Forms, or C++ Win32 desktop application to integrate modern experiences that light up for Windows 10 users. For example, you can call UWP APIs to add toast notifications to your desktop application.

For more information, see [Enhance your desktop application for Windows 10](https://docs.microsoft.com/windows/uwp/porting/desktop-to-uwp-enhance).

## Extend your desktop application with UWP XAML UI components

You can introduce modern UI elements into your WPF, Windows Forms, or C++ Win32 application by adding UWP XAML UI components. There are several ways to do this.

### Add a UWP project to your desktop solution

You can add UWP XAML UI components to your desktop application by adding a UWP project to your solution and launching that component from your desktop application. This is a good option if you want the UWP XAML UI to be compartmentalized from the other UI in your desktop application (for example, if all of the UWP XAML UI is contained in a window that is opened by your application).

For more information, see [Extend your desktop application with modern UWP components](https://docs.microsoft.com/windows/uwp/porting/desktop-to-uwp-extend).

### Host UWP controls in desktop applications (developer preview)

Starting with the Windows 10 October 2018 Update, you can add [UWP XAML controls](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/controls-by-function) directly to any UI element in a WPF, Windows Forms, or C++ Win32 application that is associated with a window handle (HWND). This means that you can fully integrate the latest UWP features such as [Windows Ink](https://docs.microsoft.com/windows/uwp/design/input/pen-and-stylus-interactions) and controls that support the [Fluent Design System](https://docs.microsoft.com/windows/uwp/design/fluent-design-system/index) into windows and other display surfaces in your desktop applications. This developer scenario is sometimes called *XAML islands*.

> [!NOTE]
> The APIs and controls that enable XAML islands are currently available as a developer preview. Although we encourage you to try them out in your own prototype code now, we do not recommend that you use them in production code at this time. These APIs and controls will continue to mature and stabilize in future Windows releases. Microsoft makes no warranties, express or implied, with respect to the information provided here.

We provide several ways to use XAML islands in your desktop applications, depending on the technology or framework you are using. For complete details, see [UWP controls in desktop applications](https://docs.microsoft.com/windows/uwp/xaml-platform/xaml-host-controls)

#### Wrapped controls (WPF and Windows Forms only)

WPF and Windows Forms applications can use a selection of wrapped UWP controls in the [Windows Community Toolkit](https://docs.microsoft.com/windows/uwpcommunitytoolkit/). You can add these controls directly to the design surface of your WPF or Windows Forms project and then use like any other WPF or Windows Forms control in your designer. We refer to these controls as *wrapped controls* because they wrap the interface and functionality of a specific UWP control.

For more information, see [Wrapped controls](https://docs.microsoft.com/windows/uwp/xaml-platform/xaml-host-controls#wrapped-controls).

#### Host controls (WPF and Windows Forms only)

For scenarios beyond those covered by the available wrapped controls, WPF and Windows Forms applications can also use the [WindowsXamlHost](https://docs.microsoft.com/windows/communitytoolkit/controls/wpf-winforms/windowsxamlhost) control in the [Windows Community Toolkit](https://docs.microsoft.com/windows/uwpcommunitytoolkit/). This control can host any UWP control that derives from [**Windows.UI.Xaml.UIElement**](https://docs.microsoft.com/uwp/api/windows.ui.xaml.uielement), including any [UWP controls](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/controls-by-function) provided by the Windows SDK as well as custom user controls.

For more information, see [Host controls](https://docs.microsoft.com/windows/uwp/xaml-platform/xaml-host-controls#host-controls).

#### UWP XAML hosting API

If you have a C++ Win32 application, you can use the *UWP XAML hosting API* to host any UWP control that derives from [**Windows.UI.Xaml.UIElement**](https://docs.microsoft.com/uwp/api/windows.ui.xaml.uielement) in any UI element in your application that has an associated window handle (HWND).

For more information, see [Using the XAML hosting API in a desktop application](https://docs.microsoft.com/en-us/windows/uwp/xaml-platform/using-the-xaml-hosting-api).

<a id="desktop-uwp-controls"/>

## UWP controls optimized for desktop applications

Here's some new and updated UWP controls that you can use to create desktop-optimized experiences with the [Fluent Design System](https://docs.microsoft.com/windows/uwp/design/fluent-design-system/index).

| Control |  Description |
|------ |--------------|
| [MenuBar](https://docs.microsoft.com/en-us/windows/uwp/design/controls-and-patterns/menus#create-a-menu-bar) | Provides a quick and simple way to expose a set of commands for apps that might need more organization or grouping then a **CommandBar** allows. |
| [DropDownButton](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/buttons#create-a-drop-down-button) | Shows a chevron as a visual indicator that it has an attached flyout that contains more options.  |
| [SplitButton](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/buttons#create-a-split-button) | Provides a button has two parts that can be invoked separately. One part behaves like a standard button and invokes an immediate action. The other part invokes a flyout that contains additional options that the user can choose from.|
| [ToggleSplitButton](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/buttons#create-a-toggle-split-button) | Provides a button has two parts that can be invoked separately. One part behaves like a toggle button that can be on or off. The other part invokes a flyout that contains additional options that the user can choose from. |
| [CommandBarFlyout](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/command-bar-flyout) |  Lets you show common user tasks in the context of an item on your UI canvas. |
| [ComboBox](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/combo-box#make-a-combo-box-editable) | You can now make a combo box editable so the user can enter values that aren't listed in the control.  |
| [TreeView](https://docs.microsoft.com/windows/uwp/design/controls-and-patterns/tree-view) | You can now configure a tree view to enable data binding, item templates, and drag and drop.  |
| [DataGridView](https://docs.microsoft.com/windows/communitytoolkit/controls/datagrid) |   Provides a flexible way to display a collection of data in rows and columns. This control is available in the [Windows Community Toolkit](https://docs.microsoft.com/windows/uwpcommunitytoolkit/).  |

## Windows UI Library

The Windows UI Library is a set of NuGet packages that provide new controls and other user interface elements for UWP apps. Windows UI Library APIs work on earlier versions of Windows 10, so your app works even if users aren't running the latest version of Windows 10. This lets you adopt new controls as they are released in the Windows UI Library without having to worry about including version checks or conditional XAML.

See [Windows UI Library (Preview version)](https://docs.microsoft.com/uwp/toolkits/winui/)


## Other current and future technologies for desktop applications

* [.NET Core 3](https://blogs.msdn.microsoft.com/dotnet/2018/05/07/net-core-3-and-support-for-windows-desktop-applications/)
* [Microsoft Graph](https://developer.microsoft.com/graph)
* [Adaptive Cards](https://adaptivecards.io/)
* [High DPI support in Windows Forms](https://docs.microsoft.com/dotnet/framework/winforms/high-dpi-support-in-windows-forms)
