---
title: AddEvictDelay
description: Specifies how many seconds after a node is evicted that the failover cluster service will wait before adding a new node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4de1dddd-ee4b-4770-8ff0-42aa0ae22e91'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["AddEvictDelay Failover Cluster ,for clusters", "AddEvictDelay Failover Cluster ,for failover clusters", "AddEvictDelay Failover Cluster"]
topic_type:
- apiref
api_name:
- AddEvictDelay
api_type:
- NA
---

# AddEvictDelay

Specifies how many seconds after a node is evicted that the failover cluster service will wait before adding a new node. The following table summarizes the attributes of the **AddEvictDelay** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 600<br/>                                       |
| Default<br/>   | 60<br/>                                        |



 

## Remarks

This property is also exposed as the **AddEvictDelay** property of the [**MSCluster\_Cluster**](https://msdn.microsoft.com/library/aa371422) WMI class.

The constant for this property is **CLUSTER\_ADD\_EVICT\_DELAY**.

## Examples

The property value portion of a [property list](property-lists.md) entry for **AddEvictDelay** can be set with with the following example code:


```C++
CLUSPROP_DWORD AddEvictDelayValue;

AddEvictDelayValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
AddEvictDelayValue.cbLength  = sizeof(DWORD);
AddEvictDelayValue.dw        = 15;
```



## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 Enterprise, Windows Server 2008 R2 Datacenter<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> <dt>

[**MSCluster\_Cluster**](https://msdn.microsoft.com/library/aa371422)
</dt> </dl>

 

 





