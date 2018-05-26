---
title: IFontCache GetJP\_ISOControl method
description: Returns the current control value.
ms.assetid: 6e4b4122-9710-4f12-9aef-5a629be3e276
keywords:
- GetJP_ISOControl method Windows Mail (formerly Outlook Express)
- GetJP_ISOControl method Windows Mail (formerly Outlook Express) , IFontCache interface
- IFontCache interface Windows Mail (formerly Outlook Express) , GetJP_ISOControl method
topic_type:
- apiref
api_name:
- IFontCache.GetJP_ISOControl
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

# IFontCache::GetJP\_ISOControl method

\[**IFontCache::GetJP\_ISOControl** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the current control value.

## Syntax


```C++
HRESULT GetJP_ISOControl(
  [out] BOOL *pfUseSIO
);
```



## Parameters

<dl> <dt>

*pfUseSIO* \[out\]
</dt> <dd>

Type: **BOOL\***

Returns a value that indicates whether to use ESC or SIO. 0 means use ESC and 1 means use SIO.

</dd> </dl>

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



 

 





