---
description: Retrieves the IContextNode object that is the source for this IContextLink.
ms.assetid: 2f55ae9c-9f63-4d49-9bf0-9e169b819e79
title: IContextLink::GetSourceNode method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextLink.GetSourceNode
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextLink::GetSourceNode method

Retrieves the [**IContextNode**](icontextnode.md) object that is the source for this [**IContextLink**](icontextlink.md).

## Syntax


```C++
HRESULT GetSourceNode(
  [out] IContextNode **ppSrcContextNodeId
);
```



## Parameters

<dl> <dt>

*ppSrcContextNodeId* \[out\]
</dt> <dd>

A pointer to the [**IContextNode**](icontextnode.md) object that is the source for this [**IContextLink**](icontextlink.md).

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on \**ppSrcContextNodeId* when you no longer need to use the source node.

 

If the [**IContextLink**](icontextlink.md) object links between a node that contains writing and a node that contains drawing, the source node is generally the node that contains drawing.

If the [**IContextLink**](icontextlink.md) object has a link type of Encloses (see [**IContextLink::GetContextLinkDirection**](icontextlink-getcontextlinkdirection.md)), the source node is the node that encloses the destination node.

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

[**IContextLink::GetDestinationNode**](icontextlink-getdestinationnode.md)
</dt> <dt>

[**ContextLinkDirection**](contextlinkdirection.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

