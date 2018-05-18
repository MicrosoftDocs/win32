---
title: MimeOleEncodeHeader function
description: Do not use. Encodes a message header string.
ms.assetid: '4306875c-c8fa-4b3c-9a10-b7f8bdd874b5'
keywords: ["MimeOleEncodeHeader function Windows Mail (formerly Outlook Express)"]
topic_type:
- apiref
api_name:
- MimeOleEncodeHeader
api_location:
- Inetcomm.dll
api_type:
- DllExport
---

# MimeOleEncodeHeader function

Do not use. Encodes a message header string.

## Syntax


```C++
HRESULT MimeOleEncodeHeader(
  _In_    HCHARSET      hCharset,
  _In_    LPPROPVARIANT pData,
  _Out_   LPSTR         *ppszEncoded,
  _Inout_ LPRFC1522INFO pRfc1522Info
);
```



## Parameters

<dl> <dt>

*hCharset* \[in\]
</dt> <dd>

Type: **HCHARSET**

Specifies the handle of the character set to use to encode the header.

</dd> <dt>

*pData* \[in\]
</dt> <dd>

Type: **LPPROPVARIANT**

Specifies a pointer to the [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072) structure that contains the header to encode (either *pData*-&gt;pszVal or *pData*-&gt;pwszVal).

</dd> <dt>

*ppszEncoded* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to an **LPSTR** that contains the encoded header. The client is responsible for freeing this pointer by calling [IMalloc::Free](http://msdn.microsoft.com/library/com/htm/cmi_m_1smd.asp).

</dd> <dt>

*pRfc1522Info* \[in, out\]
</dt> <dd>

Type: **LPRFC1522INFO**

Receives a pointer to the [**RFC1522INFO**](oe-rfc1522info.md) structure that contains [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding information for the header.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                                                                                                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *pData* or *ppszEncoded* is **NULL** or that *pData*-&gt;[vt](https://msdn.microsoft.com/library/windows/desktop/aa380072) is not equal to VT\_LPSTR ro VT\_LPWSTR. <br/> |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hCharset* is an invalid handle. <br/>                                                                                        |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Indicates that *hCharset* is **NULL** and an appropriate default character set does not exist. <br/>                                         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>           | Indicates that an attempt to allocate memory failed.<br/>                                                                                    |



 

## Remarks

See [**EncodeHeader**](oe-imimeinternational-encodeheader.md) for more information.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





