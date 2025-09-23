---
title: Win32 app isolation overview
description: The Win32 app isolation security feature for Windows provides a sandbox environment that can integrated into Win32 apps.
ms.topic: overview
ms.date: 10/01/2024
#customer intent: As a Windows developer, I want to learn about the Win32 app isolation security feature so that I can integrate it into my Win32 apps.
---

# Win32 app isolation overview

The Win32 app isolation security feature for Windows provides a sandbox environment that can be integrated into Win32 apps, providing an additional layer of security. This enhancement requires little to no change to your code.

For the latest updates and enhancements, please refer to the [Release notes](app-isolation-release-notes.md).

If you have a feature request or wish to report a bug, file an issue in our GitHub [repo](https://github.com/microsoft/win32-app-isolation/issues).

> [!IMPORTANT]
> **This feature is in preview:** Some information relates to a prerelease product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.

## Target application types

- Win32
- Desktop Bridge (Centennial)
- Desktop apps [packaged with external location](/windows/apps/desktop/modernize/grant-identity-to-nonpackaged-apps)

## Minimum requirements

The following are the minimum requirements to create an isolated Win32 app:

- Windows 11, version 24H2 (build 26100) or later.
- Development tools for packaging:
  - [Visual Studio](https://visualstudio.microsoft.com/) version 17.10.2 or greater.
- (Optional) [Application Capability Profiler (ACP)](https://github.com/microsoft/win32-app-isolation/releases/tag/v0.1.1) and [Windows Performance Recorder (WPR)](/windows-hardware/test/wpt/windows-performance-recorder) are available, if you need to identify the capabilities to use.

## Creating an isolated Win32 app

These are the steps to consider when creating an isolated Win32 app:

-  Follow the [packaging instructions](app-isolation-packaging-with-vs.md) for Visual Studio.
- If you need to identify the required capabilities:
  - Use the [ACP](app-isolation-capability-profiler.md) tool or the [Supported Capabilities](app-isolation-supported-capabilities.md) section.
  - Repackage the app with the capabilities that were identified.

## Related topics

[Application Capability Profiler](app-isolation-capability-profiler.md)

[Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler Module](app-isolation-reference/Microsoft.Windows.Win32Isolation.ApplicationCapabilityProfiler.md)

[Understanding how packaged desktop apps run on Windows](/windows/msix/desktop/desktop-to-uwp-behind-the-scenes)
