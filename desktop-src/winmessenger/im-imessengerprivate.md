---
title: IMessengerPrivate interface
description: Do not use. The IMessengerPrivate interface is a Messenger service API that provides programmatic access to the MessengerPriv object.
ms.assetid: 'b01135fd-48b5-40bc-930f-c2064fbdf12e'
keywords: ["IMessengerPrivate interface Windows Messenger", "IMessengerPrivate interface Windows Messenger , described"]
topic_type:
- apiref
api_name:
- IMessengerPrivate
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessengerPrivate interface

\[**IMessengerPrivate** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **IMessengerPrivate** interface is a Messenger service  API that provides programmatic access to the [**MessengerPriv**](im-messengerpriv-object.md) object.

## Members

The **IMessengerPrivate** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IMessengerPrivate** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMessengerPrivate** interface has these methods.



| Method                                                                     | Description                                                                                     |
|:---------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| [**AddContact**](im-imessengerprivate-addcontact-method.md)               | Adds a contact to the contact list with no prompting or notification UI.<br/>             |
| [**EnableAlertEvents**](im-imessengerprivate-enablealertevents-method.md) | Enables the Messenger client to be notified when the Messenger service fires events.<br/> |



 

## Remarks

**IMessengerPrivate** enables an application to add Windows Messenger contacts programmatically. **IMessengerPrivate** also provides a mechanism for a Messenger client application to receive notifications from the [**OnAlertReceived**](im-dmessengerprivateevents-onalertreceived.md) event.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Product<br/>                  | Messenger 4.5<br/>                                                                |
| Header<br/>                   | <dl> <dt>Msgrpriv.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrpriv.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>    |



## See also

<dl> <dt>

[**IDispatch**](c1accca9-971c-4435-8a5e-e25404a3fb25)
</dt> <dt>

[**MessengerPriv**](im-messengerpriv-object.md)
</dt> <dt>

[**OnAlertReceived**](im-dmessengerprivateevents-onalertreceived.md)
</dt> <dt>

[Messenger Lock and Key API](im-lock-and-key-ovw.md)
</dt> <dt>

[Messenger Session Invite and Messenger Private APIs](im-session-invite-ovw.md)
</dt> </dl>

 

 





