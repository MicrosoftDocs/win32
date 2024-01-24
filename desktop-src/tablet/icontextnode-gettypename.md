---
description: Retrieves a human-readable type name of this IContextNode.
ms.assetid: 02031efd-1e9c-4e96-8dc1-280cc1a6e58f
title: IContextNode::GetTypeName method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.GetTypeName
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::GetTypeName method

Retrieves a human-readable type name of this [**IContextNode**](icontextnode.md).

## Syntax


```C++
HRESULT GetTypeName(
  [out] BSTR *pbstrContextNodeType
);
```



## Parameters

<dl> <dt>

*pbstrContextNodeType* \[out\]
</dt> <dd>

A human-readable type name of this [**IContextNode**](icontextnode.md).

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) on \**pbstrContextNodeType* when you no longer need to use the string.

 

For example, this method sets *pbstrContextNodeType* to "InkWordNode" for an ink word node (see [**IContextNode::GetType**](icontextnode-gettype.md) and [Context Node Types](context-node-types.md)).

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

[**IContextNode::GetType**](icontextnode-gettype.md)
</dt> <dt>

[Context Node Types](context-node-types.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

