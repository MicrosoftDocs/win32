---
title: IMimeMessageTree SetBodyProp method
description: Sets the value of a property for a specified body.
ms.assetid: b1c4c77f-a5c8-4e3c-91c5-17bbcd4581af
keywords:
- SetBodyProp method Windows Mail (formerly Outlook Express)
- SetBodyProp method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , SetBodyProp method
topic_type:
- apiref
api_name:
- IMimeMessageTree.SetBodyProp
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

# IMimeMessageTree::SetBodyProp method

Sets the value of a property for a specified body.

## Syntax


```C++
HRESULT SetBodyProp(
  [in] HBODY          hBody,
  [in] LPCSTR         pszName,
  [in] DWORD          dwFlags,
  [in] LPCPROPVARIANT pValue
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

Specifies a bitmask that affects how the property value is stored.



| Value                                                                                                                                                                                                                                  | Meaning                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PDF_ENCODED"></span><span id="pdf_encoded"></span><dl> <dt>**PDF\_ENCODED**</dt> <dt>0x00000001</dt> </dl>                | Indicates that the value of the property is encoded in an Internet character set and possibly [RFC 1522](http://www.ietf.org/rfc/rfc1522.txt). <br/> |
| <span id="PDF_SAVENOENCODE"></span><span id="pdf_savenoencode"></span><dl> <dt>**PDF\_SAVENOENCODE**</dt> <dt>0x00000010</dt> </dl> | Indicates that when setting an address type header, the property value should not be re-encoded when the header is saved. <br/>                      |



 

</dd> <dt>

*pValue* \[in\]
</dt> <dd>

Type: **LPCPROPVARIANT**

Specifies the value to set for the property.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                   | Description                                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                          | Indicates success. <br/>                                                                                                                                                                                                                                                                                    |
| <dl> <dt>**E\_FAIL**</dt> </dl>                        | Indicates that an unknown error has occurred. <br/>                                                                                                                                                                                                                                                         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                 | Indicates that an attempt to allocate memory failed.<br/>                                                                                                                                                                                                                                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                  | Indicates that *hBody*, *pszName*, or *pValue* is **NULL**. Or, this value may indicate that *pValue*-&gt;[vt](https://msdn.microsoft.com/library/windows/desktop/aa380072) specifies a [VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127) that is unsupported or that its corresponding member in the PROPVARIANT structure is invalid; for example, a **NULL** pointer. <br/> |
| <dl> <dt>**MIME\_E\_READ\_ONLY**</dt> </dl>            | Indicates that the property is read-only, that is, the property has the MPF\_READONLY flag set in the property schema. <br/>                                                                                                                                                                                |
| <dl> <dt>**MIME\_E\_INVALID\_HEADER\_NAME**</dt> </dl> | Indicates that *pszName* is a new property that contains invalid characters. <br/>                                                                                                                                                                                                                          |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl>            | Indicates that *pszName* does not specify an existing property. <br/>                                                                                                                                                                                                                                       |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>              | Indicates that *hBody* is equal to HBODY\_ROOT (0xffffffff) and there is no root body or that the property has no data. <br/>                                                                                                                                                                               |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl>       | Indicates that *hBody* is an invalid handle. <br/>                                                                                                                                                                                                                                                          |



 

## Remarks

A property ID can also be passed into this method through the *pszName* parameter using the PIDTOSTR macro.

MimeOLE supports these variant types: VT\_LPSTR, VT\_LPWSTR, VT\_FILETIME, VT\_UI4, VT\_I4, and VT\_STREAM.

This method is equivalent to:

pMessageTree-&gt;[**BindToObject**](oe-imimemessagetree-bindtoobject.md)(*hBody*, IID\_IMimePropertySet, (LPVOID \*)&pPropertySet);

pPropertySet-&gt;[**SetProp**](oe-imimepropertyset-setprop.md)(*pszName*, *dwFlags*, *pValue*);

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





