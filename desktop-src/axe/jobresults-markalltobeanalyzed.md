---
title: JobResults MarkAllToBeAnalyzed method
description: Sets the to be analyzed indicators for all assessment results for the job.
ms.assetid: F1FBD244-5552-4FC0-A603-6A6E41000971
keywords:
- MarkAllToBeAnalyzed method Access Execution Engine
- MarkAllToBeAnalyzed method Access Execution Engine , JobResults interface
- JobResults interface Access Execution Engine , MarkAllToBeAnalyzed method
topic_type:
- apiref
api_name:
- JobResults.MarkAllToBeAnalyzed
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# JobResults::MarkAllToBeAnalyzed method

Sets the to be analyzed indicators for all assessment results for the job.

## Syntax


```C++
virtual HRESULT MarkAllToBeAnalyzed(
  [in] BOOL analyze
) = 0;
```



## Parameters

<dl> <dt>

*analyze* \[in\]
</dt> <dd>

The indicator.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The indicator is **TRUE** if all the assessment results are to analyzed, **FALSE** if all are not to be analyzed.

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

 

 





