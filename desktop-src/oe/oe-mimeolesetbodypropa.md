---
title: MimeOleSetBodyPropA function
description: Do not use. Sets the value of a property for a specified body.
ms.assetid: 104718d9-c37c-4c39-be4a-a43cac9a5d1c
keywords:
- MimeOleSetBodyPropA function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleSetBodyPropA
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MimeOleSetBodyPropA function

Do not use. Sets the value of a property for a specified body.

## Syntax


```C++
HRESULT MimeOleSetBodyPropA(
  _In_ IMimeMessageTree *pTree,
  _In_ HBODY            hBody,
  _In_ LPCSTR           pszName,
  _In_ DWORD            dwFlags,
  _In_ LPCSTR           pszData
);
```



## Parameters

<dl> <dt>

*pTree* \[in\]
</dt> <dd>

Type: **[**IMimeMessageTree**](oe-imimemessagetree.md)\***

Specifies a pointer to the [**IMimeMessageTree**](oe-imimemessagetree.md) object.

</dd> <dt>

*hBody* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the handle of the body.

</dd> <dt>

*pszName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the property name or ID.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a bitmask that affects how the property value is stored. See [**SetBodyProp**](oe-imimemessagetree-setbodyprop.md).

</dd> <dt>

*pszData* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the value to set for the property.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                     |
|----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pTree* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**MimeOleSetBodyPropW**](oe-mimeolesetbodypropw.md)
</dt> </dl>

 

 





