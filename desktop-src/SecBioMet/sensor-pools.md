---
title: Sensor Pools
description: Describes three possible sensor pools system, private, and unassigned.
ms.assetid: d7fd3c39-d719-4cfd-9af0-a87837f3f328
ms.topic: article
ms.date: 05/31/2018
---

# Sensor Pools

To support both Windows authentication scenarios and vendor defined authentication, the Windows Biometric service organizes biometric units into three possible sensor pools:

-   **Private pool** a collection of biometric units allocated for exclusive use by a client application. Private pools can support authentication scenarios that are not Windows-based, and they make it possible for an application to access the hardware of a biometric unit in a vendor-defined fashion. There can be as many private sensor pools on the system as there are biometric units.
-   **System sensor pool** a collection of sharable biometric units that provide access to Windows authentication services. This pool is used by Winlogon, UAC, and any other client that associates a SID with a specific biometric template. Each biometric service provider has one system sensor pool.
-   **Unassigned pool** contains a (possibly empty) collection of biometric units that are not assigned to either the system pool or the private pool.

Applications can use the shared system pool or they can create a private pool made up of biometric units removed from the system or unassigned pools. When an application releases its private pool, the biometric units are reconfigured and returned to their original pools. To prevent denial of service attacks, only privileged users are permitted to remove the last sensor from the system pool. For more information, see the following topics.

## In this section



| Topic                                                       | Description                                                                                                                                                                                                                                                    |
|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Private Sensor Pool](private-sensor-pool.md)<br/>   | A collection of biometric units reserved for exclusive use by a client application. Private pools support proprietary authentication methods and enable a client application to access a biometric unit by using vendor-specified control commands.<br/> |
| [System Sensor Pool](system-sensor-pool.md)<br/>     | A collection of sharable biometric units that provide access to Windows authentication services. This pool is used by Winlogon, UAC, and any other client that associates a SID with a specific biometric template.<br/>                                 |
| [System Pool Behavior](system-pool-behavior.md)<br/> | Discussion about the actions taken by the system pool when event notices are sent and when no biometric operations are pending.<br/>                                                                                                                     |



 

## Related topics

<dl> <dt>

[About the Windows Biometric Framework API](./biometric-service-api-portal.md)
</dt> </dl>

 

