---
title: ICatalogRead GetSearchResults method
description: method GetSearchResults - returns an ITopicCollection for a given query within a catalog. filter is a collection of key/value pairs to refine the search results. Supports paging.
ms.assetid: f547ed67-c2ff-4b5d-bc6e-7741157f1c18
keywords:
- GetSearchResults method HelpAPI
- GetSearchResults method HelpAPI , ICatalogRead interface
- ICatalogRead interface HelpAPI , GetSearchResults method
topic_type:
- apiref
api_name:
- ICatalogRead.GetSearchResults
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ICatalogRead::GetSearchResults method

method GetSearchResults - returns an ITopicCollection for a given query within a catalog. filter is a collection of key/value pairs to refine the search results. Supports paging.

## Syntax


```C++
HRESULT GetSearchResults(
  [in]          ICatalog         *Catalog,
  [in]          BSTR             query,
  [in]          IHelpFilter      *filter,
  [in]          long             options,
  [in]          long             pageSize,
  [in]          long             pageNumber,
  [out]         long             *totalSearchResults,
  [out, retval] ITopicCollection **pRetVal
);
```



## Parameters

<dl> <dt>

*Catalog* \[in\]
</dt> <dd></dd> <dt>

*query* \[in\]
</dt> <dd></dd> <dt>

*filter* \[in\]
</dt> <dd></dd> <dt>

*options* \[in\]
</dt> <dd></dd> <dt>

*pageSize* \[in\]
</dt> <dd></dd> <dt>

*pageNumber* \[in\]
</dt> <dd></dd> <dt>

*totalSearchResults* \[out\]
</dt> <dd></dd> <dt>

*pRetVal* \[out, retval\]
</dt> <dd></dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**ICatalogRead**](icatalogread.md)
</dt> </dl>

 

 





