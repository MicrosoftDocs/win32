---
title: Virtual System Management Classes
description: Virtualization WMI classes related to virtual system management.
ms.assetid: '65db7875-9bb9-4c38-bfe6-788f65aba06f'
---

# Virtual System Management Classes

The following are virtualization WMI classes related to virtual system management.

## In this section



| Class                                                                                                                | Description                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Msvm\_RdvComponent**](msvm-rdvcomponent.md)<br/>                                                           | Represents the state of the RDV component, which is responsible for providing a transport for parent to the guest for configuration purposes.<br/>                                                                                                           |
| [**Msvm\_RdvComponentSettingData**](msvm-rdvcomponentsettingdata.md)<br/>                                     | Represents the configured state of the Remote Desktop Virtualization (RDV) component.<br/>                                                                                                                                                                   |
| [**Msvm\_ServicingSettings**](msvm-servicingsettings.md)<br/>                                                 | Contains settings used during servicing operations.<br/>                                                                                                                                                                                                     |
| [**Msvm\_AffectedJobElement**](msvm-affectedjobelement.md)<br/>                                               | Represents an association between a job and the managed element that may be affected by its execution.<br/>                                                                                                                                                  |
| [**Msvm\_ConcreteJob**](msvm-concretejob.md)<br/>                                                             | Represents a unit of work and is used to track the progress of asynchronous operations.<br/>                                                                                                                                                                 |
| [**RequestStateChange Method**](requeststatechange-msvm-concretejob.md)<br/>                                  | Requests that the state of the job be changed to the value specified<br/>                                                                                                                                                                                    |
| [**Msvm\_ElementSettingData**](msvm-elementsettingdata.md)<br/>                                               | Associates a managed element with its configuration data.<br/>                                                                                                                                                                                               |
| [**Msvm\_Error**](msvm-error.md)<br/>                                                                         | Contains information about the severity, cause, recommended actions, and other data related to the failure of a CIM Operation.<br/>                                                                                                                          |
| [**Msvm\_HostedDependency**](msvm-hosteddependency.md)<br/>                                                   | Associates a virtual computer system instance with the computer system object representing the physical, hosting system.<br/>                                                                                                                                |
| [**Msvm\_HostedService**](msvm-hostedservice.md)<br/>                                                         | Associates a service with its hosting computer system.<br/>                                                                                                                                                                                                  |
| [**Msvm\_ServiceAffectsElement**](msvm-serviceaffectselement.md)<br/>                                         | Associates a virtual computer system instance with the management service that controls its state.<br/>                                                                                                                                                      |
| [**Msvm\_SettingsDefineState**](msvm-settingsdefinestate.md)<br/>                                             | Associates a virtual system and its devices with instances of [**CIM\_SettingData**](https://msdn.microsoft.com/library/cc136911) representing the current settings that apply to these objects.<br/>                                                                                |
| [**Msvm\_SystemExportSettingData**](msvm-systemexportsettingdata.md)<br/>                                     | Associates a virtual system and its export setting data.<br/>                                                                                                                                                                                                |
| [**Msvm\_VirtualSystemExportSettingData**](msvm-virtualsystemexportsettingdata.md)<br/>                       | Provides additional information to be used with the [**ExportVirtualSystemEx**](msvm-virtualsystemmanagementservice-exportvirtualsystemex.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.<br/> |
| [**Msvm\_VirtualSystemImportSettingData**](msvm-virtualsystemimportsettingdata.md)<br/>                       | Represents settings of a virtual system to import.<br/>                                                                                                                                                                                                      |
| [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)<br/>                       | Represents the virtualization service present on a single host system.<br/>                                                                                                                                                                                  |
| [**Msvm\_VirtualSystemManagementServiceSettingData**](msvm-virtualsystemmanagementservicesettingdata.md)<br/> | Represents the settings for the virtualization service present on a single host system.<br/>                                                                                                                                                                 |



 

## Related topics

<dl> <dt>

[Virtualization WMI Classes](virtualization-wmi-classes.md)
</dt> </dl>

 

 





