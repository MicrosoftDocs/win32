---
title: IImnAccount GetServerTypes method
description: Determines the server types supported by the account.
ms.assetid: 12efaa20-aa73-4465-b4b1-e9638f3c155c
keywords:
- GetServerTypes method Windows Mail (formerly Outlook Express)
- GetServerTypes method Windows Mail (formerly Outlook Express) , IImnAccount interface
- IImnAccount interface Windows Mail (formerly Outlook Express) , GetServerTypes method
topic_type:
- apiref
api_name:
- IImnAccount.GetServerTypes
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

# IImnAccount::GetServerTypes method

\[**IImnAccount::GetServerTypes** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Determines the server types supported by the account.

## Syntax


```C++
HRESULT GetServerTypes(
  [out] DWORD *pdwSrvTypes
);
```



## Parameters

<dl> <dt>

*pdwSrvTypes* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a pointer to a **DWORD** that contains the server type.



| Value                                                                                                                                                      | Meaning                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| <span id="SRV_NNTP"></span><span id="srv_nntp"></span><dl> <dt>**SRV\_NNTP**</dt> </dl>             | Indicates a NNTP server. <br/>      |
| <span id="SRV_SMTP"></span><span id="srv_smtp"></span><dl> <dt>**SRV\_SMTP**</dt> </dl>             | Indicates a SMTP server. <br/>      |
| <span id="SRV_POP3"></span><span id="srv_pop3"></span><dl> <dt>**SRV\_POP3**</dt> </dl>             | Indicates a POP3 server. <br/>      |
| <span id="SRV_IMAP"></span><span id="srv_imap"></span><dl> <dt>**SRV\_IMAP**</dt> </dl>             | Indicates an IMAP server. <br/>     |
| <span id="SRV_HTTPMAIL"></span><span id="srv_httpmail"></span><dl> <dt>**SRV\_HTTPMAIL**</dt> </dl> | Indicates an HTTPMail server. <br/> |
| <span id="SRV_LDAP"></span><span id="srv_ldap"></span><dl> <dt>**SRV\_LDAP**</dt> </dl>             | Indicates a LDAP server. <br/>      |



 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                      |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that the server type cannot be determined. <br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pdwSrvTypes* is **NULL**. <br/>            |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





