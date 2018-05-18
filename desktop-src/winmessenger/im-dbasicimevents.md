---
title: DBasicIMEvents interface
description: Do not use.
ms.assetid: '35985d23-b931-49a9-a7ff-7c9c39922a8f'
keywords: ["DBasicIMEvents interface Windows Messenger", "DBasicIMEvents interface Windows Messenger , described"]
topic_type:
- apiref
api_name:
- DBasicIMEvents
api_location:
- Msgsc.dll
api_type:
- COM
---

# DBasicIMEvents interface

\[**DBasicIMEvents** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **DBasicIMEvents** dispinterface handles events that are generated or received by a [**BasicIMObject**](im-basicimobject.md) object.

> [!Note]  
> The **DBasicIMEvents** dispinterface is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**DMessengerEvents**](im-dmessengerevents.md) instead.

 

## Members

The **DBasicIMEvents** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **DBasicIMEvents** also has these types of members:

-   [Events](#events)

### Events

The **DBasicIMEvents** interface has these events.



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
<td style="text-align: left;">[<strong>OnAppShutdown</strong>](im-dbasicimevents-onappshutdown.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnContactListAddResult</strong>](im-dbasicimevents-oncontactlistaddresult.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnContactListRemoveResult</strong>](im-dbasicimevents-oncontactlistremoveresult.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnLocalStateChangeResult</strong>](im-dbasicimevents-onlocalstatechangeresult.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnLogoff</strong>](im-dbasicimevents-onlogoff.md)</td>
<td style="text-align: left;">Indicates that the logoff is complete. <br/>
<blockquote>
[!Note]<br />
The [<strong>OnLogoff</strong>](im-dbasicimevents-onlogoff.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>OnSignout</strong>](im-dmessengerevents-onsignout.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnLogonResult</strong>](im-dbasicimevents-onlogonresult.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>OnUserFriendlyNameChangeResult</strong>](im-dbasicimevents-onuserfriendlynamechangeresult.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>OnUserStateChanged</strong>](im-dbasicimevents-onuserstatechanged.md)</td>
<td style="text-align: left;">Indicates that the user's state has changed. <br/>
<blockquote>
[!Note]<br />
The [<strong>OnUserStateChanged</strong>](im-dbasicimevents-onuserstatechanged.md) event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>OnContactStatusChange</strong>](im-dmessengerevents-oncontactstatuschange.md) instead.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows XP<br/>                                                                |
| End of server support<br/>    | Windows Server 2003<br/>                                                       |
| Product<br/>                  | Messenger 4.0<br/>                                                             |
| Header<br/>                   | <dl> <dt>Mdisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mdisp.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl> |



 

 





