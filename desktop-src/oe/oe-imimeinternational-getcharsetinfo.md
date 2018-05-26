---
title: IMimeInternational GetCharsetInfo method
description: Gets information about the specified character set.
ms.assetid: 98cb27d6-037d-49d8-b0ad-40b63e07a975
keywords:
- GetCharsetInfo method Windows Mail (formerly Outlook Express)
- GetCharsetInfo method Windows Mail (formerly Outlook Express) , IMimeInternational interface
- IMimeInternational interface Windows Mail (formerly Outlook Express) , GetCharsetInfo method
topic_type:
- apiref
api_name:
- IMimeInternational.GetCharsetInfo
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

# IMimeInternational::GetCharsetInfo method

Gets information about the specified character set.

## Syntax


```C++
HRESULT GetCharsetInfo(
  [in]      HCHARSET       hCharset,
  [in, out] LPINETCSETINFO pCsetInfo
);
```



## Parameters

<dl> <dt>

*hCharset* \[in\]
</dt> <dd>

Type: **HCHARSET**

Specifies the handle of the character set.

</dd> <dt>

*pCsetInfo* \[in, out\]
</dt> <dd>

Type: **LPINETCSETINFO**

Receives a pointer to a [**INETCSETINFO**](oe-inetcsetinfo.md) structure that contains information about the character set.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                       |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *hCharset* or *pCsetInfo* is **NULL**. <br/> |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hCharset* is an invalid handle. <br/>       |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





