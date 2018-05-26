---
title: MimeOleSetPropW function
description: Do not use. Sets the Unicode value of the specified property.
ms.assetid: d832c713-b4ee-4f04-906e-94fa7808ca18
keywords:
- MimeOleSetPropW function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleSetPropW
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

# MimeOleSetPropW function

Do not use. Sets the Unicode value of the specified property.

## Syntax


```C++
HRESULT MimeOleSetPropW(
  _In_ IMimePropertySet *pPropertyset,
  _In_ LPCSTR           pszName,
  _In_ DWORD            dwFlags,
  _In_ LPWSTR           pszData
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

Specifies a bitmask that affects how to set the property value. See [**SetProp**](oe-imimepropertyset-setprop.md).

</dd> <dt>

*pszData* \[in\]
</dt> <dd>

Type: **LPWSTR**

Specifies the value to set for the property.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                   | Description                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                          | Indicates success.<br/>                                                                                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>                        | Indicates that an unknown error has occurred. <br/>                                                                          |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                 | Indicates that an attempt to allocate memory failed.<br/>                                                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                  | Indicates that a pointer argument is **NULL**. See [**SetProp**](oe-imimepropertyset-setprop.md). <br/>                     |
| <dl> <dt>**MIME\_E\_READ\_ONLY**</dt> </dl>            | Indicates that the property is read-only, that is, the property has the MPF\_READONLY flag set in the property schema. <br/> |
| <dl> <dt>**MIME\_E\_INVALID\_HEADER\_NAME**</dt> </dl> | Indicates that *pszName* is a new property that contains invalid characters.<br/>                                            |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl>            | Indicates that *pszName* does not specify an existing property. <br/>                                                        |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





