---
description: Determines whether the specified IAnalysisRegion contains the same value as the current IAnalysisRegion object.
ms.assetid: 44c09cfe-65fc-4175-ad05-01c605218c58
title: IAnalysisRegion::EqualsRegion method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisRegion.EqualsRegion
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisRegion::EqualsRegion method

Determines whether the specified [**IAnalysisRegion**](ianalysisregion.md) contains the same value as the current **IAnalysisRegion** object.

## Syntax


```C++
HRESULT EqualsRegion(
  [in]  IAnalysisRegion *pOtherRegion,
  [out] VARIANT_BOOL    *pfRegionsEqual
);
```



## Parameters

<dl> <dt>

*pOtherRegion* \[in\]
</dt> <dd>

The [**IAnalysisRegion**](ianalysisregion.md) object to compare with the current **IAnalysisRegion**.

</dd> <dt>

*pfRegionsEqual* \[out\]
</dt> <dd>

**VARIANT\_TRUE** if the specified [**IAnalysisRegion**](ianalysisregion.md) contains the same value as the current IAnalysisRegion; otherwise, **VARIANT\_FALSE**.

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
</dt> </dl>

 

 




