---
title: IBasicIMOld LaunchLogonUI method
description: Initiates a Logon dialog.
ms.assetid: '77c225ed-9a4a-41d8-b908-9a211160a3cd'
keywords: ["LaunchLogonUI method Windows Messenger", "LaunchLogonUI method Windows Messenger , IBasicIMOld interface", "IBasicIMOld interface Windows Messenger , LaunchLogonUI method"]
topic_type:
- apiref
api_name:
- IBasicIMOld.LaunchLogonUI
api_location:
- Msgsc.dll
api_type:
- COM
---

# IBasicIMOld::LaunchLogonUI method

\[**LaunchLogonUI** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Initiates a Logon dialog.

> [!Note]  
> The **LaunchLogonUI** method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**Signin**](im-imessenger-signin.md) instead.

 

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



|                                  |                                                                                        |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                  |
| End of server support<br/> | Windows Server 2003<br/>                                                         |
| Header<br/>                | <dl> <dt>Basicim.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Basicim.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>   |



 

 





