---
description: Creates a new child IContextNode object.
ms.assetid: 35d2b641-fada-418b-9374-0303c7d318e5
title: IContextNode::CreateSubNode method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.CreateSubNode
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::CreateSubNode method

Creates a new child [**IContextNode**](icontextnode.md) object.

## Syntax


```C++
HRESULT CreateSubNode(
  [in]  const GUID         *pNodeType,
  [out]       IContextNode **ppContextNodeCreated
);
```



## Parameters

<dl> <dt>

*pNodeType* \[in\]
</dt> <dd>

A **GUID** that represents the type of [**IContextNode**](icontextnode.md) to create.

</dd> <dt>

*ppContextNodeCreated* \[out\]
</dt> <dd>

A pointer to the new [**IContextNode**](icontextnode.md).

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on \**ppContextNodeCreated* when you no longer need to use the context node.

 

The new [**IContextNode**](icontextnode.md) is added to this context node's collection of child nodes (see [**IContextNode::GetSubNodes**](icontextnode-getsubnodes.md)). When there are existing child nodes, the newly created **IContextNode** is added as the last child node.

For a list of context node types, see [Context Node Types](context-node-types.md).

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

[**IContextNode::DeleteSubNode**](icontextnode-deletesubnode.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

