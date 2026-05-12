---
title: Supported Capabilities
description: Provides information about the supported capabilities by Win32 app isolation.
ms.topic: concept-article
ms.date: 02/12/2025
keywords: windows, win32, windows app development, app isolation, security, sandbox, capabilities
ms.localizationpriority: medium
# customer-intent: As a Windows developer, I want to learn about the supported capabilities for Win32 app isolation apps.
---

# Supported Capabilities

This page lists all the capabilities in Windows that are supported by Win32 app isolation. Nevertheless, it's necessary to understand that this is a work in progress. As we continue to onboard more apps, we will validate support for additional capabilities. If you find capabilities that don’t work, file a bug in the issues section of Win32 app isolation [repo](https://github.com/microsoft/win32-app-isolation/issues). Currently, there are two sets of capabilities that will be detailed below.

## IsolatedWin32 Capabilities

These capabilities were created specifically for Win32 app isolated apps. They directly add functionalities back to isolated apps:

- `isolatedWin32-print` - Print documents allowing access to the existing Win32 printing infrastructure
- `isolatedWin32-sysTrayIcon` - Display notifications from the system tray (systray)
- `isolatedWin32-shellExtensionContextMenu` - Display COM-based context menu entries
- `isolatedWin32-promptForAccess` - Prompt Users for file access
- `isolatedWin32-accessToPublisherDirectory` - Access to directories that end with the publisher ID

The following capabilities allow minimal access to libraries such as MSVC runtime or other Windows/3rd Party DLLs for applications that don't support prompting:

- `isolatedWin32-dotNetBreadcrumbStore`
- `isolatedWin32-profilesRootMinimal`
- `isolatedWin32-userProfileMinimal`
- `isolatedWin32-volumeRootMinimal`

## UWP Capabilities

Win32 app isolation supports most of the [UWP capabilities](/windows/uwp/packaging/app-capability-declarations). These capabilities might be necessary for a fully operational isolated app's manifest. However, not all of them have been comprehensively tested. Consequently, this section will be updated as we continue to validate support. For more information and a complete description of each capability, refer to the [UWP capabilities](/windows/uwp/packaging/app-capability-declarations) documentation.

- `<DeviceCapability Name="microphone"/>` provides access to the microphone's audio feed, which allows the app to record audio from connected microphones
- `<DeviceCapability Name="webcam"/>` provides access to the video feed of a built-in camera or external webcam, which allows the app to capture photos

## Related content

- [Win32 app isolation overview](app-isolation-overview.md)
