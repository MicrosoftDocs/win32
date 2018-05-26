---
title: DMsgrObjectEvents OnLogonResult event
description: Indicates that an attempt has been made to sign in to the primary service.
ms.assetid: f9231631-8ca4-4b89-84b8-2049a8ba7586
keywords:
- OnLogonResult event Windows Messenger
- OnLogonResult event Windows Messenger , DMsgrObjectEvents interface
- DMsgrObjectEvents interface Windows Messenger , OnLogonResult event
topic_type:
- apiref
api_name:
- DMsgrObjectEvents.OnLogonResult
api_location:
- Msmsgs.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DMsgrObjectEvents::OnLogonResult event

\[**OnLogonResult** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that an attempt has been made to sign in to the primary service.

> [!Note]  
> The **OnLogonResult** event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**OnSignin**](im-dmessengerevents-onsignin.md) instead.

 

## Syntax


```C++
void OnLogonResult(
  [in] long         hr,
  [in] IMsgrService *pService
);
```



## Parameters

<dl> <dt>

*hr* \[in\]
</dt> <dd>

Success or error code as a **long**.

</dd> <dt>

*pService* \[in\]
</dt> <dd>

Pointer to an [**IMessengerService**](im-imessengerservice.md) interface.

</dd> </dl>

## Return value

This event does not return a value.

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Mdisp.h</dt> </dl>    |
| IDL<br/>                   | <dl> <dt>Mdisp.idl</dt> </dl>  |
| DLL<br/>                   | <dl> <dt>Msmsgs.exe</dt> </dl> |



 

 





