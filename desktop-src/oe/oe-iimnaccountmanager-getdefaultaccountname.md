---
title: IImnAccountManager GetDefaultAccountName method
description: Gets the account name that is the default for the specified account type.
ms.assetid: 09bcfcb6-f0ef-4bb1-976c-ca9e8cbba690
keywords:
- GetDefaultAccountName method Windows Mail (formerly Outlook Express)
- GetDefaultAccountName method Windows Mail (formerly Outlook Express) , IImnAccountManager interface
- IImnAccountManager interface Windows Mail (formerly Outlook Express) , GetDefaultAccountName method
topic_type:
- apiref
api_name:
- IImnAccountManager.GetDefaultAccountName
api_location:
- Msoeacct.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IImnAccountManager::GetDefaultAccountName method

\[**IImnAccountManager::GetDefaultAccountName** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Gets the account name that is the default for the specified account type.

## Syntax


```C++
HRESULT GetDefaultAccountName(
  [in] ACCTTYPE AcctType,
  [in] LPSTR    pszAccount,
  [in] ULONG    cchMax
);
```



## Parameters

<dl> <dt>

*AcctType* \[in\]
</dt> <dd>

Type: **[**ACCTTYPE**](oe-accttype.md)**

Specifies an [**ACCTTYPE**](oe-accttype.md) value that indicates the type of account.

</dd> <dt>

*pszAccount* \[in\]
</dt> <dd>

Type: **LPSTR**

Specifies a reference pointer to a string that contains the name of the account.

</dd> <dt>

*cchMax* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies the size of the account name. This buffer must allow for at least CCHMAX\_ACCOUNT\_NAME characters.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                        |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                                                     |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that an account was not found that meets the criteria.<br/>        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pszAccount* is **NULL** or that *AcctType* is invalid. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





