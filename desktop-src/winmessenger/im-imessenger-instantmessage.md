---
title: IMessenger InstantMessage method
description: Launches a conversation window with the initial recipient specified as a parameter.
ms.assetid: ea372150-165b-4b3a-95c1-67713d8ad69a
keywords:
- InstantMessage method Windows Messenger
- InstantMessage method Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , InstantMessage method
topic_type:
- apiref
api_name:
- IMessenger.InstantMessage
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

# IMessenger::InstantMessage method

\[**InstantMessage** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Launches a conversation window with the initial recipient specified as a parameter.

## Syntax


```C++
HRESULT InstantMessage(
  [in]          VARIANT   vContact,
  [out, retval] IDispatch **ppMWindow
);
```



## Parameters

<dl> <dt>

*vContact* \[in\]
</dt> <dd>

Type: **VARIANT**

A **VARIANT** that can take as its value either a **VT\_BSTR** string or a **VT\_DISPATCH** pointer to an existing [**MessengerContact**](im-messengercontact.md) object.

If the input value type is a string, this method creates a new [**MessengerContact**](im-messengercontact.md) object internally. The string should be the full sign-in name. For a Microsoft .NET Messenger Service contact, this should include an "at" sign (@) and domain name.

If the input value type is a pointer to an existing [**MessengerContact**](im-messengercontact.md) object (should be type **VT\_DISPATCH**), the existing object is used for contact information.

</dd> <dt>

*ppMWindow* \[out, retval\]
</dt> <dd>

Type: **IDispatch\*\***

A pointer to a pointer to the [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on a [**MessengerWindow**](im-messengerwindow.md) object, which can be accessed through the [**IMessengerWindow**](im-imessengerwindow.md) interface that is used to call other automation-accessible properties, such as [**Height**](im-imessengerwindow-height.md), [**Width**](im-imessengerwindow-width.md), [**Top**](im-imessengerwindow-top.md), [**Left**](im-imessengerwindow-left.md), and [**Show**](im-imessengerwindow--show.md).</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values. 



| Return code                                                                                               | Description                                                                                                                                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Success. <br/>                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>**RPC\_X\_NULL\_REF\_POINTER**</dt> </dl> | *ppMWindow* is a **NULL** pointer. <br/>                                                                                                                                                                                                                                                                               |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>              | *vContact* is **NULL**, points to a **NULL** string, or points to a string that has a space as the first character.<br/> - or -<br/> *vContact* is a **VT\_BSTR** that exceeded 129 characters.<br/> - or -<br/> *vContact* is a **VT\_BSTR** and contains a carriage return or linefeed.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>                    | Called this method against the local client user. <br/>                                                                                                                                                                                                                                                                |
| <dl> <dt>**S\_FALSE**</dt> </dl>                   | Could not bring focus to the window.<br/>                                                                                                                                                                                                                                                                              |
| <dl> <dt>**MSGR\_E\_NOT\_LOGGED\_ON**</dt> </dl>   | Client was not signed in the primary service at the time this method was called.<br/>                                                                                                                                                                                                                                  |



 

## Remarks

If a conversation window is already open to a session with the user specified by *vContact* (and *ppMWindow* has not been released), no new window is displayed, no specific HResult is returned (returns S\_OK), and the existing window instance will be referenced by the [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) pointer in the return value. If the specified *vContact* parameter represents different contacts in each case, more than one conversation window may be open in the client.

Because conversation windows are not modal, options or other client control UI can be open at the same time.

All windows will be closed if the client signs out. If the client goes offline, the [**MessengerWindow**](im-messengerwindow.md) objects that correspond to those windows will become de-referenced and should be released. Calling APIs on these objects is no longer valid.

Because there is no way to specify a secondary service contact through this method, **InstantMessage** should not be used to send an instant message to a contact who is not in the Messenger service and does not already exist as a [**MessengerContact**](im-messengercontact.md) object. To open a conversation window to a secondary service user, the *vContact* parameter should be an existing **MessengerContact** object that has already been properly established, using the desired secondary service when creating or accessing that object.

A client cannot open a message to the local client user. This will result in E\_FAIL. In this case, check [**IsSelf**](im-imessengercontact-isself.md) or do a string comparison of *vContact* and [**MySigninName**](im-imessenger-mysigninname.md).

*ppMWindow* should be released when it is no longer needed.

The Windows Messenger APIs cannot determine whether a message can be successfully delivered. The success or failure of delivery is known only to the client user in real time. The process of clicking the **Send** button (thereby submitting the message to the Messenger servers for distribution) is controlled by the client user and cannot be automated. Users of the **InstantMessage** API should still make their best effort to assure that the *vContact* string they pass specifies a legitimately addressable user. Validation and error checking for the supplied contact's name should be performed before it reaches this method. When this method is invoked, the conversation UI will always be displayed, even if the value entered for *vContact* is not a valid user or in a valid format.

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
</dt> <dt>

[**IMessengerContact**](im-imessengercontact.md)
</dt> </dl>

 

 





