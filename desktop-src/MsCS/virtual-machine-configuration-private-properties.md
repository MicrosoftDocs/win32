---
title: Virtual Machine Configuration Private Properties
description: Virtual machine (VM) configuration resources have the following private properties.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f111b82c-af00-4393-9d32-39974cf880d1'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
---

# Virtual Machine Configuration Private Properties

Virtual machine (VM) configuration [resources](resources.md) have the following [private properties](private-properties.md).



| Property                                                                                          | Status                                                                                                                                                                                                      |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DependsOnSharedVolumes**](virtual-machine-configurations-dependonsharedvolumes.md)<br/> | Required<br/> **Windows Server 2008:** The [**DependsOnSharedVolumes**](virtual-machine-configurations-dependonsharedvolumes.md) property is not supported before Windows Server 2008 R2.<br/> |
| [**VmId**](virtual-machine-configurations-vmid.md)<br/>                                    | Required<br/>                                                                                                                                                                                         |
| [**VmPhysicalDisks**](virtual-machine-configurations-vmphysicaldisks.md)<br/>              | Required<br/>                                                                                                                                                                                         |
| [**VmStoreRootPath**](virtual-machine-configurations-vmstorerootpath.md)<br/>              | Required<br/>                                                                                                                                                                                         |
| [**VmSwitchPorts**](virtual-machine-configurations-vmswitchports.md)<br/>                  | Not supported<br/> **Windows Server 2008 R2 and Windows Server 2008:** Required<br/>                                                                                                            |



 

[Cluster Administrator](cluster-administrator.md) presents the VM configuration private properties TBD.

## Related topics

<dl> <dt>

[Cluster Object Private Properties](private-properties-ref.md)
</dt> </dl>

 

 





