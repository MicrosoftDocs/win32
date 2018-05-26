---
title: ApplicationParams
description: The parameters to pass to a Volume Shadow Copy Service Task resource specific executable for use with the Task Scheduler V1.0 API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f3ec037d-28ed-47a8-aaef-69305865284e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ApplicationParams Failover Cluster , for Volume Shadow Copy Service Task private properties
- ApplicationParams Failover Cluster
topic_type:
- apiref
api_name:
- ApplicationParams
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ApplicationParams

The parameters to pass to a Volume Shadow Copy Service Task resource specific executable for use with the [Task Scheduler V1.0 API](https://msdn.microsoft.com/library/windows/desktop/aa383614). The following table summarizes the attributes of the **ApplicationParams** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | **DWORD**                                                        |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | 0 (Byte offset from beginning of string.)                        |



 

## Remarks

When a Volume Shadow Copy Service Task resource is brought online to a node, it will create a task using the Task Scheduler V1.0 API. When the resource goes offline, the task is deleted from the node.

## Examples


```C++
WCHAR szApplicationParamData[]  = L"Create Shadow /AutoRetry=15 /For=<volumeName>";
CLUSPROP_SZ_DECLARE(             ApplicationParamValue, 
                                 sizeof( szApplicationParamData ) / sizeof( WCHAR ) );

ApplicationParamValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
ApplicationParamValue.cbLength  = sizeof( szApplicationParamData );
StringCbCopy(                    ApplicationParamValue.sz, 
                                 ApplicationParamValue.cbLength, 
                                 szApplicationParamData );
```



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

 

 





