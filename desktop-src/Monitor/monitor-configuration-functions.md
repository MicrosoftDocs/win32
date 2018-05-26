---
title: Monitor Configuration Functions
description: Monitor Configuration Functions
ms.assetid: e9a00792-f471-47a4-93d7-25400e27f13f
keywords:
- monitor,functions
- monitor,high-level functions
- monitor,low-level functions
- monitor,enumeration functions
- high-level functions
- low-level functions
- enumeration functions
- monitor configuration,functions
- monitor configuration,high-level functions
- monitor configuration,low-level functions
- monitor configuration,enumeration functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Monitor Configuration Functions

The following functions are used to get information from a monitor and to change a monitor's settings. Monitor configuration functions are categorized into high-level functions, low-level functions, and enumeration functions. For more information, see [Using Monitor Configuration](using-monitor-configuration.md).

## High-Level Functions



| Function                                                                         | Description                                                                          |
|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**DegaussMonitor**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-degaussmonitor?branch=master)                                         | Degausses a monitor.                                                                 |
| [**GetMonitorBrightness**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-getmonitorbrightness?branch=master)                             | Retrieves a monitor's minimum, maximum, and current brightness settings.             |
| [**GetMonitorCapabilities**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-getmonitorcapabilities?branch=master)                         | Retrieves the configuration capabilities of a monitor.                               |
| [**GetMonitorColorTemperature**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-getmonitorcolortemperature?branch=master)                 | Retrieves a monitor's current color temperature.                                     |
| [**GetMonitorContrast**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-getmonitorcontrast?branch=master)                                 | Retrieves a monitor's minimum, maximum, and current contrast settings.               |
| [**GetMonitorDisplayAreaPosition**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-getmonitordisplayareaposition?branch=master)           | Retrieves a monitor's minimum, maximum, and current horizontal or vertical position. |
| [**GetMonitorDisplayAreaSize**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-getmonitordisplayareasize?branch=master)                   | Retrieves a monitor's minimum, maximum, and current width or height.                 |
| [**GetMonitorRedGreenOrBlueDrive**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-getmonitorredgreenorbluedrive?branch=master)           | Retrieves a monitor's red, green, or blue drive value.                               |
| [**GetMonitorRedGreenOrBlueGain**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-getmonitorredgreenorbluegain?branch=master)             | Retrieves a monitor's red, green, or blue gain value.                                |
| [**GetMonitorTechnologyType**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-getmonitortechnologytype?branch=master)                     | Retrieves the type of technology used by a monitor.                                  |
| [**RestoreMonitorFactoryColorDefaults**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-restoremonitorfactorycolordefaults?branch=master) | Restores a monitor's color settings to their factory defaults.                       |
| [**RestoreMonitorFactoryDefaults**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-restoremonitorfactorydefaults?branch=master)           | Restores a monitor's settings to their factory defaults.                             |
| [**SaveCurrentMonitorSettings**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-savecurrentmonitorsettings?branch=master)                 | Saves the current monitor settings to the display's nonvolatile storage.             |
| [**SetMonitorBrightness**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-setmonitorbrightness?branch=master)                             | Sets a monitor's brightness value.                                                   |
| [**SetMonitorColorTemperature**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-setmonitorcolortemperature?branch=master)                 | Sets a monitor's color temperature.                                                  |
| [**SetMonitorContrast**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-setmonitorcontrast?branch=master)                                 | Sets a monitor's contrast value.                                                     |
| [**SetMonitorDisplayAreaPosition**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-setmonitordisplayareaposition?branch=master)           | Sets the horizontal or vertical position of a monitor's display area.                |
| [**SetMonitorDisplayAreaSize**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-setmonitordisplayareasize?branch=master)                   | Sets the width or height of a monitor's display area.                                |
| [**SetMonitorRedGreenOrBlueDrive**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-setmonitorredgreenorbluedrive?branch=master)           | Sets a monitor's red, green, or blue drive value.                                    |
| [**SetMonitorRedGreenOrBlueGain**](/windows/win32/HighLevelMonitorConfigurationAPI/nf-highlevelmonitorconfigurationapi-setmonitorredgreenorbluegain?branch=master)             | Sets a monitor's red, green, or blue gain value.                                     |



 

## Low-Level Functions



| Function                                                                                   | Description                                                                                                    |
|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**CapabilitiesRequestAndCapabilitiesReply**](/windows/win32/LowLevelMonitorConfigurationAPI/nf-lowlevelmonitorconfigurationapi-capabilitiesrequestandcapabilitiesreply?branch=master) | Retrieves a string describing a monitor's capabilities.                                                        |
| [**GetCapabilitiesStringLength**](/windows/win32/LowLevelMonitorConfigurationAPI/nf-lowlevelmonitorconfigurationapi-getcapabilitiesstringlength?branch=master)                         | Retrieves the length of a monitor's capabilities string.                                                       |
| [**GetTimingReport**](/windows/win32/LowLevelMonitorConfigurationAPI/nf-lowlevelmonitorconfigurationapi-gettimingreport?branch=master)                                                 | Retrieves a monitor's horizontal and vertical synchronization frequencies.                                     |
| [**GetVCPFeatureAndVCPFeatureReply**](/windows/win32/LowLevelMonitorConfigurationAPI/nf-lowlevelmonitorconfigurationapi-getvcpfeatureandvcpfeaturereply?branch=master)                 | Retrieves the current value, maximum value, and code type of a Virtual Control Panel (VCP) code for a monitor. |
| [**SaveCurrentSettings**](/windows/win32/LowLevelMonitorConfigurationAPI/nf-lowlevelmonitorconfigurationapi-savecurrentsettings?branch=master)                                         | Saves the current monitor settings to the display's nonvolatile storage.                                       |
| [**SetVCPFeature**](/windows/win32/LowLevelMonitorConfigurationAPI/nf-lowlevelmonitorconfigurationapi-setvcpfeature?branch=master)                                                     | Sets the value of a Virtual Control Panel (VCP) code for a monitor.                                            |



 

## Enumeration Functions



| Function                                                                                                   | Description                                                                               |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**DestroyPhysicalMonitor**](/windows/win32/PhysicalMonitorEnumerationAPI/nf-physicalmonitorenumerationapi-destroyphysicalmonitor?branch=master)                                                   | Closes a handle to a physical monitor.                                                    |
| [**DestroyPhysicalMonitors**](/windows/win32/PhysicalMonitorEnumerationAPI/nf-physicalmonitorenumerationapi-destroyphysicalmonitors?branch=master)                                                 | Closes an array of physical monitor handles.                                              |
| [**GetNumberOfPhysicalMonitorsFromHMONITOR**](/windows/win32/PhysicalMonitorEnumerationAPI/nf-physicalmonitorenumerationapi-getnumberofphysicalmonitorsfromhmonitor?branch=master)                 | Retrieves the number of physical monitors associated with an **HMONITOR** monitor handle. |
| [**GetNumberOfPhysicalMonitorsFromIDirect3DDevice9**](/windows/win32/PhysicalMonitorEnumerationAPI/nf-physicalmonitorenumerationapi-getnumberofphysicalmonitorsfromidirect3ddevice9?branch=master) | Retrieves the number of physical monitors associated with a Direct3D device.              |
| [**GetPhysicalMonitorsFromHMONITOR**](/windows/win32/PhysicalMonitorEnumerationAPI/nf-physicalmonitorenumerationapi-getphysicalmonitorsfromhmonitor?branch=master)                                 | Retrieves the physical monitors associated with an **HMONITOR** monitor handle.           |
| [**GetPhysicalMonitorsFromIDirect3DDevice9**](/windows/win32/PhysicalMonitorEnumerationAPI/nf-physicalmonitorenumerationapi-getphysicalmonitorsfromidirect3ddevice9?branch=master)                 | Retrieves the physical monitors associated with a Direct3D device.                        |



 

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

 

 




