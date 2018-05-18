---
title: FixQuorum
description: Specifies if the cluster is in a fix quorum state.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fd67e278-d8a0-492a-b573-434b80a8e6d6'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["FixQuorum Failover Cluster ,for clusters", "FixQuorum Failover Cluster ,for failover clusters", "FixQuorum Failover Cluster"]
topic_type:
- apiref
api_name:
- FixQuorum
api_type:
- NA
---

# FixQuorum

Specifies if the cluster is in a fix quorum state. The following table summarizes the attributes of the **FixQuorum** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read-only](read-only-properties.md)<br/>     |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 1 (fix quorum state)<br/>                      |
| Default<br/>   | 0<br/>                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_FIXQUORUM**.

This property is also exposed as the **FixQuorum** property of the [**MSCluster\_Cluster**](https://msdn.microsoft.com/library/aa371422) WMI class.

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

 

 





