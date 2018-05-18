---
title: IMessenger OpenInbox method
description: IMessenger OpenInbox is no longer available for use as of Windows Vista.
ms.assetid: 'faa9a2bd-416d-4810-83ff-caded10c4b65'
keywords: ["OpenInbox method Windows Messenger", "OpenInbox method Windows Messenger , IMessenger interface", "IMessenger interface Windows Messenger , OpenInbox method"]
topic_type:
- apiref
api_name:
- IMessenger.OpenInbox
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessenger::OpenInbox method

\[**IMessenger::OpenInbox** is no longer available for use as of Windows Vista. For more information, see [Windows Messenger](im-messenger-entry.md).\]

Launches the default email application and opens the Inbox.

Calling **IMessenger::OpenInbox** on the Microsoft Exchange client version will open the user's Exchange Inbox instead of a webpage to Outlook.com or any registered default mailto: application. Otherwise, this method will return valid results only if Microsoft .NET Messenger Service is the primary and active service.

## Syntax


```C++
HRESULT OpenInbox();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

For a table of MSGR\_E\_\* constants, see [**MSGRConstants**](im-msgrconstants.md).

Returns one of the following values.



| Return code                                                                                             | Description                   |
|---------------------------------------------------------------------------------------------------------|-------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Success.<br/>           |
| <dl> <dt>**MSGR\_E\_NOT\_LOGGED\_ON**</dt> </dl> | Client is offline.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | General failure.<br/>   |



 

## Remarks

When this method is invoked on a Exchange Instant Messaging Service (IM) client, Exchange through Microsoft Outlook will always be invoked as the email client. Calling this method will launch or focus the 32-bit Outlook application with the Inbox open.

At sign-in, the Messenger client internally flags whether the Microsoft .NET Messenger Service user has an Outlook.com Inbox. If so, a browser instance will be opened to the Outlook.com Inbox. If the user does not have an Outlook.com Inbox, then a default mailto: is thrown to the operating system, which opens the mail client registered to handle this protocol in the Windows Internet Explorer browser. This behavior is identical to enabling the **My E-mail Inbox** menu options in the UI.

To use this method with Windows Messenger, you must install an add-in component that supports email integration.

The Microsoft .NET Messenger Service includes and is able to authenticate not just Microsoft Outlook.com users, but any user with a Windows Live ID. Microsoft .NET Messenger Service users may or may not have email accounts associated with their sign-in names. Users of Outlook.com always have email accounts associated with their sign-in names used for Messenger. Users of @passport.com may use the Microsoft .NET Messenger Service and authenticate through Windows Live ID into the Microsoft .NET Messenger Service, but these users do not have a corresponding email account with Passport.com. Windows Live ID also supports email name as sign-in name (EASI), which means that a user can sign in through Windows Live ID to the Microsoft .NET Messenger Service with a sign-in name that does not have either the @passport.com or "@outlook.com" suffix. In the EASI case, this sign-in name can be verified to be a legitimate email address because the person who established this Windows Live ID account must be able to respond to a verification email that is sent as part of the Windows Live ID registration process.

Services other than the Microsoft .NET Messenger Service and Exchange IM might not follow email conventions for sign-in names, in which case the **OpenInbox** method will not be useful.

> [!Note]  
> This method is available for scripting languages.

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMessenger**](im-imessenger.md)
</dt> <dt>

[**UnreadEmailCount**](im-imessenger-unreademailcount.md)
</dt> <dt>

[**SendMail**](im-imessenger-sendmail.md)
</dt> </dl>

 

 





