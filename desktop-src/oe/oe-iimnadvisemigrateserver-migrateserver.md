---
title: IImnAdviseMigrateServer MigrateServer method
description: IImnAdviseMigrateServer MigrateServer method
ms.assetid: b42f39f9-e56a-4258-aaed-69b18b790190
keywords:
- MigrateServer method Windows Mail (formerly Outlook Express)
- MigrateServer method Windows Mail (formerly Outlook Express) , IImnAdviseMigrateServer interface
- IImnAdviseMigrateServer interface Windows Mail (formerly Outlook Express) , MigrateServer method
topic_type:
- apiref
api_name:
- IImnAdviseMigrateServer.MigrateServer
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IImnAdviseMigrateServer::MigrateServer method

\[**IImnAdviseMigrateServer::MigrateServer** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

## Syntax


```C++
HRESULT MigrateServer(
  [in] DWORD       dwSrvType,
  [in] IImnAccount *pAccount
);
```



## Parameters

<dl> <dt>

*dwSrvType* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a bitmask of the server type.



| Value                                                                                                                                                      | Meaning                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| <span id="SRV_NNTP"></span><span id="srv_nntp"></span><dl> <dt>**SRV\_NNTP**</dt> </dl>             | Indicates a NNTP server. <br/>      |
| <span id="SRV_SMTP"></span><span id="srv_smtp"></span><dl> <dt>**SRV\_SMTP**</dt> </dl>             | Indicates a SMTP server. <br/>      |
| <span id="SRV_POP3"></span><span id="srv_pop3"></span><dl> <dt>**SRV\_POP3**</dt> </dl>             | Indicates a POP3 server. <br/>      |
| <span id="SRV_IMAP"></span><span id="srv_imap"></span><dl> <dt>**SRV\_IMAP**</dt> </dl>             | Indicates an IMAP server. <br/>     |
| <span id="SRV_HTTPMAIL"></span><span id="srv_httpmail"></span><dl> <dt>**SRV\_HTTPMAIL**</dt> </dl> | Indicates an HTTPMail server. <br/> |
| <span id="SRV_LDAP"></span><span id="srv_ldap"></span><dl> <dt>**SRV\_LDAP**</dt> </dl>             | Indicates a LDAP server. <br/>      |



 

</dd> <dt>

*pAccount* \[in\]
</dt> <dd>

Type: **[**IImnAccount**](oe-iimnaccount.md)\***

Specifies a pointer to an [**IImnAccount**](oe-iimnaccount.md).

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





