---
title: IImnEnumAccounts SortByAccountName method
description: Sorts the enumeration by account name.
ms.assetid: '83d7ff9d-ac0a-47b6-bc92-3ed48d77b0cf'
keywords: ["SortByAccountName method Windows Mail (formerly Outlook Express)", "SortByAccountName method Windows Mail (formerly Outlook Express) , IImnEnumAccounts interface", "IImnEnumAccounts interface Windows Mail (formerly Outlook Express) , SortByAccountName method"]
topic_type:
- apiref
api_name:
- IImnEnumAccounts.SortByAccountName
api_location:
- Msoeacct.dll
api_type:
- COM
---

# IImnEnumAccounts::SortByAccountName method

\[**IImnEnumAccounts::SortByAccountName** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sorts the enumeration by account name.

## Syntax


```C++
HRESULT SortByAccountName();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





