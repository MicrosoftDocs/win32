---
title: Virtual Machine
description: The Virtual Machine resource type is used to control the state of a virtual machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9f1dcda8-f34b-4801-a35a-970c04ddd6b8'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource types Failover Cluster ,Virtual Machine", "Virtual Machine resource type Failover Cluster", "Virtual Machine resource type Failover Cluster ,resources"]
---

# Virtual Machine

The Virtual Machine [resource type](resource-types.md) is used to control the state of a virtual machine (VM). The following table shows the mapping between the state of the VM (indicated by the **EnabledState** property of the [**Msvm\_ComputerSystem**](https://msdn.microsoft.com/library/cc136822) instance representing the VM) and the state of the Virtual Machine resource (indicated by the **State** property of the [**MSCluster\_Resource**](https://msdn.microsoft.com/library/aa371464) class or the return of [**GetClusterResourceState**](getclusterresourcestate.md) function).



<table>
<thead>
<tr class="header">
<th>VM state</th>
<th>Virtual Machine resource state</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Disabled (3)<br/></td>
<td rowspan="2"> Offline (3)<br/> ${REMOVE}$<br />
</td>
</tr>
<tr class="even">
<td>Suspended (32769)<br/></td>

</tr>
<tr class="odd">
<td>Starting (32770)<br/></td>
<td>Online Pending (129) / Online (2)<br/></td>
</tr>
<tr class="even">
<td>Stopping (32774)<br/></td>
<td rowspan="2"> Offline Pending (130) / Offline (3)<br/> ${REMOVE}$<br />
</td>
</tr>
<tr class="odd">
<td>Saving (32773)<br/></td>

</tr>
<tr class="even">
<td>Enabled (2)<br/></td>
<td rowspan="4"> Online (2)<br/> ${REMOVE}$<br />
</td>
</tr>
<tr class="odd">
<td>Paused (32768)<br/></td>

</tr>
<tr class="even">
<td>Pausing (32776)<br/></td>

</tr>
<tr class="odd">
<td>Resuming (32777)<br/></td>

</tr>
</tbody>
</table>



 

The following table summarizes the characteristics of the Virtual Machine resource type.



| Characteristic                                                   | Description                                                                                                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Required [dependencies](resource-dependencies.md)<br/>    | None.<br/>                                                                                                                                                                                                                                                                                                                                                            |
| Required [private properties](private-properties.md)<br/> | [**CheckHeartbeat**](virtual-machines-checkheartbeat.md), [**MigrationFailureReason**](virtual-machines-migrationfailurereason.md), [**MigrationProgress**](virtual-machines-migrationprogress.md), [**OfflineAction**](virtual-machines-offlineaction.md), [**ShutdownAction**](virtual-machines-shutdownaction.md), [**VmId**](virtual-machines-vmid.md)<br/> |
| Optional private properties<br/>                           | None.<br/>                                                                                                                                                                                                                                                                                                                                                            |



 

 

 





