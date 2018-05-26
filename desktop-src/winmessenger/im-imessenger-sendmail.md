---
title: IMessenger SendMail method
description: Launches a new message in the clients default e-mail application with the To line prepopulated with the sign-in name of the specified contact.
ms.assetid: d18427a6-152d-4eb6-81f8-ef5c7e36fc4a
keywords:
- SendMail method Windows Messenger
- SendMail method Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , SendMail method
topic_type:
- apiref
api_name:
- IMessenger.SendMail
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

# IMessenger::SendMail method

\[**SendMail** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Launches a new message in the client's default e-mail application with the To: line prepopulated with the sign-in name of the specified contact.

## Syntax


```C++
HRESULT SendMail(
  [in] VARIANT vContact
);
```



## Parameters

<dl> <dt>

*vContact* \[in\]
</dt> <dd>

Type: **VARIANT**

A **VARIANT** that can take as its value either a **VT\_BSTR** string or a **VT\_DISPATCH** pointer to an existing [**MessengerContact**](im-messengercontact.md) object. If the input value type is a string, this method creates a new **MessengerContact** object internally. The string should be the full sign-in name. For a Microsoft .NET Messenger Service contact, this should include the "@" symbol and domain name. If the input value type is a pointer to an existing **MessengerContact** object (should be type **VT\_DISPATCH**), the existing object is used.

</dd> </dl>

## Return value

Type: **HRESULT**

For a table of MSGR\_E\_\* constants, see [**MSGRConstants**](im-msgrconstants.md).

Returns one of the following values.



| Return code                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Success.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | *vContact* value is **NULL**, the wrong type, points to a **NULL** string, or points to a string that has a space as the first character.<br/> - or -<br/> *vContact* is a **VT\_BSTR** that exceeded 129 characters (130 if the string terminator is included in the cout. This allows for a 64-character sign-in name, @ symbol, and a 64-character domain name. This format does not have to be followed.)<br/> - or -<br/> *vContact* is a **VT\_BSTR** and contains a carriage return or linefeed.<br/> |
| <dl> <dt>**MSGR\_E\_NOT\_LOGGED\_ON**</dt> </dl> | The client is not logged in.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |



 

## Remarks

When this method is invoked on a Microsoft Exchange Instant Messaging Service (IM) client, Exchange through Microsoft Outlook will always be invoked as the mail client. Calling this method will launch or focus the 32-bit Outlook application with a new message to the specified contact.

At sign-in, the Messenger client internally flags whether the Microsoft .NET Messenger Service user has an Outlook.com Inbox. If so, a browser instance will be opened to the Outlook.com compose page, prefilled with the e-mail or sign-in name of the desired contact. If the user does not have an Outlook.com Inbox, then a default mailto: is thrown to the operating system, which opens the mail client registered to handle this protocol in the Windows Internet Explorer browser. In this case, most clients will allow the target e-mail name to be passed as part of a mailto: call and the To: line to be prefilled per the *vContact* parameter. This behavior is identical to the **Send Mail** menu option in the client UI.

In addition to dependencies on the service used by the local client user, there are also issues with the service of the contact to whom the mail is sent (for example, if *vContact* is a [**MessengerContact**](im-messengercontact.md) object in a service other than Microsoft .NET Messenger Service and Exchange IM). Not all services will always have an e-mail address accessible. Services might produce **MessengerContact** objects where there is no available e-mail address or no Messenger implementation for storing the e-mail address as a separate property from the sign-in name.

To use this method with Windows Messenger, you must install an add-in component that supports e-mail integration.

This method does not generate a conversation window, even though it takes a **VARIANT** form parameter for *vContact* like similar methods that do.

For Outlook.com, this method will always open a new default browser instance. This method cannot detect if other browser instances had a compose window or other functional areas of Outlook.com open. If Windows Live ID authentication is required to open the Outlook.com compose window, the authentication will take place automatically.

Users of Microsoft Outlook.com always have an e-mail account associated with the sign-in name used for Messenger. Users of @passport.com may authenticate through Windows Live ID into Microsoft .NET Messenger Service, but these users do not have corresponding e-mail accounts with either passport.com or Outlook.com as providers. Because Windows Live ID supports e-mail name as sign-in name (EASI), a user can sign in through Windows Live ID to the Microsoft .NET Messenger Service with a sign-in name that does not have either the @passport.com or "@outlook.com" suffix. In those cases in which there is no Outlook.com Inbox for the local client user, **SendMail** will launch the default mail client.

> [!Note]  
> This method is available for scripting languages.

 

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
</dt> </dl>

 

 





