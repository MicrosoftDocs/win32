---
title: IBasicIMOld interface
description: Do not use.
ms.assetid: '5dede41c-ab98-45c0-81dd-db36f892edda'
keywords: ["IBasicIMOld interface Windows Messenger", "IBasicIMOld interface Windows Messenger , described"]
topic_type:
- apiref
api_name:
- IBasicIMOld
api_location:
- Msgsc.dll
api_type:
- COM
---

# IBasicIMOld interface

\[**IBasicIMOld** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Messenger Basic IM Object Interface - old version.

> [!Note]  
> The **IBasicIMOld** interface is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**IMessenger**](im-imessenger.md) instead.

 

## Members

The **IBasicIMOld** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IBasicIMOld** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IBasicIMOld** interface has these methods.



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
<td style="text-align: left;">[<strong>AdviseOE</strong>](im-ibasicimold-adviseoe.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>AutoLogon</strong>](im-ibasicimold-autologon.md)</td>
<td style="text-align: left;">Initiates a Logon without using a UI if the user is connected to the network and has saved a password. <br/>
<blockquote>
[!Note]<br />
The [<strong>AutoLogon</strong>](im-ibasicimold-autologon.md) method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>AutoSignin</strong>](im-imessenger-autosignin.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>CreateUser</strong>](im-ibasicimold-createuser.md)</td>
<td style="text-align: left;">Creates a Basic IM user object. <br/>
<blockquote>
[!Note]<br />
The [<strong>CreateUser</strong>](im-ibasicimold-createuser.md) method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>GetContact</strong>](im-imessenger-getcontact.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>LaunchAddContactUI</strong>](im-ibasicimold-launchaddcontactui.md)</td>
<td style="text-align: left;">Initiates an Add Contact dialog. <br/>
<blockquote>
[!Note]<br />
The [<strong>LaunchAddContactUI</strong>](im-ibasicimold-launchaddcontactui.md) method type is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>AddContact</strong>](im-imessenger-addcontact.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>LaunchIMUI</strong>](im-ibasicimold-launchimui.md)</td>
<td style="text-align: left;">Initiates an IM Window. <br/>
<blockquote>
[!Note]<br />
The [<strong>LaunchIMUI</strong>](im-ibasicimold-launchimui.md) method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>LaunchLogonUI</strong>](im-ibasicimold-launchlogonui.md)</td>
<td style="text-align: left;">Initiates a Logon dialog. <br/>
<blockquote>
[!Note]<br />
The [<strong>LaunchLogonUI</strong>](im-ibasicimold-launchlogonui.md) method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>Signin</strong>](im-imessenger-signin.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>LaunchOptionsUI</strong>](im-ibasicimold-launchoptionsui.md)</td>
<td style="text-align: left;">Initiates an Options dialog. <br/>
<blockquote>
[!Note]<br />
The [<strong>LaunchOptionsUI</strong>](im-ibasicimold-launchoptionsui.md) method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>Logoff</strong>](im-ibasicimold-logoff.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>RemoteLaunchLogonUI</strong>](im-ibasicimold-remotelaunchlogonui.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
</tbody>
</table>



 

### Properties

The **IBasicIMOld** interface has these properties.



| Property                                                           | Access type          | Description                         |
|:-------------------------------------------------------------------|:---------------------|:------------------------------------|
| [**ContactList**](im-ibasicimold-contactlist.md)<br/>       | Read-only<br/> | Not currently supported.<br/> |
| [**LocalLogonName**](im-ibasicimold-locallogonname.md)<br/> | Read-only<br/> | Not currently supported.<br/> |
| [**LocalState**](im-ibasicimold-localstate.md)<br/>         | Read-only<br/> | Not currently supported.<br/> |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| End of client support<br/>    | Windows XP<br/>                                                                  |
| End of server support<br/>    | Windows Server 2003<br/>                                                         |
| Product<br/>                  | Messenger 4.0<br/>                                                               |
| Header<br/>                   | <dl> <dt>Basicim.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Basicim.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>   |



 

 





