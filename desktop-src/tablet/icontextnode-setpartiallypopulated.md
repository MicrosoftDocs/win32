---
description: Modifies the value that indicates whether this IContextNode is partially or fully populated.
ms.assetid: 4d8e1ec0-757d-4346-a77e-263bd612972b
title: IContextNode::SetPartiallyPopulated method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.SetPartiallyPopulated
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::SetPartiallyPopulated method

Modifies the value that indicates whether this [**IContextNode**](icontextnode.md) is partially or fully populated.

## Syntax


```C++
HRESULT SetPartiallyPopulated(
  [in] VARIANT_BOOL fPartiallyPopulated
);
```



## Parameters

<dl> <dt>

*fPartiallyPopulated* \[in\]
</dt> <dd>

**VARIANT\_TRUE** if this [**IContextNode**](icontextnode.md) is partially populated; otherwise, **VARIANT\_FALSE**.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

Use this method when your application maintains its own data structure, which is synchronized with that of the [**IInkAnalyzer**](iinkanalyzer.md). For more information, see [Data Proxy with Ink Analysis](data-proxy-with-ink-analysis.md).

When virtualizing your document tree, be sure to set the PropertyGuidsForContextNodes.RotatedBoundingBox value (using ContextNode.AddPropertyValue) on all ContextNode objects. The RotatedBoundingBox property is calculated by the InkAnalyzer and by default should be on all writing ContextNodes. However, if your application virtualizes the analysis results by setting the PartiallyPopulated property, when handling the PopulateContextNode event be sure to populate the RotatedBoundingBox property. Failure to set the RotatedBoundingBox property will result in potentially more document data being used in the current analysis operation

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IContextNode**](icontextnode.md)
</dt> <dt>

[**\_IAnalysisProxyEvents::PopulateContextNode**](-ianalysisproxyevents-populatecontextnode.md)
</dt> <dt>

[**IContextNode::CreatePartiallyPopulatedSubNode**](icontextnode-createpartiallypopulatedsubnode.md)
</dt> <dt>

[**IContextNode::GetPartiallyPopulated**](icontextnode-getpartiallypopulated.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




