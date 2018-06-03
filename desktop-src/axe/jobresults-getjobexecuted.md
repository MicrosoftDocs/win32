---
title: JobResults GetJobExecuted method
description: Returns the Job that produced this JobResults object.
ms.assetid: 0535E7E1-A81E-4C41-A5F6-C6A92061F091
keywords:
- GetJobExecuted method Access Execution Engine
- GetJobExecuted method Access Execution Engine , JobResults interface
- JobResults interface Access Execution Engine , GetJobExecuted method
topic_type:
- apiref
api_name:
- JobResults.GetJobExecuted
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# JobResults::GetJobExecuted method

Returns the [**Job**](job-if.md) that produced this **JobResults** object.

## Syntax


```C++
virtual HRESULT GetJobExecuted(
  [out, optional] JOB **job
) = 0;
```



## Parameters

<dl> <dt>

*job* \[out, optional\]
</dt> <dd>

The **Job**.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**JobResults**](jobresults.md)
</dt> </dl>

 

 





