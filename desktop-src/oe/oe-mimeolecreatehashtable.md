---
title: MimeOleCreateHashTable function
description: Do not use. On success, creates and initializes a hash table.
ms.assetid: 3992ed63-4720-4364-9208-1b60422466e7
keywords:
- MimeOleCreateHashTable function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleCreateHashTable
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

# MimeOleCreateHashTable function

Do not use. On success, creates and initializes a hash table.

## Syntax


```C++
HRESULT MimeOleCreateHashTable(
  _In_  DWORD      dwSize,
  _In_  BOOL       fDupeKeys,
  _Out_ IHashTable **ppHashTable
);
```



## Parameters

<dl> <dt>

*dwSize* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the desired size of the hash table.

</dd> <dt>

*fDupeKeys* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies whether to allow duplicate keys.

</dd> <dt>

*ppHashTable* \[out\]
</dt> <dd>

Type: **[**IHashTable**](oe-ihashtable.md)\*\***

Receives the address of a pointer to a new [**IHashTable**](oe-ihashtable.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                      |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**NOERROR**</dt> </dl>        | The table is initialized. <br/>            |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | An attempt to allocate memory failed.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates *ppHashTable* is **NULL**.<br/>  |



 

## Remarks

> [!Note]  
> User is responsible for freeing [**IHashTable**](oe-ihashtable.md) object.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





