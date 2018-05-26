---
title: AccountName
description: Contains the account name for a Windows Azure storage account.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 52753E25-2B1F-4173-BFF8-16042682B754
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- AccountName Failover Cluster
topic_type:
- apiref
api_name:
- AccountName
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AccountName

Contains the account name for a Windows Azure storage account.



| Attribute            | Value                                                         |
|----------------------|---------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string<br/>                     |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>            |
| Structure<br/> | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)<br/>                |
| Minimum<br/>   | 0<br/>                                                  |
| Maximum<br/>   | See [Maximum String Size](maximum-string-size.md)<br/> |
| Default<br/>   | 0<br/>                                                  |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_CLOUDWITNESS\_ACCOUNT\_NAME**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cloud Witness Private Properties](cloud-witness-private-properties.md)
</dt> </dl>

 

 





