---
title: IDatabase GetClientCount method
description: Retrieves the number of clients who currently have this database file open.
ms.assetid: 0a3db40a-3db3-4de3-9a45-7bd5d563c8de
keywords:
- GetClientCount method Windows Mail (formerly Outlook Express)
- GetClientCount method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , GetClientCount method
topic_type:
- apiref
api_name:
- IDatabase.GetClientCount
api_location:
- Directdb.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IDatabase::GetClientCount method

\[**GetClientCount** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the number of clients who currently have this database file open.

## Syntax


```C++
HRESULT GetClientCount(
  [out] LPDWORD pcClients
);
```



## Parameters

<dl> <dt>

*pcClients* \[out\]
</dt> <dd>

Type: **LPDWORD**

On exit, this **DWORD** will contain either 0 (if the database file is not being shared) or the number of clients who have the database open.

</dd> </dl>

## Return value

Type: **HRESULT**

This function will always return S\_OK.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Wmsdkidl.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





