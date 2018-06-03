---
title: MimeOleCreateBody function
description: Do not use. On success, creates a new message body.
ms.assetid: d67aebad-6fa4-46e9-aab5-0a1f4d08d023
keywords:
- MimeOleCreateBody function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleCreateBody
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

# MimeOleCreateBody function

Do not use. On success, creates a new message body.

## Syntax


```C++
HRESULT MimeOleCreateBody(
  _Out_ IMimeBody **ppBody
);
```



## Parameters

<dl> <dt>

*ppBody* \[out\]
</dt> <dd>

Type: **[**IMimeBody**](oe-imimebody.md)\*\***

Receives the address of a pointer to a new [**IMimeBody**](oe-imimebody.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                      |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**NOERROR**</dt> </dl>        | The table is initialized. <br/>            |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | An attempt to allocate memory failed.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates *ppBody* is **NULL**.<br/>       |



 

## Remarks

> [!Note]  
> Caller of function is responsible for freeing [**IMimeBody**](oe-imimebody.md) object.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





