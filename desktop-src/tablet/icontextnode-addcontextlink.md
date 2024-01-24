---
description: Adds a new IContextLink to the IContextNode object's collection of context links.
ms.assetid: b7b9da10-3015-4976-bc4e-1a7f69b7c85b
title: IContextNode::AddContextLink method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.AddContextLink
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::AddContextLink method

Adds a new [**IContextLink**](icontextlink.md) to the [**IContextNode**](icontextnode.md) object's collection of context links.

## Syntax


```C++
HRESULT AddContextLink(
  [in]  IContextNode         *pDestinationNode,
  [in]  ContextLinkDirection linkDirection,
  [out] IContextLink         **ppContextLinkToAdd
);
```



## Parameters

<dl> <dt>

*pDestinationNode* \[in\]
</dt> <dd>

The destination [**IContextNode**](icontextnode.md) for the new [**IContextLink**](icontextlink.md).

</dd> <dt>

*linkDirection* \[in\]
</dt> <dd>

The direction of [**IContextLink**](icontextlink.md) object to create.

</dd> <dt>

*ppContextLinkToAdd* \[out\]
</dt> <dd>

A pointer to the new [**IContextLink**](icontextlink.md) object.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) on \**ppContextLinkToAdd* when you no longer need to use the context node.

 

This [**IContextNode**](icontextnode.md) object is the source node (see [**IContextLink::GetSourceNode**](icontextlink-getsourcenode.md)) for the new [**IContextLink**](icontextlink.md) object.

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

[**IContextLinks**](icontextlinks.md)
</dt> <dt>

[**ContextLinkDirection**](contextlinkdirection.md)
</dt> <dt>

[**IContextNode::DeleteContextLink**](icontextnode-deletecontextlink.md)
</dt> <dt>

[**IContextNode::GetContextLinks**](icontextnode-getcontextlinks.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

