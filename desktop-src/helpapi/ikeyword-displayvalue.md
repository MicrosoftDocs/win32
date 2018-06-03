---
title: IKeyword DisplayValue property
description: Display value of the keyword
ms.assetid: 52b0801c-ec5d-404f-a31a-3a5fa01385b0
keywords:
- DisplayValue property HelpAPI
- DisplayValue property HelpAPI , IKeyword interface
- IKeyword interface HelpAPI , DisplayValue property
topic_type:
- apiref
api_name:
- IKeyword.DisplayValue
- IKeyword.get_DisplayValue
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

# IKeyword::DisplayValue property

Display value of the keyword

This property is read-only.

## Syntax


```C++
HRESULT get_DisplayValue(
  [out, retval] BSTR *pRetVal
);
```



## Property value

The display value of the keyword.

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

 

 





