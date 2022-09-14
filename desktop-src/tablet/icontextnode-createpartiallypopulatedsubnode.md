---
description: Creates a child IContextNode object that contains only information about type, identifier, and location.
ms.assetid: 181028fb-f67c-4c90-bb09-94b68a887bd1
title: IContextNode::CreatePartiallyPopulatedSubNode method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.CreatePartiallyPopulatedSubNode
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::CreatePartiallyPopulatedSubNode method

Creates a child [**IContextNode**](icontextnode.md) object that contains only information about type, identifier, and location.

## Syntax


```C++
HRESULT CreatePartiallyPopulatedSubNode(
  [in]  const GUID            *pNodeType,
  [in]  const GUID            *pNodeId,
  [in]        IAnalysisRegion *pNodeLocation,
  [out]       IContextNode    **pPartiallyPopulatedContextNodeCreated
);
```



## Parameters

<dl> <dt>

*pNodeType* \[in\]
</dt> <dd>

The type of context node to create.

</dd> <dt>

*pNodeId* \[in\]
</dt> <dd>

The identifier for the new node.

</dd> <dt>

*pNodeLocation* \[in\]
</dt> <dd>

The location of the new node.

</dd> <dt>

*pPartiallyPopulatedContextNodeCreated* \[out\]
</dt> <dd>

A pointer to the new, partially populated [**IContextNode**](icontextnode.md).

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on \**pPartiallyPopulatedContextNodeCreated* when you no longer need to use the context node.

 

The new [**IContextNode**](icontextnode.md) is added to this context node's collection of child nodes (see [**IContextNode::GetSubNodes**](icontextnode-getsubnodes.md)). When there are existing child nodes, the newly created **IContextNode** is added as the last child node.

For more information about type, identifier, and location, see [**IContextNode::GetType**](icontextnode-gettype.md), [**IContextNode::GetId**](icontextnode-getid.md), and [**IContextNode::GetLocation**](icontextnode-getlocation.md).

This method is used for data proxy as a way to create an [**IContextNode**](icontextnode.md) object in the context node tree before all the information about it is available. For more information, see [Data Proxy with Ink Analysis](data-proxy-with-ink-analysis.md).

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

[**IAnalysisRegion**](ianalysisregion.md)
</dt> <dt>

[**IContextNode::GetPartiallyPopulated**](icontextnode-getpartiallypopulated.md)
</dt> <dt>

[Context Node Types](context-node-types.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

