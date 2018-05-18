---
title: IMimeMessageTree GetBodyProp method
description: Gets the value of a property for a specified body.
ms.assetid: '94d68db5-14b1-489e-8b87-5864490553d3'
keywords: ["GetBodyProp method Windows Mail (formerly Outlook Express)", "GetBodyProp method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface", "IMimeMessageTree interface Windows Mail (formerly Outlook Express) , GetBodyProp method"]
topic_type:
- apiref
api_name:
- IMimeMessageTree.GetBodyProp
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessageTree::GetBodyProp method

Gets the value of a property for a specified body.

## Syntax


```C++
HRESULT GetBodyProp(
  [in]      HBODY         hBody,
  [in]      LPCSTR        pszName,
  [in]      DWORD         dwFlags,
  [in, out] LPPROPVARIANT pValue
);
```



## Parameters

<dl> <dt>

*hBody* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the handle of the body. Use HBODY\_ROOT (0xffffffff) to indicate the root body.

</dd> <dt>

*pszName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the property name or ID.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a bitmask that affects how to get the property value.



| Value                                                                                                                                                                                                                                                | Meaning                                                                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PDF_ENCODED"></span><span id="pdf_encoded"></span><dl> <dt>**PDF\_ENCODED**</dt> <dt>0x00000001</dt> </dl>                              | Indicates that the value of the property is encoded in an Internet character set and possibly [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt). <br/>                          |
| <span id="PDF_NAMEINDATA"></span><span id="pdf_nameindata"></span><dl> <dt>**PDF\_NAMEINDATA**</dt> <dt>0x00000002</dt> </dl>                     | Indicates that when getting the property value, the name of the property should be prefixed to the value.<br/>                                                                |
| <span id="PDF_HEADERFORMAT"></span><span id="pdf_headerformat"></span><dl> <dt>**PDF\_HEADERFORMAT**</dt> <dt>0x00000004\|PDF\_ENCODED</dt> </dl> | Indicates that when getting the property value, the value should be in [RFC 822](http://www.ietf.org/rfc/rfc822.txt) format. <br/>                                            |
| <span id="PDF_NOCOMMENTS"></span><span id="pdf_nocomments"></span><dl> <dt>**PDF\_NOCOMMENTS**</dt> <dt>0x00000008</dt> </dl>                     | Indicates that when getting the property value, any comments embedded in the value should be stripped out. <br/>                                                              |
| <span id="PDF_VECTOR"></span><span id="pdf_vector"></span><dl> <dt>**PDF\_VECTOR**</dt> <dt>0x00000020</dt> </dl>                                 | Indicates that when getting the value for a property that appears more than once, the values should be concatenated together (separated by carriage return line feeds). <br/> |



 

</dd> <dt>

*pValue* \[in, out\]
</dt> <dd>

Type: **LPPROPVARIANT**

Receives the value associated with the property. The client must initialize the *pValue*-&gt;[vt](https://msdn.microsoft.com/library/windows/desktop/aa380072) member to a [VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127) that is supported for the corresponding property. The client is responsible for freeing this PROPVARIANT structure by calling [PropVariantClear](http://msdn.microsoft.com/library/stg/stg/propvariantclear.asp) or by freeing pointers by calling [IMalloc::Free](http://msdn.microsoft.com/library/com/htm/cmi_m_1smd.asp).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                  | Description                                                                                          |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                         | Indicates success. <br/>                                                                       |
| <dl> <dt>**E\_FAIL**</dt> </dl>                       | Indicates that an unknown error has occurred. <br/>                                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | Indicates that *hBody*, *pszName*, or *pValue* is **NULL**. <br/>                              |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>             | Indicates that *hBody* is equal to HBODY\_ROOT (0xffffffff) and there is no root body. <br/>   |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl>      | Indicates that *hBody* is an invalid handle. <br/>                                             |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl>           | Indicates that *pszName* does not specify an existing property. <br/>                          |
| <dl> <dt>**MIME\_E\_VARTYPE\_NO\_CONVERT**</dt> </dl> | Indicates that the [VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127) cannot be converted to the requested type. <br/> |



 

## Remarks

A property ID can also be passed into this method through the *pszName* parameter using the PIDTOSTR macro.

MimeOLE supports these variant types: VT\_LPSTR, VT\_LPWSTR, VT\_FILETIME, VT\_UI4, VT\_I4, and VT\_STREAM.

This method is equivalent to:

pMessageTree-&gt;[**BindToObject**](oe-imimemessagetree-bindtoobject.md)(*hBody*, IID\_IMimePropertySet, (LPVOID \*)&pPropertySet);

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



 

 





