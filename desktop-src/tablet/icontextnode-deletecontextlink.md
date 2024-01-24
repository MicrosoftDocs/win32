---
description: Deletes an IContextLink object from the IContextNode object's link collection.
ms.assetid: c4a69a74-30d6-4099-a02a-13c8a2e52bc7
title: IContextNode::DeleteContextLink method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.DeleteContextLink
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::DeleteContextLink method

Deletes an [**IContextLink**](icontextlink.md) object from the [**IContextNode**](icontextnode.md) object's link collection.

## Syntax


```C++
HRESULT DeleteContextLink(
  [in] IContextLink *pContextLinkToDelete
);
```



## Parameters

<dl> <dt>

*pContextLinkToDelete* \[in\]
</dt> <dd>

The [**IContextLink**](icontextlink.md) object to delete.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

A context link has a source node and a destination node (see [**IContextLink::GetSourceNode**](icontextlink-getsourcenode.md) and [**IContextLink::GetDestinationNode**](icontextlink-getdestinationnode.md)). This method removes the [**IContextLink**](icontextlink.md) from both the source and destination nodes' collection of context links (see [**IContextNode::GetContextLinks**](icontextnode-getcontextlinks.md)).

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

[**IContextLink**](icontextlink.md)
</dt> <dt>

[**IContextNode::AddContextLink**](icontextnode-addcontextlink.md)
</dt> <dt>

[**IContextNode::GetContextLinks**](icontextnode-getcontextlinks.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




