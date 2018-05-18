---
title: ICatalogRead GetTableOfContents method
description: method GetTableOfContents - returns an ITopicCollection of ToC data.
ms.assetid: 'd8aacf9a-4577-4926-8aff-b1ca2da6a57d'
keywords: ["GetTableOfContents method HelpAPI", "GetTableOfContents method HelpAPI , ICatalogRead interface", "ICatalogRead interface HelpAPI , GetTableOfContents method"]
topic_type:
- apiref
api_name:
- ICatalogRead.GetTableOfContents
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ICatalogRead::GetTableOfContents method

method GetTableOfContents - returns an ITopicCollection of ToC data. ToC is from the starting point of the topic id and matching the topic locale and topic version (to support multiple locale and versions in a catalog). The return detail can be one of four levels (Children of the topicId, Siblings of the topicId, Ancestors of the topicId, or all ToC Root Nodes)

## Syntax


```C++
HRESULT GetTableOfContents(
  [in]          ICatalog         *Catalog,
  [in]          BSTR             topicId,
  [in]          IHelpFilter      *filter,
  [in]          TocReturnDetail  returnDetail,
  [out, retval] ITopicCollection **pRetVal
);
```



## Parameters

<dl> <dt>

*Catalog* \[in\]
</dt> <dd></dd> <dt>

*topicId* \[in\]
</dt> <dd></dd> <dt>

*filter* \[in\]
</dt> <dd></dd> <dt>

*returnDetail* \[in\]
</dt> <dd></dd> <dt>

*pRetVal* \[out, retval\]
</dt> <dd></dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**ICatalogRead**](icatalogread.md)
</dt> </dl>

 

 





