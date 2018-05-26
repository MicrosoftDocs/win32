---
title: FaultDomain
description: Contains the fault domains for a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: F347A607-A908-4CEC-8219-5627ADF05C2B
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- FaultDomain Failover Cluster
topic_type:
- apiref
api_name:
- FaultDomain
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# FaultDomain

Contains the fault domains for a node. A fault domain is a set of hardware components with a single point of failure, such as a rack of computers.



| Attribute            | Value                                                            |
|----------------------|------------------------------------------------------------------|
| Data type<br/> | A set of Null-terminated Unicode strings                         |
| Access<br/>    | [Read-only](read-only-properties.md)                            |
| Structure<br/> | [**CLUSPROP\_MULTI\_SZ**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_sz?branch=master)                 |
| Maximum<br/>   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default<br/>   | **NULL**                                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_NODE\_FAULT\_DOMAIN**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Node Common Properties](node-common-properties.md)
</dt> <dt>

[**FaultDomainId**](nodes-faultdomainid.md)
</dt> </dl>

 

 





