---
title: JobCompletionTimeout
description: Indicates the number of milliseconds before a pending job is deleted from the Print Spooler resource queue.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9099210a-64cc-46bc-8d58-d67e0f9b18ed
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- JobCompletionTimeout Failover Cluster ,for print spoolers
- JobCompletionTimeout Failover Cluster
topic_type:
- apiref
api_name:
- JobCompletionTimeout
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# JobCompletionTimeout

Indicates the number of milliseconds before a pending job is deleted from the [Print Spooler](print-spooler.md) resource queue. The following table summarizes the attributes of the **JobCompletionTimeout** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 0xFFFFFFFF                                |
| Default   | 0                                         |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **JobCompletionTimeout** can be set with the following example code.


```C++
DWORD          JobCompletionTimeOutData = 200;
CLUSPROP_DWORD JobCompletionTimeOutValue;

JobCompletionTimeOutValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
JobCompletionTimeOutValue.cbLength = sizeof(DWORD);
JobCompletionTimeOutValue.dw = JobCompletionTimeOutData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[Print Spooler Private Properties](print-spooler-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





