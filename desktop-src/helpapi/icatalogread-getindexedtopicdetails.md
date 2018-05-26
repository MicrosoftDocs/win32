---
title: ICatalogRead GetIndexedTopicDetails method
description: method GetIndexedTopicDetails - returns an ITopic interface containing the details of a topic identified by its topic id in an open catalog
ms.assetid: 82246743-a3eb-43f1-80e2-5cd81d9eb668
keywords:
- GetIndexedTopicDetails method HelpAPI
- GetIndexedTopicDetails method HelpAPI , ICatalogRead interface
- ICatalogRead interface HelpAPI , GetIndexedTopicDetails method
topic_type:
- apiref
api_name:
- ICatalogRead.GetIndexedTopicDetails
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

# ICatalogRead::GetIndexedTopicDetails method

method GetIndexedTopicDetails - returns an ITopic interface containing the details of a topic identified by its topic id in an open catalog

## Syntax


```C++
HRESULT GetIndexedTopicDetails(
  [in]          ICatalog    *Catalog,
  [in]          BSTR        topicId,
  [in]          IHelpFilter *filter,
  [out, retval] ITopic      **pRetVal
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

 

 





