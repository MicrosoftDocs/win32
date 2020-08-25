---
title: Using the High-Level Monitor Configuration Functions
description: Using the High-Level Monitor Configuration Functions
ms.assetid: 23e5d45d-a924-4119-b21d-b24764b53a94
keywords:
- monitor,functions
- monitor,high-level configuration functions
- monitor,enumerating physical monitors
- monitor,continuous settings
- monitor configuration,high-level configuration functions
- monitor configuration,functions
- monitor configuration,enumerating physical monitors
- monitor configuration,continuous settings
- enumerating physical monitors
- high-level configuration functions
- continuous monitor settings
ms.topic: article
ms.date: 05/31/2018
---

# Using the High-Level Monitor Configuration Functions

## Enumerating Physical Monitors

There are several functions that enumerate display devices, including [**EnumDisplayMonitors**](/windows/desktop/api/winuser/nf-winuser-enumdisplaymonitors) and [**MonitorFromWindow**](/windows/desktop/api/winuser/nf-winuser-monitorfromwindow). These functions are documented in the Windows GDI documentation, under the topic [Multiple Display Monitors](/windows/desktop/gdi/multiple-display-monitors). These functions return **HMONITOR** handles. Despite the name, however, an **HMONITOR** handle can be associated with more than one physical monitor. To configure the settings on a monitor, the application must get a unique handle to the physical monitor by calling [**GetPhysicalMonitorsFromHMONITOR**](/windows/desktop/api/PhysicalMonitorEnumerationAPI/nf-physicalmonitorenumerationapi-getphysicalmonitorsfromhmonitor).

If your application uses Direct3D, you can get a monitor handle from a Direct3D device by calling [**GetPhysicalMonitorsFromIDirect3DDevice9**](/windows/desktop/api/PhysicalMonitorEnumerationAPI/nf-physicalmonitorenumerationapi-getphysicalmonitorsfromidirect3ddevice9).

## Supported Functions

A monitor might not support all of the monitor configuration functions. To find out which functions a monitor supports, call [**GetMonitorCapabilities**](/windows/desktop/api/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-getmonitorcapabilities).

## Continuous Monitor Settings

A *continuous* monitor setting is one that can range between some minimum and maximum value. Most of the high-level monitor configuration functions control continuous monitor settings. For example, brightness and contrast are continuous settings.

Continuous monitor settings do not have defined real-world units. The units are arbitrary and can vary from one manufacturer to another. If two monitors have the same brightness value, for example, one monitor might look much brighter than another. Typically, an application will present slider controls or up-down controls to the user. The user can then adjust the settings to give the best subjective quality.

## Changes in Monitor State

A monitor can change states for various reasons, including:

-   The user changes the settings with the monitor's front-panel controls.
-   The user changes the monitor's screen resolution, refresh rate, or bit depth.
-   The application uses the low-level monitor functions to change a setting that is not accessible from the high-level functions.
-   The application calls [**RestoreMonitorFactoryColorDefaults**](/windows/desktop/api/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-restoremonitorfactorycolordefaults) or [**RestoreMonitorFactoryDefaults**](/windows/desktop/api/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-restoremonitorfactorydefaults).

All of these events can change monitor settings. They can also change the minimum and maximum value of a setting.

## Dependencies Among Monitor Settings

Changing the color temperature can change the current drive and gain settings, and the reverse is also true. Those are the only dependencies among the high-level monitor configuration functions. Other settings might be accessible only through the low-level monitor functions. There might be dependencies between those settings and the high-level settings. These dependencies are vendor-specific. An application can handle this problem in several ways:

-   Use only high-level functions.
-   After calling a low-level function, get the current value of every monitor setting. Unfortunately, this approach can be slow, because getting each setting takes about 40 milliseconds.
-   Use low-level functions only with specific monitor models whose behavior you understand.

## Disabled Monitor Settings

An application cannot disable any monitor settings by calling the high-level monitor functions. However, an application might accidentally disable a setting if it uses the low-level functions to change a monitor setting that is not supported by the high-level functions. Also, a user might disable a setting by using the front-panel control. These behaviors are vendor-specific.

If a monitor setting becomes disabled, any function that sets or retrieves that setting will fail and set the last-error code to ERROR\_DISABLED\_MONITOR\_SETTING. When this occurs, the application can do one of the following:

-   Display an error message and suggest to the user that he or she try adjusting the setting by using the front-panel control.
-   Call the [**RestoreMonitorFactoryDefaults**](/windows/desktop/api/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-restoremonitorfactorydefaults) function. If a monitor has the MC\_RESTORE\_FACTORY\_DEFAULTS\_ENABLES\_MONITOR\_SETTINGS capabilities flag, this function enables all of the monitor settings that are supported by the high-level monitor functions. Unfortunately, the function also resets the monitor settings to their factory default.

## Related topics

<dl> <dt>

[Using Monitor Configuration](using-monitor-configuration.md)
</dt> </dl>

 

 