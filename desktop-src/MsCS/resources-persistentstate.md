---
title: PersistentState
description: Specifies whether the resource should be brought online or left offline when the Cluster service is started. The following table summarizes the attributes of the PersistentState property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bc6d9b93-4060-41d4-8ffe-a1c798c23452
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- PersistentState Failover Cluster ,for resources
- PersistentState Failover Cluster
topic_type:
- apiref
api_name:
- PersistentState
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PersistentState

Specifies whether the [resource](resources.md) should be brought online or left offline when the [Cluster service](cluster-service.md) is started. The following table summarizes the attributes of the **PersistentState** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | **FALSE**                                 |
| Maximum   | **TRUE**                                  |
| Default   | **FALSE**                                 |



 

## Remarks

The data value for the **PersistentState** property can be set to **TRUE** or **FALSE**. When **PersistentState** is set to **TRUE**, the resource is automatically brought online when the Cluster service starts. When set to **FALSE**, it is left offline.

When a resource is brought online, its **PersistentState** property is deleted from the [cluster database](cluster-database.md). Therefore, **PersistentState** should only be set when a resource is offline.

To retrieve the current state of a resource, call the [**GetClusterResourceState**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_resource_state?branch=master) function.

## Examples

The property value portion of a [property list](property-lists.md) entry for **PersistentState** can be set with the following example code:


```C++
DWORD          PersistentStateData = FALSE;
CLUSPROP_DWORD PersistentStateValue;

PersistentStateValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
PersistentStateValue.cbLength  = sizeof(DWORD);
PersistentStateValue.dw        = PersistentStateData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**GetClusterResourceState**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_resource_state?branch=master)
</dt> </dl>

 

 





