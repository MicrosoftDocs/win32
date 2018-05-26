---
title: MimeOleGetBodyPropA function
description: Do not use. Gets the value of a property for a specified body.
ms.assetid: 75306d5f-1116-49de-b5b5-35da9312ecd7
keywords:
- MimeOleGetBodyPropA function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGetBodyPropA
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

# MimeOleGetBodyPropA function

Do not use. Gets the value of a property for a specified body.

## Syntax


```C++
HRESULT MimeOleGetBodyPropA(
  _In_  IMimeMessageTree *pTree,
  _In_  HBODY            hBody,
  _In_  LPCSTR           pszName,
  _In_  DWORD            dwFlags,
  _Out_ LPSTR            *ppszData
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

Specifies a bitmask that affects how to get the property value. See [**GetBodyProp**](oe-imimemessagetree-getbodyprop.md).

</dd> <dt>

*ppszData* \[out\]
</dt> <dd>

Type: **LPSTR\***

Returns address of string into which property value is saved. Note: this variable must have been initialized to point to a valid **LPSTR** before this call and user is responsible for freeing **LPSTR**.

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

[**MimeOleGetBodyPropW**](oe-mimeolegetbodypropw.md)
</dt> </dl>

 

 





