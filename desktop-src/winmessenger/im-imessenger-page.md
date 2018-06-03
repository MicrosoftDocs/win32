---
title: IMessenger Page method
description: Launches the Page window that is used to page a user, as designated by the input parameter.
ms.assetid: 2bfee1ac-4940-46c0-b47f-4431a57bf6d9
keywords:
- Page method Windows Messenger
- Page method Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , Page method
topic_type:
- apiref
api_name:
- IMessenger.Page
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

# IMessenger::Page method

\[**Page** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Launches the **Page** window that is used to page a user, as designated by the input parameter.

## Syntax


```C++
HRESULT Page(
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

A pointer to a pointer to the [IDispatch](https://msdn.microsoft.com/windows/desktop/c1accca9-971c-4435-8a5e-e25404a3fb25) interface on a [**MessengerWindow**](im-messengerwindow.md) object, which can be accessed through the [**IMessengerWindow**](im-imessengerwindow.md) interface that is used to call other automation-accessible properties, such as [**Height**](im-imessengerwindow-height.md), [**Width**](im-imessengerwindow-width.md), [**Top**](im-imessengerwindow-top.md), [**Left**](im-imessengerwindow-left.md), and [**Show**](im-imessengerwindow--show.md).

</dd> </dl>

## Return value

Type: **HRESULT**

For a table of all MSGR\_E\_\* constants [**MSGRConstants**](im-msgrconstants.md), see.

Returns one of the following values.



| Return code                                                                                                 | Description                                                                                                                                                                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Success. <br/>                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>**MSGR\_E\_PAGING\_UNAVAILABLE**</dt> </dl> | Could not initiate paging. This contact does not have mobile services enabled. The remote client must configure mobile services through its client options UI before this call will succeed. <br/>                                                                                                                     |
| <dl> <dt>**RPC\_X\_NULL\_REF\_POINTER**</dt> </dl>   | *ppMWindow* is a **NULL** pointer. <br/>                                                                                                                                                                                                                                                                               |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                | *vContact* is **NULL**, points to a **NULL** string, or points to a string that has a space as the first character.<br/> - or -<br/> *vContact* is a **VT\_BSTR** that exceeded 129 characters.<br/> - or -<br/> *vContact* is a **VT\_BSTR** and contains a carriage return or linefeed.<br/> |
| <dl> <dt>**MSGR\_E\_NOT\_LOGGED\_ON**</dt> </dl>     | Client was not signed in the primary service at the time this method was called.<br/>                                                                                                                                                                                                                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>                      | Could not create an **Instant Message** window. <br/> - or -<br/> Called this method while the **Sign In** dialog box was enabled and visible. <br/> - or -<br/> Called this method against the local client user.<br/>                                                                        |



 

## Remarks

The Microsoft Exchange Instant Messaging Service (IM) service cannot support this method. Calling this method on an Exchange service contact will fail.

To use this method with Windows Messenger, you must install an add-in component that supports paging.

*ppMWindow* should be released when it is no longer needed.

> [!Note]  
> This method is available for scripting languages but it returns E\_NOTIMPL.

 

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
</dt> </dl>

 

 





