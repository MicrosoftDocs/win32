---
title: IKeywordCollection Count property
description: Returns the number of elements in the collection
ms.assetid: e6819c5e-3aa2-4fd9-83b8-ae8b98bcef52
keywords:
- Count property HelpAPI
- Count property HelpAPI , IKeywordCollection interface
- IKeywordCollection interface HelpAPI , Count property
topic_type:
- apiref
api_name:
- IKeywordCollection.Count
- IKeywordCollection.get_Count
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IKeywordCollection::Count property

Returns the number of elements in the collection

This property is read-only.

## Syntax


```C++
HRESULT get_Count(
  [out, retval] long *pRetVal
);
```



## Property value

The number of elements in the collection.

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

 

 





