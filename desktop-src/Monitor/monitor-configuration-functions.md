---
title: Monitor Configuration Functions
description: Monitor Configuration Functions
ms.assetid: 'e9a00792-f471-47a4-93d7-25400e27f13f'
keywords: ["monitor,functions", "monitor,high-level functions", "monitor,low-level functions", "monitor,enumeration functions", "high-level functions", "low-level functions", "enumeration functions", "monitor configuration,functions", "monitor configuration,high-level functions", "monitor configuration,low-level functions", "monitor configuration,enumeration functions"]
---

# Monitor Configuration Functions

The following functions are used to get information from a monitor and to change a monitor's settings. Monitor configuration functions are categorized into high-level functions, low-level functions, and enumeration functions. For more information, see [Using Monitor Configuration](using-monitor-configuration.md).

## High-Level Functions



| Function                                                                         | Description                                                                          |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**DegaussMonitor**](degaussmonitor.md)                                         | Degausses a monitor.                                                                 |
| [**GetMonitorBrightness**](getmonitorbrightness.md)                             | Retrieves a monitor's minimum, maximum, and current brightness settings.             |
| [**GetMonitorCapabilities**](getmonitorcapabilities.md)                         | Retrieves the configuration capabilities of a monitor.                               |
| [**GetMonitorColorTemperature**](getmonitorcolortemperature.md)                 | Retrieves a monitor's current color temperature.                                     |
| [**GetMonitorContrast**](getmonitorcontrast.md)                                 | Retrieves a monitor's minimum, maximum, and current contrast settings.               |
| [**GetMonitorDisplayAreaPosition**](getmonitordisplayareaposition.md)           | Retrieves a monitor's minimum, maximum, and current horizontal or vertical position. |
| [**GetMonitorDisplayAreaSize**](getmonitordisplayareasize.md)                   | Retrieves a monitor's minimum, maximum, and current width or height.                 |
| [**GetMonitorRedGreenOrBlueDrive**](getmonitorredgreenorbluedrive.md)           | Retrieves a monitor's red, green, or blue drive value.                               |
| [**GetMonitorRedGreenOrBlueGain**](getmonitorredgreenorbluegain.md)             | Retrieves a monitor's red, green, or blue gain value.                                |
| [**GetMonitorTechnologyType**](getmonitortechnologytype.md)                     | Retrieves the type of technology used by a monitor.                                  |
| [**RestoreMonitorFactoryColorDefaults**](restoremonitorfactorycolordefaults.md) | Restores a monitor's color settings to their factory defaults.                       |
| [**RestoreMonitorFactoryDefaults**](restoremonitorfactorydefaults.md)           | Restores a monitor's settings to their factory defaults.                             |
| [**SaveCurrentMonitorSettings**](savecurrentmonitorsettings.md)                 | Saves the current monitor settings to the display's nonvolatile storage.             |
| [**SetMonitorBrightness**](setmonitorbrightness.md)                             | Sets a monitor's brightness value.                                                   |
| [**SetMonitorColorTemperature**](setmonitorcolortemperature.md)                 | Sets a monitor's color temperature.                                                  |
| [**SetMonitorContrast**](setmonitorcontrast.md)                                 | Sets a monitor's contrast value.                                                     |
| [**SetMonitorDisplayAreaPosition**](setmonitordisplayareaposition.md)           | Sets the horizontal or vertical position of a monitor's display area.                |
| [**SetMonitorDisplayAreaSize**](setmonitordisplayareasize.md)                   | Sets the width or height of a monitor's display area.                                |
| [**SetMonitorRedGreenOrBlueDrive**](setmonitorredgreenorbluedrive.md)           | Sets a monitor's red, green, or blue drive value.                                    |
| [**SetMonitorRedGreenOrBlueGain**](setmonitorredgreenorbluegain.md)             | Sets a monitor's red, green, or blue gain value.                                     |



 

## Low-Level Functions



| Function                                                                                   | Description                                                                                                    |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**CapabilitiesRequestAndCapabilitiesReply**](capabilitiesrequestandcapabilitiesreply.md) | Retrieves a string describing a monitor's capabilities.                                                        |
| [**GetCapabilitiesStringLength**](getcapabilitiesstringlength.md)                         | Retrieves the length of a monitor's capabilities string.                                                       |
| [**GetTimingReport**](gettimingreport.md)                                                 | Retrieves a monitor's horizontal and vertical synchronization frequencies.                                     |
| [**GetVCPFeatureAndVCPFeatureReply**](getvcpfeatureandvcpfeaturereply.md)                 | Retrieves the current value, maximum value, and code type of a Virtual Control Panel (VCP) code for a monitor. |
| [**SaveCurrentSettings**](savecurrentsettings.md)                                         | Saves the current monitor settings to the display's nonvolatile storage.                                       |
| [**SetVCPFeature**](setvcpfeature.md)                                                     | Sets the value of a Virtual Control Panel (VCP) code for a monitor.                                            |



 

## Enumeration Functions



| Function                                                                                                   | Description                                                                               |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**DestroyPhysicalMonitor**](destroyphysicalmonitor.md)                                                   | Closes a handle to a physical monitor.                                                    |
| [**DestroyPhysicalMonitors**](destroyphysicalmonitors.md)                                                 | Closes an array of physical monitor handles.                                              |
| [**GetNumberOfPhysicalMonitorsFromHMONITOR**](getnumberofphysicalmonitorsfromhmonitor.md)                 | Retrieves the number of physical monitors associated with an **HMONITOR** monitor handle. |
| [**GetNumberOfPhysicalMonitorsFromIDirect3DDevice9**](getnumberofphysicalmonitorsfromidirect3ddevice9.md) | Retrieves the number of physical monitors associated with a Direct3D device.              |
| [**GetPhysicalMonitorsFromHMONITOR**](getphysicalmonitorsfromhmonitor.md)                                 | Retrieves the physical monitors associated with an **HMONITOR** monitor handle.           |
| [**GetPhysicalMonitorsFromIDirect3DDevice9**](getphysicalmonitorsfromidirect3ddevice9.md)                 | Retrieves the physical monitors associated with a Direct3D device.                        |



 

## Internal Functions

The following functions are used by the monitor configuration API to access functionality in the display driver. Applications should not call these functions.

-   [**DDCCIGetCapabilitiesString**](ddccigetcapabilitiesstring.md)
-   [**DDCCIGetCapabilitiesStringLength**](ddccigetcapabilitiesstringlength.md)
-   [**DDCCIGetTimingReport**](ddccigettimingreport.md)
-   [**DDCCIGetVCPFeature**](ddccigetvcpfeature.md)
-   [**DDCCISaveCurrentSettings**](ddccisavecurrentsettings.md)
-   [**DDCCISetVCPFeature**](ddccisetvcpfeature.md)
-   [**DestroyPhysicalMonitorInternal**](destroyphysicalmonitorinternal.md)
-   [**GetNumberOfPhysicalMonitors**](getnumberofphysicalmonitors.md)
-   [**GetPhysicalMonitorDescription**](getphysicalmonitordescription.md)
-   [**GetPhysicalMonitors**](getphysicalmonitors.md)

## Related topics

<dl> <dt>

[Monitor Configuration Reference](monitor-configuration-reference.md)
</dt> </dl>

 

 




