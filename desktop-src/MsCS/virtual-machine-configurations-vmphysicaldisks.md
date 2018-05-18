---
title: VmPhysicalDisks
description: Used internally by the virtual machine (VM) configuration resource type to store information about the pass-through disks that are used by the VM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '45789eb5-bb44-4d40-af16-eb66145dc5dc'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["VmPhysicalDisks Failover Cluster ,for virtual machine configurations", "VmPhysicalDisks Failover Cluster"]
topic_type:
- apiref
api_name:
- VmPhysicalDisks
api_type:
- NA
---

# VmPhysicalDisks

Used internally by the virtual machine (VM) configuration resource type to store information about the pass-through disks that are used by the VM. This property is set using the [CLUSCTL\_RESOURCE\_VM\_CONFIG\_UPDATE](clusctl-resource-vm-config-update.md) resource control. The following table summarizes the attributes of the **VmPhysicalDisks** property.



| Attribute            | Value                                                         |
|----------------------|---------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string<br/>                     |
| Access<br/>    | [Read-only](read-only-properties.md)<br/>              |
| Status<br/>    | Required<br/>                                           |
| Structure<br/> | [**CLUSPROP\_SZ**](clusprop-sz.md)<br/>                |
| Minimum<br/>   | **NULL**<br/>                                           |
| Maximum<br/>   | see [Maximum String Size](maximum-string-size.md)<br/> |
| Default<br/>   | **NULL**<br/>                                           |



 

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Virtual Machine Configuration Private Properties](virtual-machine-configuration-private-properties.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_VM\_CONFIG\_UPDATE](clusctl-resource-vm-config-update.md)
</dt> </dl>

 

 





