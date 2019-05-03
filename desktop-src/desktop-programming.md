---
Description: Get started learning the basics of building great desktop apps in this section.
ms.assetid: 15690E05-9AF7-41A3-AF7C-8DB7C5FB9BE4
title: Get started
ms.topic: article
ms.date: 05/31/2018
---

# Get started with Win32 desktop Windows apps

The Win32 API (also called the Windows API) is the original platform for native C/C++ Windows applications that require direct access to Windows and hardware. It provides a first-class development experience without depending on a managed runtime environment like .NET and WinRT (for UWP apps for Windows 10). This makes the Win32 API the platform of choice for applications that need the highest level of performance and direct access to system hardware.

The Win32 API is just one of several app platforms you can use to build desktop Windows apps. For more info about other app platforms, see [Choose your platform](/windows/apps/choose-your-platform).

## Get set up

Follow these instructions and start creating desktop Win32 apps for Windows 10.

1. Download or update Visual Studio 2019. If you don't already have Visual Studio 2019, you can install the free Microsoft Visual Studio Community 2019. When you install Visual Studio, make sure to select the **Desktop development with C++** option. For download links, see our [Downloads](https://developer.microsoft.com/windows/downloads) page.

    > [!NOTE]
    > When you install Visual Studio, you can optionally select the **.NET desktop development** and **Universal Windows Platform development** options for access to other project types and app platforms for building desktop Windows apps.

2. If you want to build your desktop app into an [MSIX package](/windows/msix/desktop/desktop-to-uwp-root) and test or debug the packaged app on your development computer, you'll need to [enable Developer Mode on your computer](/windows/uwp/get-started/enable-your-device-for-development).

> [!NOTE]
> For scripts you can use to set up your development computer and install other features or packages, check out [this GitHub project](https://github.com/Microsoft/windows-dev-box-setup-scripts).

## Learn how to create desktop apps using the Win32 API

If you're new to building desktop apps using the Win32 API, the following tutorials and articles will help get you started.

| Topic        | Description      |
|---------------|-----------------|
| [Create your first C++ Win32 app](LearnWin32/learn-to-program-for-windows.md)    | This tutorial teaches you how to write a Windows program in C++ using Win32 and COM APIs.  |
| [Create your first app using DirectX](direct3dgetstarted/building-your-first-directx-app.md) | This basic tutorial will get you started with DirectX app development.            |
| [Programming Guide for 64-bit Windows](WinProg64/programming-guide-for-64-bit-windows.md)    | Describes programming for 64-bit versions of the Windows operating system. |
| [Using the Windows Headers](WinProg/using-the-windows-headers.md)     | Provides an overview of some of the conventions used in the Windows header files. |

You can also try out the [desktop app samples](https://github.com/Microsoft/Windows-classic-samples).

## Modernize your desktop apps for Windows 10

If you have an existing desktop Win32 app, there are many features in the Universal Windows Platform (UWP) that you can use to deliver the best possible experience on Windows 10. For example, starting in Windows 10, version 1903, you can host UWP XAML controls in your desktop Win32 app (this feature is also called XAML Islands).

Most of these UWP features are available as modular components that you can adopt in your desktop app at your own pace without having to rewrite your entire application. You can enhance your existing desktop app by choosing which parts of Windows 10 and UWP to adopt.

For more information, see [Modernize your desktop apps](/windows/apps/modernize-desktop).

## What's new in Windows 10

Learn about new Win32 APIs that have been introduced in Windows 10.

* [What's new](whats-new.md)

## Get started with Win32 features and technologies

Learn how to use a specific Windows feature or technology in your desktop Win32 apps.

:::row:::
    :::column:::
        ### User Interface programming
        ![User Interface programming](/media/illustrations/bcs-partner-advanced-management-add-user-1.svg?branch=master)
        * [Desktop User Interface](windows-application-ui-development.md)
        * [Desktop environment and shell](user-interface.md)
        * [Windows and messages](winmsg/windowing.md)
        * [Menus and other resources](menurc/resources.md)
        * [High DPI](hidpi/high-dpi-desktop-application-development-on-windows.md)
        * [Windows controls](controls/window-controls.md)
    :::column-end:::
    :::column:::
        ### Fundamentals and hardware
        ![Fundamentals and hardware](/media/illustrations/biztalk-get-started-get-started.svg?branch=master)
        * [System services](system-services.md)
        * [Networking and internet](networking.md)
        * [Data access and storage](data-access-and-storage.md)
        * [Documents and printing](printdocs/documents-and-printing.md)
        * [Security and identity](security.md)
    :::column-end:::
    :::column:::
        ### Audio and video
        ![Audio and video](/media/illustrations/dynamics-resource-library.svg?branch=master)
        * [Audio and video technologies](audio-and-video.md)
        * [Core Audio APIs](coreaudio/core-audio-apis-in-windows-vista.md)
        * [DirectShow](directshow/directshow.md)
        * [Microsoft Media Foundation](medfound/microsoft-media-foundation-sdk.md)
        * [Windows Multimedia](multimedia/windows-multimedia-start-page.md)
    :::column-end:::
:::row-end:::
:::row:::
    :::column:::
        ### Graphics, DirectX, and gaming
        ![Graphics, DirectX, and gaming](/media/illustrations/virtualization-containers-samples.svg?branch=master)
        * [Graphics and gaming technologies](graphics-and-multimedia.md)
        * [Get started with DirectX](getting-started-with-directx-graphics.md)
        * [Direct2D](direct2d/direct2d-portal.md)
        * [Direct3D](direct3d.md)
        * [XAudio2 APIs](xaudio2/xaudio2-apis-portal.md)
        * [Windows GDI](gdi/windows-gdi.md)
        * [GDI+](gdiplus/-gdiplus-gdi-start.md)
    :::column-end:::
    :::column:::
        ### Diagnostics and testing
        ![Diagnostics and testing](/media/illustrations/team-services-dev-ops-test.svg?branch=master)
        * [Diagnostics](diagnostics.md)
        * [Debugging and error handling](debugging-and-error-handling.md)
        * [Performance counters](perfctrs/performance-counters-portal.md)
        * [Windows error reporting](wer/windows-error-reporting.md)
        * [Windows events](events/windows-events.md)
        * [Debugging tools for Windows](//docs.microsoft.com/windows-hardware/drivers/debugger/index)
    :::column-end:::
    :::column:::
        ### Packaging and installation
        ![Packaging and installation](/media/illustrations/biztalk-host-integration-install-configure.svg?branch=master)
        * [MSIX](//docs.microsoft.com/windows/msix)
        * [Windows Installer](msi/windows-installer-portal.md)
        * [Windows Desktop Application Program](appxpkg/windows-desktop-application-program.md)
        * [Windows containers](//docs.microsoft.com/virtualization/windowscontainers/about/)
    :::column-end:::
:::row-end:::

## Related topics

* [Develop desktop apps](/windows/apps/desktop-apps)
* [Windows API reference](api)
* [Windows API index](apiindex/api-index-portal)
* [Windows Runtime C++ reference](winrt/reference)