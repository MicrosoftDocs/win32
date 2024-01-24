---
description: Gets the search item for the data specified. This method is called once for every URL processed by the gatherer, and retrieves a pointer to the ISearchItem object.
ms.assetid: 35893bc9-8327-44f9-a9fc-7855c5c063e3
title: ISearchProtocolUI::GetSearchItemForUrl method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISearchProtocolUI.GetSearchItemForUrl
api_type: 
- COM
api_location: 
---

# ISearchProtocolUI::GetSearchItemForUrl method

Gets the search item for the data specified. This method is called once for every URL processed by the gatherer, and retrieves a pointer to the [**ISearchItem**](-search-isearchitem.md) object.

## Syntax


```C++
HRESULT GetSearchItemForUrl(
  [in]          LPCOLESTR        pcwszURL,
  [in]          IItemPropertyBag *pPropertyBag,
  [out, retval] ISearchItem      **ppSearchItem
);
```



## Parameters

<dl> <dt>

*pcwszURL* \[in\]
</dt> <dd>

Type: **LPCOLESTR**

Pointer to a null data terminated Unicode string containing the search item for the URL being accessed.

</dd> <dt>

*pPropertyBag* \[in\]
</dt> <dd>

Type: **IItemPropertyBag\***

Pointer to an [**IItemPropertyBag**](iitempropertybag.md) object that contains information about the search item, including the properties of the item.

</dd> <dt>

*ppSearchItem* \[out, retval\]
</dt> <dd>

Type: **[**ISearchItem**](-search-isearchitem.md)\*\***

Receives the address of a pointer to the [**ISearchItem**](-search-isearchitem.md) object created by this method. This object contains information about the search item, such as the item's file name.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The **ISearchProtocolUI::GetSearchItemForUrl** method is supported only on Windows XP and Windows Server 2003, and should no longer be used.

To preview attachments with a third-party protocol handler on computers running Windows XP or Windows Server 2003, it may be necessary to use the [**ISearchProtocolUI**](-search-isearchprotocolui.md) interface, and the following APIs: the [**IItemPreviewerExt**](-search-iitempreviewerext.md), [**IItemPropertyBag**](iitempropertybag.md) and [**ISearchItem**](-search-isearchitem.md) interfaces, the [**LINKINFO**](-search-linkinfo.md) structure, and the [**LINKTYPE**](-search-linktype.md) enumeration.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |
| Redistributable<br/>          | Windows Desktop Search (WDS) 3.0<br/>          |



## See also

<dl> <dt>

[**ISearchProtocolUI**](-search-isearchprotocolui.md)
</dt> </dl>

 

 




