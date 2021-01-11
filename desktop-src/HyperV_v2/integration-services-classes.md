---
description: Integration services are software services that run on top of the guest operating system inside of a child virtual machine and as part of the virtualization stack in the management operating system to provide some level of integration with the management operating system.
ms.assetid: 7A8E9EF2-AC67-47CB-81A5-BF4C8A55D710
title: Integration services classes
ms.topic: reference
ms.date: 05/31/2018
---

# Integration services classes

Integration services are software services that run on top of the guest operating system inside of a child virtual machine and as part of the virtualization stack in the management operating system to provide some level of integration with the management operating system. They are used to address problems that arise from the high level of isolation provided by virtual machines.

The following are virtualization WMI classes related to the integration services.

## In this section



| Topic                                                                                                                | Description                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Msvm\_CopyFileToGuestJob**](msvm-copyfiletoguestjob.md)<br/>                                               | Represents a guest file service operation job. <br/>                                                                                                                                                                                                            |
| [**Msvm\_CopyFileToGuestSettingData**](msvm-copyfiletoguestsettingdata.md)<br/>                               | Represents the parameters for copying a file from the host into the guest. <br/>                                                                                                                                                                                |
| [**Msvm\_GuestFileService**](msvm-guestfileservice.md)<br/>                                                   | [**Msvm\_GuestFileService**](msvm-guestfileservice.md) contains a method that can be used to copy a file to a virtual machine from the Hyper-V host. <br/>                                                                                                     |
| [**Msvm\_GuestService**](msvm-guestservice.md)<br/>                                                           | [**Msvm\_GuestService**](msvm-guestservice.md) is the abstract base class for services in the guest that can be accessed from the host. <br/>                                                                                                                  |
| [**Msvm\_GuestServiceInterfaceComponent**](msvm-guestserviceinterfacecomponent.md)<br/>                       | Represents the state of the guest service interface component, which provides a mechanism to interact with the virtual machine from the management interfaces on the host system. <br/>                                                                         |
| [**Msvm\_GuestServiceInterfaceComponentSettingData**](msvm-guestserviceinterfacecomponentsettingdata.md)<br/> | Represents the configured state of the guest service interface component. <br/>                                                                                                                                                                                 |
| [**Msvm\_KvpExchangeComponent**](msvm-kvpexchangecomponent.md)<br/>                                           | Represents the state of the key/value pair exchange service, which provides a mechanism to exchange data between the virtual machine and the operating system running on the management operating system.<br/>                                                  |
| [**Msvm\_KvpExchangeComponentSettingData**](msvm-kvpexchangecomponentsettingdata.md)<br/>                     | Represents the configured state of the key/value pair exchange service.<br/>                                                                                                                                                                                    |
| [**Msvm\_KvpExchangeDataItem**](msvm-kvpexchangedataitem.md)<br/>                                             | Represents a key/value pair.<br/>                                                                                                                                                                                                                               |
| [**Msvm\_RegisteredGuestService**](msvm-registeredguestservice.md)<br/>                                       | Represents an association between an instance of [**Msvm\_GuestServiceInterfaceComponent**](msvm-guestserviceinterfacecomponent.md) and an instance of [**Msvm\_GuestService**](msvm-guestservice.md), which represents a service running in the guest. <br/> |
| [**Msvm\_ShutdownComponent**](msvm-shutdowncomponent.md)<br/>                                                 | Represents the state of the shutdown service, which provides a mechanism to shut down the operating system of the virtual machine from the management interfaces on the host system.<br/>                                                                       |
| [**Msvm\_ShutdownComponentSettingData**](msvm-shutdowncomponentsettingdata.md)<br/>                           | Represents the configured state of the shutdown service.<br/>                                                                                                                                                                                                   |
| [**Msvm\_TimeSyncComponent**](msvm-timesynccomponent.md)<br/>                                                 | Represents the state of the time synchronization service, which is responsible for synchronizing the system time of a virtual machine with the system time of the operating system running in the management operating system.<br/>                             |
| [**Msvm\_TimeSyncComponentSettingData**](msvm-timesynccomponentsettingdata.md)<br/>                           | Represents the configured state of the time synchronization service.<br/>                                                                                                                                                                                       |
| [**Msvm\_VssComponent**](msvm-vsscomponent.md)<br/>                                                           | Represents the state of the Volume Shadow Copy Service (VSS) service, which implements the VSS Requester in the guest operating system.<br/>                                                                                                                    |
| [**Msvm\_VssComponentSettingData**](msvm-vsscomponentsettingdata.md)<br/>                                     | Represents the configured state of the Volume Shadow Copy Service (VSS) service.<br/>                                                                                                                                                                           |



 

 

 




