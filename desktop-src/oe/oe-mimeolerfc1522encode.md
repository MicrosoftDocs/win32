---
title: MimeOleRfc1522Encode function
description: Do not use. Encodes a string using RFC 1522 format.
ms.assetid: 1de39074-8e03-4c65-af3a-835b81c5f133
keywords:
- MimeOleRfc1522Encode function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleRfc1522Encode
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MimeOleRfc1522Encode function

Do not use. Encodes a string using [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) format.

## Syntax


```C++
HRESULT MimeOleRfc1522Encode(
  _In_  LPCSTR   pszValue,
  _In_  HCHARSET pszCharset,
  _Out_ LPSTR    *ppszEncoded
);
```



## Parameters

<dl> <dt>

*pszValue* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies a **LPCSTR** that contains the string to encode.

</dd> <dt>

*pszCharset* \[in\]
</dt> <dd>

Type: **HCHARSET**

Specifies the handle of the character set to use to encode the string.

</dd> <dt>

*ppszEncoded* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to an **LPSTR** that contains the [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoded string. Note: this variable must have been initialized to point to a valid **LPSTR** before this call. Note: on success, user is responsible for freeing this pointer.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                                                                                                                                                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that a pointer parameter is **NULL**. <br/>                                                                                                                                       |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates an invalid handle. <br/>                                                                                                                                                          |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Indicates that the string could not be converted, or that [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding is not needed because there are no 8-bit characters in the string. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>           | Indicates that an attempt to allocate memory failed.<br/>                                                                                                                                   |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





