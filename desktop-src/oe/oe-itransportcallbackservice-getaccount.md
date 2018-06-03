---
title: ITransportCallbackService GetAccount method
description: Gets the mail account and server type.
ms.assetid: 0e993ac9-eb4f-4a9d-92da-239fe9b20254
keywords:
- GetAccount method Windows Mail (formerly Outlook Express)
- GetAccount method Windows Mail (formerly Outlook Express) , ITransportCallbackService interface
- ITransportCallbackService interface Windows Mail (formerly Outlook Express) , GetAccount method
topic_type:
- apiref
api_name:
- ITransportCallbackService.GetAccount
api_location:
- Msoe.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ITransportCallbackService::GetAccount method

\[**ITransportCallbackService::GetAccount** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Gets the mail account and server type.

## Syntax


```C++
HRESULT GetAccount(
  [out] LPDWORD     pdwServerType,
  [out] IImnAccount **ppAccount
);
```



## Parameters

<dl> <dt>

*pdwServerType* \[out\]
</dt> <dd>

Type: **LPDWORD**

Receives a pointer to a **DWORD** that indicates the server type.



| Value                                                                                                                                                      | Meaning                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| <span id="SRV_NNTP"></span><span id="srv_nntp"></span><dl> <dt>**SRV\_NNTP**</dt> </dl>             | Indicates a NNTP server. <br/>      |
| <span id="SRV_SMTP"></span><span id="srv_smtp"></span><dl> <dt>**SRV\_SMTP**</dt> </dl>             | Indicates a SMTP server. <br/>      |
| <span id="SRV_POP3"></span><span id="srv_pop3"></span><dl> <dt>**SRV\_POP3**</dt> </dl>             | Indicates a POP3 server. <br/>      |
| <span id="SRV_IMAP"></span><span id="srv_imap"></span><dl> <dt>**SRV\_IMAP**</dt> </dl>             | Indicates an IMAP server. <br/>     |
| <span id="SRV_HTTPMAIL"></span><span id="srv_httpmail"></span><dl> <dt>**SRV\_HTTPMAIL**</dt> </dl> | Indicates an HTTPMail server. <br/> |
| <span id="SRV_LDAP"></span><span id="srv_ldap"></span><dl> <dt>**SRV\_LDAP**</dt> </dl>             | Indicates a LDAP server. <br/>      |



 

</dd> <dt>

*ppAccount* \[out\]
</dt> <dd>

Type: **[**IImnAccount**](oe-iimnaccount.md)\*\***

Receives the address of a pointer to an [**IImnAccount**](oe-iimnaccount.md) object.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                       |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                      |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                    |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





