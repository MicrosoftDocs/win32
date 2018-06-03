---
title: IMimeInternational Rfc1522Encode method
description: Encodes a string using RFC 1522 format.
ms.assetid: dcb9b62b-154a-45f9-8be6-115a0a1967db
keywords:
- Rfc1522Encode method Windows Mail (formerly Outlook Express)
- Rfc1522Encode method Windows Mail (formerly Outlook Express) , IMimeInternational interface
- IMimeInternational interface Windows Mail (formerly Outlook Express) , Rfc1522Encode method
topic_type:
- apiref
api_name:
- IMimeInternational.Rfc1522Encode
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

# IMimeInternational::Rfc1522Encode method

Encodes a string using [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) format.

## Syntax


```C++
HRESULT Rfc1522Encode(
  [in]  LPCSTR   pszValue,
  [in]  HCHARSET hCharset,
  [out] LPSTR    *ppszEncoded
);
```



## Parameters

<dl> <dt>

*pszValue* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies a **LPCSTR** that contains the string to encode.

</dd> <dt>

*hCharset* \[in\]
</dt> <dd>

Type: **HCHARSET**

Specifies the handle of the character set to use to encode the string.

</dd> <dt>

*ppszEncoded* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to an **LPSTR** that contains the [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoded string. The client is responsible for freeing this pointer by calling [IMalloc::Free](http://msdn.microsoft.com/library/com/htm/cmi_m_1smd.asp).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                                                                                                                                                      |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                                                                                                                                                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *pszValue*, *hCharset*, or *ppszEncoded* is **NULL**. <br/>                                                                                                                 |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hCharset* is an invalid handle. <br/>                                                                                                                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Indicates that the string could not be converted or that [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding is not needed because there are no 8-bit characters in the string. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>           | Indicates that an attempt to allocate memory failed.<br/>                                                                                                                                  |



 

## Remarks

[RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding is used to prevent 8-bit characters in the header of a message from being transmitted over the Internet. A client does not have to call this method because [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) is explicitly handled when using MimeOLE message objects, such as [**IMimePropertySet**](oe-imimepropertyset.md).

This method also converts *pszValue* to the Internet code page that is specified by *hCharset*. Therefore, it is assumed that *pszValue* is in the Windows code page specified by *hCharset*.

The resulting [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoded string is returned in *ppszEncoded*. The returned string is wrapped (for example, contains carriage returns and line feeds) so that it can persist in the header of a message.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





