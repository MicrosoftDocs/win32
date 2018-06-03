---
title: ITopic locale property
description: Returns locale
ms.assetid: b538b6a4-9690-4b29-bdc8-672c1b15c58e
keywords:
- locale property HelpAPI
- locale property HelpAPI , ITopic interface
- ITopic interface HelpAPI , locale property
topic_type:
- apiref
api_name:
- ITopic.locale
- ITopic.get_locale
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

# ITopic::locale property

Returns locale

This property is read-only.

## Syntax


```C++
HRESULT get_locale(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The locale of this topic.

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

 

 





