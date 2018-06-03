---
title: IFontCache OnOptionChange method
description: Initializes the system font entry as a result of a setting change. Performs pre and post notification.
ms.assetid: c8c017f5-88d7-4985-99c3-37702f061d48
keywords:
- OnOptionChange method Windows Mail (formerly Outlook Express)
- OnOptionChange method Windows Mail (formerly Outlook Express) , IFontCache interface
- IFontCache interface Windows Mail (formerly Outlook Express) , OnOptionChange method
topic_type:
- apiref
api_name:
- IFontCache.OnOptionChange
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IFontCache::OnOptionChange method

\[**IFontCache::OnOptionChange** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Initializes the system font entry as a result of a setting change. Performs pre and post notification.

## Syntax


```C++
HRESULT OnOptionChange();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                          | Description                            |
|--------------------------------------------------------------------------------------|----------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Always returns this value. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





