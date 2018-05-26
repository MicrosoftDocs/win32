---
title: IDatabase Unlock method
description: Unlocks the message database to prevent usage by other callers.
ms.assetid: 686b4977-f47f-4264-8452-f4add738f828
keywords:
- Unlock method Windows Mail (formerly Outlook Express)
- Unlock method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , Unlock method
topic_type:
- apiref
api_name:
- IDatabase.Unlock
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

# IDatabase::Unlock method

\[**Unlock** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Unlocks the message database to prevent usage by other callers.

## Syntax


```C++
HRESULT Unlock(
  [in] LPHLOCK phLock
);
```



## Parameters

<dl> <dt>

*phLock* \[in\]
</dt> <dd>

Type: **LPHLOCK**

Specifies a handle that was received from the Lock method.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                              | Description                                |
|------------------------------------------------------------------------------------------|--------------------------------------------|
| <dl> <dt>**SUCCEEDED**</dt> </dl> | The database has been Unlocked.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





