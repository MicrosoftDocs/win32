---
title: ShutdownAction
description: Defines the action performed on the VM resource instance when actions outside of the cluster cause the VM to stop running.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f3acdf7f-a73f-498f-bd25-68d025860e17'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ShutdownAction Failover Cluster ,for virtual machines", "ShutdownAction Failover Cluster"]
topic_type:
- apiref
api_name:
- ShutdownAction
api_type:
- NA
---

# ShutdownAction

Defines the action performed on the virtual machine (VM) resource instance when actions outside the cluster (such as stopping the VM through the Hyper-V Manager or a shutdown of the operating system running in the VM) cause the VM to stop running. The following table summarizes the attributes of the **ShutdownAction** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Required                                  |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0                                         |
| Maximum   | 1                                         |
| Default   | 0                                         |



 

## Remarks

The following table summarizes the values for **ShutdownAction**.



| Name                        | Value                  | Description                                                                                                                                                                                                                                                                                                                                                            |
|-----------------------------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Offline resource<br/> | 0 (Default)<br/> | The VM resource instance is taken offline.<br/>                                                                                                                                                                                                                                                                                                                  |
| Fail resource<br/>    | 1<br/>           | The resource instance is marked as failed. The cluster service will respond to the failure based on the restart policy that is configured for the resource instance. Possible responses include attempting to restart the VM on the current node, failing over the VM to another node of the cluster, or leaving the resource instance in the failed state.<br/> |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **ShutdownAction** can be set with the following example code.


```C++
DWORD          ShutdownActionData = 1;
CLUSPROP_DWORD ShutdownActionValue;

ShutdownActionValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
ShutdownActionValue.cbLength  = sizeof(DWORD);
ShutdownActionValue.dw        = ShutdownActionData;
```



## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/> |



## See also

<dl> <dt>

[Virtual Machine Private Properties](virtual-machine-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





