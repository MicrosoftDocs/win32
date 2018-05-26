---
title: IMimeInternational FindCharset method
description: Finds the character set handle of the specified character set name.
ms.assetid: c0118154-15c2-41be-9404-d26e69ab975b
keywords:
- FindCharset method Windows Mail (formerly Outlook Express)
- FindCharset method Windows Mail (formerly Outlook Express) , IMimeInternational interface
- IMimeInternational interface Windows Mail (formerly Outlook Express) , FindCharset method
topic_type:
- apiref
api_name:
- IMimeInternational.FindCharset
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

# IMimeInternational::FindCharset method

Finds the character set handle of the specified character set name.

## Syntax


```C++
HRESULT FindCharset(
  [in]  LPCSTR     pszCharset,
  [out] LPHCHARSET phCharset
);
```



## Parameters

<dl> <dt>

*pszCharset* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the name of the character set.

</dd> <dt>

*phCharset* \[out\]
</dt> <dd>

Type: **LPHCHARSET**

Receives the handle of the default character set.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                                            |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success.<br/>                                          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pszCharset* or *phCharset* is **NULL**. <br/>    |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>      | Indicates that an attempt to allocate memory failed.<br/>        |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that *pszCharset* is invalid or cannot be found. <br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Indicates that there is no default character set.<br/>           |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





