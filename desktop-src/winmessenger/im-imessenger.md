---
title: IMessenger interface
description: Do not use. The primary interface for Windows Messenger APIs calls. Includes methods for displaying Messenger client UI, getting or setting selected properties of the local client user, and utility methods.
ms.assetid: 7bbec80f-02ea-4f3f-b535-3a20d490e095
keywords:
- IMessenger interface Windows Messenger
- IMessenger interface Windows Messenger , described
topic_type:
- apiref
api_name:
- IMessenger
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

# IMessenger interface

\[**IMessenger** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The primary interface for Windows Messenger APIs calls. Includes methods for displaying Messenger client UI, getting or setting selected properties of the local client user, and utility methods.

## Members

The **IMessenger** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IMessenger** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMessenger** interface has these methods.



| Method                                                 | Description                                                                                                                                                                                                                                                                                                                   |
|:-------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddContact**](im-imessenger-addcontact.md)         | Launches the **Add a Contact** wizard.<br/>                                                                                                                                                                                                                                                                             |
| [**AutoSignin**](im-imessenger-autosignin.md)         | Signs the local client in automatically using the last sign-in name and saved password information.<br/>                                                                                                                                                                                                                |
| [**FindContact**](im-imessenger-findcontact.md)       | Launches the **Add a Contact** wizard to the screen used for finding a contact based on information supplied as input parameters.<br/>                                                                                                                                                                                  |
| [**GetContact**](im-imessenger-getcontact.md)         | Creates a [**MessengerContact**](im-messengercontact.md) object that can be used to call methods of the Windows Messenger interfaces, such as **IMessenger**, [**IMessengerContact**](im-imessengercontact.md), and [**IMessengerContacts**](im-imessengercontacts.md).<br/>                                         |
| [**InstantMessage**](im-imessenger-instantmessage.md) | Launches a conversation window with the initial recipient specified as a parameter.<br/>                                                                                                                                                                                                                                |
| [**InviteApp**](im-imessenger-inviteapp.md)           | Issues an invitation to a user to use a specified application.<br/>                                                                                                                                                                                                                                                     |
| [**MediaWizard**](im-imessenger-mediawizard.md)       | Launches the **Audio and Video Tuning Wizard** dialog box.<br/>                                                                                                                                                                                                                                                         |
| [**OpenInbox**](im-imessenger-openinbox.md)           | Launches the default e-mail application and opens the Inbox.<br/>                                                                                                                                                                                                                                                       |
| [**OptionsPages**](im-imessenger-optionspages.md)     | Launches the **Options** dialog box with a specified tab displayed.<br/>                                                                                                                                                                                                                                                |
| [**Page**](im-imessenger-page.md)                     | Launches the **Page** window that is used to page a user, as designated by the input parameter.<br/>                                                                                                                                                                                                                    |
| [**Phone**](im-imessenger-phone.md)                   | Launches the **Phone Call** dialog box.<br/>                                                                                                                                                                                                                                                                            |
| [**SendFile**](im-imessenger-sendfile.md)             | Launches the **Send File** mode of a conversation window to a specified contact.<br/>                                                                                                                                                                                                                                   |
| [**SendMail**](im-imessenger-sendmail.md)             | Launches a new message in the client's default e-mail application with the To: line prepopulated with the sign-in name of the specified contact.<br/>                                                                                                                                                                   |
| [**Signin**](im-imessenger-signin.md)                 | Launches the Messenger client **Sign In** dialog box and populates the sign-in name field. The behavior of this method will vary, depending on the Messenger client version, the host operating system, and the primary service for the client. For more information, see the Remarks section later in this topic.<br/> |
| [**Signout**](im-imessenger-signout.md)               | Signs the current client user out of all Mesenger services.<br/>                                                                                                                                                                                                                                                        |
| [**StartVoice**](im-imessenger-startvoice.md)         | Launches a Messenger conversation window to initiate a voice message session with a particular contact, pending acceptance of the invitation.<br/>                                                                                                                                                                      |
| [**ViewProfile**](im-imessenger-viewprofile.md)       | Launches a new browser instance, allowing the client user to view properties of the specified contact through the **Public Profiles** feature.<br/>                                                                                                                                                                     |



 

### Properties

The **IMessenger** interface has these properties.



| Property                                                                      | Access type          | Description                                                                                                                                                                                                                                                                                            |
|:------------------------------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MyContacts**](im-imessenger-mycontacts.md)<br/>                     | Read-only<br/> | Retrieves the contact list contained in the client or [**Messenger**](im-messenger.md) object. The retrieved list is a [**MessengerContacts**](im-messengercontacts.md) collection object that can be manipulated with the [**IMessengerContacts**](im-imessengercontacts.md) interface.<br/> |
| [**MyFriendlyName**](im-imessenger-myfriendlyname.md)<br/>             | Read-only<br/> | Deprecated in Windows Messenger 5.0. Retrieves the friendly (display) name of the local client user.<br/>                                                                                                                                                                                        |
| [**MyPhoneNumber**](im-imessenger-myphonenumber.md)<br/>               | Read-only<br/> | Retrieves the stored phone number of the local client user.<br/>                                                                                                                                                                                                                                 |
| [**MyProperty**](im-imessenger-myproperty.md)<br/>                     | Read-only<br/> | Reserved. Do not use.<br/>                                                                                                                                                                                                                                                                       |
| [**MyServiceId**](im-imessenger-myserviceid.md)<br/>                   | Read-only<br/> | Deprecated in Windows Messenger 5.0. Retrieves the service ID, a GUID, of the primary service to which the local client user is currently signed in.<br/>                                                                                                                                        |
| [**MyServiceName**](im-imessenger-myservicename.md)<br/>               | Read-only<br/> | Deprecated in Windows Messenger 5.0. Retrieves the service name of the primary service to which the local client user is currently signed in.<br/>                                                                                                                                               |
| [**MySigninName**](im-imessenger-mysigninname.md)<br/>                 | Read-only<br/> | Deprecated in Windows Messenger 5.0. Sign-in name.<br/>                                                                                                                                                                                                                                          |
| [**MyStatus**](im-imessenger-mystatus.md)<br/>                         | Read-only<br/> | Deprecated in Windows Messenger 5.0. Service status.<br/>                                                                                                                                                                                                                                        |
| [**ReceiveFileDirectory**](im-imessenger-receivefiledirectory.md)<br/> | Read-only<br/> | Retrieves the local path to the directory currently being used to store any files received through file transfer.<br/>                                                                                                                                                                           |
| [**Services**](im-imessenger-services.md)<br/>                         | Read-only<br/> | Returns a list of services being used by the Messenger client.<br/>                                                                                                                                                                                                                              |
| [**UnreadEmailCount**](im-imessenger-unreademailcount.md)<br/>         | Read-only<br/> | Retrieves the current number of unread e-mail messages in the Inbox assigned to the currently signed-in client user.<br/>                                                                                                                                                                        |
| [**Window**](im-imessenger-window.md)<br/>                             | Read-only<br/> | Gets a pointer to a [**MessengerWindow**](im-messengerwindow.md) object that is used to control automation properties of the main application window, including dimensions, positioning, and visibility.<br/>                                                                                   |



 

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



 

 





