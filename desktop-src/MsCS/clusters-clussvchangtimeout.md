---
title: ClusSvcHangTimeout
description: Controls the amount of time, in seconds, that the cluster network driver waits between Failover Cluster Service heartbeats before it determines that the Failover Cluster Service has stopped responding.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 88AD4C48-2DFE-4F67-B2F8-BA147DD64D09
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusSvcHangTimeout Failover Cluster
topic_type:
- apiref
api_name:
- ClusSvcHangTimeout
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusSvcHangTimeout

Controls the amount of time, in seconds, that the cluster network driver waits between Failover Cluster Service heartbeats before it determines that the Failover Cluster Service has stopped responding.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 6                                         |
| Maximum   | 0xFFFFFFFF                                |
| Default   | 60                                        |



 

## Remarks

The constant for this property is **CLUSTER\_HANG\_TIMEOUT\_KEYNAME**.

## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 Enterprise, Windows Server 2008 R2 Datacenter<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





