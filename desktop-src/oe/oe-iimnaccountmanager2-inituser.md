---
title: IImnAccountManager2 InitUser method
description: Initializes the account for the current user.
ms.assetid: a60db8ff-335c-4614-8c3a-655218f8f033
keywords:
- InitUser method Windows Mail (formerly Outlook Express)
- InitUser method Windows Mail (formerly Outlook Express) , IImnAccountManager2 interface
- IImnAccountManager2 interface Windows Mail (formerly Outlook Express) , InitUser method
topic_type:
- apiref
api_name:
- IImnAccountManager2.InitUser
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

# IImnAccountManager2::InitUser method

\[**IImnAccountManager2::InitUser** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Initializes the account for the current user.

## Syntax


```C++
HRESULT InitUser(
  [in] IImnAdviseMigrateServer *pAdviseMigrateServer,
  [in] REFGUID                 rguidID,
  [in] DWORD                   dwFlags
);
```



## Parameters

<dl> <dt>

*pAdviseMigrateServer* \[in\]
</dt> <dd>

Type: **[**IImnAdviseMigrateServer**](oe-iimnadvisemigrateserver.md)\***

Specifies a pointer to an [**IImnAdviseMigrateServer**](oe-iimnadvisemigrateserver.md) object. To receive notification when an account is migrated, the client must implement the **IImnAdviseMigrateServer** interface. This parameter can be **NULL**.

</dd> <dt>

*rguidID* \[in\]
</dt> <dd>

Type: **REFGUID**

Specifies the user's GUID.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Not used.

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



 

 





