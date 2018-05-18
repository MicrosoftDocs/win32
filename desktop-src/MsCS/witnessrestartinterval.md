---
title: WitnessRestartInterval
description: Specifies how long (in minutes) the system will wait before attempting to restart a failed file share witness resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7e90aab7-e89e-44ef-9730-28c5ded6025e'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["WitnessRestartInterval Failover Cluster , for Cluster common properties", "WitnessRestartInterval Failover Cluster"]
topic_type:
- apiref
api_name:
- WitnessRestartInterval
api_type:
- NA
---

# WitnessRestartInterval

When using a Node and File Share Majority quorum mode, specifies how long (in minutes) the system will wait before attempting to restart a failed file share witness resource. The following table summarizes the attributes of the **WitnessRestartInterval** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md)<br/> |
| Minimum<br/>   | 5 minutes<br/>                                 |
| Maximum<br/>   | 1,440 (24 hours)<br/>                          |
| Default<br/>   | 15 minutes<br/>                                |



 

## Remarks

The constant for this property is **CLUSTER\_WITNESS\_FAILED\_RESTART\_INTERVAL**.

This property is also exposed as the **WitnessRestartInterval** property of the [**MSCluster\_Cluster**](https://msdn.microsoft.com/library/aa371422) WMI class.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> <dt>

[**MSCluster\_Cluster**](https://msdn.microsoft.com/library/aa371422)
</dt> </dl>

 

 





