---
description: Retrieves an array of bytes that contains the application-specific and internal property data for this IContextNode.
ms.assetid: f26d71a7-fe71-48a8-9c8f-9c4d99261df1
title: IContextNode::SavePropertiesData method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IContextNode.SavePropertiesData
api_type: 
- COM
api_location: 
- IACom.dll
---

# IContextNode::SavePropertiesData method

Retrieves an array of bytes that contains the application-specific and internal property data for this [**IContextNode**](icontextnode.md).

## Syntax


```C++
HRESULT SavePropertiesData(
  [in, out] ULONG *pulPropertiesDataSize,
  [out]     BYTE  **ppbPropertiesData
);
```



## Parameters

<dl> <dt>

*pulPropertiesDataSize* \[in, out\]
</dt> <dd>

The size of the data array containing the property information. The value passed in is not used.

</dd> <dt>

*ppbPropertiesData* \[out\]
</dt> <dd>

A pointer to an 8-bit unsigned integer array that contains the application-specific and internal property data.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, use [**CoTaskMemFree**](/windows/desktop/api/combaseapi/nf-combaseapi-cotaskmemfree) to release the memory from \**ppbPropertiesData* when you no longer need the information.

 

Use this method when your application maintains its own data structure, which is synchronized with that of the [**IInkAnalyzer**](iinkanalyzer.md). This method saves the property data that the **IInkAnalyzer** has set on the [**IContextNode**](icontextnode.md).

For more information about synchronizing your application data with the [**IInkAnalyzer**](iinkanalyzer.md), see [Data Proxy with Ink Analysis](data-proxy-with-ink-analysis.md).

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

[**IContextNode::LoadPropertiesData**](icontextnode-loadpropertiesdata.md)
</dt> <dt>

[**IContextNode::AddPropertyData**](icontextnode-addpropertydata.md)
</dt> <dt>

[**IContextNode::GetPropertyData**](icontextnode-getpropertydata.md)
</dt> <dt>

[**IContextNode::RemovePropertyData**](icontextnode-removepropertydata.md)
</dt> <dt>

[**IContextNode::GetPropertyDataIds**](icontextnode-getpropertydataids.md)
</dt> <dt>

[**IContextNode::ContainsPropertyData**](icontextnode-containspropertydata.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

