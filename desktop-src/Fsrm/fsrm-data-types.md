---
title: FSRM Data Types
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1c54a6b5-d12f-4e47-acf4-2b78c399eee5
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
description: 
keywords:
- FSRM_OBJECT_ID
- FSRM_QUOTA_THRESHOLD
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FSRM Data Types

File Server Resource Manager (FSRM) defines the following data types:


```C++
typedef GUID FSRM_OBJECT_ID;
typedef long FSRM_QUOTA_THRESHOLD;
```



<dl> <dt>

**FSRM\_OBJECT\_ID**
</dt> <dd>

Identifies an FSRM storage object.

</dd> <dt>

**FSRM\_QUOTA\_THRESHOLD**
</dt> <dd>

Defines the percentage of disk space used, as a whole number, at which matching or exceeding will trigger actions associated with the threshold.

</dd> </dl>

## Requirements



|                                     |                                                                                                                                                                                                                                                                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                                                                                                                                                                                                                                          |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                                                                                                                                                                                                                                                     |
| Header<br/>                   | <dl> <dt>FsrmEnums.h (For **FSRM\_OBJECT\_ID**) (include Fsrm.h, FsrmPipeline.h, FsrmQuota.h, FsrmReports.h, FsrmScreen.h, or FsrmTlb.h); </dt> <dt>FsrmQuota.h (For **FSRM\_QUOTA\_THRESHOLD**) (include FsrmTlb.h)</dt> </dl> |



 

 





