---
title: IImnAccountManager GetAccountCount method
description: Counts accounts of the specified type.
ms.assetid: 8c44e230-52b8-4063-ab61-f7c21e15760c
keywords:
- GetAccountCount method Windows Mail (formerly Outlook Express)
- GetAccountCount method Windows Mail (formerly Outlook Express) , IImnAccountManager interface
- IImnAccountManager interface Windows Mail (formerly Outlook Express) , GetAccountCount method
topic_type:
- apiref
api_name:
- IImnAccountManager.GetAccountCount
api_location:
- Msoeacct.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IImnAccountManager::GetAccountCount method

\[**IImnAccountManager::GetAccountCount** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Counts accounts of the specified type.

## Syntax


```C++
HRESULT GetAccountCount(
  [in]  ACCTTYPE AcctType,
  [out] ULONG    *pcServers
);
```



## Parameters

<dl> <dt>

*AcctType* \[in\]
</dt> <dd>

Type: **[**ACCTTYPE**](oe-accttype.md)**

Specifies a value from [**ACCTTYPE**](oe-accttype.md) that indicates the type of account to count.

</dd> <dt>

*pcServers* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the number of accounts found.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                     |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *AcctType* or *pcServers* is invalid.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





