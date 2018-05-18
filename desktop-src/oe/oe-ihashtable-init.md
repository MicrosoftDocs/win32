---
title: IHashTable Init method
description: On success, initializes a hash table.
ms.assetid: '861abe4c-ae3e-4fcf-abac-1c557596ab4c'
keywords: ["Init method Windows Mail (formerly Outlook Express)", "Init method Windows Mail (formerly Outlook Express) , IHashTable interface", "IHashTable interface Windows Mail (formerly Outlook Express) , Init method"]
topic_type:
- apiref
api_name:
- IHashTable.Init
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IHashTable::Init method

\[**IHashTable::Init** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

On success, initializes a hash table.

## Syntax


```C++
HRESULT Init(
  [in] DWORD dwSize,
  [in] BOOL  fDupeKeys
);
```



## Parameters

<dl> <dt>

*dwSize* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the desired hash table size.

</dd> <dt>

*fDupeKeys* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies whether to allow duplicate keys.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                      |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**NOERROR**</dt> </dl>        | The table is initialized. <br/>            |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | An attempt to allocate memory failed.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





