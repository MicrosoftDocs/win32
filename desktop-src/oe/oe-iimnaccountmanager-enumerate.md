---
title: IImnAccountManager Enumerate method
description: Creates an IImnEnumAccounts object that allows a client to enumerate accounts that support specific servers.
ms.assetid: 'f212a7ae-eddf-4bd6-9e7f-7c32fa075860'
keywords: ["Enumerate method Windows Mail (formerly Outlook Express)", "Enumerate method Windows Mail (formerly Outlook Express) , IImnAccountManager interface", "IImnAccountManager interface Windows Mail (formerly Outlook Express) , Enumerate method"]
topic_type:
- apiref
api_name:
- IImnAccountManager.Enumerate
api_location:
- Msoeacct.dll
api_type:
- COM
---

# IImnAccountManager::Enumerate method

\[**IImnAccountManager::Enumerate** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Creates an [**IImnEnumAccounts**](oe-iimnenumaccounts.md) object that allows a client to enumerate accounts that support specific servers.

## Syntax


```C++
HRESULT Enumerate(
  [in]  DWORD            dwSrvTypes,
  [out] IImnEnumAccounts **ppEnumAccounts
);
```



## Parameters

<dl> <dt>

*dwSrvTypes* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the server types to enumerate.



| Value                                                                                                                                                      | Meaning                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| <span id="SRV_NNTP"></span><span id="srv_nntp"></span><dl> <dt>**SRV\_NNTP**</dt> </dl>             | Indicates a NNTP server. <br/>      |
| <span id="SRV_SMTP"></span><span id="srv_smtp"></span><dl> <dt>**SRV\_SMTP**</dt> </dl>             | Indicates a SMTP server. <br/>      |
| <span id="SRV_POP3"></span><span id="srv_pop3"></span><dl> <dt>**SRV\_POP3**</dt> </dl>             | Indicates a POP3 server. <br/>      |
| <span id="SRV_IMAP"></span><span id="srv_imap"></span><dl> <dt>**SRV\_IMAP**</dt> </dl>             | Indicates an IMAP server. <br/>     |
| <span id="SRV_HTTPMAIL"></span><span id="srv_httpmail"></span><dl> <dt>**SRV\_HTTPMAIL**</dt> </dl> | Indicates an HTTPMail server. <br/> |
| <span id="SRV_LDAP"></span><span id="srv_ldap"></span><dl> <dt>**SRV\_LDAP**</dt> </dl>             | Indicates a LDAP server. <br/>      |



 

</dd> <dt>

*ppEnumAccounts* \[out\]
</dt> <dd>

Type: **[**IImnEnumAccounts**](oe-iimnenumaccounts.md)\*\***

Receives the address of a pointer to the new [**IImnEnumAccounts**](oe-iimnenumaccounts.md) object. The client is responsible for releasing this object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppEnumAccounts* is **NULL**. <br/>         |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/> |
| <dl> <dt>**E\_NoAccounts**</dt> </dl>  | Indicates that no accounts are configured.<br/>            |



 

## Remarks

If a client needs to enumerate all accounts, pass in SRV\_ALL for dwSrvTypes. The accounts are enumerated in sorted order by AP\_ACCOUNT\_NAME.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





