---
title: IMsgrObject interface
description: Do not use.
ms.assetid: 1697ac9d-6a52-456e-9303-b4a0bed6ef62
keywords:
- IMsgrObject interface Windows Messenger
- IMsgrObject interface Windows Messenger , described
topic_type:
- apiref
api_name:
- IMsgrObject
api_location:
- Msmsgs.exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IMsgrObject interface

\[**IMsgrObject** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **IMsgrObject** interface provides methods and properties to handle the **Messenger Object**.

> [!Note]  
> The **IMsgrObject** interface is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**IMessenger**](im-imessenger.md) instead.

 

## Members

The **IMsgrObject** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IMsgrObject** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMsgrObject** interface has these methods.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Method</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>CreateIMSession</strong>](im-imsgrobject-createimsession.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>CreateUser</strong>](im-imsgrobject-createuser.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>FindUser</strong>](im-imsgrobject-finduser.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>LocalOption</strong>](im-imsgrobject-localoption.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>Logoff</strong>](im-imsgrobject-logoff.md)</td>
<td style="text-align: left;">Signs the current client user out of all Messenger services. <br/>
<blockquote>
[!Note]<br />
The [<strong>Logoff</strong>](im-imsgrobject-logoff.md) method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>Signout</strong>](im-imessenger-signout.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>Logon</strong>](im-imsgrobject-logon.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>RequestURLPost</strong>](im-imsgrobject-requesturlpost.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>SendAppInvite</strong>](im-imsgrobject-sendappinvite.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>SendAppInviteAccept</strong>](im-imsgrobject-sendappinviteaccept.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>SendAppInviteCancel</strong>](im-imsgrobject-sendappinvitecancel.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>SendInviteMail</strong>](im-imsgrobject-sendinvitemail.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>SessionRequestAccept</strong>](im-imsgrobject-sessionrequestaccept.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>SessionRequestCancel</strong>](im-imsgrobject-sessionrequestcancel.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
</tbody>
</table>



 

### Properties

The **IMsgrObject** interface has these properties.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Access type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>IMSessions</strong>](im-imsgrobject-imsessions.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>List</strong>](im-imsgrobject-list.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Retrieves information about users from an [<strong>MLIST</strong>](im-mlist.md). <br/>
<blockquote>
[!Note]<br />
The [<strong>List</strong>](im-imsgrobject-list.md) property is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>LocalFriendlyName</strong>](im-imsgrobject-localfriendlyname.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Retrieves the friendly (display) name of the local client user. <br/>
<blockquote>
[!Note]<br />
The [<strong>LocalFriendlyName</strong>](im-imsgrobject-localfriendlyname.md) property is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>MyFriendlyName</strong>](im-imessenger-myfriendlyname.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>LocalLogonName</strong>](im-imsgrobject-locallogonname.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Retrieves the sign-in name of the local client user. <br/>
<blockquote>
[!Note]<br />
The [<strong>LocalLogonName</strong>](im-imsgrobject-locallogonname.md) property is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>MySigninName</strong>](im-imessenger-mysigninname.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>LocalState</strong>](im-imsgrobject-localstate.md)<br/></td>
<td style="text-align: left;"></td>
<td style="text-align: left;">Sets or retrieves the connection state of the local client user in the primary service. <br/>
<blockquote>
[!Note]<br />
The [<strong>LocalState</strong>](im-imsgrobject-localstate.md) property is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>MyStatus</strong>](im-imessenger-mystatus.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>Services</strong>](im-imsgrobject-services.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>UnreadEmail</strong>](im-imsgrobject-unreademail.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
</tbody>
</table>



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Product<br/>                  | Messenger 4.0<br/>                                                              |
| Header<br/>                   | <dl> <dt>Mdisp.h</dt> </dl>    |
| IDL<br/>                      | <dl> <dt>Mdisp.idl</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Msmsgs.exe</dt> </dl> |



## See also

<dl> <dt>

[**IDispatch**](https://msdn.microsoft.com/windows/desktop/c1accca9-971c-4435-8a5e-e25404a3fb25)
</dt> <dt>

[**IMsgrObject**](im-imsgrobject.md)
</dt> </dl>

 

 





