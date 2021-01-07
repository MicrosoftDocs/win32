---
description: Causes one or more properties to be saved into the property bag. The IItemPropertyBag interface is supported only on Windows XP and Windows Server 2003, and should no longer be used.
ms.assetid: 35491fbc-fb1c-4bad-86e8-9f19856ed7cb
title: IItemPropertyBag::Write method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IItemPropertyBag.Write
api_type: 
- COM
api_location: 
---

# IItemPropertyBag::Write method

Causes one or more properties to be saved into the property bag. The [**IItemPropertyBag**](iitempropertybag.md) interface is supported only on Windows XP and Windows Server 2003, and should no longer be used.

## Syntax


```C++
HRESULT Write(
  [in] ULONG    cProperties,
  [in] ITEMPROP *pPropBag,
  [in] VARIANT  *pvarValue
);
```



## Parameters

<dl> <dt>

*cProperties* \[in\]
</dt> <dd>

The number of properties to save. This argument specifies the number of elements in the arrays at *pPropBag* and *pvarValue*.

</dd> <dt>

*pPropBag* \[in\]
</dt> <dd>

Pointer to an array of [**ITEMPROP**](/windows/desktop/api/subsmgr/ns-subsmgr-itemprop) structures that specifies the properties to be saved.

</dd> <dt>

*pvarValue* \[in\]
</dt> <dd>

Pointer to a **VARIANT** whose type depends on the data type of the property information that it contains.

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

 

 




