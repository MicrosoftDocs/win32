---
title: BackupInProgress
description: Indicates whether or not a Volume Shadow Copy Service Task is currently in progress for a specific volume on the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e0c72dac-91de-4f78-9faa-0ea9fbed6387
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- BackupInProgress Failover Cluster , for Cluster common properties
- BackupInProgress Failover Cluster
topic_type:
- apiref
api_name:
- BackupInProgress
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# BackupInProgress

Indicates whether or not a Volume Shadow Copy Service Task is currently in progress for a specific volume on the cluster. The following table summarizes the attributes of the **BackupInProgress** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 0                                         |
| Maximum   | 1                                         |
| Default   | 0                                         |



 

## Remarks

The constant for this property is **CLUSTER\_CSA\_VSS\_STATE**.

## Examples

The property value portion of a property list entry for **BackupInProgress** can be set with the following example code.


```C++
CLUSPROP_DWORD BackupInProgressValue;
BackupInProgressValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
BackupInProgressValue.cbLength = sizeof(DWORD);
BackupInProgressValue.dw = 0;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





