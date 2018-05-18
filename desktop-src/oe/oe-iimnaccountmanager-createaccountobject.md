---
title: IImnAccountManager CreateAccountObject method
description: Creates an empty account object.
ms.assetid: '15c2cc00-ea80-4bd5-bc49-eb28a6d8bcac'
keywords: ["CreateAccountObject method Windows Mail (formerly Outlook Express)", "CreateAccountObject method Windows Mail (formerly Outlook Express) , IImnAccountManager interface", "IImnAccountManager interface Windows Mail (formerly Outlook Express) , CreateAccountObject method"]
topic_type:
- apiref
api_name:
- IImnAccountManager.CreateAccountObject
api_location:
- Msoeacct.dll
api_type:
- COM
---

# IImnAccountManager::CreateAccountObject method

\[**IImnAccountManager::CreateAccountObject** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates an empty account object.

## Syntax


```C++
HRESULT CreateAccountObject(
  [in]  ACCTTYPE    AcctType,
  [out] IImnAccount **ppAccount
);
```



## Parameters

<dl> <dt>

*AcctType* \[in\]
</dt> <dd>

Type: **[**ACCTTYPE**](oe-accttype.md)**

Specifies an [**ACCTTYPE**](oe-accttype.md) structure that contains the account type to create.

</dd> <dt>

*ppAccount* \[out\]
</dt> <dd>

Type: **[**IImnAccount**](oe-iimnaccount.md)\*\***

Receives the address of a pointer to the new [**IImnAccount**](oe-iimnaccount.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                            |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                                         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/>                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppAccount* is **NULL** or that *AcctType* is out of range. <br/> |



 

## Remarks

A client should use this method to add a new account.

A client can use the property interface of [**IImnAccount**](oe-iimnaccount.md) to set the properties of the new account and then call [**SaveChanges**](oe-iimnaccount-savechanges.md) to save it.

[**IImnAccount**](oe-iimnaccount.md) can be released without calling [**SaveChanges**](oe-iimnaccount-savechanges.md), which results in no changes.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





