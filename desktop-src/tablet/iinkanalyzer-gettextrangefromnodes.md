---
description: Finds the text range in the recognized string that corresponds to a collection of IContextNode objects.
ms.assetid: 2c5bc4a1-08de-4872-b552-6d22924ce2a8
title: IInkAnalyzer::GetTextRangeFromNodes method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.GetTextRangeFromNodes
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::GetTextRangeFromNodes method

Finds the text range in the recognized string that corresponds to a collection of [**IContextNode**](icontextnode.md) objects.

## Syntax


```C++
HRESULT GetTextRangeFromNodes(
  [out] LONG          *plStart,
  [out] LONG          *plLength,
  [in]  IContextNodes *pNodesToSearch
);
```



## Parameters

<dl> <dt>

*plStart* \[out\]
</dt> <dd>

A 32-bit signed integer that indicates the start of the text range. This parameter is passed uninitialized.

</dd> <dt>

*plLength* \[out\]
</dt> <dd>

A 32-bit signed integer that indicates the length of the text range. This parameter is passed uninitialized.

</dd> <dt>

*pNodesToSearch* \[in\]
</dt> <dd>

The collection of [**IContextNode**](icontextnode.md) objects for which to find the text range.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

If *pNodesToSearch* contains [**IContextNode**](icontextnode.md) objects that are not adjacent, this method returns the smallest text range that covers all of the **IContextNode** objects.

This method throws an E\_INVALIDARG exception when *pNodesToSearch* contains an [**IContextNode**](icontextnode.md) that is not associated with the [**IInkAnalyzer**](iinkanalyzer.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IInkAnalyzer**](iinkanalyzer.md)
</dt> </dl>

 

 




