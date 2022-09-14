---
description: Gets all of the analysis hint IContextNode objects that are attached to the IInkAnalyzer.
ms.assetid: 97cff025-3d9e-4137-b1ac-635153804744
title: IInkAnalyzer::GetAnalysisHints method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.GetAnalysisHints
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::GetAnalysisHints method

Gets all of the analysis hint [**IContextNode**](icontextnode.md) objects that are attached to the [**IInkAnalyzer**](iinkanalyzer.md).

## Syntax


```C++
HRESULT GetAnalysisHints(
  [out] IContextNodes **ppAnalysisHints
);
```



## Parameters

<dl> <dt>

*ppAnalysisHints* \[out\]
</dt> <dd>

A pointer to all the analysis hint [**IContextNode**](icontextnode.md) objects in the [**IInkAnalyzer**](iinkanalyzer.md).

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on *ppAnalysisHints* when you no longer need to use the object.

 

This method returns an empty collection if no analysis hint nodes are attached to the [**IInkAnalyzer**](iinkanalyzer.md).

An analysis hint node is an [**IContextNode**](icontextnode.md) with a context node type of AnalysisHint (see [**IContextNode::GetType**](icontextnode-gettype.md) and [Context Node Types](context-node-types.md)).

To add context information to the hint, use [**IContextNode::AddPropertyData**](icontextnode-addpropertydata.md) with the *pPropertyDataId* parameter set to one of the globally unique identifiers (GUIDs) in the [Analysis Hint Properties](analysis-hint-properties.md) constants.

To find which property values are set on a context node, use [**IContextNode::GetPropertyDataIds**](icontextnode-getpropertydataids.md). To find the value of a property, use [**IContextNode::GetPropertyData**](icontextnode-getpropertydata.md).

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

[**IContextNode**](icontextnode.md)
</dt> <dt>

[**IInkAnalyzer::CreateAnalysisHint Method**](iinkanalyzer-createanalysishint.md)
</dt> <dt>

[**IInkAnalyzer::DeleteAnalysisHint Method**](iinkanalyzer-deleteanalysishint.md)
</dt> <dt>

[**IInkAnalyzer::GetAnalysisHintsByName Method**](iinkanalyzer-getanalysishintsbyname.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

