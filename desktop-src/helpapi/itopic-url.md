---
title: ITopic Url property
description: Returns topic URL
ms.assetid: 7d5013d7-97ee-477d-afea-2c9ebe5571ef
keywords:
- Url property HelpAPI
- Url property HelpAPI , ITopic interface
- ITopic interface HelpAPI , Url property
topic_type:
- apiref
api_name:
- ITopic.Url
- ITopic.get_Url
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

# ITopic::Url property

Returns topic URL

This property is read-only.

## Syntax


```C++
HRESULT get_Url(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The topic URL.

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

 

 





