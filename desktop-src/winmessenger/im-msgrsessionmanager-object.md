---
title: MsgrSessionManager object
description: The Messenger client session manager object.
ms.assetid: 4ef48320-1403-4ddf-a7de-fc74c6c4c231
keywords:
- MsgrSessionManager object Windows Messenger
- MsgrSessionManager object Windows Messenger , described
topic_type:
- apiref
api_name:
- MsgrSessionManager
api_location:
- Msgrpriv.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MsgrSessionManager object

\[**MsgrSessionManager** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

The Messenger client session manager object.

-   [Interfaces](#interfaces)

### Interfaces

The **MsgrSessionManager** object defines these interfaces.



| Interface                                                         | Description                                                                                                                                 |
|:------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| [**DMsgrSessionManagerEvents**](im-dmsgrsessionmanagerevents.md) | Fires events in the Messenger client when notifications from [**IMsgrSessionManager**](im-imsgrsessionmanager.md) are received.<br/> |
| [**IMsgrLock**](im-imsgrlock.md)                                 | Enables an application to unlock Licensed Messenger objects.<br/>                                                                     |
| [**IMsgrSessionManager**](im-imsgrsessionmanager.md)             |                                                                                                                                             |



 

## Remarks

For an application to use the **MsgrSessionManager** object, the object must first be unlocked. For more information, see [Messenger Lock and Key API](im-lock-and-key-ovw.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Product<br/>                  | Messenger 4.0<br/>                                                                |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl> |
| IID<br/>                      | CLSID\_MsgrSessionManager is defined as E3A3B1D9-5675-43c0-BF04-37BE11939FB7<br/> |



## See also

<dl> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> </dl>

 

 





