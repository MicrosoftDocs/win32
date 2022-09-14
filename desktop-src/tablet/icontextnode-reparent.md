---
description: Moves this IContextNode object from its parent context node's collection of subnodes to the specified context node's collection of subnodes.
ms.assetid: e19ecbe3-f7aa-499c-86a1-236dc9056fd9
title: IContextNode::Reparent method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.Reparent
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::Reparent method

Moves this [**IContextNode**](icontextnode.md) object from its parent context node's collection of subnodes to the specified context node's collection of subnodes.

## Syntax


```C++
HRESULT Reparent(
  [in] IContextNode *pNewParent
);
```



## Parameters

<dl> <dt>

*pNewParent* \[in\]
</dt> <dd>

The new parent node for this [**IContextNode**](icontextnode.md) object.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

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

[**IContextNode::GetParentNode**](icontextnode-getparentnode.md)
</dt> <dt>

[**IContextNode::GetSubNodes**](icontextnode-getsubnodes.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




