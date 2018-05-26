---
title: IHashTable Find method
description: On success, finds a specified hash table entry.
ms.assetid: 0e556819-9046-4494-a907-af8ad04cf7e6
keywords:
- Find method Windows Mail (formerly Outlook Express)
- Find method Windows Mail (formerly Outlook Express) , IHashTable interface
- IHashTable interface Windows Mail (formerly Outlook Express) , Find method
topic_type:
- apiref
api_name:
- IHashTable.Find
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IHashTable::Find method

\[**IHashTable::Find** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

On success, finds a specified hash table entry.

## Syntax


```C++
HRESULT Find(
  [in]  LPCSTR psz,
  [in]  BOOL   fRemove,
  [out] LPVOID *ppv
);
```



## Parameters

<dl> <dt>

*psz* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies a pointer to the entry to find.

</dd> <dt>

*fRemove* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies whether to remove the found entry.

</dd> <dt>

*ppv* \[out\]
</dt> <dd>

Type: **LPVOID\***

If found, specifies a pointer to the entry.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The entry was found. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





