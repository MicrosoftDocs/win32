---
title: ITopic ParentTopicLocale property
description: Returns parent topic locale
ms.assetid: 4abe8476-cb01-437f-99d9-70851a4a77cd
keywords:
- ParentTopicLocale property HelpAPI
- ParentTopicLocale property HelpAPI , ITopic interface
- ITopic interface HelpAPI , ParentTopicLocale property
topic_type:
- apiref
api_name:
- ITopic.ParentTopicLocale
- ITopic.get_ParentTopicLocale
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

# ITopic::ParentTopicLocale property

Returns parent topic locale

This property is read-only.

## Syntax


```C++
HRESULT get_ParentTopicLocale(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The local of the parent topic.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITopic**](itopic.md)
</dt> </dl>

 

 





