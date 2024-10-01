---
title: Win32 app isolation overview
description: The Win32 app isolation security feature for Windows provides a sandbox environment that can integrated into Win32 apps.
ms.topic: article
ms.date: 08/26/2024
---

# Win32 app isolation overview

The Win32 app isolation security feature for Windows provides a sandbox environment that can integrated into Win32 apps, providing an additional layer of security. This enhancement requires little to no change to your code.

## Target application types

- Win32
- Desktop Bridge (Centennial)

## Minimum requirements

- Windows insider version >= 25357 (Canary channel only)
- Dev tool to package
  - [Visual Studio](https://visualstudio.microsoft.com/) version 17.10.2 or greater
  - or [Customized MSIX Packaging Tool](https://github.com/microsoft/win32-app-isolation/releases/tag/v0.1.1)
- (optional) [ACP](https://github.com/microsoft/win32-app-isolation/releases/tag/v0.1.1) and [WPR](/windows-hardware/test/wpt/windows-performance-recorder), if need to identify the capabilities to use

## Creating a Win32 app isolation app

- If you are using Visual Studio to build your project
  - Follow the [instructions](app-isolation-packaging-with-vs.md) for Visual Studio
- Or if you have the Win32 installer / MSIX package
  - [Create](app-isolation-msix-packaging.md#packaging-an-isolated-win32-app-with-msix) the MSIX package from the Win32 installer
  - [Turn](app-isolation-msix-packaging.md#convert-an-existing-msix-app-to-run-isolated) the MSIX Package to isolated Win32 app
- If you need to Identify the required capabilities
  - Use [Application Capability Profiler](app-isolation-capability-profiler.md)
  - Repackage the app with the capabilities

## Related topics

[Application Capability Profiler](app-isolation-capability-profiler.md)

[Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler Module](app-isolation-reference/Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler.md)
