---
title: IBasicIMUser interface
description: Do not use.
ms.assetid: c9daacfb-849d-4bf0-ae14-790cf3d05c94
keywords:
- IBasicIMUser interface Windows Messenger
- IBasicIMUser interface Windows Messenger , described
topic_type:
- apiref
api_name:
- IBasicIMUser
api_location:
- Msgsc.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IBasicIMUser interface

\[**IBasicIMUser** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. Messenger User for an OE Private interface.

> [!Note]  
> The **IBasicIMUser** interface is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**IMessenger**](im-imessenger.md) instead.

 

## Members

The **IBasicIMUser** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IBasicIMUser** also has these types of members:

-   [Properties](#properties)

### Properties

The **IBasicIMUser** interface has these properties.



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
<td style="text-align: left;">[<strong>FriendlyName</strong>](im-ibasicimuser-friendlyname.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>LogonName</strong>](im-ibasicimuser-logonname.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Retrieves the Logon Name of the user. <br/>
<blockquote>
[!Note]<br />
The [<strong>LogonName</strong>](im-ibasicimuser-logonname.md) property is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>SigninName</strong>](im-imessengercontact-signinname.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>State</strong>](im-ibasicimuser-state.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Retrieves the state of the user. <br/>
<blockquote>
[!Note]<br />
The [<strong>State</strong>](im-ibasicimuser-state.md) property is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>Status</strong>](im-imessengercontact-status.md) instead.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                   |
| End of client support<br/>    | Windows XP<br/>                                                                  |
| End of server support<br/>    | Windows Server 2003<br/>                                                         |
| Product<br/>                  | Messenger 4.0<br/>                                                               |
| Header<br/>                   | <dl> <dt>Basicim.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Basicim.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>   |



 

 





