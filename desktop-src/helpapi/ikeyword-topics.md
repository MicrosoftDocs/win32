---
title: IKeyword Topics property
description: Returns an ITopicCollection containing all ITopics associated with this keyword
ms.assetid: b1759f64-17b5-4820-a74f-e7c88a5fa786
keywords:
- Topics property HelpAPI
- Topics property HelpAPI , IKeyword interface
- IKeyword interface HelpAPI , Topics property
topic_type:
- apiref
api_name:
- IKeyword.Topics
- IKeyword.get_Topics
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

# IKeyword::Topics property

Returns an ITopicCollection containing all ITopics associated with this keyword

This property is read-only.

## Syntax


```C++
HRESULT get_Topics(
  [out, retval] ITopicCollection **pRetVal
);
```



## Property value

The ITopicCollection that contains all ITopics associated with this keyword.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**IKeyword**](ikeyword.md)
</dt> </dl>

 

 





