---
title: IImnAccount GetAccountType method
description: Retrieves the type of the account.
ms.assetid: 851b63b9-c876-48f3-ac51-f549b033662f
keywords:
- GetAccountType method Windows Mail (formerly Outlook Express)
- GetAccountType method Windows Mail (formerly Outlook Express) , IImnAccount interface
- IImnAccount interface Windows Mail (formerly Outlook Express) , GetAccountType method
topic_type:
- apiref
api_name:
- IImnAccount.GetAccountType
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

# IImnAccount::GetAccountType method

\[**IImnAccount::GetAccountType** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the type of the account.

## Syntax


```C++
HRESULT GetAccountType(
  [out] ACCTTYPE *pAcctType
);
```



## Parameters

<dl> <dt>

*pAcctType* \[out\]
</dt> <dd>

Type: **[**ACCTTYPE**](oe-accttype.md)\***

Receives a pointer to the [**ACCTTYPE**](oe-accttype.md) structure that contains the account type.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                         |
|----------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pAcctType* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





