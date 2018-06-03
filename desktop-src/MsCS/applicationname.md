---
title: ApplicationName
description: Name and path of a Volume Shadow Copy Service Task resource specific executable, formated for use with the Task Scheduler V1.0 API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a55517f4-b2bd-4dd9-b73d-f0843f1320c4
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ApplicationName Failover Cluster , for Volume Shadow Copy Service Task private properties
- ApplicationName Failover Cluster
topic_type:
- apiref
api_name:
- ApplicationName
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ApplicationName

Name and path of a Volume Shadow Copy Service Task resource specific executable, formated for use with the [Task Scheduler V1.0 API](https://msdn.microsoft.com/library/windows/desktop/aa383614). The following table summarizes the attributes of the **ApplicationName** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

When a Volume Shadow Copy Service Task resource is brought online to a node, it will create a task using the Task Scheduler V1.0 API. When the resource goes offline, the task is deleted from the node.

The [**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare) macro creates a [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/) structure with an array of the correct size.

The constant for this property is **CLUSREG\_NAME\_VSSTASK\_APPNAME**.

## Examples


```C++
WCHAR szApplicationNameData[]  = L"%systemroot%\\system32\\vssadmin.exe";
CLUSPROP_SZ_DECLARE( ApplicationNameValue, 
                     sizeof( szApplicationNameData ) / sizeof( WCHAR ) );

ApplicationNameValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
ApplicationNameValue.cbLength  = sizeof( szApplicationNameData );
StringCbCopy(                    ApplicationNameValue.sz, 
                                 ApplicationNameValue.cbLength, 
                                 szApplicationNameData );
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

 

 





