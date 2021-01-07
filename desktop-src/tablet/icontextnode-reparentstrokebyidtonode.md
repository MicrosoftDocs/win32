---
description: Moves stroke data from this IContextNode to the specified IContextNode.
ms.assetid: 583f2de9-d32e-4177-83d1-4abbd0f9f960
title: IContextNode::ReparentStrokeByIdToNode method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.ReparentStrokeByIdToNode
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::ReparentStrokeByIdToNode method

Moves stroke data from this [**IContextNode**](icontextnode.md) to the specified **IContextNode**.

## Syntax


```C++
HRESULT ReparentStrokeByIdToNode(
  [in] LONG         lStrokeId,
  [in] IContextNode *pContextNodeDestination
);
```



## Parameters

<dl> <dt>

*lStrokeId* \[in\]
</dt> <dd>

The identifier of the stroke to move.

</dd> <dt>

*pContextNodeDestination* \[in\]
</dt> <dd>

The [**IContextNode**](icontextnode.md) object to which to move the stroke data.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

The specified [**IContextNode**](icontextnode.md) object must be one of the following types from the [Context Node Types](context-node-types.md) constants: **InkWord**, **InkDrawing**, **InkBullet**, or **UnclassifiedInk**. Attempting to move a stroke to any other type of **IContextNode** object results in a return value of **E\_INVALIDARG**.

This method can be called from any [**IContextNode**](icontextnode.md) object, including non-ink leaf **IContextNode** objects. The specified stroke must be referenced by one of the descendants of this **IContextNode** object or **E\_INVALIDARG** is returned.

If either this [**IContextNode**](icontextnode.md) or the **IContextNode** in *pContextNodeDestination* is confirmed, **E\_INVALIDARG** is returned (see [**IContextNode::IsConfirmed**](icontextnode-isconfirmed.md)).

The ink analyzer does not delete empty context nodes from its results tree in response to this method.

-   An ink leaf node that does not reference any stroke data is an empty node.
-   A container node that does not reference any child nodes is an empty node.

An empty node generates errors if it is in the tree during an ink analysis operation. To remove a node from the ink analyzer's tree, call the parent node's [**IContextNode::DeleteSubNode**](icontextnode-deletesubnode.md) method (see [**IContextNode::GetParentNode**](icontextnode-getparentnode.md)).

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

[**IContextNode::SetStrokes**](icontextnode-setstrokes.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




