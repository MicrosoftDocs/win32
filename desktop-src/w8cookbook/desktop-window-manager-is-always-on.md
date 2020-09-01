---
title: Desktop Window Manager is always on
description: Desktop Window Manager is always on
ms.assetid: 36E2DD1B-E480-47A9-850B-3057119641C0
ms.topic: article
ms.date: 05/31/2018
---

# Desktop Window Manager is always on

## Platforms

**Clients** – Windows 8  
**Servers** – Windows Server 2012  


## Description

In Windows 8, Desktop Window Manager (DWM) is always ON and cannot be disabled by end users and apps. As in Windows 7, DWM is used to compose the desktop. In addition to experiences enabled in Windows 7, now DWM desktop composition enables desktop composition for all themes, support for Stereoscopic 3D, and management, separation, and protection of the experience with Windows Store apps.

**Desktop composition for all themes**

In Windows Vista and Windows 7, desktop composition is enabled only with the AERO Glass Theme. Hence users of Windows Classic and high contrast themes cannot use experiences enabled by desktop composition such as Windows Flip, automatic scaling for high resolution (DPI) scaling, thumbnail Preview and full screen magnifier. In addition, in these earlier versions of Windows, app developers must write and maintain multiple code paths – one where desktop composition is enabled and another where desktop composition is disabled.

With Windows 8, desktop composition is enabled for all themes. Users of Windows Classic and high contrast themes can use the experiences enabled by desktop composition such as Windows Flip, automatic scaling for high resolution (DPI) scaling, thumbnail previews, and full screen magnifier. In addition, developers don’t need to write and maintain multiple code paths, thereby simplifying development.

**Support for stereoscopic 3D**

DWM desktop composition supports rendering and presentation of windowed and full-screen stereoscopic 3D app content.

**Management, separation and protection of the experience with Windows Store apps**

DWM desktop composition enables separation and protection of desktop app windows from the new Windows Store app windows by managing and separating the desktop app windows from the Windows Store app windows. Since desktop composition is responsible for managing all app windows, disabling desktop composition can result in unexpected behavior. In addition desktop composition is responsible for composing the new Start menu as well as additional window animations that form the core personality of the new Windows operating system.

## Controlling desktop composition

In Windows Vista and Windows 7, desktop composition is disabled in a number of scenarios. In Windows 8, DWM desktop composition is a core operating system component and cannot be disabled. With a few exceptions, desktop composition is always on; it’s started before the user logon and remains active for the duration of a session. This section describes how Windows 8 treats the scenarios in Windows 7 where desktop composition is disabled.

**Server SKU and certain client SKUs**

In Windows 8, all server and client SKUs have desktop composition enabled. This ensures that server admins and users can benefit from the experiences enabled by desktop composition.

**Fundamental requirements for desktop composition**

Windows 8 ensures that graphics adapter and system color depth requirements are met through WDDM driver support and system color depth.

**WDDM driver support**

If a system does not have a WDDM-compliant graphics driver, Windows 8 uses Microsoft Basic Display Adapter as the default adapter. Since DWM always runs on the default adapter, it will choose Microsoft Basic Display Adapter to compose the desktop when a WDDM-compliant graphics driver is not available (whether not installed or disabled) on the system.

Microsoft Basic Display Adapter is a software rasterizer that uses the CPU rather than the GPU to perform all the drawing. Note that the performance of desktop composition on Microsoft Basic Display Adapter (especially animations) may not be as smooth as when running desktop composition on a GPU.

**System color depth**

Desktop Composition cannot run unless the color depth is set to 32 bits per pixel. In Windows 7 the color depth of the system can be changed in these scenarios:

-   An end user uses the Windows Display control panel or a 3rd party control panel to change the system color
-   An end user runs an app that changes the color depth of the system through a public API

Unlike Windows 7, Windows 8 does not support color depth other than 32 bits per pixel. The user can no longer change the color depth of the system by using the control panel.

In addition, app developers cannot use APIs to change the color depth of the system. Windows 8 will detect apps that try to change the color depth of the system to less than 32 bits per pixel, and inform the user that an app compatibility shim must be applied to run the apps. After confirmation from the user, the app compatibility shim is applied and the shim virtualizes the low color mode to the app while keeping the system running at 32 bits per pixel.

**WinSAT**

In Windows 8, desktop composition does not depend on WinSAT scores. Moreover, WinSAT no longer includes DWM assessment.

**App compatibility and user action**

In Windows 8:

-   All of the options for disabling desktop composition that exist in Window 7 are removed
-   Desktop composition is responsible for composing all themes
-   Apps cannot use DwmEnableComposition to disable desktop composition. In order to maintain backward compatibility, a call to this API will return success; however, desktop composition is not disabled
-   The "Disable desktop composition" shim is removed
-   The option to "Disable desktop composition" from the compatibility tab of the Application Properties dialogue box is removed

**An app uses a mirroring driver for remoting**

In Windows 8:

-   Does not support mirror drivers for remoting scenarios; while most of the existing apps that use mirror drivers should continue to work, due to the infrastructural change required to support existing mirror drivers in Windows 8 with DWM ON, some features or apps that use mirror drivers may not work
-   Does support Desktop Duplication APIs for app developers who use mirror drivers for remoting scenarios.
-   Does not support existing Accessibility Mirror Drivers
-   Existing Mirror Drivers must be updated to ensure that they are compatible with Windows 8

**Remote desktop connection**

In Windows 8, desktop composition is always enabled for a remote desktop connection. A client computer connecting to a Windows 8 remote computer will always get desktop composition enabled for the remote desktop session irrespective of the Windows client version. Desktop composition is supported for multiple monitors on the client machine as well as for the remote app session.

In addition, when connecting to a Windows 8 remote computer, these settings in the Remote Desktop Connection client do not take effect:

-   Color depth
-   "Enable composition” checkbox

The color depth of the connection is always set to 32 bits per pixel and desktop composition is always enabled.

 

 




