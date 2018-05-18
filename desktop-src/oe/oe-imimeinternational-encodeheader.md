---
title: IMimeInternational EncodeHeader method
description: Encodes a message header string.
ms.assetid: '2c946961-cd2b-4fcc-857a-6318653af8bf'
keywords: ["EncodeHeader method Windows Mail (formerly Outlook Express)", "EncodeHeader method Windows Mail (formerly Outlook Express) , IMimeInternational interface", "IMimeInternational interface Windows Mail (formerly Outlook Express) , EncodeHeader method"]
topic_type:
- apiref
api_name:
- IMimeInternational.EncodeHeader
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeInternational::EncodeHeader method

Encodes a message header string.

## Syntax


```C++
HRESULT EncodeHeader(
  [in]      HCHARSET      hCharset,
  [in]      LPPROPVARIANT pData,
  [out]     LPSTR         *ppszEncoded,
  [in, out] LPRFC1522INFO pRfc1522Info
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

Encoding converts the header string to a Internet code page and may apply [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding if the header contains 8-bit characters.

If *hCharset* is **NULL**, the default header character set is used to convert the header to an Internet code page.

The valid values for *pData*-&gt;[vt](https://msdn.microsoft.com/library/windows/desktop/aa380072) include VT\_LPSTR or VT\_LPWSTR. If the header is going to be encoded into 7-bit Unicode Transformation Format (UTF-7) or 8-bit Unicode Transformation Format (UTF-8), the client should use VT\_LPWSTR to pass the header text into this method to minimize data loss.

When *pRfc1522Info*-&gt;**fRfc1522Allowed** is **FALSE**, MimeOLE does not attempt to encode the header using [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt). [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) should not be used in non-MIME messages.

When *pRfc1522Info*-&gt;**fRfc1522Allowed** is equal to **TRUE**, and *pRfc1522Info*-&gt;**fAllow8bit** is set to **TRUE**, MimeOLE does not attempt to encode the header using [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt).

When *pRfc1522Info* is **NULL**, MimeOLE defaults *pRfc1522Info*-&gt;**fRfc1522Allowed** to **TRUE** and *pRfc1522Info*-&gt;**fAllow8bit** to **FALSE**.

When [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding is used to encode the header, *pRfc1522Info*-&gt;**fRfc1522Used** is set to **TRUE**. Otherwise, it is set to **FALSE**.

When the header is going to be encoded into UTF-7 or UTF-8, it is always encoded using [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt), no matter what *pRfc1522Info* specifies.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





