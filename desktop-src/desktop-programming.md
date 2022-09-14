---
description: Get started learning the basics of building great desktop apps in this section.
ms.assetid: 15690E05-9AF7-41A3-AF7C-8DB7C5FB9BE4
title: Get started
ms.topic: reference
ms.date: 05/31/2018
---

# Get started with desktop Windows apps that use the Win32 API

The Win32 API (also called the Windows API) is the original platform for native C/C++ Windows applications that require direct access to Windows and hardware. It provides a first-class development experience without depending on a managed runtime environment like .NET and WinRT (for UWP apps for Windows 10). This makes the Win32 API the platform of choice for applications that need the highest level of performance and direct access to system hardware.

> [!NOTE]
> This documentation covers how to create desktop Windows apps with the Win32 API. The Win32 API is one of several app platforms you can use to build desktop Windows apps. For more info about other app platforms, see [Choose your platform](/windows/apps/desktop/choose-your-platform).

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

You can also browse the [desktop app samples](https://github.com/Microsoft/Windows-classic-samples).

## Modernize your desktop apps for Windows 10

If you have an existing desktop Win32 app, there are many features in the Universal Windows Platform (UWP) that you can use to deliver the best possible experience on Windows 10. For example, starting in Windows 10, version 1903, you can host UWP XAML controls in your desktop Win32 app using a feature called XAML Islands.

Most of these UWP features are available as modular components that you can adopt in your desktop app at your own pace without having to rewrite your entire application. You can enhance your existing desktop app by choosing which parts of Windows 10 and UWP to adopt.

For more information, see [Modernize your desktop apps](/windows/apps/desktop/modernize).

## C++/WinRT

Optionally, you can configure your development computer to use [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/). C++/WinRT is an entirely standard modern C++17 language projection enables you to easily consume Windows Runtime APIs Windows Runtime (WinRT) APIs from your C++ Win32 desktop application. C++/WinRT is implemented as a header-file-based library.

To configure your project for C++/WinRT:

* For new projects, you can install the [C++/WinRT Visual Studio Extension (VSIX)](https://marketplace.visualstudio.com/items?itemName=CppWinRTTeam.cppwinrt101804264) and use one of the C++/WinRT project templates included in that extension.
* For existing Windows desktop application projects, you can install the [Microsoft.Windows.CppWinRT](https://www.nuget.org/packages/Microsoft.Windows.CppWinRT/) NuGet package in the project.

For more details about these options, see [this article](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt#visual-studio-support-for-cwinrt-xaml-the-vsix-extension-and-the-nuget-package).

## What's new for Win32 APIs in Windows 10

To learn about new Win32 APIs that have been introduced in Windows 10, see [what's new](whats-new.md).

## Get started with Win32 features and technologies

Win32 APIs exist for many features and technologies in Windows 10, including core user interface and windowing APIs, audio and graphics, and networking. For guidance and code samples about using these APIs, [see our features and technologies index](desktop-app-technologies.md).

## Related topics

* [Develop desktop apps](/windows/apps/desktop)
* [Windows API reference](/windows/desktop/api/)
* [Windows API index](/windows/desktop/apiindex/api-index-portal)
* [Windows Runtime C++ reference](/windows/desktop/winrt/reference)
