---
title: ITopic ContentFilter method
description: Returns the content filter values for the topic
ms.assetid: 4195d86b-7d05-4df0-a487-a2de53339fd2
keywords:
- ContentFilter method HelpAPI
- ContentFilter method HelpAPI , ITopic interface
- ITopic interface HelpAPI , ContentFilter method
topic_type:
- apiref
api_name:
- ITopic.ContentFilter
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

# ITopic::ContentFilter method

Returns the content filter values for the topic

## Syntax


```C++
HRESULT ContentFilter(
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

 

 





