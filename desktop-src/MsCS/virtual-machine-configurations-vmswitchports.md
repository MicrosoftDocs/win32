---
title: VmSwitchPorts
description: Used internally by the virtual machine (VM) configuration resource type to store information about the VM network switch ports that are used by the VM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cc85bfda-d41d-49fc-a3e6-a66ca8ca6666
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- VmSwitchPorts Failover Cluster ,for virtual machine configurations
- VmSwitchPorts Failover Cluster
topic_type:
- apiref
api_name:
- VmSwitchPorts
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VmSwitchPorts

\[This property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2008 R2 and Windows Server 2008:  **

Used internally by the virtual machine (VM) configuration resource type to store information about the VM network switch ports that are used by the VM. This property is set using the [CLUSCTL\_RESOURCE\_VM\_CONFIG\_UPDATE](clusctl-resource-vm-config-update.md) resource control. The following table summarizes the attributes of the **VmSwitchPorts** property.



| Attribute            | Value                                                           |
|----------------------|-----------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string containing a **GUID**<br/> |
| Access<br/>    | [Read-only](read-only-properties.md)<br/>                |
| Status<br/>    | Required<br/>                                             |
| Structure<br/> | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)<br/>                  |
| Minimum<br/>   | **NULL**<br/>                                             |
| Maximum<br/>   | see [Maximum String Size](maximum-string-size.md)<br/>   |
| Default<br/>   | **NULL**<br/>                                             |



 

## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/>       |
| End of client support<br/>    | None supported<br/>                                                       |
| End of server support<br/>    | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/> |



## See also

<dl> <dt>

[Virtual Machine Configuration Private Properties](virtual-machine-configuration-private-properties.md)
</dt> <dt>

[CLUSCTL\_RESOURCE\_VM\_CONFIG\_UPDATE](clusctl-resource-vm-config-update.md)
</dt> </dl>

 

 





