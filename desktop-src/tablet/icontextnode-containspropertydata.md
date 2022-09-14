---
description: Determines whether the IContextNode object contains data stored under the specified identifier.
ms.assetid: ac3a85a2-abf8-4ac4-8779-d9fda89497d4
title: IContextNode::ContainsPropertyData method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.ContainsPropertyData
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::ContainsPropertyData method

Determines whether the [**IContextNode**](icontextnode.md) object contains data stored under the specified identifier.

## Syntax


```C++
HRESULT ContainsPropertyData(
  [in]  const GUID         *pPropertyDataId,
  [out]       VARIANT_BOOL *pbContains
);
```



## Parameters

<dl> <dt>

*pPropertyDataId* \[in\]
</dt> <dd>

The identifier for the data.

</dd> <dt>

*pbContains* \[out\]
</dt> <dd>

**VARIANT\_TRUE** if the [**IContextNode**](icontextnode.md) object contains data stored under the specified identifier; otherwise, **VARIANT\_FALSE**.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

In addition to application-specific data, you can also use this method to determine whether this [**IContextNode**](icontextnode.md) contains other internal data (see [Analysis Hint Properties](analysis-hint-properties.md) and [Context Node Properties](context-node-properties.md)).

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

[**IContextNode::AddPropertyData**](icontextnode-addpropertydata.md)
</dt> <dt>

[**IContextNode::GetPropertyData**](icontextnode-getpropertydata.md)
</dt> <dt>

[**IContextNode::GetPropertyDataIds**](icontextnode-getpropertydataids.md)
</dt> <dt>

[**IContextNode::LoadPropertiesData**](icontextnode-loadpropertiesdata.md)
</dt> <dt>

[**IContextNode::RemovePropertyData**](icontextnode-removepropertydata.md)
</dt> <dt>

[**IContextNode::SavePropertiesData**](icontextnode-savepropertiesdata.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 




