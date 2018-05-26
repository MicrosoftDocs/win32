---
title: IMimeInternational SetDefaultCharset method
description: Sets the default character set for MimeOLE.
ms.assetid: 3f333c53-25e8-4aca-b11f-48fa26bf51fd
keywords:
- SetDefaultCharset method Windows Mail (formerly Outlook Express)
- SetDefaultCharset method Windows Mail (formerly Outlook Express) , IMimeInternational interface
- IMimeInternational interface Windows Mail (formerly Outlook Express) , SetDefaultCharset method
topic_type:
- apiref
api_name:
- IMimeInternational.SetDefaultCharset
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

# IMimeInternational::SetDefaultCharset method

Sets the default character set for MimeOLE.

## Syntax


```C++
HRESULT SetDefaultCharset(
  [in] HCHARSET hCharset
);
```



## Parameters

<dl> <dt>

*hCharset* \[in\]
</dt> <dd>

Type: **HCHARSET**

Specifies the handle of the character set.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                 |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                               |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *hCharset* is **NULL**. <br/>          |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hCharset* is an invalid handle. <br/> |



 

## Remarks

The default character set is used for messages without character set information. When MimeOLE is initialized, it automatically computes the default character set using the local system code page.

MimeOLE supports only a single global character set for an instance of MimeOLE.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





