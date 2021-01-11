---
description: Retrieves the region of the document that corresponds to changes that were made in the IInkAnalyzer object's context node tree as a result of ink analysis.
ms.assetid: 25d511fb-ba2d-4c46-8a8c-8bb4187c9a5c
title: IAnalysisStatus::GetAppliedChangesRegion method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisStatus.GetAppliedChangesRegion
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisStatus::GetAppliedChangesRegion method

Retrieves the region of the document that corresponds to changes that were made in the [**IInkAnalyzer**](iinkanalyzer.md) object's context node tree as a result of ink analysis.

## Syntax


```C++
HRESULT GetAppliedChangesRegion(
  [out] IAnalysisRegion **pAppliedChangesRegion
);
```



## Parameters

<dl> <dt>

*pAppliedChangesRegion* \[out\]
</dt> <dd>

A pointer to the [**IAnalysisRegion**](ianalysisregion.md) of the document where changes were made.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on \**pAppliedChangesRegion* when you no longer need to use the analysis region.

 

This method is most frequently used when the application receives information for debugging purposes and needs to invalidate the area where changes might occur so that the debugging information is painted.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IAnalysisStatus**](ianalysisstatus.md)
</dt> <dt>

[**IAnalysisRegion**](ianalysisregion.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

