---
title: AutoBalancerLevel
description: Specifies the auto balancer level.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 817F7375-777C-4F61-A8D5-D2266675B038
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- AutoBalancerLevel
- CLUSTER_NAME_AUTO_BALANCER_LEVEL
- AutoBalancerLevel Failover Cluster
topic_type:
- apiref
api_name:
- AutoBalancerLevel
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AutoBalancerLevel

Specifies the auto balancer level.



| Attribute            | Value                                       |
|----------------------|---------------------------------------------|
| Data type<br/> | **DWORD**                                   |
| Access<br/>    | [Read/write](read-write-properties.md)     |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)   |
| Minimum<br/>   | **CLUSTER\_AUTO\_BALANCER\_LEVEL\_MIN**     |
| Maximum<br/>   | **CLUSTER\_AUTO\_BALANCER\_LEVEL\_MAX**     |
| Default<br/>   | **CLUSTER\_AUTO\_BALANCER\_LEVEL\_DEFAULT** |



 

## Remarks

The constant for this property is **CLUSTER\_NAME\_AUTO\_BALANCER\_LEVEL**.

This property can contain the following values.



| Constant                                    | Value                                    | Description                                                               |
|---------------------------------------------|------------------------------------------|---------------------------------------------------------------------------|
| **CLUSTER\_AUTO\_BALANCER\_LEVEL\_LOW**     | 1<br/>                             | Low<br/> Balance when CPU or memory load exceeds 80%.<br/>    |
| **CLUSTER\_AUTO\_BALANCER\_LEVEL\_MEDIUM**  | 2<br/>                             | Medium<br/> Balance when CPU or memory load exceeds 70%.<br/> |
| **CLUSTER\_AUTO\_BALANCER\_LEVEL\_HIGH**    | 3<br/>                             | High<br/> Balance when CPU or memory load exceeds 60%.<br/>   |
| **CLUSTER\_AUTO\_BALANCER\_LEVEL\_MIN**     | **CLUSTER\_AUTO\_BALANCER\_LEVEL\_LOW**  |                                                                           |
| **CLUSTER\_AUTO\_BALANCER\_LEVEL\_MAX**     | **CLUSTER\_AUTO\_BALANCER\_LEVEL\_HIGH** |                                                                           |
| **CLUSTER\_AUTO\_BALANCER\_LEVEL\_DEFAULT** | **CLUSTER\_AUTO\_BALANCER\_LEVEL\_LOW**  |                                                                           |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





