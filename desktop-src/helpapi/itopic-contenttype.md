---
title: ITopic ContentType method
description: Returns this topics content types (if defined in the content)
ms.assetid: 472ee747-08f7-4f61-abe0-642ef327a639
keywords:
- ContentType method HelpAPI
- ContentType method HelpAPI , ITopic interface
- ITopic interface HelpAPI , ContentType method
topic_type:
- apiref
api_name:
- ITopic.ContentType
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

# ITopic::ContentType method

Returns this topic's content types (if defined in the content)

## Syntax


```C++
HRESULT ContentType(
  [out, retval] SAFEARRAY BSTR
);
```



## Parameters

<dl> <dt>

*BSTR* \[out, retval\]
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

[**ITopic**](itopic.md)
</dt> </dl>

 

 





