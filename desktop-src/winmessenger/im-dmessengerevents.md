---
title: DMessengerEvents interface
description: Do not use. The DMessengerEvents dispinterface handles events that are generated or received by a Messenger object.
ms.assetid: c0c03037-9037-4218-bddc-942933538e60
keywords:
- DMessengerEvents interface Windows Messenger
- DMessengerEvents interface Windows Messenger , described
topic_type:
- apiref
api_name:
- DMessengerEvents
api_location:
- Msgsc.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# DMessengerEvents interface

\[**DMessengerEvents** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **DMessengerEvents** dispinterface handles events that are generated or received by a [**Messenger**](im-messenger.md) object.

## Members

The **DMessengerEvents** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **DMessengerEvents** also has these types of members:

-   [Events](#events)

### Events

The **DMessengerEvents** interface has these events.



| Event                                                                                  | Description                                                                                                                                                                                                                                                          |
|:---------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**OnAppShutdown**](im-dmessengerevents-onappshutdown.md)                             | Indicates that the client application is about to shut down for purposes of a client upgrade initiated either by the server or client user.<br/>                                                                                                               |
| [**OnContactAddedToGroup**](im-dmessengerevents-oncontactaddedtogroup.md)             | Indicates that a contact has been added to a group.<br/>                                                                                                                                                                                                       |
| [**OnContactBlockChange**](im-dmessengerevents-oncontactblockchange.md)               | Indicates that the block settings of a contact in the local client's Contact List have changed. Queries whether the contact is blocked by the local client user.<br/>                                                                                          |
| [**OnContactFriendlyNameChange**](im-dmessengerevents-oncontactfriendlynamechange.md) | Indicates that a contact in the client's Contact List has changed the friendly name.<br/>                                                                                                                                                                      |
| [**OnContactListAdd**](im-dmessengerevents-oncontactlistadd.md)                       | Indicates the result of an attempt to add to the [**Messenger**](im-messenger.md) object's Contact List. <br/>                                                                                                                                                |
| [**OnContactListRemove**](im-dmessengerevents-oncontactlistremove.md)                 | Indicates the result of an attempt to remove a contact from the [**Messenger**](im-messenger.md) object's Contact List. <br/>                                                                                                                                 |
| [**OnContactPagerChange**](im-dmessengerevents-oncontactpagerchange.md)               | Indicates that a contact in the local client's Contact List has changed the pager information access permissions.<br/>                                                                                                                                         |
| [**OnContactPhoneChange**](im-dmessengerevents-oncontactphonechange.md)               | Indicates that the phone information of a contact in the local client's Contact List has changed.<br/>                                                                                                                                                         |
| [**OnContactPropertyChange**](im-dmessengerevents-oncontactpropertychange.md)         | Indicates that property information for a contact in the local client's Contact List has changed.<br/>                                                                                                                                                         |
| [**OnContactRemovedFromGroup**](im-dmessengerevents-oncontactremovedfromgroup.md)     | Indicates that a contact has been removed from a group.<br/>                                                                                                                                                                                                   |
| [**OnContactStatusChange**](im-dmessengerevents-oncontactstatuschange.md)             | Indicates that the status of a contact in the local client's Contact List has changed, and returns the current state of the contact.<br/>                                                                                                                      |
| [**OnGroupAdded**](im-dmessengerevents-ongroupadded.md)                               | Indicates that a new group has been created.<br/>                                                                                                                                                                                                              |
| [**OnGroupNameChanged**](im-dmessengerevents-ongroupnamechanged.md)                   | Indicates that the name of a group has been changed.<br/>                                                                                                                                                                                                      |
| [**OnGroupRemoved**](im-dmessengerevents-ongroupremoved.md)                           | Indicates that a group has been deleted.<br/>                                                                                                                                                                                                                  |
| [**OnIMWindowContactAdded**](im-dmessengerevents-onimwindowcontactadded.md)           | Indicates that a contact has been added to the ongoing conversation.<br/>                                                                                                                                                                                      |
| [**OnIMWindowContactRemoved**](im-dmessengerevents-onimwindowcontactremoved.md)       | Indicates that a contact has been removed from the ongoing conversation.<br/>                                                                                                                                                                                  |
| [**OnIMWindowCreated**](im-dmessengerevents-onimwindowcreated.md)                     | Indicates that a new conversation window has been opened.<br/>                                                                                                                                                                                                 |
| [**OnIMWindowDestroyed**](im-dmessengerevents-onimwindowdestroyed.md)                 | Indicates that a new conversation window has been closed.<br/>                                                                                                                                                                                                 |
| [**OnMyFriendlyNameChange**](im-dmessengerevents-onmyfriendlynamechange.md)           | Indicates that the local client's friendly name has been changed or that a change was attempted.<br/>                                                                                                                                                          |
| [**OnMyPhoneChange**](im-dmessengerevents-onmyphonechange.md)                         | Indicates that the local client's phone contact information has been changed or that a change was attempted.<br/>                                                                                                                                              |
| [**OnMyPropertyChange**](im-dmessengerevents-onmypropertychange.md)                   | Indicates that an uncategorized element of the local client's property information has been changed or that a change was attempted.<br/>                                                                                                                       |
| [**OnMyStatusChange**](im-dmessengerevents-onmystatuschange.md)                       | Indicates that the status of the local client has changed or that a status change was attempted, and returns the current status of the local client.<br/>                                                                                                      |
| [**OnSignin**](im-dmessengerevents-onsignin.md)                                       | Indicates that an attempt has been made to sign in to the primary service.<br/>                                                                                                                                                                                |
| [**OnSignout**](im-dmessengerevents-onsignout.md)                                     | Indicates that the local client has signed out of the primary service. <br/>                                                                                                                                                                                   |
| [**OnUnreadEmailChange**](im-dmessengerevents-onunreademailchange.md)                 | Indicates the number of unread e-mail messages in the Messenger client's correlated Outlook.com Inbox that have changed from the last count of previous [**OnUnreadEmailChange**](im-dmessengerevents-onunreademailchange.md) events or initial sign-in.<br/> |



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Product<br/>                  | Messenger 4.0<br/>                                                              |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





