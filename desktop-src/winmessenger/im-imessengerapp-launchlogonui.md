---
title: IMessengerApp LaunchLogonUI method
description: Launches the Messenger client Sign In dialog box and populates the sign-in name field.
ms.assetid: 1c3dd27f-c6c8-4936-a3af-a4fb297770a4
keywords:
- LaunchLogonUI method Windows Messenger
- LaunchLogonUI method Windows Messenger , IMessengerApp interface
- IMessengerApp interface Windows Messenger , LaunchLogonUI method
topic_type:
- apiref
api_name:
- IMessengerApp.LaunchLogonUI
api_location:
- Msmsgs.exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMessengerApp::LaunchLogonUI method

\[**LaunchLogonUI** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Launches the Messenger client **Sign In** dialog box and populates the sign-in name field.

> [!Note]  
> The **LaunchLogonUI** enumerated type is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**Signin**](im-imessenger-signin.md) instead.

 

## Syntax


```C++
HRESULT LaunchLogonUI();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Mdisp.h</dt> </dl>    |
| IDL<br/>                   | <dl> <dt>Mdisp.idl</dt> </dl>  |
| DLL<br/>                   | <dl> <dt>Msmsgs.exe</dt> </dl> |



 

 





