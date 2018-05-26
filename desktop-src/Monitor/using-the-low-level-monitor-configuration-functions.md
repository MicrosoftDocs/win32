---
title: Using the Low-Level Monitor Configuration Functions
description: Using the Low-Level Monitor Configuration Functions
ms.assetid: 014a144b-d01a-4bc1-959d-08a643b3e1f5
keywords:
- monitor,functions
- monitor,low-level configuration functions
- monitor,DDC/CI
- monitor,Display Data Channel Command Interface
- monitor configuration,low-level configuration functions
- monitor configuration,functions
- monitor configuration,DDC/CI
- monitor configuration,Display Data Channel Command Interface
- low-level configuration functions
- Display Data Channel Command Interface
- DDC/CI
- VESA Monitor Control Command Set (MCCS)
- Monitor Control Command Set (MCCS)
- MCCS (Monitor Control Command Set)
- Virtual Control Panel (VCP)
- VCP (Virtual Control Panel)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the Low-Level Monitor Configuration Functions

Before using the low-level monitor configuration functions, you should be familiar with these standards:

-   Display Data Channel Command Interface (DDC/CI)
-   VESA Monitor Control Command Set (MCCS)

The low-level functions work by getting and setting the values of Virtual Control Panel (VCP) codes. A VCP code can be *continuous* or *noncontinuous*. Continuous codes can assume any value between zero and a vendor-specific maximum value. Noncontinuous codes support a defined set of values, which is also specific to the vendor.

To use the low-level monitor configuration functions, perform the following steps:

1.  Obtain an **HMONITOR** handle by calling [**EnumDisplayMonitors**](https://msdn.microsoft.com/library/windows/desktop/dd162610) or [**MonitorFromWindow**](https://msdn.microsoft.com/library/windows/desktop/dd145064).
2.  Call [**GetNumberOfPhysicalMonitorsFromHMONITOR**](/windows/win32/PhysicalMonitorEnumerationAPI/nf-physicalmonitorenumerationapi-getnumberofphysicalmonitorsfromhmonitor?branch=master) to get the number of physical monitors associated with the **HMONITOR** handle.
3.  Call [**GetPhysicalMonitorsFromHMONITOR**](/windows/win32/PhysicalMonitorEnumerationAPI/nf-physicalmonitorenumerationapi-getphysicalmonitorsfromhmonitor?branch=master) to get a list of handles to the physical monitors.
4.  Call [**GetCapabilitiesStringLength**](/windows/win32/LowLevelMonitorConfigurationAPI/nf-lowlevelmonitorconfigurationapi-getcapabilitiesstringlength?branch=master) to get the length of a monitor's DDC/CI capabilities string. The capabilities string is an ASCII string that contains static information about the monitor. One part of the string lists the VCP codes that the monitor supports. The string also lists the supported values of the noncontinuous VCP codes.
5.  Allocate a buffer to hold the capabilities string and call [**CapabilitiesRequestAndCapabilitiesReply**](/windows/win32/LowLevelMonitorConfigurationAPI/nf-lowlevelmonitorconfigurationapi-capabilitiesrequestandcapabilitiesreply?branch=master) to get the string.
6.  Parse the capabilities string to determine which VCP codes the monitor supports.
7.  For a continuous VCP code, call [**GetVCPFeatureAndVCPFeatureReply**](/windows/win32/LowLevelMonitorConfigurationAPI/nf-lowlevelmonitorconfigurationapi-getvcpfeatureandvcpfeaturereply?branch=master) to get the current and maximum values of the code. For a noncontinuous VCP code, parse the capabilities string to get the supported values.
8.  Call [**SetVCPFeature**](/windows/win32/LowLevelMonitorConfigurationAPI/nf-lowlevelmonitorconfigurationapi-setvcpfeature?branch=master) to set a new value for a VCP code.

## Related topics

<dl> <dt>

[**Using Monitor Configuration**](using-monitor-configuration.md)
</dt> </dl>

 

 




