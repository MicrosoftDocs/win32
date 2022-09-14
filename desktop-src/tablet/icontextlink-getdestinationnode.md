---
description: Retrieves the IContextNode object that is the destination for this IContextLink.
ms.assetid: 7e185e69-821b-409b-bc58-d89a4aefeb23
title: IContextLink::GetDestinationNode method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextLink.GetDestinationNode
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextLink::GetDestinationNode method

Retrieves the [**IContextNode**](icontextnode.md) object that is the destination for this [**IContextLink**](icontextlink.md).

## Syntax


```C++
HRESULT GetDestinationNode(
  [out] IContextNode **ppDstContextNodeId
);
```



## Parameters

<dl> <dt>

*ppDstContextNodeId* \[out\]
</dt> <dd>

A pointer to the [**IContextNode**](icontextnode.md) object that is the destination for this [**IContextLink**](icontextlink.md).

</dd> </dl>

## Return value

For a description of return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on \**ppDstContextNodeId* when you no longer need to use the destination node.

 

If the [**IContextLink**](icontextlink.md) object links between a node that contains writing and a node that contains drawing, the destination node is generally the node that contains writing.

If the [**IContextLink**](icontextlink.md) object has a link type of Encloses (see [**IContextLink::GetContextLinkDirection**](icontextlink-getcontextlinkdirection.md)), the destination node is the [**IContextNode**](icontextnode.md) object that is enclosed.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IContextLink**](icontextlink.md)
</dt> <dt>

[**IContextLink::GetSourceNode**](icontextlink-getsourcenode.md)
</dt> <dt>

[**ContextLinkDirection**](contextlinkdirection.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

