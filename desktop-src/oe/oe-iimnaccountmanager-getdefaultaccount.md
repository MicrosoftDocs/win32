---
title: IImnAccountManager GetDefaultAccount method
description: Gets the account object that is the default for the specified account type.
ms.assetid: fe7bf779-51c1-402b-8b0f-36a8cf65c4fb
keywords:
- GetDefaultAccount method Windows Mail (formerly Outlook Express)
- GetDefaultAccount method Windows Mail (formerly Outlook Express) , IImnAccountManager interface
- IImnAccountManager interface Windows Mail (formerly Outlook Express) , GetDefaultAccount method
topic_type:
- apiref
api_name:
- IImnAccountManager.GetDefaultAccount
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

# IImnAccountManager::GetDefaultAccount method

\[**IImnAccountManager::GetDefaultAccount** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Gets the account object that is the default for the specified account type.

## Syntax


```C++
HRESULT GetDefaultAccount(
  [in]  ACCTTYPE    AcctType,
  [out] IImnAccount **ppAccount
);
```



## Parameters

<dl> <dt>

*AcctType* \[in\]
</dt> <dd>

Type: **[**ACCTTYPE**](oe-accttype.md)**

Specifies an [**ACCTTYPE**](oe-accttype.md) value that indicates the type of account.

</dd> <dt>

*ppAccount* \[out\]
</dt> <dd>

Type: **[**IImnAccount**](oe-iimnaccount.md)\*\***

Receives the address of a pointer to the [**IImnAccount**](oe-iimnaccount.md) object found. The client is responsible for releasing this object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                      |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that an account was not found that meets the criteria.<br/>      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *ppAccount* is **NULL** or that *AcctType* is invalid.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





