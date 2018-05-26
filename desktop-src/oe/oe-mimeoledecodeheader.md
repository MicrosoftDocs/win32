---
title: MimeOleDecodeHeader function
description: Do not use. Decodes a message header string.
ms.assetid: 54c71463-7004-4bfd-82d3-73dc2553a6eb
keywords:
- MimeOleDecodeHeader function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleDecodeHeader
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MimeOleDecodeHeader function

Do not use. Decodes a message header string.

## Syntax


```C++
HRESULT MimeOleDecodeHeader(
  _In_    HCHARSET      hCharset,
  _In_    LPCSTR        pszData,
  _Out_   LPPROPVARIANT pDecoded,
  _Inout_ LPRFC1522INFO pRfc1522Info
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

Specifies an **LPCSTR** that contains the header to decode.

</dd> <dt>

*pDecoded* \[out\]
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
| <dl> <dt>**E\_FAIL**</dt> </dl>                       | Indicates that *hCharset* is **NULL** and that an appropriate character set in which to decode the header cannot be identified. <br/>          |
| <dl> <dt>**MIME\_S\_NO\_CHARSET\_CONVERT**</dt> </dl> | Indicates that a character set conversion failed or was not performed on the header.<br/>                                                      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                | Indicates that an attempt to allocate memory failed.<br/>                                                                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | Indicates that *pszData* or *pDecoded* is **NULL** or that *pDecoded*-&gt;[vt](https://msdn.microsoft.com/library/windows/desktop/aa380072) is not equal to VT\_LPSTR ro VT\_LPWSTR. <br/> |



 

## Remarks

See [**DecodeHeader**](oe-imimeinternational-decodeheader.md) for more information.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





