---
title: IFontCacheNotify OnPreFontChange method
description: Tells the ListView to dump any custom fonts it is using.
ms.assetid: 'd285810d-ddae-4b00-9a8a-625de492c380'
keywords: ["OnPreFontChange method Windows Mail (formerly Outlook Express)", "OnPreFontChange method Windows Mail (formerly Outlook Express) , IFontCacheNotify interface", "IFontCacheNotify interface Windows Mail (formerly Outlook Express) , OnPreFontChange method"]
topic_type:
- apiref
api_name:
- IFontCacheNotify.OnPreFontChange
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IFontCacheNotify::OnPreFontChange method

\[**IFontCacheNotify::OnPreFontChange** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Hit by the font cache before it changes the fonts in use. Tells the ListView to dump any custom fonts it is using.

## Syntax


```C++
HRESULT OnPreFontChange();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





