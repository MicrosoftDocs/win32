---
description: Adds a new analysis hint node with an infinite area to the IInkAnalyzer.
ms.assetid: 4cc592c4-456f-4aa5-9a87-d9427de487f3
title: IInkAnalyzer::CreateAnalysisHint method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.CreateAnalysisHint
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::CreateAnalysisHint method

Adds a new analysis hint node with an infinite area to the [**IInkAnalyzer**](iinkanalyzer.md).

## Syntax


```C++
HRESULT CreateAnalysisHint(
  [out] IContextNode **ppAnalysisHint
);
```



## Parameters

<dl> <dt>

*ppAnalysisHint* \[out\]
</dt> <dd>

The new analysis hint node.

</dd> </dl>

## Return value

See [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md) for a description of the return values.

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on *ppAnalysisHint* when you no longer need to use the object.

 

To provide extra context information for the [**IInkAnalyzer**](iinkanalyzer.md), you can add analysis hints to the ink analyzer. Analysis hints can improve recognition accuracy. For example, you can add factoid and guide information for fields in a form application.

This method creates a new [**IContextNode**](icontextnode.md) with a context node type of AnalysisHint (see [**IContextNode::GetType**](icontextnode-gettype.md)) and adds the new hint as a subnode of the [**IInkAnalyzer**](iinkanalyzer.md) object's root node (see [**IContextNode::GetSubNodes**](icontextnode-getsubnodes.md) and [**IInkAnalyzer::GetRootNode Method**](iinkanalyzer-getrootnode.md)).

To add context information to the hint, use [**IContextNode::AddPropertyData**](icontextnode-addpropertydata.md) with the *pPropertyDataId* parameter set to one of the [Analysis Hint Properties](analysis-hint-properties.md) constants.

If a hint is assigned an infinite area, termed a global hint, the [**IInkAnalyzer**](iinkanalyzer.md) applies the hint's context to all ink that is not within another hint's area. Multiple hints may be attached to a single **IInkAnalyzer**. However, only one global hint can be attached to a single ink analyzer, and no non-global hints can overlap. For more information about the types of context information that a hint can provide, see [Analysis Hint Properties](analysis-hint-properties.md).

Adding an analysis hint does not mark the hint's area for reanalysis. To mark the area within the hint for reanalysis, use [**IInkAnalyzer::SetDirtyRegion Method**](iinkanalyzer-setdirtyregion.md) to set the dirty region to the union of the current dirty region and area of the analysis hint.

When using hints for a form application, the application should avoid mixing text context with ink in the forms. This means for example that text field names should not be created in the analysis tree. Hints are meant to associate the ink to areas on pages; any text context interferes with this ink-to-hint association. The analysis operation may merge the ink and the text context in the same writing region which would prevent the ink from being associated with the hint area.

For more information about ink analysis, see [Ink Analysis Overview](ink-analysis-overview.md).

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
</dt> <dt>

[**IContextNode::AddPropertyData**](icontextnode-addpropertydata.md)
</dt> <dt>

[**IInkAnalyzer::DeleteAnalysisHint Method**](iinkanalyzer-deleteanalysishint.md)
</dt> <dt>

[**IInkAnalyzer::GetAnalysisHints Method**](iinkanalyzer-getanalysishints.md)
</dt> <dt>

[**IInkAnalyzer::GetAnalysisHintsByName Method**](iinkanalyzer-getanalysishintsbyname.md)
</dt> <dt>

[Analysis Hint Properties](analysis-hint-properties.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

