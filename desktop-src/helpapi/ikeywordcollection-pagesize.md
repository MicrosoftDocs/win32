---
title: IKeywordCollection pageSize property
description: Returns the page size of the collection
ms.assetid: 1fcad9d7-02e3-45a5-b005-bef86908a81d
keywords:
- pageSize property HelpAPI
- pageSize property HelpAPI , IKeywordCollection interface
- IKeywordCollection interface HelpAPI , pageSize property
topic_type:
- apiref
api_name:
- IKeywordCollection.pageSize
- IKeywordCollection.get_pageSize
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

# IKeywordCollection::pageSize property

Returns the page size of the collection

This property is read-only.

## Syntax


```C++
HRESULT get_pageSize(
  [out, retval] long *pRetVal
);
```



## Property value

The page size of the collection.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**IKeywordCollection**](ikeywordcollection.md)
</dt> </dl>

 

 





