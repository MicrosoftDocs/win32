---
title: IMessenger UnreadEmailCount property
description: Retrieves the current number of unread e-mail messages in the Inbox assigned to the currently signed-in client user.
ms.assetid: 106fb15c-0276-4ad8-8fed-c83eea733bda
keywords:
- UnreadEmailCount property Windows Messenger
- UnreadEmailCount property Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , UnreadEmailCount property
topic_type:
- apiref
api_name:
- IMessenger.UnreadEmailCount
- IMessenger.get_UnreadEmailCount
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

# IMessenger::UnreadEmailCount property

\[**UnreadEmailCount** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the current number of unread e-mail messages in the Inbox assigned to the currently signed-in client user.

This property is read-only.

## Syntax


```C++
HRESULT get_UnreadEmailCount(
  [in]          MUAFOLDER mFolder,
  [out, retval] LONG      *plCount
);
```



## Property value

A pointer to a **LONG** that provides the total number of unread e-mail messages in the client user's e-mail Inbox. This value is determined upon initial client sign-in. If a user accesses the Outlook.com Inbox and reads those messages, an [**OnUnreadEmailChange**](im-dmessengerevents-onunreademailchange.md) event will be issued; the client should use the value of the *cUnreadEmail* parameter in the event to get the new unread message count.

## Error codes

For a table of MSGR\_E\_\* constants, see [**MSGRConstants**](im-msgrconstants.md).

Returns one of the following values.



| Name                                                                                                  | Meaning                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                                                                                                                                                                                                                                                                                                      |
| <dl> <dt>S\_FALSE</dt> </dl>                   | No Inbox is available. This may be the result for Microsoft .NET Messenger Service users whose sign-in names are not in the outlook.com domain. If this is the case, *plCount* will be -1 to differentiate it from the following second case. <br/> - or -<br/> Returned for scripting only. Client not signed in.<br/> |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *plCount* is a **NULL** pointer.<br/>                                                                                                                                                                                                                                                                                               |
| <dl> <dt>E\_FAIL</dt> </dl>                    | Attempted to specify *mFolder* as a value other than **MUAFOLDER\_INBOX**<br/>                                                                                                                                                                                                                                                      |
| <dl> <dt>MSGR\_E\_NOT\_LOGGED\_ON</dt> </dl>   | Returned for Visual Basic and Visual C++ only. Client is not signed in. Client must be signed in to check this value. If this error result is returned, *plCount* will be returned as -1.<br/>                                                                                                                                      |



## Remarks

When this method is invoked on a Microsoft Exchange Instant Messaging Service (IM) client, Exchange through Microsoft Outlook will always be invoked as the mail client. Calling this method will not determine the unread e-mail count in that client or account. If a Microsoft .NET Messenger Service is signed in as a primary or secondary service to the Exchange IM service, this method will return the number of unread e-mail messages from the Outlook.com Inbox.

At sign-in, the Messenger client internally flags whether the Microsoft .NET Messenger Service user has an Outlook.com Inbox. If so, the count is determined from the Outlook.com Inbox.

If the user does not have an Outlook.com Inbox, no value can be returned (will return -1). For information about why not all Outlook.com service users have Inboxes, see [**OpenInbox**](im-imessenger-openinbox.md).

To use this method in Windows Messenger, you must install an add-in component that supports e-mail integration.

For users who are not signed in, calling this method will not return a *plCount* value at all (VT\_EMPTY, not zero) and will not result in an error.

> [!Note]  
> The following remarks apply for scripting languages.
>
> -   This property is scriptable.
> -   You should not return MSGR\_E\_NOT\_LOGGED\_ON to avoid an exception.
> -   Clear the value returned to the user.

 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





