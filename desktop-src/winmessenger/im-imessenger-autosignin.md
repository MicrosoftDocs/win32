---
title: IMessenger AutoSignin method
description: Signs the local client in automatically using the last sign-in name and saved password information.
ms.assetid: '6a82a1f7-0dc8-4275-a4df-6a02afbc5462'
keywords: ["AutoSignin method Windows Messenger", "AutoSignin method Windows Messenger , IMessenger interface", "IMessenger interface Windows Messenger , AutoSignin method"]
topic_type:
- apiref
api_name:
- IMessenger.AutoSignin
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessenger::AutoSignin method

\[**AutoSignin** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Signs the local client in automatically using the last sign-in name and saved password information.

## Syntax


```C++
HRESULT AutoSignin();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

For a table of MSGR\_E\_\* constants, see [**MSGRConstants**](im-msgrconstants.md). Returns one of the following values.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><dl> <dt><strong>S_OK</strong></dt> </dl></td>
<td>Success. See Remarks.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>MSGR_E_LOGON_UI_ACTIVE</strong></dt> </dl></td>
<td>The <strong>Sign In</strong> dialog box was enabled and visible when this method was called.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>S_FALSE</strong></dt> </dl></td>
<td>Client was already signed in (scripting).<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>MSGR_E_ALREADY_LOGGED_ON</strong></dt> </dl></td>
<td>Client was already signed in.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>E_FAIL</strong></dt> </dl></td>
<td>Returned for one of the following reasons: <br/>
<ul>
<li>First-time user.</li>
<li>No available credentials.</li>
<li>Cannot determine local state.</li>
<li>Lost connection.</li>
<li>Password encoding failed.</li>
<li>Unspecified internal error. Cannot access object.</li>
</ul>
<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

This method always signs the user in to the primary service. This method's behavior depends on the primary service on the client. The Microsoft Exchange Instant Messaging Service (IM) client offers users the option to use Exchange as the primary service. The **AutoSignin** method will not launch the secondary sign-in dialog box for any configured secondary services on any client. Only the primary service can be signed into using this method. To sign in to all services, use [**Signin**](im-imessenger-signin.md). This method will always display the **Sign In** dialog box, even with cached credentials.

If saving the password locally is not enabled by a specific user option, this method will fail.

This method is used for initial sign-in if necessary, but requires that the sign-in credentials are previously stored by the client user.

If this method fails, implementers can display the **Sign In** dialog box by calling [**Signin**](im-imessenger-signin.md) with **NULL** strings for sign-in name and password.

Because sign-in relies on server authentication, several possible error conditions are not checked for by the HResult of **AutoSignin**; instead, they are returned in the [**Signin**](im-imessenger-signin.md) event. These error conditions include, but are not limited to, bad credentials stored from the last sign-in attempt, a blank sign-in name or password, and connection problems, each of which is differentiated by the *hr* parameter of the event. To determine whether the sign-in sequence succeeded, clients should always check both the HResult of **AutoSignin** and the *hr* parameter of the **Signin** event.

> [!Note]  
> The following remarks apply to scripting languages.
>
> -   This method is scriptable.
> -   You should not return MSGR\_E\_NOT\_LOGGED\_ON to avoid an exception.
> -   Clear the value returned to the user.

 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





