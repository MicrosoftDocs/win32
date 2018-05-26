---
title: CurrentDirectory
description: Current directory of the Volume Shadow Copy Service Task resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 37c7ab3e-2470-403b-bf65-de1792304429
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CurrentDirectory Failover Cluster , for Volume Shadow Copy Service Task private properties
- CurrentDirectory Failover Cluster
topic_type:
- apiref
api_name:
- CurrentDirectory
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CurrentDirectory

Specifies the current directory of the Volume Shadow Copy Service Task resource. The following table summarizes the attributes of the **CurrentDirectory** property.



| Attribute | Value                                                                                           |
|-----------|-------------------------------------------------------------------------------------------------|
| Data type | Null-terminated Unicode string that can contain unexpanded references to environment variables. |
| Access    | [Read/write](read-write-properties.md)                                                         |
| Status    | Optional                                                                                        |
| Format    | **CLUSPROP\_FORMAT\_EXPAND\_SZ**                                                                |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                                                             |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).)                                |
| Default   | None                                                                                            |



 

## Remarks

The [**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master) macro creates a [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) structure with an array of the correct size.

The constant for this property is **CLUSREG\_NAME\_GENAPP\_CURRENT\_DIRECTORY**.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Volume Shadow Copy Service Task Private Properties](volume-shadow-copy-service-task-private-properties.md)
</dt> <dt>

[Task Scheduler V1.0 API](https://msdn.microsoft.com/library/windows/desktop/aa383614)
</dt> </dl>

 

 





