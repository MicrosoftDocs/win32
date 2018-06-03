---
title: MimeOleCreateMessageParts function
description: Do not use. On success, creates and initializes a message parts.
ms.assetid: 7f27c48f-05b7-4512-bd4b-16b875ea4af5
keywords:
- MimeOleCreateMessageParts function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleCreateMessageParts
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

# MimeOleCreateMessageParts function

Do not use. On success, creates and initializes a message parts.

## Syntax


```C++
HRESULT MimeOleCreateMessageParts(
  _Out_ IMimeMessageParts **ppParts
);
```



## Parameters

<dl> <dt>

*ppParts* \[out\]
</dt> <dd>

Type: **[**IMimeMessageParts**](oe-imimemessageparts.md)\*\***

Receives the address of a pointer to a new [**IMimeMessageParts**](oe-imimemessageparts.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                    |
|-----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                 |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates *ppParts* is **NULL**.<br/>    |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates memory allocation failed.<br/> |



 

## Remarks

> [!Note]  
> Caller of function is responsible for freeing [**IMimeMessageParts**](oe-imimemessageparts.md) object.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





