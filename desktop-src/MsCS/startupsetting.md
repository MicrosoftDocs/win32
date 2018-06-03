---
title: StartupSetting
description: Startup setting.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0EEF5C78-61C8-4316-976F-EE2495E4CFB5
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- StartupSetting Failover Cluster
topic_type:
- apiref
api_name:
- StartupSetting
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StartupSetting

Startup setting.



| Attribute | Value                                            |
|-----------|--------------------------------------------------|
| Data type | **DWORD**                                        |
| Access    | [Read/write](read-write-properties.md)          |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)        |
| Minimum   | **GROUPSET\_READY\_SETTING\_DELAY**              |
| Maximum   | **GROUPSET\_READY\_SETTING\_APPLICATION\_READY** |
| Default   | **GROUPSET\_READY\_SETTING\_DELAY**              |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_GROUPSET\_STARTUP\_SETTING**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Groupset Common Properties](collection-common-properties.md)
</dt> </dl>

 

 





