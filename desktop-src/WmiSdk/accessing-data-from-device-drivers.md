---
description: The Windows Driver Model (WDM) provider grants access to the classes, instances, methods, and events of hardware drivers that conform to the WDM model.
ms.assetid: 8686a613-0e53-4e6e-b193-7839abfb70de
ms.tgt_platform: multiple
title: Accessing Data from Device Drivers
ms.topic: article
ms.date: 05/31/2018
---

# Accessing Data from Device Drivers

The Windows Driver Model (WDM) provider grants access to the classes, instances, methods, and events of hardware drivers that conform to the WDM model. The classes for hardware drivers reside in the \\\\root\\wmi namespace.

The WDM provider is of interest to those who write device drivers and to administrators who are interested in device driver data.

The following sections are discussed in this topic:

-   [Information for Device Driver Writers](#information-for-device-driver-writers)
-   [Information for Administrators and Users of Driver Data](#information-for-administrators-and-users-of-driver-data)
-   [Related topics](#related-topics)

## Information for Device Driver Writers

WMI classes related to a specific device driver are created when the WDM provider extracts the binary MOF from the device driver executable file. This takes place whenever WMI is started, a new device driver is installed, or the instance of [WMIBinaryMofResource](/windows/desktop/WmiCoreProv/wmibinarymofresource) for a particular driver is deleted. By checking Wmiprov.log, you can determine if an error resulting in failure occurred while extracting the binary MOF file. Details of [mofcomp](mofcomp.md) errors are reported in Mofcomp.log. For more information, see [WMI Log Files](wmi-log-files.md). For performance reasons, the WDM provider does not generate events while creating or deleting classes due to a WDM provider starting or stopping.

The WDM provider transforms all WNODE data into class information. If an error is encountered when transforming the data from WNODE to class data, it is reported in Wmiprov.log with the header formatted and bytes rendered in the same form as a memory dump.

Changes made to driver security settings do not take effect until the WDM provider is unloaded and reloaded. For more information, see [Unloading a Provider](unloading-a-provider.md).

WMI can also make high-performance counters for hardware drivers available. For more information about creating high-performance classes and displaying data in Perfmon System Monitor, see [Improving the Efficiency of an Instance Provider](improving-the-efficiency-of-an-instance-provider.md). For more information about writing WMI-enabled device drivers, see [https://www.microsoft.com/ddk](https://msdn.microsoft.com/library/aa972908.aspx). For more information about WDM specific qualifiers in the MOF file, see [**Qualifiers Specific to the WDM Provider**](qualifiers-specific-to-the-wdm-provider.md).

## Information for Administrators and Users of Driver Data

Listing the instances of the [WMIBinaryMofResource](/windows/desktop/WmiCoreProv/wmibinarymofresource) class provides a list of the drivers in the system and information about whether the WDM provider succeeded in compiling the MOFs for each driver. You can force the provider to recompile and regenerate the classes for a driver by deleting the instance of WMIBinaryMofResource that represents that driver. Details of [mofcomp](mofcomp.md) errors are reported in the Mofcomp.log.

If the WMI namespace is corrupted, it can be deleted and reopened to force WDM to rebuild the driver classes. For more information about opening a namespace, see [Creating Hierarchies Within WMI](creating-hierarchies-within-wmi.md).

Driver classes can occasionally get "stranded" if driver loading is interrupted or other abnormal operations occur. The WDM provider will only search for and clean up "stranded" classes when a new driver is installed or when the **Software\\Microsoft\\WBEM\\WDMProvider** registry key value **ProcessStrandedClasses** is set to **TRUE**. Setting this value to **TRUE** slows WMI startup performance because of the cleanup operation. The default value is **FALSE**. The WDM provider only checks this registry value when the "Root\\Wmi" namespace is opened for the first time.

If security changes are made to a WDM device driver, the changes will not go into effect until the WDM provider is unloaded and reloaded. The Windows Management service must be stopped and restarted to accomplish this.

## Related topics

<dl> <dt>

[Using WMI](using-wmi.md)
</dt> </dl>

 

 
