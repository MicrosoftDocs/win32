---
title: IFontCacheNotify OnPostFontChange method
description: Hit by the font cache after it updates the fonts in use. Sets the new font for the current charset.
ms.assetid: d790f596-f9e6-4dc9-b960-61bbf2b07fb0
keywords:
- OnPostFontChange method Windows Mail (formerly Outlook Express)
- OnPostFontChange method Windows Mail (formerly Outlook Express) , IFontCacheNotify interface
- IFontCacheNotify interface Windows Mail (formerly Outlook Express) , OnPostFontChange method
topic_type:
- apiref
api_name:
- IFontCacheNotify.OnPostFontChange
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IFontCacheNotify::OnPostFontChange method

\[**IFontCacheNotify::OnPostFontChange** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Hit by the font cache after it updates the fonts in use. Sets the new font for the current charset.

## Syntax


```C++
HRESULT OnPostFontChange();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





