---
title: IDatabase GetUserData method
description: Retrieves the data set by the caller in SetUserData.
ms.assetid: a3ea93a4-38f3-44d3-9868-ea1b14053b3a
keywords:
- GetUserData method Windows Mail (formerly Outlook Express)
- GetUserData method Windows Mail (formerly Outlook Express) , IDatabase interface
- IDatabase interface Windows Mail (formerly Outlook Express) , GetUserData method
topic_type:
- apiref
api_name:
- IDatabase.GetUserData
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

# IDatabase::GetUserData method

Retrieves the data set by the caller in SetUserData.

## Syntax


```C++
HRESULT GetUserData(
  [out] LPVOID pvUserData,
  [in]  ULONG  cbUserData
);
```



## Parameters

<dl> <dt>

*pvUserData* \[out\]
</dt> <dd>

Type: **LPVOID**

Specifies the memory location to write the user data to. Should be allocated to at least the size specified by cbUserData.

</dd> <dt>

*cbUserData* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the size of pvUserData.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                              | Description                                                      |
|------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**SUCCEEDED**</dt> </dl> | Indicates the record has been successfully retrieved.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Directdb.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Directdb.dll (version 6.0 or later)</dt> </dl> |



 

 





