---
description: Adds a piece of application-specific data.
ms.assetid: 86ba37ac-8e65-4397-8ed1-37463152bebd
title: IContextNode::AddPropertyData method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.AddPropertyData
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::AddPropertyData method

Adds a piece of application-specific data.

## Syntax


```C++
HRESULT AddPropertyData(
  [in] const GUID  *pPropertyDataId,
  [in]       ULONG ulPropertyDataSize,
  [in]       BYTE  *pbPropertiesData
);
```



## Parameters

<dl> <dt>

*pPropertyDataId* \[in\]
</dt> <dd>

A globally unique identifier (GUID) that is used to identify the type of data.

</dd> <dt>

*ulPropertyDataSize* \[in\]
</dt> <dd>

The size of the data in bytes.

</dd> <dt>

*pbPropertiesData* \[in\]
</dt> <dd>

\[in, size\_is(ulPropertyDataSize)\]

An 8-bit unsigned integer array containing the property information to add.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

Use **IContextNode::AddPropertyData** to associate data with a context node. To retrieve the data later, use [**IContextNode::GetPropertyData**](icontextnode-getpropertydata.md).

The ink analyzer may delete the node as part of ink analysis, unless the context node is confirmed (see [**IContextNode::Confirm**](icontextnode-confirm.md)). For more information about synchronizing your application data with the [**IInkAnalyzer**](iinkanalyzer.md), see [Data Proxy with Ink Analysis](data-proxy-with-ink-analysis.md).

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

[**IContextNode::GetPropertyDataIds**](icontextnode-getpropertydataids.md)
</dt> <dt>

[**IContextNode::ContainsPropertyData**](icontextnode-containspropertydata.md)
</dt> <dt>

[**IContextNode::LoadPropertiesData**](icontextnode-loadpropertiesdata.md)
</dt> <dt>

[**IContextNode::RemovePropertyData**](icontextnode-removepropertydata.md)
</dt> <dt>

[**IContextNode::SavePropertiesData**](icontextnode-savepropertiesdata.md)
</dt> </dl>

 

 




