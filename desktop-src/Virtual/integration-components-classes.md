---
title: Integration Services Classes
description: Integration services are software services that run on top of the guest operating system inside of a child virtual machine (VM) and as part of the virtualization stack in the management operating system to provide some level of integration with the management operating system.
ms.assetid: 'b068c65b-d746-4d7d-9fd9-ca71e8ae7fa3'
---

# Integration Services Classes

Integration services are software services that run on top of the guest operating system inside of a child virtual machine (VM) and as part of the virtualization stack in the management operating system to provide some level of integration with the management operating system. They are used to address problems that arise from the high level of isolation provided by VMs.

The following are virtualization WMI classes related to the integration services.

## In this section



| Class                                                                                            | Description                                                                                                                                                                                                                               |
|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Msvm\_HeartbeatComponent**](msvm-heartbeatcomponent.md)<br/>                           | Represents the state of the heartbeat service, which is responsible for monitoring the state of a virtual machine by reporting a heartbeat at regular intervals.<br/>                                                               |
| [**Msvm\_HeartbeatComponentSettingData**](msvm-heartbeatcomponentsettingdata.md)<br/>     | Represents the configured state of the heartbeat service.<br/>                                                                                                                                                                      |
| [**Msvm\_KvpExchangeComponent**](msvm-kvpexchangecomponent.md)<br/>                       | Represents the state of the key/value pair exchange service, which provides a mechanism to exchange data between the virtual machine and the operating system running on the management operating system.<br/>                      |
| [**Msvm\_KvpExchangeComponentSettingData**](msvm-kvpexchangecomponentsettingdata.md)<br/> | Represents the configured state of the key/value pair exchange service.<br/>                                                                                                                                                        |
| [**Msvm\_KvpExchangeDataItem**](msvm-kvpexchangedataitem.md)<br/>                         | Represents a key/value pair.<br/>                                                                                                                                                                                                   |
| [**Msvm\_ShutdownComponent**](msvm-shutdowncomponent.md)<br/>                             | Represents the state of the shutdown service, which provides a mechanism to shut down the operating system of the virtual machine from the management interfaces on the host system.<br/>                                           |
| [**Msvm\_ShutdownComponentSettingData**](msvm-shutdowncomponentsettingdata.md)<br/>       | Represents the configured state of the shutdown service.<br/>                                                                                                                                                                       |
| [**Msvm\_TimeSyncComponent**](msvm-timesynccomponent.md)<br/>                             | Represents the state of the time synchronization service, which is responsible for synchronizing the system time of a virtual machine with the system time of the operating system running in the management operating system.<br/> |
| [**Msvm\_TimeSyncComponentSettingData**](msvm-timesynccomponentsettingdata.md)<br/>       | Represents the configured state of the time synchronization service.<br/>                                                                                                                                                           |
| [**Msvm\_VssComponent**](msvm-vsscomponent.md)<br/>                                       | Represents the state of the Volume Shadow Copy Service (VSS) service, which implements the VSS Requester in the guest operating system.<br/>                                                                                        |
| [**Msvm\_VssComponentSettingData**](msvm-vsscomponentsettingdata.md)<br/>                 | Represents the configured state of the Volume Shadow Copy Service (VSS) service.<br/>                                                                                                                                               |



 

## Related topics

<dl> <dt>

[Virtualization WMI Classes](virtualization-wmi-classes.md)
</dt> </dl>

 

 





