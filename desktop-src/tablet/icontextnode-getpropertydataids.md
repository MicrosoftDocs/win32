---
description: Retrieves the identifiers for which there is property data.
ms.assetid: c9c491b7-95e2-421a-8632-f65844cd5ef9
title: IContextNode::GetPropertyDataIds method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.GetPropertyDataIds
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::GetPropertyDataIds method

Retrieves the identifiers for which there is property data.

## Syntax


```C++
HRESULT GetPropertyDataIds(
  [out] ULONG *pulGuidCount,
  [out] GUID  **ppGuids
);
```



## Parameters

<dl> <dt>

*pulGuidCount* \[out\]
</dt> <dd>

The number of properties.

</dd> <dt>

*ppGuids* \[out\]
</dt> <dd>

The identifiers for which there is property data.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, use [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) to release the memory from \**ppGuids* when you no longer need the information.

 

This method returns the application-specific identifiers for property data that has been added. It also returns the identifiers for the internal property data, which are described by the [Context Node Properties](context-node-properties.md) constants.

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

[**IContextNode::GetPropertyData**](icontextnode-getpropertydata.md)
</dt> <dt>

[**IContextNode::ContainsPropertyData**](icontextnode-containspropertydata.md)
</dt> <dt>

[**IContextNode::RemovePropertyData**](icontextnode-removepropertydata.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

