---
description: Retrieves the ink leaf nodes that contain the specified strokes.
ms.assetid: d9ebc57d-63f5-4175-8bb6-a688b98823d4
title: IInkAnalyzer::FindInkLeafNodesForStrokes method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.FindInkLeafNodesForStrokes
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::FindInkLeafNodesForStrokes method

Retrieves the ink leaf nodes that contain the specified strokes.

## Syntax


```C++
HRESULT FindInkLeafNodesForStrokes(
  [in]  ULONG         ulStrokeIdsCount,
  [in]  LONG          *plStrokeIds,
  [out] IContextNodes **ppContextNodesFound
);
```



## Parameters

<dl> <dt>

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

The collection of [**IContextNode**](icontextnode.md) objects that contain all the ink leaf nodes that contain the strokes with identifiers in the *plStrokeIds* array.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on *ppContextNodesFound* when you no longer need to use the object.

 

Leaf nodes do not contain child nodes. Ink nodes contain stroke data. Examples of ink leaf nodes are InkWord, InkDrawing, andInkBullet [**IContextNode**](icontextnode.md) objects. For more information, see [Context Node Types](context-node-types.md).

If no nodes contain the specified strokes, an empty [**IContextNodes**](icontextnodes.md) collection is returned. Similarly, if *ulStrokeIdsCount* is zero, an empty **IContextNodes** collection is returned.

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

[**IInkAnalyzer::FindLeafNodes Method**](iinkanalyzer-findleafnodes.md)
</dt> <dt>

[**IInkAnalyzer::FindNode Method**](iinkanalyzer-findnode.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesOfType Method**](iinkanalyzer-findnodesoftype.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesOfTypeForStrokes Method**](iinkanalyzer-findnodesoftypeforstrokes.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesOfTypeInSubTree Method**](iinkanalyzer-findnodesoftypeinsubtree.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesWithCallBack Method**](iinkanalyzer-findnodeswithcallback.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesWithCallBackInSubTree Method**](iinkanalyzer-findnodeswithcallbackinsubtree.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

