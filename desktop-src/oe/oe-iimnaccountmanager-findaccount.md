---
title: IImnAccountManager FindAccount method
description: Allows a client to find an account by a property value.
ms.assetid: 21404f0a-c786-4de9-8021-5a9d14a7b349
keywords:
- FindAccount method Windows Mail (formerly Outlook Express)
- FindAccount method Windows Mail (formerly Outlook Express) , IImnAccountManager interface
- IImnAccountManager interface Windows Mail (formerly Outlook Express) , FindAccount method
topic_type:
- apiref
api_name:
- IImnAccountManager.FindAccount
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

# IImnAccountManager::FindAccount method

\[**IImnAccountManager::FindAccount** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Allows a client to find an account by a property value.

## Syntax


```C++
HRESULT FindAccount(
  [in]  DWORD       dwPropTag,
  [in]  LPCSTR      pszSearchData,
  [out] IImnAccount **ppAccount
);
```



## Parameters

<dl> <dt>

*dwPropTag* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that contains the AP\_\* property to search on. To search for an account by name, set this parameter to AP\_ACCOUNT\_NAME.

</dd> <dt>

*pszSearchData* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the property value to search on, for example the account name.

</dd> <dt>

*ppAccount* \[out\]
</dt> <dd>

Type: **[**IImnAccount**](oe-iimnaccount.md)\*\***

Receives the address of a pointer to the [**IImnAccount**](oe-iimnaccount.md) object found. The client is responsible for releasing this object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                               |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                             |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an account was not found that met the criteria.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *dwPropTag* or *pszSearchData* is **NULL**.<br/>     |
| <dl> <dt>**E\_NoAccounts**</dt> </dl>  | Indicates that no accounts are configured.<br/>                     |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/>          |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





