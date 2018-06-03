---
title: IMessenger2 interface
description: Do not use. The secondary interface for the Windows Messenger API calls.
ms.assetid: 54be871d-3dcc-48d5-ab29-23cae10b02ef
keywords:
- IMessenger2 interface Windows Messenger
- IMessenger2 interface Windows Messenger , described
topic_type:
- apiref
api_name:
- IMessenger2
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

# IMessenger2 interface

\[**IMessenger2** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The secondary interface for the Windows Messenger API calls.

## Members

The **IMessenger2** interface inherits from [**IMessenger**](im-imessenger.md). **IMessenger2** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMessenger2** interface has these methods.



| Method                                            | Description                                                                                                                            |
|:--------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateGroup**](im-imessenger2-creategroup.md) | Creates a new group to the [**MessengerGroups**](im-messengergroups.md) collection object.<br/>                                 |
| [**StartVideo**](im-imessenger2-startvideo.md)   | Launches a conversation window to initiate a video session with a particular contact, pending acceptance of the invitation.<br/> |



 

### Properties

The **IMessenger2** interface has these properties.



| Property                                                                 | Access type          | Description                                                                                                                                                                                                                                                                        |
|:-------------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ContactsSortOrder**](im-imessenger2-contactssortorder.md)<br/> |                      | Sets or retrieves the current sort order for the local client, which is used to determine if the contacts should be sorted by groups or by their online/offline status.<br/>                                                                                                 |
| [**MyGroups**](im-imessenger2-mygroups.md)<br/>                   | Read-only<br/> | Retrieves the Group list contained in the [**Messenger**](im-messenger.md) object. The retrieved list is a [**MessengerGroups**](im-messengergroups.md) collection object that can be manipulated with the [**IMessengerGroups**](im-imessengergroups.md) interface.<br/> |



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Product<br/>                  | Messenger 4.5<br/>                                                              |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





