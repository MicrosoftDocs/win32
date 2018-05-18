---
title: IMimeMessageW GetPropW method
description: Gets a property value for the root header of the message.
ms.assetid: '0a99bc7b-1aa2-4edc-b94e-d8d695cf4d72'
keywords: ["GetPropW method Windows Mail (formerly Outlook Express)", "GetPropW method Windows Mail (formerly Outlook Express) , IMimeMessageW interface", "IMimeMessageW interface Windows Mail (formerly Outlook Express) , GetPropW method"]
topic_type:
- apiref
api_name:
- IMimeMessageW.GetPropW
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessageW::GetPropW method

Gets a property value for the root header of the message.

## Syntax


```C++
HRESULT GetPropW(
  [in]      LPCWSTR       pwszName,
  [in]      DWORD         dwFlags,
  [in, out] LPPROPVARIANT pValue
);
```



## Parameters

<dl> <dt>

*pwszName* \[in\]
</dt> <dd>

Type: **LPCWSTR**

Specifies the property name or property ID.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the bitmask that affects how to get the property value.



| Value                                                                                                                                                                  | Meaning                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PDF_ENCODED"></span><span id="pdf_encoded"></span><dl> <dt>**PDF\_ENCODED**</dt> </dl>                | The value of the property is encoded in an Internet character set and possibly RFC1522. Used in both getting and setting a property.<br/> |
| <span id="PDF_NAMEINDATA"></span><span id="pdf_nameindata"></span><dl> <dt>**PDF\_NAMEINDATA**</dt> </dl>       | The name of the property must be prefixed to the property value.<br/>                                                                     |
| <span id="PDF_HEADERFORMAT"></span><span id="pdf_headerformat"></span><dl> <dt>**PDF\_HEADERFORMAT**</dt> </dl> | The value should be formatted according to RFC822 (character set encoded, wrapped, etc.).<br/>                                            |
| <span id="PDF_NOCOMMENTS"></span><span id="pdf_nocomments"></span><dl> <dt>**PDF\_NOCOMMENTS**</dt> </dl>       | Any comments embedded in the value must be stripped out.<br/>                                                                             |
| <span id="PDF_SAVENOENCODE"></span><span id="pdf_savenoencode"></span><dl> <dt>**PDF\_SAVENOENCODE**</dt> </dl> | When the header is saved, this value must not be re-encoded.<br/>                                                                         |
| <span id="PDF_VECTOR"></span><span id="pdf_vector"></span><dl> <dt>**PDF\_VECTOR**</dt> </dl>                   | If the property appears multiple times, the values are concatenated together (separated by carriage return line feeds).<br/>              |



 

</dd> <dt>

*pValue* \[in, out\]
</dt> <dd>

Type: **LPPROPVARIANT**

Receives the value associated with the property. The client must initialize the *pValue*-&gt;[vt](https://msdn.microsoft.com/library/windows/desktop/aa380072) member to a [VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127) that is supported for the corresponding property. The client is responsible for freeing this PROPVARIANT structure by calling [PropVariantClear](http://msdn.microsoft.com/library/stg/stg/propvariantclear.asp) or by freeing pointers by calling [IMalloc::Free](http://msdn.microsoft.com/library/com/htm/cmi_m_1smd.asp).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                  | Description                                                                                         |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                         | Indicates success.<br/>                                                                       |
| <dl> <dt>**E\_FAIL**</dt> </dl>                       | Indicates that an unknown error has occurred. <br/>                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | Indicates that *pwszName* or *pValue* is **NULL**.<br/>                                       |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl>           | Indicates that *pwszName* does not identify an existing property. <br/>                       |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>             | Indicates that no data is associated with the property.<br/>                                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                | Indicates that an attempt to allocate memory failed.<br/>                                     |
| <dl> <dt>**MIME\_E\_VARTYPE\_NO\_CONVERT**</dt> </dl> | Indicates that the [VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127) cannot be converted to the requested type.<br/> |



 

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



 

 





