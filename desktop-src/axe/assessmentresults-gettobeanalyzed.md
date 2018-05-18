---
title: AssessmentResults GetToBeAnalyzed method
description: Returns the indicator of whether the assessment results are to be analyzed.
ms.assetid: 'D9636B07-8F39-4266-8F8A-1606293B5F87'
keywords: ["GetToBeAnalyzed method Access Execution Engine", "GetToBeAnalyzed method Access Execution Engine , AssessmentResults interface", "AssessmentResults interface Access Execution Engine , GetToBeAnalyzed method"]
topic_type:
- apiref
api_name:
- AssessmentResults.GetToBeAnalyzed
api_location:
- AxeCore.dll
api_type:
- COM
---

# AssessmentResults::GetToBeAnalyzed method

Returns the indicator of whether the assessment results are to be analyzed.

## Syntax


```C++
virtual HRESULT GetToBeAnalyzed(
  [out] BOOL *analyze
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

The indicator is **TRUE** if the assessment results are to be analyzed, **FALSE** otherwise.

Set this indicator with [**SetToBeAnalyzed**](assessmentresults-settobeanalyzed.md).

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

 

 





