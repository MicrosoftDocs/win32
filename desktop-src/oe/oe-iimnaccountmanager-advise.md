---
title: IImnAccountManager Advise method
description: Adds an advise account object to an array of advise account objects.
ms.assetid: 'abcf8deb-e360-46b8-ab75-f3b966f7f17f'
keywords: ["Advise method Windows Mail (formerly Outlook Express)", "Advise method Windows Mail (formerly Outlook Express) , IImnAccountManager interface", "IImnAccountManager interface Windows Mail (formerly Outlook Express) , Advise method"]
topic_type:
- apiref
api_name:
- IImnAccountManager.Advise
api_location:
- Msoeacct.dll
api_type:
- COM
---

# IImnAccountManager::Advise method

\[**IImnAccountManager::Advise** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Adds an advise account object to an array of advise account objects.

## Syntax


```C++
HRESULT Advise(
  [in]  IImnAdviseAccount *pAdviseAccount,
  [out] DWORD             *pdwConnection
);
```



## Parameters

<dl> <dt>

*pAdviseAccount* \[in\]
</dt> <dd>

Type: **[**IImnAdviseAccount**](oe-iimnadviseaccount.md)\***

Specifies a pointer to an [**IImnAdviseAccount**](oe-iimnadviseaccount.md) object.

</dd> <dt>

*pdwConnection* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a pointer to a **DWORD** that contains the index of the advise account in the array.

</dd> </dl>

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



 

 





