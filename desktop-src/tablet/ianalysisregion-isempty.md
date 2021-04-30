---
description: Retrieves a value indicating whether the IAnalysisRegion represents an empty region.
ms.assetid: 3a536b01-e7ee-4103-88c4-d83377ea9fdb
title: IAnalysisRegion::IsEmpty method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisRegion.IsEmpty
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisRegion::IsEmpty method

Retrieves a value indicating whether the [**IAnalysisRegion**](ianalysisregion.md) represents an empty region.

## Syntax


```C++
HRESULT IsEmpty(
  [out] VARIANT_BOOL *pfIsEmpty
);
```



## Parameters

<dl> <dt>

*pfIsEmpty* \[out\]
</dt> <dd>

**VARIANT\_TRUE** if the represented region is empty; otherwise, **VARIANT\_FALSE**.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IAnalysisRegion**](ianalysisregion.md)
</dt> <dt>

[**IAnalysisRegion::IsInfinite Method**](ianalysisregion-isinfinite.md)
</dt> <dt>

[**IAnalysisRegion::MakeEmpty Method**](ianalysisregion-makeempty.md)
</dt> <dt>

[**IAnalysisRegion::MakeInfinite Method**](ianalysisregion-makeinfinite.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




