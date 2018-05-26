---
title: ITopic Category method
description: Returns topic categories (if defined in the content)
ms.assetid: ba80608d-bf63-4bf8-b750-fa444eed61a0
keywords:
- Category method HelpAPI
- Category method HelpAPI , ITopic interface
- ITopic interface HelpAPI , Category method
topic_type:
- apiref
api_name:
- ITopic.Category
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

# ITopic::Category method

Returns topic categories (if defined in the content)

## Syntax


```C++
HRESULT Category(
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

 

 





