---
title: Windows Messenger Client Reference
description: Client reference information for Windows Messenger.
ms.assetid: f5aad38c-25d1-4890-92dc-643a31be8d30
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Messenger Client Reference

\[Windows Messenger is no longer available for use as of Windows Vista. For more information, see [Windows Messenger](im-messenger-entry.md).\]

This documentation provides information about the Windows Messenger API which is a set of interfaces for objects related to the Messenger client. These APIs expose standard automation, messaging, and window management functionality.

New applications should not use this set of interfaces. These interfaces exist for backward compatibility with legacy applications. These interfaces will be unavailable in the future.

The [**Messenger**](im-messenger.md) interfaces include the basic object interface; several interfaces that house entities such as users, windows, and lists; and an event sink (connection point) interface.

## Enums



<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>[<strong>BASICIM_Constants</strong>](im-basicim-constants.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>BIMSTATE</strong>](im-bimstate.md)Do not use. Specifies local or remote client state.
<blockquote>
[!Note]<br />
The [<strong>BIMSTATE</strong>](im-bimstate.md) enumerated type is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>MISTATUS</strong>](im-mistatus.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td>[<strong>BIMUSERPROPERTY</strong>](im-bimuserproperty.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FONTSIZE</strong>](im-fontsize.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INFOBAR</strong>](im-infobar.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MCONNECTIONTYPE</strong>](im-mconnectiontype.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MCONTACTPROPERTY</strong>](im-mcontactproperty.md)Do not use. Used to ask for the property that indicates which groups a user belongs to, or the contact's e-mail address.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MFILETRANSFER_FLAGS</strong>](im-mfiletransfer-flags.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MFIRSTTIME_FLAGS</strong>](im-mfirsttime-flags.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MFOLDER</strong>](im-mfolder.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MINVITE_FLAGS</strong>](im-minvite-flags.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MISTATUS</strong>](im-mistatus.md)Do not use. Specifies local or remote client state. The user can select these options from the <strong>File</strong> menu of the <strong>Messenger</strong> window or by clicking the <strong>Messenger</strong> icon in the taskbar. The current state of the local user is detected on the local client. The current state of the remote clients is detected through the server automatically. Not all states are valid for remote clients. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>MLIST</strong>](im-mlist.md)Do not use. Used to retrieve information about contact lists.
<blockquote>
[!Note]<br />
The [<strong>MLIST</strong>](im-mlist.md) enumerated type is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>MLOCALOPTION</strong>](im-mlocaloption.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MLOCALOPTION_LIMITS</strong>](im-mlocaloption-limits.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MMESSENGERPROPERTY</strong>](im-mmessengerproperty.md)Do not use. Used to retrieve the Messenger client version and client locale ID (LCID). <br/></td>
</tr>
<tr class="odd">
<td>[<strong>MMSGPRIVACY</strong>](im-mmsgprivacy.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MMSGTYPE</strong>](im-mmsgtype.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MOPTDLGPAGE</strong>](im-moptdlgpage.md)Do not use. Specifies which page of the Messenger client <strong>Options</strong> dialog box to display to the user.
<blockquote>
[!Note]<br />
The [<strong>MOPTDLGPAGE</strong>](im-moptdlgpage.md) enumerated type is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>MOPTIONPAGE</strong>](im-moptionpage.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>MOPTIONPAGE</strong>](im-moptionpage.md)Do not use. Specifies which page of the Messenger client <strong>Options</strong> dialog box to display to the user through the user interface (UI) and several related tracking constants. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>MPFLFIELD</strong>](im-mpflfield.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MPHONE_TYPE</strong>](im-mphone-type.md)Do not use. Specifies which phone number of a given contact is used.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MPROMPT</strong>](im-mprompt.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MPROXYTYPE</strong>](im-mproxytype.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MSERVICEPROPERTY</strong>](im-mserviceproperty.md)Do not use. Used to ask for the property of a service. <br/></td>
</tr>
<tr class="even">
<td>[<strong>MSERVICE_FLAGS</strong>](im-mservice-flags.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MSGRConstants</strong>](im-msgrconstants.md)Do not use. The following are constants used for error and success returns of methods and properties of the Windows Messenger APIs. <br/></td>
</tr>
<tr class="even">
<td>[<strong>MSGRConstants</strong>](im-msgrobject-msgrconstants.md)Do not use. The following are constants used for error or success returns of methods and properties of the Windows Messenger APIs.
<blockquote>
[!Note]<br />
The [<strong>MSGRConstants</strong>](im-msgrobject-msgrconstants.md) enumerated type is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>MSGRConstants</strong>](im-msgrconstants.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td>[<strong>MSTATE</strong>](im-mstate.md)Do not use. Specifies local or remote client state.
<blockquote>
[!Note]<br />
The [<strong>MSTATE</strong>](im-mstate.md) enumerated type is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>MISTATUS</strong>](im-mistatus.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>MSVCSTATUS</strong>](im-msvcstatus.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MUAFOLDER</strong>](im-muafolder.md)Do not use. Used for selecting the folder for the count of unread messages.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MUASORT</strong>](im-muasort.md)Do not use. Specifies how the Contact List should be sorted.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MUPDATE_FLAGS</strong>](im-mupdate-flags.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MURLTYPE</strong>](im-murltype.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MUSERPROPERTY</strong>](im-muserproperty.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MWINDOWPROPERTY</strong>](im-mwindowproperty.md)Do not use. Used to turn on or off the conversation window sidebar and toolbar. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>SSTATE</strong>](im-sstate.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>VOICESESSIONSTATE</strong>](im-voicesessionstate.md)Not currently supported.<br/></td>
</tr>
</tbody>
</table>



 

## Events



<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>[<strong>OnAppShutdown</strong>](im-dbasicimevents-onappshutdown.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnContactListAddResult</strong>](im-dbasicimevents-oncontactlistaddresult.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnContactListRemoveResult</strong>](im-dbasicimevents-oncontactlistremoveresult.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnLocalStateChangeResult</strong>](im-dbasicimevents-onlocalstatechangeresult.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnLogoff</strong>](im-dbasicimevents-onlogoff.md)Indicates that the logoff is complete.
<blockquote>
[!Note]<br />
The [<strong>OnLogoff</strong>](im-dbasicimevents-onlogoff.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>OnSignout</strong>](im-dmessengerevents-onsignout.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>OnLogonResult</strong>](im-dbasicimevents-onlogonresult.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnUserFriendlyNameChangeResult</strong>](im-dbasicimevents-onuserfriendlynamechangeresult.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnUserStateChanged</strong>](im-dbasicimevents-onuserstatechanged.md)Indicates that the user's state has changed.
<blockquote>
[!Note]<br />
The [<strong>OnUserStateChanged</strong>](im-dbasicimevents-onuserstatechanged.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>OnContactStatusChange</strong>](im-dmessengerevents-oncontactstatuschange.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnBeforeLaunchIMUI</strong>](im-dmsgrobjectevents-onbeforelaunchimui.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnDestroyIMUI</strong>](im-dmsgrobjectevents-ondestroyimui.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnFileTransferIMUI</strong>](im-dmsgrobjectevents-onfiletransferimui.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnIndicateMessageReceivedIMUI</strong>](im-dmsgrobjectevents-onindicatemessagereceivedimui.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnInfobarTextIMUI</strong>](im-dmsgrobjectevents-oninfobartextimui.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnMicrophoneMuteIMUI</strong>](im-dmsgrobjectevents-onmicrophonemuteimui.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnSendEnabledIMUI</strong>](im-dmsgrobjectevents-onsendenabledimui.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnShowIMUI</strong>](im-dmsgrobjectevents-onshowimui.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnStatusTextIMUI</strong>](im-dmsgrobjectevents-onstatustextimui.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnTitlebarTextIMUI</strong>](im-dmsgrobjectevents-ontitlebartextimui.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnVoiceSessionStateIMUI</strong>](im-dmsgrobjectevents-onvoicesessionstateimui.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnAppShutdown</strong>](im-dmessengerevents-onappshutdown.md)Indicates that the client application is about to shut down for purposes of a client upgrade initiated either by the server or client user.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnContactAddedToGroup</strong>](im-dmessengerevents-oncontactaddedtogroup.md)Indicates that a contact has been added to a group.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnContactBlockChange</strong>](im-dmessengerevents-oncontactblockchange.md)Indicates that the block settings of a contact in the local client's Contact List have changed. Queries whether the contact is blocked by the local client user.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnContactFriendlyNameChange</strong>](im-dmessengerevents-oncontactfriendlynamechange.md)Indicates that a contact in the client's Contact List has changed the friendly name.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnContactListAdd</strong>](im-dmessengerevents-oncontactlistadd.md)Indicates the result of an attempt to add to the [<strong>Messenger</strong>](im-messenger.md) object's Contact List. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnContactListRemove</strong>](im-dmessengerevents-oncontactlistremove.md)Indicates the result of an attempt to remove a contact from the [<strong>Messenger</strong>](im-messenger.md) object's Contact List. <br/></td>
</tr>
<tr class="even">
<td>[<strong>OnContactPagerChange</strong>](im-dmessengerevents-oncontactpagerchange.md)Indicates that a contact in the local client's Contact List has changed the pager information access permissions.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnContactPhoneChange</strong>](im-dmessengerevents-oncontactphonechange.md)Indicates that the phone information of a contact in the local client's Contact List has changed.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnContactPropertyChange</strong>](im-dmessengerevents-oncontactpropertychange.md)Indicates that property information for a contact in the local client's Contact List has changed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnContactRemovedFromGroup</strong>](im-dmessengerevents-oncontactremovedfromgroup.md)Indicates that a contact has been removed from a group.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnContactStatusChange</strong>](im-dmessengerevents-oncontactstatuschange.md)Indicates that the status of a contact in the local client's Contact List has changed, and returns the current state of the contact.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnGroupAdded</strong>](im-dmessengerevents-ongroupadded.md) Indicates that a new group has been created.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnGroupNameChanged</strong>](im-dmessengerevents-ongroupnamechanged.md) Indicates that the name of a group has been changed.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnGroupRemoved</strong>](im-dmessengerevents-ongroupremoved.md)Indicates that a group has been deleted.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnIMWindowContactAdded</strong>](im-dmessengerevents-onimwindowcontactadded.md) Indicates that a contact has been added to the ongoing conversation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnIMWindowContactRemoved</strong>](im-dmessengerevents-onimwindowcontactremoved.md) Indicates that a contact has been removed from the ongoing conversation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnIMWindowCreated</strong>](im-dmessengerevents-onimwindowcreated.md) Indicates that a new conversation window has been opened.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnIMWindowDestroyed</strong>](im-dmessengerevents-onimwindowdestroyed.md)Indicates that a new conversation window has been closed.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnMyFriendlyNameChange</strong>](im-dmessengerevents-onmyfriendlynamechange.md) Indicates that the local client's friendly name has been changed or that a change was attempted.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnMyPhoneChange</strong>](im-dmessengerevents-onmyphonechange.md) Indicates that the local client's phone contact information has been changed or that a change was attempted.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnMyPropertyChange</strong>](im-dmessengerevents-onmypropertychange.md)Indicates that an uncategorized element of the local client's property information has been changed or that a change was attempted.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnMyStatusChange</strong>](im-dmessengerevents-onmystatuschange.md)Indicates that the status of the local client has changed or that a status change was attempted, and returns the current status of the local client.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnSignin</strong>](im-dmessengerevents-onsignin.md)Indicates that an attempt has been made to sign in to the primary service.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnSignout</strong>](im-dmessengerevents-onsignout.md)Indicates that the local client has signed out of the primary service. <br/></td>
</tr>
<tr class="even">
<td>[<strong>OnUnreadEmailChange</strong>](im-dmessengerevents-onunreademailchange.md)Indicates the number of unread e-mail messages in the Messenger client's correlated Outlook.com Inbox that have changed from the last count of previous [<strong>OnUnreadEmailChange</strong>](im-dmessengerevents-onunreademailchange.md) events or initial sign-in.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnAppInviteAccepted</strong>](im-dmsgrobjectevents-onappinviteaccepted.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnAppInviteCancelled</strong>](im-dmsgrobjectevents-onappinvitecancelled.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnAppInviteReceived</strong>](im-dmsgrobjectevents-onappinvitereceived.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnAppShutDown</strong>](im-dmsgrobjectevents-onappshutdown.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnBuddyPropertyChangeResult</strong>](im-dmsgrobjectevents-onbuddypropertychangeresult.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnFileTransferCancelled</strong>](im-dmsgrobjectevents-onfiletransfercancelled.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnFileTransferInviteAccepted</strong>](im-dmsgrobjectevents-onfiletransferinviteaccepted.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnFileTransferInviteCancelled</strong>](im-dmsgrobjectevents-onfiletransferinvitecancelled.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnFileTransferInviteReceived</strong>](im-dmsgrobjectevents-onfiletransferinvitereceived.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnFileTransferStatusChange</strong>](im-dmsgrobjectevents-onfiletransferstatuschange.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnFindResult</strong>](im-dmsgrobjectevents-onfindresult.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnInviteMailResult</strong>](im-dmsgrobjectevents-oninvitemailresult.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnInviteUser</strong>](im-dmsgrobjectevents-oninviteuser.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnListAddResult</strong>](im-dmsgrobjectevents-onlistaddresult.md)Indicates the result of an attempt to add to the <strong>Messenger User</strong> object's User List.
<blockquote>
[!Note]<br />
The [<strong>OnListAddResult</strong>](im-dmsgrobjectevents-onlistaddresult.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>OnContactListAdd</strong>](im-dmessengerevents-oncontactlistadd.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnListRemovedResult</strong>](im-dmsgrobjectevents-onlistremoveresult.md)Indicates the result of an attempt to remove a user from the <strong>Messenger User</strong> object's User List.
<blockquote>
[!Note]<br />
The [<strong>OnListRemovedResult</strong>](im-dmsgrobjectevents-onlistremoveresult.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>OnContactListRemove</strong>](im-dmessengerevents-oncontactlistremove.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>OnLocalFriendlyNameChangeResult</strong>](im-dmsgrobjectevents-onlocalfriendlynamechangeresult.md)Indicates that the settings of a user in the local client's User List have changed.
<blockquote>
[!Note]<br />
The [<strong>OnLocalFriendlyNameChangeResult</strong>](im-dmsgrobjectevents-onlocalfriendlynamechangeresult.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>OnMyFriendlyNameChange</strong>](im-dmessengerevents-onmyfriendlynamechange.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnLocalPropertyChangeResult</strong>](im-dmsgrobjectevents-onlocalpropertychangeresult.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnLocalStateChangeResult</strong>](im-dmsgrobjectevents-onlocalstatechangeresult.md)Indicates that the status of the local client has been changed or that a status change was attempted.
<blockquote>
[!Note]<br />
The [<strong>OnLocalStateChangeResult</strong>](im-dmsgrobjectevents-onlocalstatechangeresult.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>OnMyStatusChange</strong>](im-dmessengerevents-onmystatuschange.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnLogonoff</strong>](im-dmsgrobjectevents-onlogonoff.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnLogonResult</strong>](im-dmsgrobjectevents-onlogonresult.md)Indicates that an attempt has been made to sign in to the primary service.
<blockquote>
[!Note]<br />
The [<strong>OnLogonResult</strong>](im-dmsgrobjectevents-onlogonresult.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>OnSignin</strong>](im-dmessengerevents-onsignin.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnMessagePrivacyChangeResult</strong>](im-dmsgrobjectevents-onmessageprivacychangeresult.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnNewerClientAvailable</strong>](im-dmsgrobjectevents-onnewerclientavailable.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnNewSessionRequest</strong>](im-dmsgrobjectevents-onnewsessionrequest.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnNotificationReceived</strong>](im-dmsgrobjectevents-onnotificationreceived.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnPrimaryServiceChanged</strong>](im-dmsgrobjectevents-onprimaryservicechanged.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnPromptChangeResult</strong>](im-dmsgrobjectevents-onpromptchangeresult.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnRequestURLPostResult</strong>](im-dmsgrobjectevents-onrequesturlpostresult.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnRequestURLResult</strong>](im-dmsgrobjectevents-onrequesturlresult.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnSendResult</strong>](im-dmsgrobjectevents-onsendresult.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnServiceLogonoff</strong>](im-dmsgrobjectevents-onservicelogonoff.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnSessionStateChange</strong>](im-dmsgrobjectevents-onsessionstatechange.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnSPMessageReceived</strong>](im-dmsgrobjectevents-onspmessagereceived.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnTextReceived</strong>](im-dmsgrobjectevents-ontextreceived.md)Indicates that a message has been received.
<blockquote>
[!Note]<br />
The [<strong>OnTextReceived</strong>](im-dmsgrobjectevents-ontextreceived.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>OnTrustChanged</strong>](im-dmsgrobjectevents-ontrustchanged.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnUnreadEmailChanged</strong>](im-dmsgrobjectevents-onunreademailchanged.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnUserDropped</strong>](im-dmsgrobjectevents-onuserdropped.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnUserFriendlyNameChangeResult</strong>](im-dmsgrobjectevents-onuserfriendlynamechangeresult.md)Indicates that a user in the User List has changed his or her friendly name.
<blockquote>
[!Note]<br />
The [<strong>OnUserFriendlyNameChangeResult</strong>](im-dmsgrobjectevents-onuserfriendlynamechangeresult.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>OnContactFriendlyNameChange</strong>](im-dmessengerevents-oncontactfriendlynamechange.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>OnUserJoin</strong>](im-dmsgrobjectevents-onuserjoin.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>OnUserLeave</strong>](im-dmsgrobjectevents-onuserleave.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>OnUserStateChanged</strong>](im-dmsgrobjectevents-onuserstatechanged.md)Not currently supported.<br/></td>
</tr>
</tbody>
</table>



 

## DispInterfaces



<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>[<strong>DBasicIMEvents</strong>](im-dbasicimevents.md)Do not use. The [<strong>DBasicIMEvents</strong>](im-dbasicimevents.md) dispinterface handles events that are generated or received by a [<strong>BasicIMObject</strong>](im-basicimobject.md) object.
<blockquote>
[!Note]<br />
The [<strong>DBasicIMEvents</strong>](im-dbasicimevents.md) dispinterface is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>DMessengerEvents</strong>](im-dmessengerevents.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>DMessengerAppEvents</strong>](im-dmessengerappevents.md)Do not use. The [<strong>DMessengerAppEvents</strong>](im-dmessengerappevents.md) dispinterface handles events that are generated or received by a [<strong>MessengerApp</strong>](im-messengerapp.md) object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DMessengerEvents</strong>](im-dmessengerevents.md)Do not use. The [<strong>DMessengerEvents</strong>](im-dmessengerevents.md) dispinterface handles events that are generated or received by a [<strong>Messenger</strong>](im-messenger.md) object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DMsgrObjectEvents</strong>](im-dmsgrobjectevents.md)Do not use. The [<strong>DMsgrObjectEvents</strong>](im-dmsgrobjectevents.md) dispinterface handles events that are generated or received by a [<strong>MsgrObject</strong>](im-msgrobject.md) object.
<blockquote>
[!Note]<br />
The [<strong>DMsgrObjectEvents</strong>](im-dmsgrobjectevents.md) dispinterface is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>DMessengerEvents</strong>](im-dmessengerevents.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
</tbody>
</table>



 

## Interfaces



<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>[<strong>IBasicIM</strong>](im-ibasicim.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IBasicIMOld</strong>](im-ibasicimold.md)Do not use. Messenger Basic IM Object Interface - old version.
<blockquote>
[!Note]<br />
The [<strong>IBasicIMOld</strong>](im-ibasicimold.md) interface is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>IMessenger</strong>](im-imessenger.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IBasicIMUser</strong>](im-ibasicimuser.md)Do not use. Messenger User for an OE Private interface.
<blockquote>
[!Note]<br />
The [<strong>IBasicIMUser</strong>](im-ibasicimuser.md) interface is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>IMessenger</strong>](im-imessenger.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>IBasicIMUser2</strong>](im-ibasicimuser2.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IBasicIMUsers</strong>](im-ibasicimusers.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMessenger</strong>](im-imessenger.md)Do not use. The primary interface for Windows Messenger APIs calls. Includes methods for displaying Messenger client UI, getting or setting selected properties of the local client user, and utility methods.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMessenger2</strong>](im-imessenger2.md)Do not use. The secondary interface for the Windows Messenger API calls.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMessenger3</strong>](im-imessenger3.md)Do not use. The third interface for the Windows Messenger API calls.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMessengerApp</strong>](im-imessengerapp.md)Do not use. The [<strong>IMessengerApp</strong>](im-imessengerapp.md) interface provides methods and properties to handle Messenger applications.
<blockquote>
[!Note]<br />
The [<strong>IMessengerApp</strong>](im-imessengerapp.md) interface is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>IMessenger</strong>](im-imessenger.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>IMessengerApp2</strong>](im-imessengerapp2.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMessengerApp3</strong>](im-imessengerapp3.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMessengerContact</strong>](im-imessengercontact.md)Do not use. The primary interface for an individual [<strong>MessengerContact</strong>](im-messengercontact.md) object (the local representation of a remote user). Each contact in the contact list exists as its own <strong>MessengerContact</strong> object.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMessengerContacts</strong>](im-imessengercontacts.md)Do not use. An interface that manipulates the contact list, which maintains a collection of users in a[<strong>Messenger</strong>](im-messenger.md)object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMessengerConversationWnd</strong>](im-imessengerconversationwnd.md)Do not use. An interface that returns an [IDispatch](https://msdn.microsoft.com/windows/desktop/c1accca9-971c-4435-8a5e-e25404a3fb25) pointer to an [<strong>IMessengerContacts</strong>](im-imessengercontacts.md) collection that contains the participants of that conversation, excluding the local user. This is a read-only collection. [<strong>Remove</strong>](im-imessengergroups-remove.md) cannot be used on this collection. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMessengerGroup</strong>](im-imessengergroup.md)Do not use. The [<strong>IMessengerGroup</strong>](im-imessengergroup.md) interface provides methods and properties to handle a group's collection of users.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMessengerGroups</strong>](im-imessengergroups.md)Do not use. The [<strong>IMessengerGroups</strong>](im-imessengergroups.md) interface provides methods and properties to handle groups of users.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMessengerIMWindow</strong>](im-imessengerimwindow.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMessengerIMWindows</strong>](im-imessengerimwindows.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMessengerService</strong>](im-imessengerservice.md)Do not use. The primary interface for an individual [<strong>MessengerService</strong>](im-messengerservice.md) object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMessengerServices</strong>](im-imessengerservices.md)Do not use. Manipulates the list of services.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMessengerWindow</strong>](im-imessengerwindow.md)Do not use. The automation interface for a Messenger window.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMsgrHost</strong>](im-imsgrhost.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMsgrIMSession</strong>](im-imsgrimsession.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMsgrIMSessions</strong>](im-imsgrimsessions.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMsgrObject</strong>](im-imsgrobject.md)Do not use. The [<strong>IMsgrObject</strong>](im-imsgrobject.md) interface provides methods and properties to handle the <strong>Messenger Object</strong>.
<blockquote>
[!Note]<br />
The [<strong>IMsgrObject</strong>](im-imsgrobject.md) interface is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>IMessenger</strong>](im-imessenger.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>IMsgrObject2</strong>](im-imsgrobject2.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMsgrPassportClient</strong>](im-imsgrpassportclient.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMsgrService</strong>](im-imsgrservice.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMsgrServices</strong>](im-imsgrservices.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMsgrSP</strong>](im-imsgrsp.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMsgrSP2</strong>](im-imsgrsp2.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMsgrUser</strong>](im-imsgruser.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMsgrUser2</strong>](im-imsgruser2.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMsgrUsers</strong>](im-imsgrusers.md)Do not use. The [<strong>IMsgrUsers</strong>](im-imsgrusers.md) interface provides methods and properties to handle the <strong>Messenger User</strong> object.
<blockquote>
[!Note]<br />
The [<strong>IMsgrUsers</strong>](im-imsgrusers.md) interface is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>IMessengerContacts</strong>](im-imessengercontacts.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMsgrWebScriptManager</strong>](im-imsgrwebscriptmanager.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IMsnMessengerIMWindow</strong>](im-imsnmessengerimwindow.md)Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IMsnMessengerIMWindow2</strong>](im-imsnmessengerimwindow2.md)Not currently supported.<br/></td>
</tr>
</tbody>
</table>



 

## Objects



<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>[<strong>BasicIMObject</strong>](im-basicimobject.md)Do not use. The Windows Messenger Basic Instant Messaging Service (IM) object.
<blockquote>
[!Note]<br />
The [<strong>BasicIMObject</strong>](im-basicimobject.md) object is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>Messenger</strong>](im-messenger.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
<tr class="even">
<td>[<strong>Messenger</strong>](im-messenger.md)Do not use. The [<strong>Messenger</strong>](im-messenger.md) object implements the [<strong>IMessenger3</strong>](im-imessenger3.md) interface and [<strong>DMessengerEvents</strong>](im-dmessengerevents.md) dispinterface. This object maintains lists of users and performs most automation functions.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MessengerApp</strong>](im-messengerapp.md)Not currently supported.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MessengerContact</strong>](im-messengercontact.md)Do not use. The [<strong>MessengerContact</strong>](im-messengercontact.md) object corresponds to the [<strong>IMessengerContact</strong>](im-imessengercontact.md) interface. This object provides a local representation of a remote contact. It represents a single user as stored in the [<strong>Messenger</strong>](im-messenger.md) object's internal contact list.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MessengerContacts</strong>](im-messengercontacts.md)Do not use. The [<strong>MessengerContacts</strong>](im-messengercontacts.md) object corresponds to the [<strong>IMessengerContacts</strong>](im-imessengercontacts.md) interface. It is a collection object of contacts in the contact list.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MessengerConversationWnd</strong>](im-messengerconversationwnd.md)Do not use. The [<strong>MessengerConversationWnd</strong>](im-messengerconversationwnd.md) object corresponds to the [<strong>IMessengerConversationWnd</strong>](im-imessengerconversationwnd.md) interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MessengerGroup</strong>](im-messengergroup.md)Do not use. The [<strong>MessengerGroup</strong>](im-messengergroup.md) object corresponds to the [<strong>IMessengerGroup</strong>](im-imessengergroup.md) interface. It represents a single group as stored in the [<strong>Messenger</strong>](im-messenger.md) object's internal group list.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MessengerGroups</strong>](im-messengergroups.md)Do not use. The [<strong>MessengerGroups</strong>](im-messengergroups.md) corresponds to the [<strong>IMessengerGroups</strong>](im-imessengergroups.md) interface. It is a collection object of groups in the contact list.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MessengerNative</strong>](im-messengernative.md)Do not use. This is the native messenger object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MessengerService</strong>](im-messengerservice.md)Do not use. The [<strong>MessengerService</strong>](im-messengerservice.md) object corresponds to the [<strong>IMessengerService</strong>](im-imessengerservice.md) interface. This object represents a single service.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MessengerServices</strong>](im-messengerservices.md)Do not use. The [<strong>MessengerServices</strong>](im-messengerservices.md) corresponds to the [<strong>IMessengerServices</strong>](im-imessengerservices.md) interface. It represents a list of services in the [<strong>Messenger</strong>](im-messenger.md) object.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MessengerWindow</strong>](im-messengerwindow.md)Do not use. The [<strong>MessengerWindow</strong>](im-messengerwindow.md) object corresponds to the [<strong>IMessengerWindow</strong>](im-imessengerwindow.md) interface. This object can represent either the main application window or a conversation window that contains one or more active sessions between contacts and the local client user.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MsgrObject</strong>](im-msgrobject.md)Do not use. The [<strong>MsgrObject</strong>](im-msgrobject.md) object.
<blockquote>
[!Note]<br />
The [<strong>MsgrObject</strong>](im-msgrobject.md) object is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>Messenger</strong>](im-messenger.md) and [<strong>MessengerContacts</strong>](im-messengercontacts.md) instead.
</blockquote>
<br/> <br/></td>
</tr>
</tbody>
</table>



 

## Structures



|                                                                             |
|-----------------------------------------------------------------------------|
| [**LOGFONT\_DATA**](im-logfont-data.md)Not currently supported.<br/> |



 

 

 





