---
title: MimeOleGetPropW function
description: Do not use. Gets the Unicode value of the specified property.
ms.assetid: db2d848e-c753-480c-91a5-eb04d8321a31
keywords:
- MimeOleGetPropW function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGetPropW
- MimeOleGetPropW
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

# MimeOleGetPropW function

Do not use. Gets the Unicode value of the specified property.

## Syntax


```C++
HRESULT MimeOleGetPropW(
  _In_  IMimePropertySet *pPropertyset,
  _In_  LPCSTR           pszName,
  _In_  DWORD            dwFlags,
  _Out_ LPWSTR           *ppszData
);
```



## Parameters

<dl> <dt>

*pPropertyset* \[in\]
</dt> <dd>

Type: **[**IMimePropertySet**](oe-imimepropertyset.md)\***

Specifies a pointer to an [**IMimePropertySet**](oe-imimepropertyset.md) object.

</dd> <dt>

*pszName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the property name or ID.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a bitmask that affects how to get the property value. See [**GetProp**](oe-imimepropertyset-getprop.md).

</dd> <dt>

*ppszData* \[out\]
</dt> <dd>

Type: **LPWSTR\***

Receives the value associated with the property. Note: this variable must have been initialized to point to a valid **LPWSTR** before this call and user is responsible for freeing what is pointed to by this parameter.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                   | Description                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                          | Indicates success. <br/>                                                                                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>                        | Indicates that an unknown error has occurred. <br/>                                                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                  | Indicates that a pointer argument is **NULL**. <br/>                                                                    |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl>            | Indicates that *pszName* does not specify an existing property. <br/>                                                   |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>              | Indicates that no data is associated with the property. <br/>                                                           |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                 | Indicates that an attempt to allocate memory failed.<br/>                                                               |
| <dl> <dt>**MIME\_E\_INVALID\_HEADER\_NAME**</dt> </dl> | Indicates that *pszName* is invalid according to the [RFC 822](http://www.ietf.org/rfc/rfc822.txt) specification. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |
| Unicode and ANSI names<br/>   | **MimeOleGetPropW** (Unicode)<br/>                                                                       |



 

 





