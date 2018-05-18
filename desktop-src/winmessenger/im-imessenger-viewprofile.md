---
title: IMessenger ViewProfile method
description: Launches a new browser instance, allowing the client user to view properties of the specified contact through the Public Profiles feature.
ms.assetid: 'f0c045b9-8ad1-4909-bfc7-d7c82af22859'
keywords: ["ViewProfile method Windows Messenger", "ViewProfile method Windows Messenger , IMessenger interface", "IMessenger interface Windows Messenger , ViewProfile method"]
topic_type:
- apiref
api_name:
- IMessenger.ViewProfile
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessenger::ViewProfile method

\[**ViewProfile** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Launches a new browser instance, allowing the client user to view properties of the specified contact through the **Public Profiles** feature.

## Syntax


```C++
HRESULT ViewProfile(
  [in] VARIANT vContact
);
```



## Parameters

<dl> <dt>

*vContact* \[in\]
</dt> <dd>

Type: **VARIANT**

A **VARIANT** that can take as its value either a **VT\_BSTR** string or a **VT\_DISPATCH** pointer to an existing [**MessengerContact**](im-messengercontact.md) object. If the input value type is a string, this method creates a new **MessengerContact** object internally. The string should be the full sign-in name. For a Microsoft .NET Messenger Service contact, this should include the "at" sign (@) and domain name. If the input value type is a pointer to an existing **MessengerContact** object (should be type **VT\_DISPATCH**), the existing object is used.

</dd> </dl>

## Return value

Type: **HRESULT**

For a table of MSGR\_E\_\* constants, see[**MSGRConstants**](im-msgrconstants.md).

Returns one of the following values.



| Return code                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Success.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | *vContact* value is **NULL**, the wrong type, points to a **NULL** string, or points to a string that has a space as the first character.<br/> - or -<br/> *vContact* is a **VT\_BSTR** that exceeded 129 characters (130 if the string terminator is included in the cout. This allows for a 64-character sign-in name, @ symbol, and a 64-character domain name. This format does not have to be followed.)<br/> - or -<br/> *vContact* is a **VT\_BSTR** and contains a carriage return or linefeed.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Unspecified failure.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <dl> <dt>**MSGR\_E\_NOT\_LOGGED\_ON**</dt> </dl> | Client is offline.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |



 

## Remarks

This option is available in the Microsoft Exchange Instant Messaging Service (IM) client, but only for Microsoft .NET Messenger Service users.

Calling this method on a user or service other than the Microsoft .NET Messenger Service will launch the browser instance, but the interface will not find a valid user. Because profiles (and each element of data therein) are opt-in, even Microsoft .NET Messenger Service users are not guaranteed to have profiles available.

To use this method with Windows Messenger, you must install an add-in component that supports viewing profiles.

This method will launch the Web page even if a contact does not have a public profile established or enabled for view. Error messaging on that Web page may inform the client user that the specified contact does not have a profile available.

This method should be called on the local user's sign-in name to obtain public profile information on the local client user.

> [!Note]  
> This method is available for scripting languages but it returns E\_NOTIMPL.

 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMessenger**](im-imessenger.md)
</dt> <dt>

[**IMessengerContact**](im-imessengercontact.md)
</dt> </dl>

 

 





