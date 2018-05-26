---
title: IMimePropertySet SetProp method
description: Sets the value of the specified property.
ms.assetid: 63775940-7436-4051-993c-db33df4ab97c
keywords:
- SetProp method Windows Mail (formerly Outlook Express)
- SetProp method Windows Mail (formerly Outlook Express) , IMimePropertySet interface
- IMimePropertySet interface Windows Mail (formerly Outlook Express) , SetProp method
topic_type:
- apiref
api_name:
- IMimePropertySet.SetProp
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

# IMimePropertySet::SetProp method

Sets the value of the specified property.

## Syntax


```C++
HRESULT SetProp(
  [in] LPCSTR         pszName,
  [in] DWORD          dwFlags,
  [in] LPCPROPVARIANT pValue
);
```



## Parameters

<dl> <dt>

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



| Return code                                                                                                   | Description                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                          | Indicates success.<br/>                                                                                                                                                                                                                                                              |
| <dl> <dt>**E\_FAIL**</dt> </dl>                        | Indicates that an unknown error has occurred. <br/>                                                                                                                                                                                                                                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                 | Indicates that an attempt to allocate memory failed.<br/>                                                                                                                                                                                                                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                  | Indicates that *pszName* or *pValue* is **NULL**. Might also indicate that *pValue*-&gt;[vt](https://msdn.microsoft.com/library/windows/desktop/aa380072) specifies a [VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127) that is not supported or that its corresponding member in the PROPVARIANT structure is invalid, such as **NULL** pointer. <br/> |
| <dl> <dt>**MIME\_E\_READ\_ONLY**</dt> </dl>            | Indicates that the property is read-only, that is, the property has the MPF\_READONLY flag set in the property schema. <br/>                                                                                                                                                         |
| <dl> <dt>**MIME\_E\_INVALID\_HEADER\_NAME**</dt> </dl> | Indicates that *pszName* is a new property that contains invalid characters.<br/>                                                                                                                                                                                                    |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl>            | Indicates that *pszName* does not specify an existing property. <br/>                                                                                                                                                                                                                |



 

## Remarks

A property ID can also be passed into this method through the *pszName* parameter using the PIDTOSTR macro.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





