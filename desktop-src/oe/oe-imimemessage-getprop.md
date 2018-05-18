---
title: IMimeMessage GetProp method
description: Gets a property value for the root header of the message.
ms.assetid: '522ea0ac-4896-4388-b879-2b5433c95bf4'
keywords: ["GetProp method Windows Mail (formerly Outlook Express)", "GetProp method Windows Mail (formerly Outlook Express) , IMimeMessage interface", "IMimeMessage interface Windows Mail (formerly Outlook Express) , GetProp method"]
topic_type:
- apiref
api_name:
- IMimeMessage.GetProp
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessage::GetProp method

Gets a property value for the root header of the message.

## Syntax


```C++
HRESULT GetProp(
  [in]      LPCSTR        pszName,
  [in]      DWORD         dwFlags,
  [in, out] LPPROPVARIANT pValue
);
```



## Parameters

<dl> <dt>

*pszName* \[in\]
</dt> <dd>

Type: **LPCSTR**

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
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | Indicates that *pszName* or *pValue* is **NULL**.<br/>                                        |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl>           | Indicates that *pszName* does not identify an existing property. <br/>                        |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>             | Indicates that no data is associated with the property.<br/>                                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                | Indicates that an attempt to allocate memory failed.<br/>                                     |
| <dl> <dt>**MIME\_E\_VARTYPE\_NO\_CONVERT**</dt> </dl> | Indicates that the [VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127) cannot be converted to the requested type.<br/> |



 

## Remarks

A property ID can also be passed into this method through the *pszName* parameter using the PIDTOSTR macro.

MimeOLE supports these variant types: VT\_LPSTR, VT\_LPWSTR, VT\_FILETIME, VT\_UI4, VT\_I4, and VT\_STREAM.

This method is equivalent to:

pMessage-&gt;[**BindToObject**](oe-imimemessagetree-bindtoobject.md)(HBODY\_ROOT, IID\_IMimePropertySet, (LPVOID \*)&pPropertySet);

pPropertySet-&gt;[**GetProp**](oe-imimepropertyset-getprop.md)(*pszName*, *dwFlags*, *pValue*);

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





