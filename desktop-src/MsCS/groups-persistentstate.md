---
title: PersistentState
description: Specifies whether a group should be automatically brought online when the cluster forms. The following table summarizes the attributes of the PersistentState property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f5c059f6-5b18-456f-b961-b111be920278'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["PersistentState Failover Cluster ,for groups", "PersistentState Failover Cluster"]
topic_type:
- apiref
api_name:
- PersistentState
api_type:
- NA
---

# PersistentState

Specifies whether a [group](groups.md) should be automatically brought online when the [*cluster*](c-gly.md#-wolf-cluster-gly) forms. The following table summarizes the attributes of the **PersistentState** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | **FALSE** (0)                             |
| Maximum   | **TRUE** (1)                              |
| Default   | **FALSE**                                 |



 

## Remarks

Set **PersistentState** to **TRUE** (1) for any group that should be automatically brought online when the cluster forms (for information on the form/join process, see [Nodes](nodes.md)). The default value is **FALSE** (0) which means that the group is left offline when the cluster forms.

[Resources](resources.md) use their group's **PersistentState** property when they lack a value for their own [**PersistentState**](resources-persistentstate.md) property.

## Examples

The property value portion of a [property list](property-lists.md) entry for **PersistentState** can be set with the following example code.


```C++
DWORD PersistentStateData = FALSE;
CLUSPROP_DWORD PersistentStateValue;

PersistentStateValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
PersistentStateValue.cbLength = sizeof(DWORD);
PersistentStateValue.dw = PersistentStateData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> <dt>

[**PersistentState**](resources-persistentstate.md)
</dt> </dl>

 

 





