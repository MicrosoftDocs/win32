---
title: Virtual System Classes
description: Virtualization WMI classes related to the virtual system.
ms.assetid: 'cbcf3cb5-85bd-4c8b-a770-b91748ee1f8d'
---

# Virtual System Classes

The following are virtualization WMI classes related to the virtual system.

## In this section



| Class                                                                                                | Description                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Msvm\_ComputerSystem**](msvm-computersystem.md)<br/>                                       | Represents a physical computer system or virtual computer system (VM).<br/>                                                                                                                                                                                                                          |
| [**Msvm\_ConcreteComponent**](msvm-concretecomponent.md)<br/>                                 | A generic association used to establish 'part of' relationships between managed elements.<br/>                                                                                                                                                                                                       |
| [**Msvm\_LastAppliedSettingData**](msvm-lastappliedsettingdata.md)<br/>                       | An association between a virtual system and the setting data of the snapshot which was most recently applied to the virtual system.<br/>                                                                                                                                                             |
| [**Msvm\_ParentChildSettingData**](msvm-parentchildsettingdata.md)<br/>                       | An association between an instance of [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) and the **Msvm\_VirtualSystemSettingData** instance that represents the most recent snapshot upon which this object is based.<br/>                                                     |
| [**Msvm\_PreviousSettingData**](msvm-previoussettingdata.md)<br/>                             | An association between a virtual system and the setting data of the snapshot that is the parent to the virtual system.<br/>                                                                                                                                                                          |
| [**Msvm\_SummaryInformation**](msvm-summaryinformation.md)<br/>                               | Used in the [**GetSummaryInformation**](getsummaryinformation-msvm-virtualsystemmanagementservice.md) method in the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class to quickly retrieve common information related to a virtual machine or snapshot.<br/> |
| [**Msvm\_SystemDevice**](msvm-systemdevice.md)<br/>                                           | Associates a logical device with the parent system.<br/>                                                                                                                                                                                                                                             |
| [**Msvm\_VirtualSystemGlobalSettingData**](msvm-virtualsystemglobalsettingdata.md)<br/>       | Represents the global settings for a virtual system.<br/>                                                                                                                                                                                                                                            |
| [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md)<br/>                   | Represents the virtualization-specific settings for a virtual system.<br/>                                                                                                                                                                                                                           |
| [**Msvm\_VirtualSystemSettingDataComponent**](msvm-virtualsystemsettingdatacomponent.md)<br/> | A generic association used to establish 'part of' relationships between one instance of [**CIM\_VirtualSystemSettingData**](https://msdn.microsoft.com/library/cc136954) and one or more instances of [**CIM\_ResourceAllocationSettingData**](https://msdn.microsoft.com/library/mt146214).<br/>                     |



 

## Related topics

<dl> <dt>

[Virtualization WMI Classes](virtualization-wmi-classes.md)
</dt> </dl>

 

 





