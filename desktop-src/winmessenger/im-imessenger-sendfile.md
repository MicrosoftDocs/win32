---
title: IMessenger SendFile method
description: Launches the Send File mode of a conversation window to a specified contact.
ms.assetid: e366a488-1877-4ab3-9801-1334461a027f
keywords:
- SendFile method Windows Messenger
- SendFile method Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , SendFile method
topic_type:
- apiref
api_name:
- IMessenger.SendFile
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

# IMessenger::SendFile method

\[**SendFile** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Launches the **Send File** mode of a conversation window to a specified contact.

## Syntax


```C++
HRESULT SendFile(
  [in]          VARIANT   vContact,
  [in]          BSTR      bstrFileName,
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

*bstrFileName* \[in\]
</dt> <dd>

Type: **BSTR**

A **BSTR** specifying the name and local path of the file to send. If a valid value is passed into this parameter (**NULL** or empty string, and is less than or equal to 260 characters) then a standard **File** dialog box is displayed, allowing the user to specify a file to send. If a path is specified with the file name, the dialog box will open in that directory. Specifying a file name for *bstrFileName* populates the dialog box and does not attempt to validate or determine that the specified file exists.

</dd> <dt>

*ppMWindow* \[out, retval\]
</dt> <dd>

Type: **IDispatch\*\***

A pointer to a pointer to the [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on a [**MessengerWindow**](im-messengerwindow.md) object, which can be accessed through the [**IMessengerWindow**](im-imessengerwindow.md) interface that is used to call other automation-accessible properties, such as [**Height**](im-imessengerwindow-height.md), [**Width**](im-imessengerwindow-width.md), [**Top**](im-imessengerwindow-top.md), [**Left**](im-imessengerwindow-left.md), and [**Show**](im-imessengerwindow--show.md)

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Success. <br/>                                                                                                                                                                                                                                                                                                                                                                                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>              | *bstrFileName* exceeded 260 characters.<br/> - or -<br/> *vContact* value is **NULL**, the wrong type, points to a **NULL** string, or points to a string that has a space as the first character. <br/> - or -<br/> *vContact* is **VT\_BSTR** that exceeded 129 characters.<br/> - or -<br/> *bstrFileName* is **VT\_BSTR** and contains a carriage return, or linefeed.<br/> |
| <dl> <dt>**RPC\_X\_NULL\_REF\_POINTER**</dt> </dl> | *ppMWindow* is a **NULL** pointer.<br/>                                                                                                                                                                                                                                                                                                                                                                             |
| <dl> <dt>**MSGR\_E\_NOT\_LOGGED\_ON**</dt> </dl>   | Client is not signed in to the primary service at the time this method was called.<br/>                                                                                                                                                                                                                                                                                                                             |
| <dl> <dt>**E\_FAIL**</dt> </dl>                    | This method was called against the local client user.<br/>                                                                                                                                                                                                                                                                                                                                                          |



 

## Remarks

Both the sender and receiver clients must be capable of file transfer, which is potentially affected by firewalls, user preferences, routing, and so on. If no preexisting conversation window has been sent, a new one is created on the local client. A file can also be sent through an existing conversation window. It is not necessary to send text in order to initiate the file transfer.

The destination contact must accept or decline the file transfer. Because this method is asynchronous, there is no way to know through the API whether the destination user has accepted or declined. The status of the file transfer can be read through system messages in the conversation window created by this method.

If successful, calling this method will either open a new conversation window or send an existing one to the foreground of the destination contact's computer. If the window is not in the foreground on the destination client, it may initially appear as a pop-up message on the system tray. If a conversation window is already open to a session with the user specified by *vContact* (and *ppMWindow* has not been released), no new window is displayed, no specific HRESULT is returned (returns S\_OK), and the existing window instance will be referenced by the [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) pointer in the return value.

All conversation windows will be closed if the client signs out. If the client goes offline, the [**MessengerWindow**](im-messengerwindow.md) objects corresponding to those windows will become dereferenced and should be released. Calling APIs on these objects is no longer valid.

A client cannot open a message or invitation to the local client user. This will result in E\_FAIL. In this case, check [**IsSelf**](im-imessengercontact-isself.md) or do a string comparison of *vContact* and [**MySigninName**](im-imessenger-mysigninname.md).

*ppMWindow* should be released when it is no longer needed.

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

[**InstantMessage**](im-imessenger-instantmessage.md)
</dt> <dt>

[**InviteApp**](im-imessenger-inviteapp.md)
</dt> </dl>

 

 





