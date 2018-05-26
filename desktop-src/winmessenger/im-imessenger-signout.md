---
title: IMessenger Signout method
description: Signs the current client user out of all Mesenger services.
ms.assetid: d6ea6bb0-3730-44b2-8a03-2aa7e1af1799
keywords:
- Signout method Windows Messenger
- Signout method Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , Signout method
topic_type:
- apiref
api_name:
- IMessenger.Signout
api_location:
- Msgsc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMessenger::Signout method

\[**Signout** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Signs the current client user out of all Mesenger services.

## Syntax


```C++
HRESULT Signout();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                                                                             |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Success.<br/>                                                                                                     |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Could not find the [**Messenger**](im-messenger.md) object or could not send the outgoing protocol message.<br/> |
| <dl> <dt>**MSGR\_E\_NOT\_LOGGED\_ON**</dt> </dl> | Not signed in to the primary service when the sign-out was attempted.<br/>                                        |



 

## Remarks

If the client supports sign-in to multiple services, this method will disconnect the client from all services.

If successful, invoking this method will result in a [**OnSignout**](im-dmessengerevents-onsignout.md) event. Signing out also results in a [**OnMyStatusChange**](im-dmessengerevents-onmystatuschange.md) event with *mMYStatusOE*=**MISTATUS\_LOCAL\_DISCONNECTING\_FROM\_SERVER**. This state persists until the server of the service receives and responds to the protocol-level logoff command.

> [!Note]  
> This method is not available for scripting languages.

 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMessenger**](im-imessenger.md)
</dt> <dt>

[**OnAppShutdown**](im-dmessengerevents-onappshutdown.md)
</dt> </dl>

 

 





