---
title: AssessmentResults GetCanBeAnalyzed method
description: Returns the cannot analyze reason for this AssessmentResults object.
ms.assetid: 409A7CD0-9A69-46E7-BE75-A1D49A10F547
keywords:
- GetCanBeAnalyzed method Access Execution Engine
- GetCanBeAnalyzed method Access Execution Engine , AssessmentResults interface
- AssessmentResults interface Access Execution Engine , GetCanBeAnalyzed method
topic_type:
- apiref
api_name:
- AssessmentResults.GetCanBeAnalyzed
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

# AssessmentResults::GetCanBeAnalyzed method

Returns the cannot analyze reason for this **AssessmentResults** object.

## Syntax


```C++
virtual HRESULT GetCanBeAnalyzed(
  [out] CannotAnalyzeReason *reason
) const = 0;
```



## Parameters

<dl> <dt>

*reason* \[out\]
</dt> <dd>

The cannot analyze reason.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

The cannot analyze reason is a member of [**CannotAnalyzeReason**](cannotanalyzereason.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**AssessmentResults**](assessmentresults-struct.md)
</dt> </dl>

 

 





