---
title: ITopic FetchContent method
description: method FetchContent - returns a data stream containing the XHTML data for the topic
ms.assetid: edcfe747-4dab-46d7-80ec-0cce91b4583b
keywords:
- FetchContent method HelpAPI
- FetchContent method HelpAPI , ITopic interface
- ITopic interface HelpAPI , FetchContent method
topic_type:
- apiref
api_name:
- ITopic.FetchContent
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

# ITopic::FetchContent method

method FetchContent - returns a data stream containing the XHTML data for the topic

## Syntax


```C++
HRESULT FetchContent(
  [out, retval] IUnknown **pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out, retval\]
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

 

 





