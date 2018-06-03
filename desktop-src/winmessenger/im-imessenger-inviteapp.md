---
title: IMessenger InviteApp method
description: Issues an invitation to a user to use a specified application.
ms.assetid: 5190329f-9f36-41f8-be6c-bf808a515c9a
keywords:
- InviteApp method Windows Messenger
- InviteApp method Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , InviteApp method
topic_type:
- apiref
api_name:
- IMessenger.InviteApp
api_location:
- Msgsc.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMessenger::InviteApp method

\[**InviteApp** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Issues an invitation to a user to use a specified application.

## Syntax


```C++
HRESULT InviteApp(
  [in]          VARIANT   vContact,
  [in]          BSTR      bstrAppID,
  [out, retval] IDispatch **ppMWindow
);
```



## Parameters

<dl> <dt>

*vContact* \[in\]
</dt> <dd>

Type: **VARIANT**

A **VARIANT** that designates a particular contact. This **VARIANT** should be either:

-   A **VT\_BSTR** **VARIANT** that contains the sign-in name of the contact.
-   A **VT\_DISPATCH** **VARIANT** that contains a pointer to a [**MessengerContact**](im-messengercontact.md) object that has already been established for a particular contact.

</dd> <dt>

*bstrAppID* \[in\]
</dt> <dd>

Type: **BSTR**

The GUID in **BSTR** form used to register the application that the remote user is being invited to share. This corresponds to the values set in the system registry during the installation of that application.

**Important**  To parse the GUID, you must include the curly braces { } on either side as part of this string. This parameter is a string, not a GUID structure, so it works in scripting.

</dd> <dt>

*ppMWindow* \[out, retval\]
</dt> <dd>

Type: **IDispatch\*\***

A pointer to a pointer to the [IDispatch](https://msdn.microsoft.com/windows/desktop/c1accca9-971c-4435-8a5e-e25404a3fb25) interface on a [**MessengerWindow**](im-messengerwindow.md) object, which can be accessed through the [**IMessengerWindow**](im-imessengerwindow.md) interface that is used to call other automation-accessible properties, such as [**Height**](im-imessengerwindow-height.md), [**Width**](im-imessengerwindow-width.md), [**Top**](im-imessengerwindow-top.md), [**Left**](im-imessengerwindow-left.md), and [**Show**](im-imessengerwindow--show.md).</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Success. <br/>                                                                                                                                                                                                                                                                                                                                                                                                |
| <dl> <dt>**RPC\_X\_NULL\_REF\_POINTER**</dt> </dl>  | *ppMWindow* is a **NULL** pointer. <br/>                                                                                                                                                                                                                                                                                                                                                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>               | **NULL** object or an empty string given for *bstrAppID*.<br/> - or -<br/> *vContact* is **NULL**, points to a **NULL** string, or points to a string that has a space as the first character.<br/> - or -<br/> *vContact* is a **VT\_BSTR** that exceeded 129 characters.<br/> - or -<br/> *vContact* is a **VT\_BSTR** and contains a carriage return or linefeed.<br/> |
| <dl> <dt>**S\_OUTOFMEMORY**</dt> </dl>              | Could not allocate memory for the new string.<br/>                                                                                                                                                                                                                                                                                                                                                            |
| <dl> <dt>**E\_FAIL**</dt> </dl>                     | Client was not signed in to the primary service at the time this method was called.<br/> - or -<br/> Called this method against the local client user.<br/>                                                                                                                                                                                                                                       |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl>                  | Cannot be called from script.<br/>                                                                                                                                                                                                                                                                                                                                                                            |
| <dl> <dt>**MSGR\_E\_POLICY\_RESTRICTED**</dt> </dl> | Windows Messenger 5.0 and later. The local computer or local user policy does not allow user to share applications. <br/>                                                                                                                                                                                                                                                                                     |



 

## Remarks

This interface is supported for contacts on Microsoft .NET Messenger Service as well as Microsoft Exchange Instant Messaging Service (IM).

If a conversation window is already open to a session with the user specified by *vContact* (and *ppMWindow* has not been released), no new window is displayed, no specific HResult is returned (returns S\_OK), and the existing window instance will be referenced by the [IDispatch](https://msdn.microsoft.com/windows/desktop/c1accca9-971c-4435-8a5e-e25404a3fb25) pointer in the return value.

This interface issues the invitation request only. The application to be used as an invite application must be compatible with Microsoft DirectPlay. The inviting client must have the application specified in the invitation installed. The API cannot determine whether the invitee's client has the application. Acceptance of the invitation will ultimately be a requirement for the full application invite sequence to succeed.

All windows will be closed if the client signs out. If the client goes offline, the [**MessengerWindow**](im-messengerwindow.md) objects that correspond to those windows will become dereferenced and should be released. Calling APIs on these objects is no longer valid.

A client cannot open a message or invitation to the local client user. This will result in E\_FAIL. This is also enforced by the UI. Check [**IsSelf**](im-imessengercontact-isself.md) or do a string comparison of *vContact* and [**MySigninName**](im-imessenger-mysigninname.md).

To determine valid applications on the inviting client, Windows Messenger code scans the registry and checks for DirectPlay compatibility associated with the given GUID. Currently, the only application not compatible with DirectPlay that can be used for invitations is Microsoft NetMeeting. Use the Windows 95 Active Setup GUID, {44BBA842-CC51-11CF-AAFA-00AA00B6015C}, even if the client platform is Microsoft Windows NT or Windows 2000 (which normally registers a Windows NT-specific GUID for NetMeeting).

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



 

 





