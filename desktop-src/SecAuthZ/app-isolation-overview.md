---
title: Win32 app isolation overview
description: The Win32 app isolation security feature for Windows provides a sandbox environment that can integrated into Win32 apps.
ms.topic: overview
ms.date: 10/01/2024
#customer intent: As a Windows developer, I want to learn about the Win32 app isolation security feature so that I can integrate it into my Win32 apps.
---

# Win32 app isolation overview

The Win32 app isolation security feature for Windows provides a sandbox environment that can integrated into Win32 apps, providing an additional layer of security. This enhancement requires little to no change to your code.

> [!IMPORTANT]
> **This feature is in preview:** Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

## Target application types

- Win32
- Desktop Bridge (Centennial)

## Minimum requirements

The following are the minimum requirements to create a Win32 app isolation app:

- Windows 11, version 24H2 (build 26100) or later.
- Development tools for packaging:
  - [Visual Studio](https://visualstudio.microsoft.com/) version 17.10.2 or greater.
  - Or use the [Customized MSIX Packaging Tool](https://github.com/microsoft/win32-app-isolation/releases/tag/v0.1.1) on GitHub.
- (Optional) [Application Capability Profiler (ACP)](https://github.com/microsoft/win32-app-isolation/releases/tag/v0.1.1) and [Windows Performance Recorder (WPR)](/windows-hardware/test/wpt/windows-performance-recorder) are available, if you need to identify the capabilities to use.

## Creating a Win32 app isolation app

These are the steps to consider when creating a Win32 app isolation app:

- If you are using Visual Studio to build your project:
  - Follow the [packaging instructions](app-isolation-packaging-with-vs.md) for Visual Studio.
- Or if you have the Win32 installer / MSIX package:
  - [Create](app-isolation-msix-packaging.md#packaging-an-isolated-win32-app-with-msix) an MSIX package from a Win32 installer.
  - [Turn](app-isolation-msix-packaging.md#convert-an-existing-msix-app-to-run-isolated) an MSIX Package into an isolated Win32 app.
- If you need to identify the required capabilities:
  - Use the [ACP](app-isolation-capability-profiler.md) tool.
  - Repackage the app with the capabilities that were identified.

## Related topics

[Application Capability Profiler](app-isolation-capability-profiler.md)

[Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler Module](app-isolation-reference/Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler.md)

[Understanding how packaged desktop apps run on Windows](/windows/msix/desktop/desktop-to-uwp-behind-the-scenes)
