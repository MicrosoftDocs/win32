---
title: ITopicCollection Count property
description: Returns the number of elements in the collection
ms.assetid: 73487672-80b8-40a0-a113-d0fba31b6841
keywords:
- Count property HelpAPI
- Count property HelpAPI , ITopicCollection interface
- ITopicCollection interface HelpAPI , Count property
topic_type:
- apiref
api_name:
- ITopicCollection.Count
- ITopicCollection.get_Count
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

# ITopicCollection::Count property

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

[**ITopicCollection**](itopiccollection.md)
</dt> </dl>

 

 





