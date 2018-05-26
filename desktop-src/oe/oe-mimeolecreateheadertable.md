---
title: MimeOleCreateHeaderTable function
description: Do not use. On success, creates and initializes a header table.
ms.assetid: 05539f5b-768c-401c-9927-c2661276f392
keywords:
- MimeOleCreateHeaderTable function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleCreateHeaderTable
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

# MimeOleCreateHeaderTable function

Do not use. On success, creates and initializes a header table.

## Syntax


```C++
HRESULT MimeOleCreateHeaderTable(
  _Out_ IMimeHeaderTable **ppTable
);
```



## Parameters

<dl> <dt>

*ppTable* \[out\]
</dt> <dd>

Type: **[**IMimeHeaderTable**](oe-imimeheadertable.md)\*\***

On success, receives address of pointer to a new header table.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                 |
|----------------------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates *ppTable* is **NULL**.<br/> |



 

## Remarks

> [!Note]  
> Caller of function is responsible for freeing [**IMimeHeaderTable**](oe-imimeheadertable.md) object.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





