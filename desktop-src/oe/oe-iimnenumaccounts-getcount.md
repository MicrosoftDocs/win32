---
title: IImnEnumAccounts GetCount method
description: Determines the number of accounts in the enumeration.
ms.assetid: '0fc577fd-f2a8-4600-b391-f55059e1b31e'
keywords: ["GetCount method Windows Mail (formerly Outlook Express)", "GetCount method Windows Mail (formerly Outlook Express) , IImnEnumAccounts interface", "IImnEnumAccounts interface Windows Mail (formerly Outlook Express) , GetCount method"]
topic_type:
- apiref
api_name:
- IImnEnumAccounts.GetCount
api_location:
- Msoeacct.dll
api_type:
- COM
---

# IImnEnumAccounts::GetCount method

\[**IImnEnumAccounts::GetCount** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Determines the number of accounts in the enumeration.

## Syntax


```C++
HRESULT GetCount(
  [out] ULONG *pcItems
);
```



## Parameters

<dl> <dt>

*pcItems* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the number of accounts.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                      |
|----------------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success.<br/>                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pcItems* is **NULL**.<br/> |



 

## Remarks

A client would typically use this method to determine the number of accounts so that it can pre-allocate an array to hold the accounts.

This method always returns the total number of accounts, not the number of remaining accounts to enumerate.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





