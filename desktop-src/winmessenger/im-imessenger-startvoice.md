---
title: IMessenger StartVoice method
description: Launches a Messenger conversation window to initiate a voice message session with a particular contact, pending acceptance of the invitation.
ms.assetid: ee6874f7-f9df-4d23-bddc-d0d5bbb0a26e
keywords:
- StartVoice method Windows Messenger
- StartVoice method Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , StartVoice method
topic_type:
- apiref
api_name:
- IMessenger.StartVoice
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

# IMessenger::StartVoice method

\[**StartVoice** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Launches a Messenger conversation window to initiate a voice message session with a particular contact, pending acceptance of the invitation.

## Syntax


```C++
HRESULT StartVoice(
  [in]          VARIANT   vContact,
  [out, retval] IDispatch **ppMWindow
);
```



## Parameters

<dl> <dt>

*vContact* \[in\]
</dt> <dd>

Type: **VARIANT**

A **VARIANT** that can take as its value either a **VT\_BSTR** string or a **VT\_DISPATCH** pointer to an existing [**MessengerContact**](im-messengercontact.md) object. If the input value type is a string, this method creates a new **MessengerContact** object internally. The string should be the full sign-in name. For a Microsoft .NET Messenger Service contact, this should include the "@" symbol and domain name. If the input value type is a pointer to an existing **MessengerContact** object (should be type **VT\_DISPATCH**), the existing object is used.

</dd> <dt>

*ppMWindow* \[out, retval\]
</dt> <dd>

Type: **IDispatch\*\***

A pointer to a pointer to the [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on a [**MessengerWindow**](im-messengerwindow.md) object, which can be accessed through the [**IMessengerWindow**](im-imessengerwindow.md) interface that is used to call other automation-accessible properties, such as [**Height**](im-imessengerwindow-height.md), [**Width**](im-imessengerwindow-width.md), [**Top**](im-imessengerwindow-top.md), [**Left**](im-imessengerwindow-left.md), and [**Show**](im-imessengerwindow--show.md).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                | Description                                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Success. <br/>                                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>               | *vContact* is **NULL**, the wrong type, points to a **NULL** string, or points to a string that has a space as the first character.<br/> - or -<br/> *vContact* is a **VT\_BSTR** that exceeded 129 characters.<br/> - or -<br/> *vContact* is a **VT\_BSTR** and contains a carriage return or linefeed.<br/> |
| <dl> <dt>**RPC\_X\_NULL\_REF\_POINTER**</dt> </dl>  | *ppMWindow* is a **NULL** pointer. <br/>                                                                                                                                                                                                                                                                                               |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>              | Internal object copy failed.<br/>                                                                                                                                                                                                                                                                                                      |
| <dl> <dt>**MSGR\_E\_NOT\_LOGGED\_ON**</dt> </dl>    | Client was not signed in the primary service at the time this method was called.<br/>                                                                                                                                                                                                                                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>                     | Message could not be initiated for some other reason.<br/> - or -<br/> Called this method against the local client user.<br/>                                                                                                                                                                                              |
| <dl> <dt>**MSGR\_E\_POLICY\_RESTRICTED**</dt> </dl> | Windows Messenger 5.0 and later. The local computer or local user policy does not allow users to start a voice communication. <br/>                                                                                                                                                                                                    |



 

## Remarks

Calling this API invokes the initial dialog box but does not track further actions. Failure of a voice channel initiation after the initial creation of the UI will return an error to which the client and client user will have to respond.

Both the sender and receiver clients must be capable of voice communication, which is potentially affected by firewalls, user preferences, routing, and so on. If no preexisting conversation window to this contact has been sent, a new window is created on the local client. Voice communication can also be sent through an existing conversation window. It is not necessary to send text in order to initiate the voice communication exchange.

If successful, calling this method will either open a new conversation window or send an existing one to the foreground of the destination contact's computer. This may initially appear as a pop-up message on the system tray if the window is not in the foreground on the destination client. If a window is already open to a session with the user specified by *vContact* (and *ppMWindow* has not been released), no new window is displayed, no specific HResult is returned (returns S\_OK), and the existing window instance will be referenced by the [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) pointer in the return value.

All windows will be closed if the client signs out. If the client goes offline, the [**MessengerWindow**](im-messengerwindow.md) objects corresponding to those windows will become dereferenced and should be released. Calling APIs on these objects is no longer valid.

A client cannot open a message or invitation to the local client user. This will result in E\_FAIL. In this case, check [**IsSelf**](im-imessengercontact-isself.md) or do a string comparison of *vContact* and [**MySigninName**](im-imessenger-mysigninname.md).

Like file transfers or invitations, voice communication requires the destination contact to accept or decline. However, there is no way to determine whether the destination contact is capable of voice communication, has accepted or declined, or is actually receiving the transmission. Because the voice communication features are integrated with a standard conversation window, the two parties can always communicate through text as a possible fallback.

Voice communication requires that both parties complete the **Audio and Video Tuning** wizard to align input and output levels for audio hardware on their client computers. Calling this method on a client that has not yet set audio levels will first display the **Audio and Video Tuning** wizard so that the user has a chance to set the levels at least once. For more information, see [**MediaWizard**](im-imessenger-mediawizard.md). It may be possible to detect whether the local client has run this wizard by checking to see if the registry keys

**HKEY\_CURRENT\_USER**\\**Software**\\**Microsoft**\\**MessengerService**\\**WaveIn Device ID**

and

**HKEY\_CURRENT\_USER**\\**Software**\\**Microsoft**\\**MessengerService**\\**WaveOut Device ID**

have been established. These key locations may vary in different operating systems.

*ppMWindow* should be released when it is no longer needed.

> [!Note]  
> This method is not available for scripting languages.

 

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
</dt> <dt>

[**InstantMessage**](im-imessenger-instantmessage.md)
</dt> <dt>

[**InviteApp**](im-imessenger-inviteapp.md)
</dt> <dt>

[**SendFile**](im-imessenger-sendfile.md)
</dt> </dl>

 

 





