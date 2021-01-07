---
description: Retrieves a value indicating whether the IAnalysisRegion represents an infinite region.
ms.assetid: b84ec9ec-42d0-4d03-b78b-433e55d04897
title: IAnalysisRegion::IsInfinite method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisRegion.IsInfinite
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisRegion::IsInfinite method

Retrieves a value indicating whether the [**IAnalysisRegion**](ianalysisregion.md) represents an infinite region.

## Syntax


```C++
HRESULT IsInfinite(
  [out] VARIANT_BOOL *pfIsInfinite
);
```



## Parameters

<dl> <dt>

*pfIsInfinite* \[out\]
</dt> <dd>

**VARIANT\_TRUE** if the represented region is infinite; otherwise, **VARIANT\_FALSE**.

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

[**IAnalysisRegion::IsEmpty Method**](ianalysisregion-isempty.md)
</dt> <dt>

[**IAnalysisRegion::MakeEmpty Method**](ianalysisregion-makeempty.md)
</dt> <dt>

[**IAnalysisRegion::MakeInfinite Method**](ianalysisregion-makeinfinite.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




