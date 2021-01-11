---
description: Returns the stroke identifiers that are associated with this IAnalysisAlternate.
ms.assetid: 495d485f-0d16-4085-9213-cc55f3f259f0
title: IAnalysisAlternate::GetStrokeIds method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisAlternate.GetStrokeIds
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisAlternate::GetStrokeIds method

Returns the stroke identifiers that are associated with this [**IAnalysisAlternate**](ianalysisalternate.md).

## Syntax


```C++
HRESULT GetStrokeIds(
  [in, out] ULONG *pulStrokeIdsCount,
  [out]     LONG  **pplStrokeIds
);
```



## Parameters

<dl> <dt>

*pulStrokeIdsCount* \[in, out\]
</dt> <dd>

A pointer to a **ULONG** that is set to the number of stroke identifiers associated with this [**IAnalysisAlternate**](ianalysisalternate.md).

</dd> <dt>

*pplStrokeIds* \[out\]
</dt> <dd>

\[out, size\_is(\**pulStrokeIdsCount* \* sizeof(LONG))\]

An array of **LONG** of length *pulStrokeIdsCount* that is set to the stroke identifiers associated with this [**IAnalysisAlternate**](ianalysisalternate.md).

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, use [CoTaskMemFree](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) to release the memory from \**pplStrokeIds* when you no longer need the information.

 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IAnalysisAlternate**](ianalysisalternate.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

