---
description: Retrieves all of the IContextNode objects of the specified type that contain the specified strokes.
ms.assetid: c674a03b-841c-4a9c-8268-302bc4038934
title: IInkAnalyzer::FindNodesOfTypeForStrokes method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.FindNodesOfTypeForStrokes
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::FindNodesOfTypeForStrokes method

Retrieves all of the [**IContextNode**](icontextnode.md) objects of the specified type that contain the specified strokes.

## Syntax


```C++
HRESULT FindNodesOfTypeForStrokes(
  [in]  const GUID          *pNodeType,
  [in]        ULONG         ulStrokeIdsCount,
  [in]        LONG          *plStrokeIds,
  [out]       IContextNodes **ppContextNodesFound
);
```



## Parameters

<dl> <dt>

*pNodeType* \[in\]
</dt> <dd>

The globally unique identifier (GUID) that specifies the node type.

</dd> <dt>

*ulStrokeIdsCount* \[in\]
</dt> <dd>

The number of stroke identifiers passed in.

</dd> <dt>

*plStrokeIds* \[in\]
</dt> <dd>

An array of the stroke identifiers.

</dd> <dt>

*ppContextNodesFound* \[out\]
</dt> <dd>

The collection of [**IContextNode**](icontextnode.md) objects that contain all the nodes of type *pNodeType* that contain the strokes with identifiers in the *plStrokeIds* array.

</dd> </dl>

## Return value

For a description of return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on \**ppContextNodesFound* when you no longer need to use the object.

 

The *pNodeType* property must contain a GUID from the [Context Node Types](context-node-types.md) constants.

If the specified node type is not a leaf node, but one of the node's descendants references a stroke in the strokes collection, that node is added to the collection that is returned.

If the [**IInkAnalyzer**](iinkanalyzer.md) contains no such [**IContextNode**](icontextnode.md), an empty [**IContextNodes**](icontextnodes.md) collection is returned.

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

[**IInkAnalyzer::FindInkLeafNodes Method**](iinkanalyzer-findinkleafnodes.md)
</dt> <dt>

[**IInkAnalyzer::FindInkLeafNodesForStrokes Method**](iinkanalyzer-findinkleafnodesforstrokes.md)
</dt> <dt>

[**IInkAnalyzer::FindLeafNodes Method**](iinkanalyzer-findleafnodes.md)
</dt> <dt>

[**IInkAnalyzer::FindNode Method**](iinkanalyzer-findnode.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesOfType Method**](iinkanalyzer-findnodesoftype.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesOfTypeInSubTree Method**](iinkanalyzer-findnodesoftypeinsubtree.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesWithCallBack Method**](iinkanalyzer-findnodeswithcallback.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesWithCallBackInSubTree Method**](iinkanalyzer-findnodeswithcallbackinsubtree.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

