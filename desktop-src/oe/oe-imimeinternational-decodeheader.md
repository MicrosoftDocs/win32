---
title: IMimeInternational DecodeHeader method
description: Decodes a message header string.
ms.assetid: f1708656-572c-4788-8c73-71499aa149e5
keywords:
- DecodeHeader method Windows Mail (formerly Outlook Express)
- DecodeHeader method Windows Mail (formerly Outlook Express) , IMimeInternational interface
- IMimeInternational interface Windows Mail (formerly Outlook Express) , DecodeHeader method
topic_type:
- apiref
api_name:
- IMimeInternational.DecodeHeader
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

# IMimeInternational::DecodeHeader method

Decodes a message header string.

## Syntax


```C++
HRESULT DecodeHeader(
  [in]      HCHARSET      hCharset,
  [in]      LPCSTR        pszData,
  [in, out] LPPROPVARIANT pDecoded,
  [in, out] LPRFC1522INFO pRfc1522Info
);
```



## Parameters

<dl> <dt>

*hCharset* \[in\]
</dt> <dd>

Type: **HCHARSET**

Specifies the handle of the character set to use to decode the header text.

</dd> <dt>

*pszData* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies a **LPCSTR** that contains the header to decode.

</dd> <dt>

*pDecoded* \[in, out\]
</dt> <dd>

Type: **LPPROPVARIANT**

Receives a pointer to the [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072) structure that contains the decoded header.

</dd> <dt>

*pRfc1522Info* \[in, out\]
</dt> <dd>

Type: **LPRFC1522INFO**

Receives a pointer to the [**RFC1522INFO**](oe-rfc1522info.md) structure that contains [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding information for the header.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                  | Description                                                                                                                                          |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                         | Indicates success.<br/>                                                                                                                        |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl>      | Indicates that *hCharset* is an invalid handle. <br/>                                                                                          |
| <dl> <dt>**E\_FAIL**</dt> </dl>                       | Indicates that *hCharset* is **NULL** and an appropriate character set cannot be identified to decode the header in. <br/>                     |
| <dl> <dt>**MIME\_S\_NO\_CHARSET\_CONVERT**</dt> </dl> | Indicates that a character set conversion failed or was not performed on the header. <br/>                                                     |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                | Indicates that an attempt to allocate memory failed.<br/>                                                                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | Indicates that *pszData* or *pDecoded* is **NULL** or that *pDecoded*-&gt;[vt](https://msdn.microsoft.com/library/windows/desktop/aa380072) is not equal to VT\_LPSTR ro VT\_LPWSTR. <br/> |



 

## Remarks

The header is passed in *pszData*. If the header was encoded using [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt), the [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding is removed and information about the [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding is returned in *pRfc1522Info*. When the header is decoded successfully, it is returned in *pDecoded*. The header is converted from an Internet code page to the Windows code page as specified by *hCharset*.

If *hCharset* is **NULL** and the header is encoded in [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt), the character set from the [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding is used to translate the header. Otherwise, if *hCharset* is **NULL** and the string is not encoded in [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt), the default character set is used to translate the header.

If *hCharset* is not **NULL**, *hCharset* is always used to translate the header to a Windows code page, even if the header is encoded in [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt). This overrides the character set contained in the [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding.

If the header was encoded in [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt), *pRfc1522Info*-&gt;**fRfc1522Used** is set to **TRUE** and *pRfc1522Info*-&gt;**hRfc1522Cset** is set to the character set that was contained in the [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoding. Otherwise, if the header was not [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt) encoded, *pRfc1522Info*-&gt;**fRfc1522Used** is set to **FALSE** and *pRfc1522Info*-&gt;**hRfc1522Cset** is set to **NULL**.

The valid values for *pDecoded*-&gt;[vt](https://msdn.microsoft.com/library/windows/desktop/aa380072) include VT\_LPSTR or VT\_LPWSTR. If VT\_LPWSTR is specified, MimeOLE decodes the header into a Unicode string. Using VT\_LPWSTR is optimal because if a string is encoded in Unicode Transformation Format (UTF), there is no data loss during decoding.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





