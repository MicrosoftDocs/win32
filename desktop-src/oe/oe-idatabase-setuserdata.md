---
title: IDatabase SetUserData method
description: Allows the caller to set a block of user defined data. Can be retrieved by calling GetUserData.
ms.assetid: 'd7aa1af0-8d38-4d7d-b9da-ca21a8fe85b4'
keywords: ["SetUserData method Windows Mail (formerly Outlook Express)", "SetUserData method Windows Mail (formerly Outlook Express) , IDatabase interface", "IDatabase interface Windows Mail (formerly Outlook Express) , SetUserData method"]
topic_type:
- apiref
api_name:
- IDatabase.SetUserData
api_location:
- Directdb.dll
api_type:
- COM
---

# IDatabase::SetUserData method

Allows the caller to set a block of user defined data. Can be retrieved by calling GetUserData.

## Syntax


```C++
void SetUserData(
  [in] LPVOID pvUserData,
  [in] ULONG  cbUserData
);
```



## Parameters

<dl> <dt>

*pvUserData* \[in\]
</dt> <dd>

Type: **LPVOID**

Specifies the memory location to read the user data from. Should be allocated to at least the size specified by cbUserData.

</dd> <dt>

*cbUserData* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the size of pvUserData.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





