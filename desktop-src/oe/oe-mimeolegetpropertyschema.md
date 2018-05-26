---
title: MimeOleGetPropertySchema function
description: Do not use. Returns an interface used to manipulate MimeOLEs global property schema.
ms.assetid: 47486934-3f0c-477b-84c8-27cbc34b69c7
keywords:
- MimeOleGetPropertySchema function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGetPropertySchema
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

# MimeOleGetPropertySchema function

Do not use. Returns an interface used to manipulate MimeOLE's global property schema.

## Syntax


```C++
HRESULT MimeOleGetPropertySchema(
  _Out_ IMimePropertySchema **ppSchema
);
```



## Parameters

<dl> <dt>

*ppSchema* \[out\]
</dt> <dd>

Type: **[**IMimePropertySchema**](oe-imimepropertyschema.md)\*\***

Receives the address of a pointer to an [**IMimePropertySchema**](oe-imimepropertyschema.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                 |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that a pointer parameter is **NULL**. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an allocation failed. <br/>            |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





