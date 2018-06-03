---
title: ITopicCollection Current property
description: Gets the current ITopic element in the collection
ms.assetid: 1ac65c9e-403b-454f-bdfb-dc0e4d6b99ff
keywords:
- Current property HelpAPI
- Current property HelpAPI , ITopicCollection interface
- ITopicCollection interface HelpAPI , Current property
topic_type:
- apiref
api_name:
- ITopicCollection.Current
- ITopicCollection.get_Current
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

# ITopicCollection::Current property

Gets the current ITopic element in the collection

This property is read-only.

## Syntax


```C++
HRESULT get_Current(
  [out, retval] IUnknown **pRetVal
);
```



## Property value

The current ITopic element in the collection.

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

 

 





