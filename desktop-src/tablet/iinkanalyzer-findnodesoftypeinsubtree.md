---
description: Retrieves all of the IContextNode objects of the specified type that are descendants of the specified IContextNode object.
ms.assetid: 7e57d6ec-fe04-44c6-904f-7a212bbfcd19
title: IInkAnalyzer::FindNodesOfTypeInSubTree method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.FindNodesOfTypeInSubTree
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::FindNodesOfTypeInSubTree method

Retrieves all of the [**IContextNode**](icontextnode.md) objects of the specified type that are descendants of the specified **IContextNode** object.

## Syntax


```C++
HRESULT FindNodesOfTypeInSubTree(
  [in]  const GUID          *pNodeType,
  [in]        IContextNode  *pContextNodeToSearchFrom,
  [out]       IContextNodes **ppContextNodesFound
);
```



## Parameters

<dl> <dt>

*pNodeType* \[in\]
</dt> <dd>

The **GUID** that specifies the node type.

</dd> <dt>

*pContextNodeToSearchFrom* \[in\]
</dt> <dd>

The [**IContextNode**](icontextnode.md) object whose descendants are searched.

</dd> <dt>

*ppContextNodesFound* \[out\]
</dt> <dd>

The [**IContextNodes**](icontextnodes.md) collection containing all nodes of type *pNodeType* that are descendants of *pContextNodeToSearchFrom*.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on *ppContextNodesFound* when you no longer need to use the object.

 

If the [**IInkAnalyzer**](iinkanalyzer.md) does not contain the *pContextNodeToSearchFrom* node, this method returns an error code.

The *pNodeType* property must contain a globally unique identifier (GUID) from the [Context Node Types](context-node-types.md) constants.

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

[**IInkAnalyzer::FindNodesOfTypeForStrokes Method**](iinkanalyzer-findnodesoftypeforstrokes.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesWithCallBack Method**](iinkanalyzer-findnodeswithcallback.md)
</dt> <dt>

[**IInkAnalyzer::FindNodesWithCallBackInSubTree Method**](iinkanalyzer-findnodeswithcallbackinsubtree.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

