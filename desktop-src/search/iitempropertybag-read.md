---
description: Causes one or more properties to be read from the property bag. The IItemPropertyBag interface is supported only on Windows XP and Windows Server 2003, and should no longer be used.
ms.assetid: 78a63ef0-1b79-4b07-9121-a6fbd1116c4b
title: IItemPropertyBag::Read method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IItemPropertyBag.Read
api_type: 
- COM
api_location: 
---

# IItemPropertyBag::Read method

Causes one or more properties to be read from the property bag. The [**IItemPropertyBag**](iitempropertybag.md) interface is supported only on Windows XP and Windows Server 2003, and should no longer be used.

## Syntax


```C++
HRESULT Read(
  [in]  ULONG    cProperties,
  [in]  ITEMPROP *pPropBag,
  [out] VARIANT  *pvarValue,
  [out] HRESULT  *phrError
);
```



## Parameters

<dl> <dt>

*cProperties* \[in\]
</dt> <dd>

The number of properties to read. This argument specifies the number of elements in the arrays at *pPropBag*, *pvarValue*, and *phrError*.

</dd> <dt>

*pPropBag* \[in\]
</dt> <dd>

Pointer to an array of [**ITEMPROP**](/windows/desktop/api/subsmgr/ns-subsmgr-itemprop) structures that specifies the properties that are requested.

</dd> <dt>

*pvarValue* \[out\]
</dt> <dd>

Receives a pointer that returns an array of **VARIANT** structures that receives the property values.

</dd> <dt>

*phrError* \[out\]
</dt> <dd>

Pointer to an array of **HRESULT** values that receives the result of each property read. There must be at least *cProperties* elements in this array.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. Otherwise, it returns an **HRESULT** error code.

## Remarks

The [**IItemPropertyBag**](iitempropertybag.md) interface is supported only on Windows XP and Windows Server 2003, and should no longer be used.

To preview attachments with a third-party protocol handler on computers running Windows XP or Windows Server 2003, it may be necessary to use the [**IItemPropertyBag**](iitempropertybag.md) interface and the following APIs: the [**ISearchProtocolUI**](-search-isearchprotocolui.md), [**IItemPreviewerExt**](-search-iitempreviewerext.md) and [**ISearchItem**](-search-isearchitem.md) interfaces, the [**LINKINFO**](-search-linkinfo.md) and [**ITEMPROP**](/windows/desktop/api/subsmgr/ns-subsmgr-itemprop) structures, and the [**LINKTYPE**](-search-linktype.md) enumeration.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| Redistributable<br/>          | Windows Desktop Search (WDS) 3.0<br/>          |



## See also

<dl> <dt>

[**IItemPropertyBag**](iitempropertybag.md)
</dt> </dl>

 

 




