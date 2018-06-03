---
title: IMessengerApp interface
description: Do not use.
ms.assetid: 60ce7cb3-2c2f-4cd2-a1dc-23e75eb1434e
keywords:
- IMessengerApp interface Windows Messenger
- IMessengerApp interface Windows Messenger , described
topic_type:
- apiref
api_name:
- IMessengerApp
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

# IMessengerApp interface

\[**IMessengerApp** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **IMessengerApp** interface provides methods and properties to handle Messenger applications.

> [!Note]  
> The **IMessengerApp** interface is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [**IMessenger**](im-imessenger.md) instead.

 

## Members

The **IMessengerApp** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/windows/desktop/ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IMessengerApp** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMessengerApp** interface has these methods.



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
<td style="text-align: left;">[<strong>AutoLogon</strong>](im-imessengerapp-autologon.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>LaunchAddContactUI</strong>](im-imessengerapp-launchaddcontactui.md)</td>
<td style="text-align: left;">Launches the Contact wizard for adding a contact. <br/>
<blockquote>
[!Note]<br />
The [<strong>LaunchAddContactUI</strong>](im-imessengerapp-launchaddcontactui.md) method is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>AddContact</strong>](im-imessenger-addcontact.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>LaunchIMUI</strong>](im-imessengerapp-launchimui.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>LaunchLogonUI</strong>](im-imessengerapp-launchlogonui.md)</td>
<td style="text-align: left;">Launches the Messenger client <strong>Sign In</strong> dialog box and populates the sign-in name field. <br/>
<blockquote>
[!Note]<br />
The [<strong>LaunchLogonUI</strong>](im-imessengerapp-launchlogonui.md) enumerated type is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger. You should use [<strong>Signin</strong>](im-imessenger-signin.md) instead.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>LaunchOptionsUI</strong>](im-imessengerapp-launchoptionsui.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>Quit</strong>](im-imessengerapp-quit.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>RequestURLPost</strong>](im-imessengerapp-requesturlpost.md)</td>
<td style="text-align: left;">Not currently supported.<br/></td>
</tr>
</tbody>
</table>



 

### Properties

The **IMessengerApp** interface has these properties.



| Property                                                                         | Access type           | Description                         |
|:---------------------------------------------------------------------------------|:----------------------|:------------------------------------|
| [**Application**](im-imessengerapp-application.md)<br/>                   | Read-only<br/>  | Not currently supported.<br/> |
| [**CachedPassword**](im-imessengerapp-cachedpassword.md)<br/>             | Write-only<br/> | Not currently supported.<br/> |
| [**FirstTimeCredentials**](im-imessengerapp-firsttimecredentials.md)<br/> | Write-only<br/> | Not currently supported.<br/> |
| [**FullName**](im-imessengerapp-fullname.md)<br/>                         | Read-only<br/>  | Not currently supported.<br/> |
| [**Height**](im-imessengerapp-height.md)<br/>                             | Write-only<br/> | Not currently supported.<br/> |
| [**HWND**](im-imessengerapp-hwnd.md)<br/>                                 | Read-only<br/>  | Not currently supported.<br/> |
| [**IMWindows**](im-imessengerapp-imwindows.md)<br/>                       | Read-only<br/>  | Not currently supported.<br/> |
| [**Left**](im-imessengerapp-left.md)<br/>                                 | Write-only<br/> | Not currently supported.<br/> |
| [**Name**](im-imessengerapp-name.md)<br/>                                 | Read-only<br/>  | Not currently supported.<br/> |
| [**Parent**](im-imessengerapp-parent.md)<br/>                             | Read-only<br/>  | Not currently supported.<br/> |
| [**Path**](im-imessengerapp-path.md)<br/>                                 | Read-only<br/>  | Not currently supported.<br/> |
| [**StatusBar**](im-imessengerapp-statusbar.md)<br/>                       | Write-only<br/> | Not currently supported.<br/> |
| [**StatusText**](im-imessengerapp-statustext.md)<br/>                     | Write-only<br/> | Not currently supported.<br/> |
| [**TaskbarIcon**](im-imessengerapp-taskbaricon.md)<br/>                   | Read-only<br/>  | Not currently supported.<br/> |



 

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

[**IMessengerApp**](im-imessengerapp.md)
</dt> </dl>

 

 





