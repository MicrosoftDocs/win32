---
title: DisableGroupPreferredOwnerRandomization
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d8649f3e-be70-4e8e-a13f-5f1ff09fce9f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DisableGroupPreferredOwnerRandomization Failover Cluster ,for clusters
- DisableGroupPreferredOwnerRandomization Failover Cluster
topic_type:
- apiref
api_name:
- DisableGroupPreferredOwnerRandomization
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DisableGroupPreferredOwnerRandomization

\[This property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2008 R2, Windows Server 2008 and Windows Server 2003:  **

Controls whether the [*cluster*](c-gly.md#-wolf-cluster-gly) service randomizes its internal list of available [nodes](nodes.md) in the event of a group failover event.



| Attribute | Value                                                                                                               |
|-----------|---------------------------------------------------------------------------------------------------------------------|
| Data type | **DWORD**                                                                                                           |
| Access    | [Read/write](read-write-properties.md)                                                                             |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)                                                                           |
| Minimum   | FALSE (0). The cluster service selects a node at random when a group failover event occurs.                         |
| Maximum   | TRUE (1). The cluster service selects a node in order of the internal node list when a group failover event occurs. |
| Default   | **FALSE**                                                                                                           |



 

## Remarks

If a preferred owner list for resource groups is not specified, the cluster service randomizes the list it keeps internally to describe which node is selected for use when a group failover event occurs. If an ordered list is required for failover, this property should be set to true to disable this randomization

## Examples

The property value portion of a [property list](property-lists.md) entry for **EnableEventLogReplication** can be set with the following example code:


```C++
CLUSPROP_DWORD PropertyValue;
PropertyValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
PropertyValue.cbLength = sizeof(DWORD);
PropertyValue.dw = TRUE;
```



## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2003 Enterprise, Windows Server 2003 Datacenter<br/>       |
| End of client support<br/>    | None supported<br/>                                                       |
| End of server support<br/>    | Windows Server 2008 R2 Enterprise, Windows Server 2008 R2 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





