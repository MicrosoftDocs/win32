---
title: CheckHeartbeat
description: Indicates whether the heartbeat of the VM should be used to determine the health of the VM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a9c61a77-668f-407f-a8f5-6b9b22234431
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CheckHeartbeat Failover Cluster ,for virtual machines
- CheckHeartbeat Failover Cluster
topic_type:
- apiref
api_name:
- CheckHeartbeat
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CheckHeartbeat

Indicates whether the heartbeat of the virtual machine (VM) should be used to determine the health of the VM. To enable the **CheckHeartbeat** property, the Heartbeat Integration Component must be installed in the guest VM. The following table summarizes the attributes of the **CheckHeartbeat** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Required                                  |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 0                                         |
| Maximum   | 1                                         |
| Default   | 0                                         |



 

## Remarks

The following table summarizes the values for **CheckHeartbeat**.



| Name                             | Value                  | Description                                                                                  |
|----------------------------------|------------------------|----------------------------------------------------------------------------------------------|
| Don't Check Heartbeat<br/> | 0 (Default)<br/> | The heartbeat is not checked.<br/>                                                     |
| Check Heartbeat<br/>       | 1<br/>           | The heartbeat is checked; if the heartbeat fails, a resource failure is signaled.<br/> |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **CheckHeartbeat** can be set with the following example code.


```C++
DWORD          CheckHeartbeatData = 1;
CLUSPROP_DWORD CheckHeartbeatValue;

CheckHeartbeatValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
CheckHeartbeatValue.cbLength  = sizeof(DWORD);
CheckHeartbeatValue.dw        = CheckHeartbeatData;
```



## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/> |



## See also

<dl> <dt>

[Virtual Machine Private Properties](virtual-machine-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





