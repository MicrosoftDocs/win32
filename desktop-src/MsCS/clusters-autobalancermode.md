---
title: AutoBalancerMode
description: The auto balancer mode.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5283E07F-E44B-4C23-96AA-ADF622DB7A28
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- AutoBalancerMode
- CLUSTER_NAME_AUTO_BALANCER_MODE
- AutoBalancerMode Failover Cluster
topic_type:
- apiref
api_name:
- AutoBalancerMode
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AutoBalancerMode

The auto balancer mode.



| Attribute            | Value                                     |
|----------------------|-------------------------------------------|
| Data type<br/> | **DWORD**                                 |
| Access<br/>    | [Read/write](read-write-properties.md)   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum<br/>   | **CLUSTER\_AUTO\_BALANCER\_MIN**          |
| Maximum<br/>   | **CLUSTER\_AUTO\_BALANCER\_LEVEL\_MAX**   |
| Default<br/>   | **CLUSTER\_AUTO\_BALANCER\_DEFAULT**      |



 

## Remarks

The constant for this property is **c**.

This property can contain the following values.



| Constant                             | Value                                | Description                                           |
|--------------------------------------|--------------------------------------|-------------------------------------------------------|
| **CLUSTER\_AUTO\_BALANCER\_DISABLE** | 0<br/>                         | Disabled<br/>                                   |
| **CLUSTER\_AUTO\_BALANCER\_NODEUP**  | 1<br/>                         | Balance on node join only.<br/>                 |
| **CLUSTER\_AUTO\_BALANCER\_ALWAYS**  | 2<br/>                         | Balance on node join and every 30 minutes.<br/> |
| **CLUSTER\_AUTO\_BALANCER\_MIN**     | **CLUSTER\_AUTO\_BALANCER\_DISABLE** |                                                       |
| **CLUSTER\_AUTO\_BALANCER\_DEFAULT** | **CLUSTER\_AUTO\_BALANCER\_ALWAYS**  |                                                       |
| **CLUSTER\_AUTO\_BALANCER\_MAX**     | **CLUSTER\_AUTO\_BALANCER\_ALWAYS**  |                                                       |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





