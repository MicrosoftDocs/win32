---
description: Suggests the security policy to be applied to the browser.
ms.assetid: 73541611-2024-4c33-ab03-e3204244c46c
title: IItemPreviewerExt::SuggestBrowserPolicy method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IItemPreviewerExt.SuggestBrowserPolicy
api_type: 
- COM
api_location: 
---

# IItemPreviewerExt::SuggestBrowserPolicy method

Suggests the security policy to be applied to the browser.

## Syntax


```C++
HRESULT SuggestBrowserPolicy(
  [in]          DWORD dwContext,
  [out, retval] DWORD *pdwFlags
);
```



## Parameters

<dl> <dt>

*dwContext* \[in\]
</dt> <dd>

Type: **DWORD**

The context identifier for the operation. Override the *dwContext* default to set the context identifier to a value of your choosing.

</dd> <dt>

*pdwFlags* \[out, retval\]
</dt> <dd>

Type: **DWORD\***

A pointer to a DWORD value containing verification check flags. The **BROWSERPOLICY\_UNTRUSTED\_CONTENT** flag disables any possibility of the preview being able to run script or ActiveX. The parameter *pdwFlags* must not be a **NULL** pointer.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The [**IItemPreviewerExt**](-search-iitempreviewerext.md) interface is supported only on Windows XP and Windows Server 2003, and should no longer be used.

To preview attachments with a third-party protocol handler on computers running Windows XP or Windows Server 2003, it may be necessary to use the [**IItemPreviewerExt**](-search-iitempreviewerext.md) interface, and the following APIs: the [**ISearchProtocolUI**](-search-isearchprotocolui.md), [**IItemPropertyBag**](iitempropertybag.md) and [**ISearchItem**](-search-isearchitem.md) interfaces, the [**LINKINFO**](-search-linkinfo.md) structure, and the [**LINKTYPE**](-search-linktype.md) enumeration.

Using the **BROWSERPOLICY\_UNTRUSTED\_CONTENT** flag is strongly recommended to disable any possibility of the preview being able to run script or ActiveX. The **IItemPreviewerExt::SuggestBrowserPolicy** method can return information on whether the item being previewed is trusted or not. This will allow the previewer trident control to execute script, and even ActiveX controls. Because the previewer often uses temporary files to generate the preview, doing so can result in unexpected script and code execution in the Local Computer zone.

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

 

 




