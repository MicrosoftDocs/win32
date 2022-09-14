---
description: Retrieves an array of rectangles that defines the area of the IAnalysisRegion.
ms.assetid: 40de4c27-4b3b-4db3-af08-cb53e638db6b
title: IAnalysisRegion::GetRegionScans method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAnalysisRegion.GetRegionScans
api_type: 
- COM
api_location: 
- IACom.dll
---

# IAnalysisRegion::GetRegionScans method

Retrieves an array of rectangles that defines the area of the [**IAnalysisRegion**](ianalysisregion.md).

## Syntax


```C++
HRESULT GetRegionScans(
  [out] ULONG *pulCount,
  [out] RECT  **pRegionScans
);
```



## Parameters

<dl> <dt>

*pulCount* \[out\]
</dt> <dd>

The number of rectangles returned in *pRegionScans*.

</dd> <dt>

*pRegionScans* \[out\]
</dt> <dd>

A pointer to an array of rectangles that defines the area of the [**IAnalysisRegion**](ianalysisregion.md).

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

If *pRegionScans* is passed as **NULL**, the **GetRegionScans** method returns **S\_OK** and the number of rectangles is returned in *pulCount*.

> [!Caution]  
> To avoid a memory leak, use [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) to release the memory from \**pRegionScans* when you no longer need the information.

 

The bounds of the rectangles are in ink-space coordinates.

The union of the returned rectangles represents the area of the [**IAnalysisRegion**](ianalysisregion.md).

## Examples

The following example shows how to get the rectangles that define the area of the [**IAnalysisRegion**](ianalysisregion.md), `region` and how to get only the number of rectangles.


```C++
// Get the count and the rectangles.
ULONG count = 0;
RECT* rects = 0;
region->GetRegionScans(&count, &rects);

// Use rects

::CoTaskMemFree(rects);

// GetRegionScans just gets the count and returns S_OK
ULONG number = 0;
region->GetRegionScans(&number, NULL); 
```



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

[**IAnalysisRegion::GetBounds Method**](ianalysisregion-getbounds.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

