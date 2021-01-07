---
description: Permits processing of a transformation command encountered in a preview template.
ms.assetid: 0b81b780-8bd1-4667-a0a1-65319f209603
title: IItemPreviewerExt::ProcessTransformCommand method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IItemPreviewerExt.ProcessTransformCommand
api_type: 
- COM
api_location: 
---

# IItemPreviewerExt::ProcessTransformCommand method

Permits processing of a transformation command encountered in a preview template.

## Syntax


```C++
HRESULT ProcessTransformCommand(
  [in]          DWORD     dwContext,
  [in]          LPCOLESTR pwszName,
  [in]          LPCOLESTR pwszArg,
  [out, retval] VARIANT   *pvarResult
);
```



## Parameters

<dl> <dt>

*dwContext* \[in\]
</dt> <dd>

Type: **DWORD**

The context identifier for the operation. Override the *dwContext* default to set the context identifier to a value of your choosing.

</dd> <dt>

*pwszName* \[in\]
</dt> <dd>

Type: **LPCOLESTR**

A pointer to the name of the transformation command as a Unicode string.

</dd> <dt>

*pwszArg* \[in\]
</dt> <dd>

Type: **LPCOLESTR**

A pointer to the argument as a Unicode string.

</dd> <dt>

*pvarResult* \[out, retval\]
</dt> <dd>

Type: **VARIANT\***

A pointer to the result variant. *pvarResult* must not be a **NULL** pointer.

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

 

 




