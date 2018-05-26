---
title: IImnAccountManager ValidateDefaultSendAccount method
description: Allows a client to force the Account Manager to validate the default Send account.
ms.assetid: 08ba48b2-80ef-469f-a793-60adc5bf83ef
keywords:
- ValidateDefaultSendAccount method Windows Mail (formerly Outlook Express)
- ValidateDefaultSendAccount method Windows Mail (formerly Outlook Express) , IImnAccountManager interface
- IImnAccountManager interface Windows Mail (formerly Outlook Express) , ValidateDefaultSendAccount method
topic_type:
- apiref
api_name:
- IImnAccountManager.ValidateDefaultSendAccount
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

# IImnAccountManager::ValidateDefaultSendAccount method

\[**IImnAccountManager::ValidateDefaultSendAccount** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Allows a client to force the Account Manager to validate the default Send account.

## Syntax


```C++
HRESULT ValidateDefaultSendAccount();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method ensures that a valid Simple Mail Transport Protocol (SMTP) account is set as the default.

If a client allows configuration of defaults, it is possible that users could delete their default Send account.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





