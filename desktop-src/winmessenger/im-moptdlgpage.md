---
title: MOPTDLGPAGE enumeration
description: Do not use.
ms.assetid: a7d669bd-fcfe-4f7d-af92-6dc0052c393a
keywords:
- MOPTDLGPAGE enumeration Windows Messenger
- LockError enumeration Windows Messenger
topic_type:
- apiref
api_name:
- LockError
api_location:
- Mdisp.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# MOPTDLGPAGE enumeration

\[**MOPTDLGPAGE** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Specifies which page of the Messenger client **Options** dialog box to display to the user.

> [!Note]  
> The **MOPTDLGPAGE** enumerated type is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**MOPTIONPAGE**](im-moptionpage.md) instead.

 

## Syntax


```C++
typedef enum  { 
  MOPTDLG_GENERAL_PAGE,
  MOPTDLG_PRIVACY_PAGE      = 1,
  MOPTDLG_EXCHANGE_PAGE     = 2,
  MOPTDLG_ACCOUNTS_PAGE     = 3,
  MOPTDLG_CONNECTION_PAGE   = 4,
  MOPTDLG_PREFERENCES_PAGE  = 5,
  MOPTDLG_SERVICES_PAGE     = 6,
  MOPTDLG_PHONE_PAGE        = 7
} LockError;
```



## Constants

<dl> <dt>

<span id="MOPTDLG_GENERAL_PAGE"></span><span id="moptdlg_general_page"></span>**MOPTDLG\_GENERAL\_PAGE**
</dt> <dd>

Display the **Personal** tab of the **Options** dialog box (default).

</dd> <dt>

<span id="MOPTDLG_PRIVACY_PAGE"></span><span id="moptdlg_privacy_page"></span>**MOPTDLG\_PRIVACY\_PAGE**
</dt> <dd>

Display the **Privacy** tab of the **Options** dialog box.

</dd> <dt>

<span id="MOPTDLG_EXCHANGE_PAGE"></span><span id="moptdlg_exchange_page"></span>**MOPTDLG\_EXCHANGE\_PAGE**
</dt> <dd>

Display the **Accounts** tab of the **Options** dialog box.

</dd> <dt>

<span id="MOPTDLG_ACCOUNTS_PAGE"></span><span id="moptdlg_accounts_page"></span>**MOPTDLG\_ACCOUNTS\_PAGE**
</dt> <dd>

Display the **Accounts** tab of the **Options** dialog box.

</dd> <dt>

<span id="MOPTDLG_CONNECTION_PAGE"></span><span id="moptdlg_connection_page"></span>**MOPTDLG\_CONNECTION\_PAGE**
</dt> <dd>

Display the **Connection** tab of the **Options** dialog box.

</dd> <dt>

<span id="MOPTDLG_PREFERENCES_PAGE"></span><span id="moptdlg_preferences_page"></span>**MOPTDLG\_PREFERENCES\_PAGE**
</dt> <dd>

Display the **Preferences** tab of the **Options** dialog box.

</dd> <dt>

<span id="MOPTDLG_SERVICES_PAGE"></span><span id="moptdlg_services_page"></span>**MOPTDLG\_SERVICES\_PAGE**
</dt> <dd>

Reserved.

</dd> <dt>

<span id="MOPTDLG_PHONE_PAGE"></span><span id="moptdlg_phone_page"></span>**MOPTDLG\_PHONE\_PAGE**
</dt> <dd>

Display the **Phone** tab of the **Options** dialog box.

</dd> </dl>

## Requirements



|                                  |                                                                                      |
|----------------------------------|--------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                |
| End of server support<br/> | Windows Server 2003<br/>                                                       |
| Header<br/>                | <dl> <dt>Mdisp.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Mdisp.idl</dt> </dl> |



 

 





