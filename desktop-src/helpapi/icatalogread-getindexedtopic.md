---
title: ICatalogRead GetIndexedTopic method
description: method GetIndexedTopic - returns a data stream containing the XHTML data for a topic identified by its topic id in an open catalog
ms.assetid: '9c16d88b-4ca3-4553-aa3b-d3f1b7e7e2f0'
keywords: ["GetIndexedTopic method HelpAPI", "GetIndexedTopic method HelpAPI , ICatalogRead interface", "ICatalogRead interface HelpAPI , GetIndexedTopic method"]
topic_type:
- apiref
api_name:
- ICatalogRead.GetIndexedTopic
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
---

# ICatalogRead::GetIndexedTopic method

method GetIndexedTopic - returns a data stream containing the XHTML data for a topic identified by its topic id in an open catalog

## Syntax


```C++
HRESULT GetIndexedTopic(
  [in]          ICatalog    *Catalog,
  [in]          BSTR        topicId,
  [in]          IHelpFilter *filter,
  [out, retval] IUnknown    **pRetVal
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
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**ICatalogRead**](icatalogread.md)
</dt> </dl>

 

 





