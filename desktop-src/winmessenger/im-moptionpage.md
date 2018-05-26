---
title: MOPTIONPAGE enumeration
description: Do not use. Specifies which page of the Messenger client Options dialog box to display to the user through the user interface (UI) and several related tracking constants.
ms.assetid: 59c2de1f-1393-4e99-836f-feb60eb40e27
keywords:
- MOPTIONPAGE enumeration Windows Messenger
- LockError enumeration Windows Messenger
topic_type:
- apiref
api_name:
- LockError
api_location:
- Msgrua.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MOPTIONPAGE enumeration

\[**MOPTIONPAGE** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Specifies which page of the Messenger client **Options** dialog box to display to the user through the user interface (UI) and several related tracking constants.

## Syntax


```C++
typedef enum  { 
  MOPT_GENERAL_PAGE,
  MOPT_PRIVACY_PAGE      = 1,
  MOPT_EXCHANGE_PAGE     = 2,
  MOPT_ACCOUNTS_PAGE     = 3,
  MOPT_CONNECTION_PAGE   = 4,
  MOPT_PREFERENCES_PAGE  = 5,
  MOPT_SERVICES_PAGE     = 6,
  MOPT_PHONE_PAGE        = 7
} LockError;
```



## Constants

<dl> <dt>

<span id="MOPT_GENERAL_PAGE"></span><span id="mopt_general_page"></span>**MOPT\_GENERAL\_PAGE**
</dt> <dd>

Display the **Personal** tab of the **Options** dialog box (default).

</dd> <dt>

<span id="MOPT_PRIVACY_PAGE"></span><span id="mopt_privacy_page"></span>**MOPT\_PRIVACY\_PAGE**
</dt> <dd>

Display the **Privacy** tab of the **Options** dialog box.

</dd> <dt>

<span id="MOPT_EXCHANGE_PAGE"></span><span id="mopt_exchange_page"></span>**MOPT\_EXCHANGE\_PAGE**
</dt> <dd>

Display the **Accounts** tab of the **Options** dialog box. This tab is not available in Windows Messenger version 4.5 or later.

</dd> <dt>

<span id="MOPT_ACCOUNTS_PAGE"></span><span id="mopt_accounts_page"></span>**MOPT\_ACCOUNTS\_PAGE**
</dt> <dd>

Display the **Accounts** tab of the **Options** dialog box.

</dd> <dt>

<span id="MOPT_CONNECTION_PAGE"></span><span id="mopt_connection_page"></span>**MOPT\_CONNECTION\_PAGE**
</dt> <dd>

Display the **Connection** tab of the **Options** dialog box.

</dd> <dt>

<span id="MOPT_PREFERENCES_PAGE"></span><span id="mopt_preferences_page"></span>**MOPT\_PREFERENCES\_PAGE**
</dt> <dd>

Display the **Preferences** tab of the **Options** dialog box.

</dd> <dt>

<span id="MOPT_SERVICES_PAGE"></span><span id="mopt_services_page"></span>**MOPT\_SERVICES\_PAGE**
</dt> <dd>

Reserved.

</dd> <dt>

<span id="MOPT_PHONE_PAGE"></span><span id="mopt_phone_page"></span>**MOPT\_PHONE\_PAGE**
</dt> <dd>

Display the **Phone** tab of the **Options** dialog box.

</dd> </dl>

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |



 

 





