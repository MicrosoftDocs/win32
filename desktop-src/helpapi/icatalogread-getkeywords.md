---
title: ICatalogRead GetKeywords method
description: method GetKeywords - returns an IKeywordCollection of all of the keywords in the catalog
ms.assetid: c15b71e6-bf1a-4991-9a87-1f281f3debe4
keywords:
- GetKeywords method HelpAPI
- GetKeywords method HelpAPI , ICatalogRead interface
- ICatalogRead interface HelpAPI , GetKeywords method
topic_type:
- apiref
api_name:
- ICatalogRead.GetKeywords
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

# ICatalogRead::GetKeywords method

method GetKeywords - returns an IKeywordCollection of all of the keywords in the catalog

## Syntax


```C++
HRESULT GetKeywords(
  [in]           ICatalog           *Catalog,
  [in, optional] long               useCache,
  [out, retval]  IKeywordCollection **pRetVal
);
```



## Parameters

<dl> <dt>

*Catalog* \[in\]
</dt> <dd></dd> <dt>

*useCache* \[in, optional\]
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

 

 





