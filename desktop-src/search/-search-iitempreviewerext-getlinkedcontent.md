---
description: Permits the extension to rich content for a property.
ms.assetid: d1b09ea0-7263-4b7c-8c59-25251bb6b285
title: IItemPreviewerExt::GetLinkedContent method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IItemPreviewerExt.GetLinkedContent
api_type: 
- COM
api_location: 
---

# IItemPreviewerExt::GetLinkedContent method

Permits the extension to rich content for a property.

## Syntax


```C++
HRESULT GetLinkedContent(
  [in]          DWORD     dwContext,
  [in]          LPCOLESTR pwszProp,
  [out, retval] LINKINFO  *pInfo
);
```



## Parameters

<dl> <dt>

*dwContext* \[in\]
</dt> <dd>

Type: **DWORD**

The context identifier for the operation. Override the *dwContext* default to set the context identifier to a value of your choosing.

</dd> <dt>

*pwszProp* \[in\]
</dt> <dd>

Type: **LPCOLESTR**

A pointer to the property of the linked content as a Unicode string.

</dd> <dt>

*pInfo* \[out, retval\]
</dt> <dd>

Type: **[**LINKINFO**](-search-linkinfo.md)\***

Receives a pointer to the [**LINKINFO**](-search-linkinfo.md) structure in which the method returns information about the transaction. *pInfo* must not be a **NULL** pointer.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The [**IItemPreviewerExt**](-search-iitempreviewerext.md) interface is supported only on Windows XP and Windows Server 2003, and should no longer be used.

To preview attachments with a third-party protocol handler on computers running Windows XP or Windows Server 2003, it may be necessary to use the [**IItemPreviewerExt**](-search-iitempreviewerext.md) interface, and the following APIs: the [**ISearchProtocolUI**](-search-isearchprotocolui.md), [**IItemPropertyBag**](iitempropertybag.md) and [**ISearchItem**](-search-isearchitem.md) interfaces, the [**LINKINFO**](-search-linkinfo.md) structure, and the [**LINKTYPE**](-search-linktype.md) enumeration.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| Redistributable<br/>          | Windows Desktop Search (WDS) 3.0<br/>          |



## See also

<dl> <dt>

[**IItemPreviewerExt**](-search-iitempreviewerext.md)
</dt> </dl>

 

 




