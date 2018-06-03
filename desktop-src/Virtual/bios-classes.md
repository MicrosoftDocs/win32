---
title: BIOS Classes
description: The virtual BIOS is a software image that is loaded into RAM to configure some of the basic aspects of and boot a computer system. There is one BIOS element per computer system and that element cannot be replaced or removed.
ms.assetid: 61fa8f65-bcdf-4a7d-8c0b-5ea5986842e6
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BIOS Classes

The virtual BIOS is a software image that is loaded into RAM to configure some of the basic aspects of and boot a computer system. There is one BIOS element per computer system and that element cannot be replaced or removed. Thus, there is no resource pool for adding new BIOS elements to the virtual system. The BIOS element also does not have its own SettingData class to describe the settings for the BIOS. Settings for the BIOS, such as serial numbers, boot order, and num lock state, are found in the [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) class.

The following are virtualization WMI classes related to the BIOS. These classes are in the \\\\.\\Root\\Virtualization namespace.

## In this section



| Class                                                    | Description                                                                                             |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**Msvm\_BIOSElement**](msvm-bioselement.md)<br/> | Represents the low-level software that is loaded into RAM to configure and start the system.<br/> |
| [**Msvm\_SystemBIOS**](msvm-systembios.md)<br/>   | Used to associate a virtual system with its BIOS.<br/>                                            |



 

## Related topics

<dl> <dt>

[Virtualization WMI Classes](virtualization-wmi-classes.md)
</dt> </dl>

 

 





