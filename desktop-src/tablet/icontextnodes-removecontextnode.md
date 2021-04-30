---
description: Removes an IContextNode object from this collection.
ms.assetid: ddda506d-4e39-486d-ac7d-211dc7869a73
title: IContextNodes::RemoveContextNode method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNodes.RemoveContextNode
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNodes::RemoveContextNode method

Removes an [**IContextNode**](icontextnode.md) object from this collection.

## Syntax


```C++
HRESULT RemoveContextNode(
  [in] IContextNode *pContextNode
);
```



## Parameters

<dl> <dt>

*pContextNode* \[in\]
</dt> <dd>

The [**IContextNode**](icontextnode.md) object to remove.

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

[**IContextNodes**](icontextnodes.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




