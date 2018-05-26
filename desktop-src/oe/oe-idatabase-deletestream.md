---
title: IDatabase DeleteStream method
description: Deletes the stream from the database.
ms.assetid: 29577ee2-501c-46b3-99ef-f457cf404c00
keywords:
- DeleteStream method Windows Mail (formerly Outlook Express)
- DeleteStream method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , DeleteStream method
topic_type:
- apiref
api_name:
- IDatabase.DeleteStream
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

# IDatabase::DeleteStream method

\[**DeleteStream** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Deletes the stream from the database. Can be called even when the stream is currently opened in that case, the stream will be deleted when it is closed.

## Syntax


```C++
HRESULT DeleteStream(
  [in] FILEADDRESS faStart
);
```



## Parameters

<dl> <dt>

*faStart* \[in\]
</dt> <dd>

Type: **FILEADDRESS**

The stream to delete.

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



 

 





