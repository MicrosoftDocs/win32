---
description: Reorders a specified child IContextNode object to the specified index.
ms.assetid: 1cee73af-8d5b-4d5d-bc67-a3ac6f4b2462
title: IContextNode::MoveSubNodeToPosition method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.MoveSubNodeToPosition
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::MoveSubNodeToPosition method

Reorders a specified child [**IContextNode**](icontextnode.md) object to the specified index.

## Syntax


```C++
HRESULT MoveSubNodeToPosition(
  [in] IContextNode *pSubnodeToMove,
  [in] ULONG        ulNewIndex
);
```



## Parameters

<dl> <dt>

*pSubnodeToMove* \[in\]
</dt> <dd>

The [**IContextNode**](icontextnode.md) object to move.

</dd> <dt>

*ulNewIndex* \[in\]
</dt> <dd>

The index for the new position of the subnode.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

Returns **E\_INVALIDARG** if *pSubnodeToMove* is not a child node of this [**IContextNode**](icontextnode.md).

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

[**IContextNode::CreateSubNode**](icontextnode-createsubnode.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




