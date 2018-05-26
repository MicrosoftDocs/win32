---
title: IMsgrLock interface
description: Do not use. The IMsgrLock interface implements an API that is used to unlock Licensed Messenger objects.
ms.assetid: 688b7ac9-4cde-4f64-9a42-db5311517715
keywords:
- IMsgrLock interface Windows Messenger
- IMsgrLock interface Windows Messenger , described
topic_type:
- apiref
api_name:
- IMsgrLock
api_location:
- Msgsc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMsgrLock interface

\[**IMsgrLock** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **IMsgrLock** interface implements an API that is used to unlock Licensed Messenger objects.

## Members

The **IMsgrLock** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IMsgrLock** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMsgrLock** interface has these methods.



| Method                                                           | Description                                                                                                                |
|:-----------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------|
| [**RequestChallenge**](im-imsgrlock-requestchallenge-method.md) | Initiates an authentication challenge-response transaction between a Messenger client and a Messenger service .<br/> |
| [**SendResponse**](im-imsgrlock-sendresponse-method.md)         | Sends authentication data from a Messenger client to a Messenger service .<br/>                                      |



 

### Properties

The **IMsgrLock** interface has these properties.



| Property                                                  | Access type          | Description                                 |
|:----------------------------------------------------------|:---------------------|:--------------------------------------------|
| [**Status**](im-imsgrlock-status-property.md)<br/> | Read-only<br/> | Returns the Lock and Key status.<br/> |



 

## Remarks

The **IMsgrLock** interface is implemented in the [**MsgrSessionManager**](im-msgrsessionmanager-object.md) and [**MessengerPriv**](im-messengerpriv-object.md) objects, both of these objects expose Messenger service APIs and are locked by default. The **IMsgrLock** interface provides the mechanism that enables an application to programmatically unlock Messenger service APIs.

To unlock one of the objects that expose a Messenger service API, the methods and properties of **IMsgrLock** are used in conjuction with the notifications fired by the [**DMsgrSessionManagerEvents**](im-dmsgrsessionmanagerevents.md) and [**DMessengerPrivateEvents**](im-dmessengerprivateevents.md) dispinterfaces, depending on which object type is being unlocked. The [**MsgrSessionManager**](im-msgrsessionmanager-object.md) is an object that exposes Messenger service APIs. If it is created by an application, this object must be unlocked using **IMsgrLock** before it can be used. For the **MsgrSessionManager** object, event notifications are fired from the **DMsgrSessionManagerEvents** dispinterface. For the [**MessengerPriv**](im-messengerpriv-object.md) object, event notifications are fired from the **DMessengerPrivateEvents** dispinterface.

If more than one Messenger service object is used in an application, then each object must be unlocked seperately before its interface members can be used. For more information on unlocking objects using **IMsgrLock** see [Messenger Lock and Key API](im-lock-and-key-ovw.md).

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
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>    |



## See also

<dl> <dt>

[**MsgrSessionManager**](im-msgrsessionmanager-object.md)
</dt> <dt>

[**MessengerPriv**](im-messengerpriv-object.md)
</dt> <dt>

[**DMsgrSessionManagerEvents**](im-dmsgrsessionmanagerevents.md)
</dt> <dt>

[**DMessengerPrivateEvents**](im-dmessengerprivateevents.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> </dl>

 

 





