---
title: IDatabase CreateStream method
description: Creates a new stream resource inside of the database.
ms.assetid: 72c7ec20-e6ec-4f8b-b62e-72f974fb7568
keywords:
- CreateStream method Windows Mail (formerly Outlook Express)
- CreateStream method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , CreateStream method
topic_type:
- apiref
api_name:
- IDatabase.CreateStream
api_location:
- Directdb.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDatabase::CreateStream method

\[**CreateStream** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates a new stream resource inside of the database.

## Syntax


```C++
HRESULT CreateStream(
  [out] LPFILEADDRESS pfaStart
);
```



## Parameters

<dl> <dt>

*pfaStart* \[out\]
</dt> <dd>

Type: **LPFILEADDRESS**

On success, contains an identifier for the stream to be used with other stream functions in this database.

</dd> </dl>

## Return value

Type: **HRESULT**

Use the SUCCEEDED macro to determine whether the operation succeeded.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





