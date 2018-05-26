---
title: JobResults GetToBeAnalyzedCount method
description: Returns the count of assessment results to be analyzed for the job.
ms.assetid: 450D918B-6C76-4D37-9227-6C3D1D0281BC
keywords:
- GetToBeAnalyzedCount method Access Execution Engine
- GetToBeAnalyzedCount method Access Execution Engine , JobResults interface
- JobResults interface Access Execution Engine , GetToBeAnalyzedCount method
topic_type:
- apiref
api_name:
- JobResults.GetToBeAnalyzedCount
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

# JobResults::GetToBeAnalyzedCount method

Returns the count of assessment results to be analyzed for the job.

## Syntax


```C++
virtual HRESULT GetToBeAnalyzedCount(
  [out] INT *analyzeCount
) const = 0;
```



## Parameters

<dl> <dt>

*analyzeCount* \[out\]
</dt> <dd>

The count.

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

 

 





