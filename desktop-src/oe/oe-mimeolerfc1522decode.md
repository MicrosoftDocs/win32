---
title: MimeOleRfc1522Decode function
description: Do not use. Decodes an RFC 1522 encoded string and, if found, stores the name of the character set contained in the encoded string.
ms.assetid: '08a6c69a-1a1d-42b2-8659-47ed4ef15293'
keywords: ["MimeOleRfc1522Decode function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleRfc1522Decode
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleRfc1522Decode function

Do not use. Decodes an [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoded string and, if found, stores the name of the character set contained in the encoded string.

## Syntax


```C++
HRESULT MimeOleRfc1522Decode(
  _In_    LPCSTR pszValue,
  _Inout_ LPSTR  pszCharset,
  _In_    ULONG  cchmax,
  _Out_   LPSTR  *ppszDecoded
);
```



## Parameters

<dl> <dt>

*pszValue* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoded string.

</dd> <dt>

*pszCharset* \[in, out\]
</dt> <dd>

Type: **LPSTR**

If found, receives the name of the character set contained in the [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding.

</dd> <dt>

*cchmax* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that contains the maximum number of characters that can be copied into *pszCharset*.

</dd> <dt>

*ppszDecoded* \[out\]
</dt> <dd>

Type: **LPSTR\***

If not **NULL**, receives a pointer to an **LPSTR** that contains the [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) decoded string. Note: this parameter must have been initialized to point to a valid **LPSTR** before this call; also, user is responsible for freeing this pointer.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                 |
|----------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                               |
| <dl> <dt>**S\_FALSE**</dt> </dl>      | Indicates that the conversion failed. <br/>           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pszValue* is **NULL**. <br/>          |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that the character set was not found. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





