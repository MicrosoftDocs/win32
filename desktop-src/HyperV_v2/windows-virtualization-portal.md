---
description: Microsoft Hyper-V server provides a scalable, reliable, and highly available virtual machine management environment. Hyper-V virtual machine software consolidates servers and development and testing environments.
ms.assetid: 3359A33F-528B-4955-8B37-30523B8AD33A
title: Hyper-V WMI provider (V2)
ms.topic: article
ms.date: 05/31/2018
---

# Hyper-V WMI provider (V2)

## Purpose

Hyper-V provides a scalable, reliable, and highly available virtualized server computing environment. It enables one or more guest operating systems to run concurrently on a single physical computer. Key uses for virtual machine technology include the following:

-   Server consolidation
-   Consolidation of development and testing environments
-   Simplified disaster recovery

## In this section



| Topic                                                                                                 | Description                                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [About the Hyper-V WMI provider](about-the-virtualization-wmi-provider.md)<br/>                | The WMI provider for Hyper-V enable developers, and scripters, to quickly build custom tools, utilities, and enhancements for the virtualization platform. The WMI interfaces can manage all aspects of the Hyper-V services.<br/> |
| [Using the Hyper-V WMI provider](using-the-virtualization-wmi-provider.md)<br/>                | The following topics describe how to use the Hyper-V WMI provider.<br/>                                                                                                                                                            |
| [Hyper-V WMI classes](hyper-v-wmi-classes.md)<br/>                                             | The following are the Hyper-V WMI classes.<br/>                                                                                                                                                                                    |
| [Hyper-V application health monitoring API](hyper-v-application-health-monitoring-api.md)<br/> | The Hyper-V application health monitoring API is used to monitor the health state of applications running in a virtual machine.<br/>                                                                                               |
| [Hyper-V replication API](hyper-v-replication-api.md)<br/>                                     | The Hyper-V replication API is used to control virtual machine replication and failover recovery.<br/>                                                                                                                             |
| [Hyper-V metrics API](hyper-v-metrics-api.md)<br/>                                             | The Hyper-V metrics API is used to monitor the health state of applications running in a virtual machine.<br/>                                                                                                                     |
| [Hyper-V networking API](hyper-v-networking-api.md)<br/>                                       | The Hyper-V networking API is used to control networking in Hyper-V.<br/>                                                                                                                                                          |
| [Hyper-V migration API](hyper-v-storage-migration-api.md)<br/>                                 | The Hyper-V migration API is used to control storage and live migration in Hyper-V.<br/>                                                                                                                                           |
| [Hyper-V virtual Fibre Channel API](hyper-v-virtual-fiber-channels-api.md)<br/>                | The Hyper-V virtual Fibre Channel API is used to control virtual Fibre Channel adapters in Hyper-V.<br/>                                                                                                                           |
| [Hyper-V VM placement API](hyper-v-vm-placement-api.md)<br/>                                   | The Hyper-V virtual machine (VM) placement API contains the compatibility info for the VMs or hosting computer system.<br/>                                                                                                        |
| [Threshold classes](threshold-classes.md)<br/>                                                 | Contains the classes introduced in Windows 10.<br/>                                                                                                                                                                                |
| [RS2 Classes](redstone-classes.md)<br/>                                                        | Contains the new classes for Windows 10, version 1703.<br/>                                                                                                                                                                        |
| [RS3 Classes](rs3-classes.md)<br/>                                                             | Contains the new classes for Windows 10, version 1709.<br/>                                                                                                                                                                        |
| [Hyper-V glossary](virtualization-glossary.md)<br/>                                            | Glossary of terms used in the Windows Virtualization SDK documentation.<br/>                                                                                                                                                       |



 

## Run-time requirements

Hyper-V services require an x64-based system that supports hardware-assisted virtualization running Hyper-V. Programs that interact with the Hyper-V WMI interfaces however, can run remotely on any system that supports WMI.

## Related topics

<dl> <dt>

[Hyper-V (Windows Server 2008 R2 Technical Library)](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc753637(v=ws.10))
</dt> <dt>

[Windows Management Instrumentation](/windows/desktop/WmiSdk/wmi-start-page)
</dt> <dt>

[Windows Server Virtualization](https://www.microsoft.com/windowsserver2008/virtualization/default.mspx)
</dt> </dl>

 

