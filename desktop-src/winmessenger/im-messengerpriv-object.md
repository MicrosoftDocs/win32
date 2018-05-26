---
title: MessengerPriv object
description: The Messenger service MessengerPriv object.
ms.assetid: fa970a56-31f5-468e-b009-198d8427c5ae
keywords:
- MessengerPriv object Windows Messenger
- MessengerPriv object Windows Messenger , described
topic_type:
- apiref
api_name:
- MessengerPriv
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

# MessengerPriv object

\[**MessengerPriv** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

The Messenger service **MessengerPriv** object.

-   [Interfaces](#interfaces)

### Interfaces

The **MessengerPriv** object defines these interfaces.



| Interface                                                     | Description                                                                                                                             |
|:--------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| [**DMessengerPrivateEvents**](im-dmessengerprivateevents.md) | Fires events in the Messenger client when notifications from [**IMessengerPrivate**](im-imessengerprivate.md) are received.<br/> |
| [**IMessengerPrivate**](im-imessengerprivate.md)             | Enables an application to add Windows Messenger contacts programmatically.<br/>                                                   |
| [**IMsgrLock**](im-imsgrlock.md)                             | Enables an application to unlock Licensed Messenger objects.<br/>                                                                 |



 

## Remarks

By default, the **MessengerPriv** object is locked. For more information about unlocking the Messenger service  API, see [Messenger Lock and Key API](im-lock-and-key-ovw.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Product<br/>                  | Messenger 4.5<br/>                                                                |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl> |
| IID<br/>                      | CLSID\_MessengerPrivate is defined as AB1D8565-40E9-4616-984D-98465687E82C<br/>   |



 

 





