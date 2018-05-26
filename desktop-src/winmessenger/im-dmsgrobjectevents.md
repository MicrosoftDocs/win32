---
title: DMsgrObjectEvents interface
description: Do not use.
ms.assetid: cb6f5781-170f-46ac-9dd1-9adc35fdaa21
keywords:
- DMsgrObjectEvents interface Windows Messenger
- DMsgrObjectEvents interface Windows Messenger , described
topic_type:
- apiref
api_name:
- DMsgrObjectEvents
api_location:
- Msmsgs.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DMsgrObjectEvents interface

\[**DMsgrObjectEvents** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **DMsgrObjectEvents** dispinterface handles events that are generated or received by a [**MsgrObject**](im-msgrobject.md) object.

> [!Note]  
> The **DMsgrObjectEvents** dispinterface is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**DMessengerEvents**](im-dmessengerevents.md) instead.

 

## Members

The **DMsgrObjectEvents** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **DMsgrObjectEvents** also has these types of members:

-   [Events](#events)

### Events

The **DMsgrObjectEvents** interface has these events.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Event</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>OnAppInviteAccepted</strong>](im-dmsgrobjectevents-onappinviteaccepted.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnAppInviteCancelled</strong>](im-dmsgrobjectevents-onappinvitecancelled.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnAppInviteReceived</strong>](im-dmsgrobjectevents-onappinvitereceived.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnAppShutDown</strong>](im-dmsgrobjectevents-onappshutdown.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnBuddyPropertyChangeResult</strong>](im-dmsgrobjectevents-onbuddypropertychangeresult.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnFileTransferCancelled</strong>](im-dmsgrobjectevents-onfiletransfercancelled.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnFileTransferInviteAccepted</strong>](im-dmsgrobjectevents-onfiletransferinviteaccepted.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnFileTransferInviteCancelled</strong>](im-dmsgrobjectevents-onfiletransferinvitecancelled.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnFileTransferInviteReceived</strong>](im-dmsgrobjectevents-onfiletransferinvitereceived.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnFileTransferStatusChange</strong>](im-dmsgrobjectevents-onfiletransferstatuschange.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnFindResult</strong>](im-dmsgrobjectevents-onfindresult.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnInviteMailResult</strong>](im-dmsgrobjectevents-oninvitemailresult.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnInviteUser</strong>](im-dmsgrobjectevents-oninviteuser.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnListAddResult</strong>](im-dmsgrobjectevents-onlistaddresult.md)</td>
<td style="text-align: left;">Indicates the result of an attempt to add to the <strong>Messenger User</strong> object's User List. <br/>
<blockquote>
[!Note]<br />
The [<strong>OnListAddResult</strong>](im-dmsgrobjectevents-onlistaddresult.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>OnContactListAdd</strong>](im-dmessengerevents-oncontactlistadd.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnListRemovedResult</strong>](im-dmsgrobjectevents-onlistremoveresult.md)</td>
<td style="text-align: left;">Indicates the result of an attempt to remove a user from the <strong>Messenger User</strong> object's User List. <br/>
<blockquote>
[!Note]<br />
The [<strong>OnListRemovedResult</strong>](im-dmsgrobjectevents-onlistremoveresult.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>OnContactListRemove</strong>](im-dmessengerevents-oncontactlistremove.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnLocalFriendlyNameChangeResult</strong>](im-dmsgrobjectevents-onlocalfriendlynamechangeresult.md)</td>
<td style="text-align: left;">Indicates that the settings of a user in the local client's User List have changed. <br/>
<blockquote>
[!Note]<br />
The [<strong>OnLocalFriendlyNameChangeResult</strong>](im-dmsgrobjectevents-onlocalfriendlynamechangeresult.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>OnMyFriendlyNameChange</strong>](im-dmessengerevents-onmyfriendlynamechange.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnLocalPropertyChangeResult</strong>](im-dmsgrobjectevents-onlocalpropertychangeresult.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnLocalStateChangeResult</strong>](im-dmsgrobjectevents-onlocalstatechangeresult.md)</td>
<td style="text-align: left;">Indicates that the status of the local client has been changed or that a status change was attempted. <br/>
<blockquote>
[!Note]<br />
The [<strong>OnLocalStateChangeResult</strong>](im-dmsgrobjectevents-onlocalstatechangeresult.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>OnMyStatusChange</strong>](im-dmessengerevents-onmystatuschange.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnLogonoff</strong>](im-dmsgrobjectevents-onlogonoff.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnLogonResult</strong>](im-dmsgrobjectevents-onlogonresult.md)</td>
<td style="text-align: left;">Indicates that an attempt has been made to sign in to the primary service. <br/>
<blockquote>
[!Note]<br />
The [<strong>OnLogonResult</strong>](im-dmsgrobjectevents-onlogonresult.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>OnSignin</strong>](im-dmessengerevents-onsignin.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnMessagePrivacyChangeResult</strong>](im-dmsgrobjectevents-onmessageprivacychangeresult.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnNewerClientAvailable</strong>](im-dmsgrobjectevents-onnewerclientavailable.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnNewSessionRequest</strong>](im-dmsgrobjectevents-onnewsessionrequest.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnNotificationReceived</strong>](im-dmsgrobjectevents-onnotificationreceived.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnPrimaryServiceChanged</strong>](im-dmsgrobjectevents-onprimaryservicechanged.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnPromptChangeResult</strong>](im-dmsgrobjectevents-onpromptchangeresult.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnRequestURLPostResult</strong>](im-dmsgrobjectevents-onrequesturlpostresult.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnRequestURLResult</strong>](im-dmsgrobjectevents-onrequesturlresult.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnSendResult</strong>](im-dmsgrobjectevents-onsendresult.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnServiceLogonoff</strong>](im-dmsgrobjectevents-onservicelogonoff.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnSessionStateChange</strong>](im-dmsgrobjectevents-onsessionstatechange.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnSPMessageReceived</strong>](im-dmsgrobjectevents-onspmessagereceived.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnTextReceived</strong>](im-dmsgrobjectevents-ontextreceived.md)</td>
<td style="text-align: left;">Indicates that a message has been received. <br/>
<blockquote>
[!Note]<br />
The [<strong>OnTextReceived</strong>](im-dmsgrobjectevents-ontextreceived.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnTrustChanged</strong>](im-dmsgrobjectevents-ontrustchanged.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnUnreadEmailChanged</strong>](im-dmsgrobjectevents-onunreademailchanged.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnUserDropped</strong>](im-dmsgrobjectevents-onuserdropped.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnUserFriendlyNameChangeResult</strong>](im-dmsgrobjectevents-onuserfriendlynamechangeresult.md)</td>
<td style="text-align: left;">Indicates that a user in the User List has changed his or her friendly name. <br/>
<blockquote>
[!Note]<br />
The [<strong>OnUserFriendlyNameChangeResult</strong>](im-dmsgrobjectevents-onuserfriendlynamechangeresult.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>OnContactFriendlyNameChange</strong>](im-dmessengerevents-oncontactfriendlynamechange.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnUserJoin</strong>](im-dmsgrobjectevents-onuserjoin.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnUserLeave</strong>](im-dmsgrobjectevents-onuserleave.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnUserStateChanged</strong>](im-dmsgrobjectevents-onuserstatechanged.md)</td>
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



 

 





