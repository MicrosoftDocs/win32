---
title: Messenger object
description: Do not use. The Messenger object implements the IMessenger3 interface and DMessengerEvents dispinterface. This object maintains lists of users and performs most automation functions.
ms.assetid: df8c17a7-63ae-4e72-bb8d-71c60e84a845
keywords:
- Messenger object Windows Messenger
- Messenger object Windows Messenger , described
topic_type:
- apiref
api_name:
- Messenger
api_location:
- Msgrua.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Messenger object

\[**Messenger** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **Messenger** object implements the [**IMessenger3**](im-imessenger3.md) interface and [**DMessengerEvents**](im-dmessengerevents.md) dispinterface. This object maintains lists of users and performs most automation functions.

## Remarks

System and MSMSGS.EXE implement this object.

The following interfaces exist for several helper objects implemented within MSMSGS.EXE: [**IMessenger2**](im-imessenger2.md), [**IMessengerContacts**](im-imessengercontacts.md), [**IMessengerContact**](im-imessengercontact.md), [**IMessengerWindow**](im-imessengerwindow.md), [**IMessengerGroup**](im-imessengergroup.md), [**IMessengerGroups**](im-imessengergroups.md), [**IMessengerService**](im-imessengerservice.md), [**IMessengerServices**](im-imessengerservices.md), [**IMessengerConversationWnd**](im-imessengerconversationwnd.md). Note that these interfaces are not accessible directly from the **Messenger** object.

> [!Note]  
> The following remark applies to scriptable languages.
>
> -   Although some scriptable members of the **Messenger** object deal with user-specific information (for example, friendly name or sign-in name), user-specific information is never available through script.

 

### Interfaces Implemented



[**IMessenger3**](im-imessenger3.md)

[**DMessengerEvents**](im-dmessengerevents.md)



 

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
| IID<br/>                      | CLSID\_Messenger is defined as B69003B3-C55E-4B48-836C-BC5946FC3B28<br/>        |



 

 





