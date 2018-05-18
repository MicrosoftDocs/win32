---
title: IMimeMessageW SetPropW method
description: Sets a property value for the root header of the message.
ms.assetid: '510ae708-3508-4cba-8919-12f56802bdf9'
keywords: ["SetPropW method Windows Mail (formerly Outlook Express)", "SetPropW method Windows Mail (formerly Outlook Express) , IMimeMessageW interface", "IMimeMessageW interface Windows Mail (formerly Outlook Express) , SetPropW method"]
topic_type:
- apiref
api_name:
- IMimeMessageW.SetPropW
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessageW::SetPropW method

\[**SetPropW** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sets a property value for the root header of the message.

## Syntax


```C++
HRESULT SetPropW(
  [in] LPCWSTR        pwszName,
  [in] DWORD          dwFlags,
  [in] LPCPROPVARIANT pValue
);
```



## Parameters

<dl> <dt>

*pwszName* \[in\]
</dt> <dd>

Type: **LPCWSTR**

Specifies the property name or ID.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a bitmask that affects how the property value is stored.



| Value                                                                                                                                                                  | Meaning                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PDF_ENCODED"></span><span id="pdf_encoded"></span><dl> <dt>**PDF\_ENCODED**</dt> </dl>                | The value of the property is encoded in an Internet character set and possibly RFC1522. Used in both getting and setting a property.<br/> |
| <span id="PDF_NAMEINDATA"></span><span id="pdf_nameindata"></span><dl> <dt>**PDF\_NAMEINDATA**</dt> </dl>       | The name of the property must be prefixed to the property value.<br/>                                                                     |
| <span id="PDF_HEADERFORMAT"></span><span id="pdf_headerformat"></span><dl> <dt>**PDF\_HEADERFORMAT**</dt> </dl> | The value should be formatted according to RFC822 (character set encoded, wrapped, etc.).<br/>                                            |
| <span id="PDF_NOCOMMENTS"></span><span id="pdf_nocomments"></span><dl> <dt>**PDF\_NOCOMMENTS**</dt> </dl>       | Any comments embedded in the value must be stripped out.<br/>                                                                             |
| <span id="PDF_SAVENOENCODE"></span><span id="pdf_savenoencode"></span><dl> <dt>**PDF\_SAVENOENCODE**</dt> </dl> | When the header is saved, this value must not be re-encoded.<br/>                                                                         |
| <span id="PDF_VECTOR"></span><span id="pdf_vector"></span><dl> <dt>**PDF\_VECTOR**</dt> </dl>                   | If the property appears multiple times, the values are concatenated together (separated by carriage-return line feeds).<br/>              |



 

</dd> <dt>

*pValue* \[in\]
</dt> <dd>

Type: **LPCPROPVARIANT**

Specifies the value to set for the property.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                   | Description                                                                                                                                                                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                          | Indicates success.<br/>                                                                                                                                                                                                                                                             |
| <dl> <dt>**E\_FAIL**</dt> </dl>                        | Indicates that an unknown error has occurred. <br/>                                                                                                                                                                                                                                 |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                 | Indicates that an attempt to allocate memory failed.<br/>                                                                                                                                                                                                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                  | Indicates that *pwszName* or *pValue* is **NULL**. Also may indicate that *pValue*-&gt;[vt](https://msdn.microsoft.com/library/windows/desktop/aa380072) specifies a [VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127) that is not supported or that its corresponding member in the PROPVARIANT structure is invalid, such as **NULL** pointer. <br/> |
| <dl> <dt>**MIME\_E\_READ\_ONLY**</dt> </dl>            | Indicates that the property is read-only, that is, the property has the MPF\_READONLY flag set in the property schema. <br/>                                                                                                                                                        |
| <dl> <dt>**MIME\_E\_INVALID\_HEADER\_NAME**</dt> </dl> | Indicates that *pwszName* is a new property that contains invalid characters.<br/>                                                                                                                                                                                                  |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl>            | Indicates that *pwszName* specifies a property ID that does not exist in the property schema.<br/>                                                                                                                                                                                  |



 

## Remarks

MIMEOLE supports these variant types: VT\_LPSTR, VT\_LPWSTR, VT\_FILETIME, VT\_UI4, VT\_I4, and VT\_STREAM.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





