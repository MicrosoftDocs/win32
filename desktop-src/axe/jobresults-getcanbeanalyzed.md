---
title: JobResults GetCanBeAnalyzed method
description: Returns an indicator of whether the job results can be analyzed.
ms.assetid: F0EF1A0F-786B-4D14-B054-883E60DBFD88
keywords:
- GetCanBeAnalyzed method Access Execution Engine
- GetCanBeAnalyzed method Access Execution Engine , JobResults interface
- JobResults interface Access Execution Engine , GetCanBeAnalyzed method
topic_type:
- apiref
api_name:
- JobResults.GetCanBeAnalyzed
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

# JobResults::GetCanBeAnalyzed method

Returns an indicator of whether the job results can be analyzed.

## Syntax


```C++
virtual HRESULT GetCanBeAnalyzed(
  [out] BOOL *analyze
) const = 0;
```



## Parameters

<dl> <dt>

*analyze* \[out\]
</dt> <dd>

The indicator.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The indicator is **TRUE** if the job results can be analyzed, **FALSE** otherwise. The job results can be analyzed if any of the assessments in the job supports re-analysis. An assessment supports re-analysis if its manifest contains the [**AnalyzeFolder**](analyzefolder.md) element.

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

 

 





