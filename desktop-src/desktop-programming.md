---
Description: Get started learning the basics of building great desktop apps in this section.
ms.assetid: 15690E05-9AF7-41A3-AF7C-8DB7C5FB9BE4
title: Get started
ms.topic: article
ms.date: 05/31/2018
---

# Get started with desktop Windows apps that use the Win32 API

The Win32 API (also called the Windows API) is the original platform for native C/C++ Windows applications that require direct access to Windows and hardware. It provides a first-class development experience without depending on a managed runtime environment like .NET and WinRT (for UWP apps for Windows 10). This makes the Win32 API the platform of choice for applications that need the highest level of performance and direct access to system hardware.

The Win32 API is just one of several app platforms you can use to build desktop Windows apps. For more info about other app platforms, see [Choose your platform](/windows/apps/choose-your-platform).

## Get set up

Follow these instructions and start creating desktop apps for Windows 10 that use the Win32 API.

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

See [what's new](whats-new.md) to learn about new Win32 APIs that have been introduced in Windows 10.

## Get started with Win32 features and technologies

To get started learning about the Win32 APIs for key Windows features and technologies, see the following articles. For a more in-depth index of all features and technologies, see [this article](desktop-app-technologies.md).

* [Desktop User Interface](windows-application-ui-development.md)
* [Desktop environment and shell](user-interface.md)
* [Accessibility](accessibility.md)
* [Audio and video technologies](audio-and-video.md) 
* [Graphics and gaming technologies](graphics-and-multimedia.md)
* [System services](system-services.md)
* [Networking and Internet](networking.md)
* [Data access and storage](data-access-and-storage.md)
* [Security and identity](security.md)
* [Diagnostics](diagnostics.md)
* [Debugging and error handling](debugging-and-error-handling.md)
* [Application installation and servicing](application-installing-and-servicing.md)
* [MSIX packaging and deployment](//docs.microsoft.com/windows/msix)

## Related topics

* [Develop desktop apps](/windows/apps/desktop-apps)
* [Windows API reference](api)
* [Windows API index](apiindex/api-index-portal)
* [Windows Runtime C++ reference](winrt/reference)