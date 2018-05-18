---
title: AssessmentResults SetToBeAnalyzed method
description: Sets the indicator of whether the assessment results are to be analyzed.
ms.assetid: '539946DA-2601-4AAE-8CB7-86A97FA33551'
keywords: ["SetToBeAnalyzed method Access Execution Engine", "SetToBeAnalyzed method Access Execution Engine , AssessmentResults interface", "AssessmentResults interface Access Execution Engine , SetToBeAnalyzed method"]
topic_type:
- apiref
api_name:
- AssessmentResults.SetToBeAnalyzed
api_location:
- AxeCore.dll
api_type:
- COM
---

# AssessmentResults::SetToBeAnalyzed method

Sets the indicator of whether the assessment results are to be analyzed.

## Syntax


```C++
virtual HRESULT SetToBeAnalyzed(
  [in] BOOL analyze
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

The indicator is **TRUE** if the assessment results are to be analyzed, **FALSE** otherwise.

Get this indicator with [**GetToBeAnalyzed**](assessmentresults-gettobeanalyzed.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**AssessmentResults**](assessmentresults-struct.md)
</dt> </dl>

 

 





