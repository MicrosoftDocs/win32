---
description: Retrieves all of the analysis hint IContextNode objects that are attached to the IInkAnalyzer and that have the specified name.
ms.assetid: 15269ee0-055c-424e-be49-945f47e8a77e
title: IInkAnalyzer::GetAnalysisHintsByName method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.GetAnalysisHintsByName
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::GetAnalysisHintsByName method

Retrieves all of the analysis hint [**IContextNode**](icontextnode.md) objects that are attached to the [**IInkAnalyzer**](iinkanalyzer.md) and that have the specified name.

## Syntax


```C++
HRESULT GetAnalysisHintsByName(
  [in]  BSTR          hintName,
  [out] IContextNodes **ppAnalysisHints
);
```



## Parameters

<dl> <dt>

*hintName* \[in\]
</dt> <dd>

The hint name for which to search.

</dd> <dt>

*ppAnalysisHints* \[out\]
</dt> <dd>

The analysis hint [**IContextNode**](icontextnode.md) objects in the [**IInkAnalyzer**](iinkanalyzer.md) that have the specified name.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md) the return values.

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on *ppAnalysisHints* when you no longer need to use the object.

 

This method returns an empty collection if no such analysis hint nodes are attached to the [**IInkAnalyzer**](iinkanalyzer.md).

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

[**IInkAnalyzer::GetAnalysisHints Method**](iinkanalyzer-getanalysishints.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

