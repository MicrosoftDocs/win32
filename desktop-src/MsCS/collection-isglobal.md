---
title: IsGlobal
description: Indicates whether this set must be started and ready before any other sets should be started.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ACE3C43E-F10E-4D06-BC07-953FFA55FC10
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- IsGlobal Failover Cluster
topic_type:
- apiref
api_name:
- IsGlobal
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IsGlobal

Indicates whether this set must be started and ready before any other sets should be started. All sets with **IsGlobal** set to **TRUE** will be started before any set with **IsGlobal** set to **FALSE** is started.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)<br/> |
| Minimum<br/>   | (**DWORD**)**FALSE**<br/>                      |
| Maximum<br/>   | (**DWORD**)**TRUE**<br/>                       |
| Default<br/>   | (**DWORD**)**FALSE**<br/>                      |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_GROUPSET\_IS\_GLOBAL**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Groupset Common Properties](collection-common-properties.md)
</dt> </dl>

 

 





