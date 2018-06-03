---
title: Windows Network Virtualization
description: Windows Network Virtualization enables customer virtual machine networks to decouple virtual machine networks from physical networks, provides flexibility in virtual machine provisioning, and allows customers to bring their IP addresses and topologies into cloud datacenters.
ms.assetid: 4f8c00af-0182-4f20-b49c-5a56f698d725
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Network Virtualization

## Purpose

Windows Network Virtualization enables customer virtual machine networks to decouple virtual machine networks from physical networks, provides flexibility in virtual machine provisioning, and allows customers to bring their IP addresses and topologies into cloud datacenters. The notification API enables the Windows Network Virtualization (WNV) module in the network stack to notify management infrastructure about missing policy or policy update events.

The main network virtualization policies are provisioned by the Windows Management Instrumentation (WMI) [Net Virtualization classes](https://msdn.microsoft.com/library/hh872477). The optional notification API specified here allows the network virtualization module (also known as the WNV driver) in the network stack to notify the management infrastructure about missing policy or policy update events due to new virtual machine provisioning or virtual machine migration.

Developers can use the WNV notification API to implement on-demand policy requests to a datacenter management server or orchestrator that reacts to virtual machine life cycle events such as provisioning and live migration. These events cause the WNV driver to generate event notifications for the active communication to the effected virtual machines. By requesting and consuming these notifications, developers can trigger policy update requests from individual hosts to a policy server to retrieve the most current policies using the WMI provider.

## In this section



| Topic                                                                                       | Description                                                                                              |
|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [WNV notification enumerations](windows-network-virtualization-enumerations.md)<br/> | The Windows Network Virtualization (WNV) notification API defines the following enumerations.<br/> |
| [WNV notification functions](windows-network-virtualization-functions.md)<br/>       | The Windows Network Virtualization (WNV) notification API defines the following functions.<br/>    |
| [WNV notification structures](windows-network-virtualization-structures.md)<br/>     | The Windows Network Virtualization (WNV) notification API defines the following structures.<br/>   |



 

## Developer audience

Windows Network Virtualization is designed for use by C/C++ programmers. Programmers should also be familiar with Hyper-V Network Virtualization architecture and policy requirements.

## Run-time requirements

Windows Network Virtualization is supported only in Windows Server 2012. It requires the Hyper-V Role to be installed to allow Hyper-V Network Virtualization to operate.

## Related topics

<dl> <dt>

[Hyper-V Network Virtualization Overview](http://go.microsoft.com/fwlink/p/?linkid=263545)
</dt> <dt>

[Windows Server 2012 Hyper-V Network Virtualization Survival Guide](http://go.microsoft.com/fwlink/p/?linkid=263541)
</dt> <dt>

[WMI Net Virtualization classes](https://msdn.microsoft.com/library/hh872477)
</dt> </dl>

 

 





