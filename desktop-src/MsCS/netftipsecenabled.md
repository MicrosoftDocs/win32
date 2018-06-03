---
title: NetftIPSecEnabled
description: Specifies whether Internet Protocol Security (IPSec) encryption is enabled for inter-node cluster communication.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0F5FF8E2-BD9A-4C20-BAAB-CFB1BC6D7274
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- NetftIPSecEnabled Failover Cluster
topic_type:
- apiref
api_name:
- NetftIPSecEnabled
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NetftIPSecEnabled

Specifies whether Internet Protocol Security (IPSec) encryption is enabled for inter-node cluster communication. "0" enables IPSec, "1" disables it.



| Attribute            | Value                                     |
|----------------------|-------------------------------------------|
| Data type<br/> | **DWORD**                                 |
| Access<br/>    | [Read/write](read-write-properties.md)   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum<br/>   | 0<br/>                              |
| Maximum<br/>   | 1<br/>                              |
| Default<br/>   | 1<br/>                              |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_NETFT\_IPSEC\_ENABLED**.

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | None supported<br/>         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





