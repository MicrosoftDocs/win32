---
title: MimeOleCreateWebDocument function
description: Do not use. On success, creates and initializes a new Web document.
ms.assetid: cf0b89ef-40dc-47c0-a7e2-d28dbab4ab45
keywords:
- MimeOleCreateWebDocument function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleCreateWebDocument
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

# MimeOleCreateWebDocument function

Do not use. On success, creates and initializes a new Web document.

## Syntax


```C++
HRESULT MimeOleCreateWebDocument(
  _In_  LPCSTR           pszBase,
  _In_  LPCSTR           pszURL,
  _Out_ IMimeWebDocument **ppDocument
);
```



## Parameters

<dl> <dt>

*pszBase* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies pointer to a **null**-terminated string containing the name of the base file.

</dd> <dt>

*pszURL* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies pointer to a **null**-terminated string containing the URL.

</dd> <dt>

*ppDocument* \[out\]
</dt> <dd>

Type: **[**IMimeWebDocument**](oe-imimewebdocument.md)\*\***

Receives the address of a pointer to a new [**IMimeWebDocument**](oe-imimewebdocument.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates attempt to allocate memory failed.<br/>          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates an incoming pointer parameter was **NULL**.<br/> |



 

## Remarks

> [!Note]  
> Caller of function is responsible for freeing [**IMimeWebDocument**](oe-imimewebdocument.md) object.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





