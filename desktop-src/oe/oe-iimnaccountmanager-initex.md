---
title: IImnAccountManager InitEx method
description: Initializes the new IImnAccountManager object.
ms.assetid: 1db6e0b7-1f5a-436f-a1b3-83898eb01aeb
keywords:
- InitEx method Windows Mail (formerly Outlook Express)
- InitEx method Windows Mail (formerly Outlook Express) , IImnAccountManager interface
- IImnAccountManager interface Windows Mail (formerly Outlook Express) , InitEx method
topic_type:
- apiref
api_name:
- IImnAccountManager.InitEx
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

# IImnAccountManager::InitEx method

\[**IImnAccountManager::InitEx** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Initializes the new [**IImnAccountManager**](oe-iimnaccountmanager.md) object.

## Syntax


```C++
HRESULT InitEx(
  [in] IImnAdviseMigrateServer *pAdviseMigrateServer,
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

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that indicates how to initialize the object.

<dl><span id="ACCT_INIT_ATHENA"></span><span id="acct_init_athena"></span><dt>

**ACCT\_INIT\_ATHENA**
</dt><span id="ACCT_INIT_OUTLOOK"></span><span id="acct_init_outlook"></span><dt>

**ACCT\_INIT\_OUTLOOK**
</dt> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                                |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success. <br/>                                             |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Indicates that an unknown error has occurred. <br/>                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>           | Indicates that an attempt to allocate memory failed. <br/>           |
| <dl> <dt>**E\_RegCreateKeyFailed**</dt> </dl>    | Indicates that an attempt to create a registry key failed. <br/>     |
| <dl> <dt>**E\_RegQueryInfoKeyFailed**</dt> </dl> | Indicates that a query to the registry for information failed. <br/> |



 

## Remarks

A client application should call this method immediately after calling [CoCreateInstance](http://msdn.microsoft.com/library/com/html/7295a55b-12c7-4ed0-a7a4-9ecee16afdec.asp) to obtain a pointer to a new, uninitialized [**IImnAccountManager**](oe-iimnaccountmanager.md) object.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





