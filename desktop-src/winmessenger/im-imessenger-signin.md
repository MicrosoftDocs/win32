---
title: IMessenger Signin method
description: Launches the Messenger client Sign In dialog box and populates the sign-in name field.
ms.assetid: '8396a31f-9349-47c8-a535-441fdd76f982'
keywords: ["Signin method Windows Messenger", "Signin method Windows Messenger , IMessenger interface", "IMessenger interface Windows Messenger , Signin method"]
topic_type:
- apiref
api_name:
- IMessenger.Signin
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessenger::Signin method

\[**Signin** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Launches the Messenger client  **Sign In** dialog box and populates the sign-in name field. The behavior of this method will vary, depending on the Messenger client version, the host operating system, and the primary service for the client. For more information, see the Remarks section later in this topic.

## Syntax


```C++
HRESULT Signin(
  [in] long hwndParent,
  [in] BSTR bstrSigninName,
  [in] BSTR bstrPassword
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

Type: **long**

A **LONG**. Reserved. All current implementations should set this parameter to 0 or **NULL**.

</dd> <dt>

*bstrSigninName* \[in\]
</dt> <dd>

Type: **BSTR**

The sign-in name of the user to be signed in, as a **BSTR**. For the Microsoft .NET Messenger Service, this should include the @ symbol and domain name.

</dd> <dt>

*bstrPassword* \[in\]
</dt> <dd>

Type: **BSTR**

The password associated with the account of the user defined in *bstrSigninName*, as a **BSTR**.The password is entered as plain text but is passed through the protocol in a hashed format. The password is relevant only if *bstrSigninName* is not **NULL** or empty. The maximum allowable length for the password depends on the version of the Messenger client. For more information, see the Remarks section later in this topic.

</dd> </dl>

## Return value

Type: **HRESULT**

For a table of all MSGR\_E\_\* constants [**MSGRConstants**](im-msgrconstants.md), see.

Returns one of the following values.



| Return code                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Success. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <dl> <dt>**S\_FALSE**</dt> </dl>                     | The **Sign In** dialog box is already open.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                | Values provided failed validation tests. The sign-in name or password cannot contain spaces, carriage returns, or linefeed characters. Some services will not accept ANSI values greater than 128. The sign-in name cannot be longer than 129 characters (not including the terminating **null** character). The password cannot exceed the maximum password length, which is dependent on the version of the Messenger client. These are the input limits enforced on the client. There may be other limits established by the service upon initial account creation.<br/> - or -<br/> The state of the [**Messenger**](im-messenger.md) object cannot be determined. In scripting, E\_INVALIDARG will not be returned in the first case because *bstrSigninName* and *bstrPassword* are always ignored.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>               | String comparison or concatenation failed, or memeory couldnot be allocated for new objects created at sign-in.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| <dl> <dt>**E\_FAIL**</dt> </dl>                      | Could not create an **Sign In** dialog box, or the [**Messenger**](im-messenger.md) object is not responding or has not been created.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>**MSGR\_E\_ALREADY\_LOGGED\_ON**</dt> </dl> | The current user is already signed in.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>**S\_FALSE**</dt> </dl>                     | (Scripting) The current user is already signed in. S\_FALSE cannot usually be captured in scripting error trapping, because the initial error bit is not 1 in this HResult. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <dl> <dt>**MSGR\_E\_AUDIO\_UI\_ACTIVE**</dt> </dl>   | The **Audio and Video Tuning Wizard** is already open.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>**MSGR\_E\_option\_UI\_ACTIVE**</dt> </dl>  | The **Options** is already open.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| <dl> <dt>**MSGR\_E\_OTHER\_UI\_ACTIVE**</dt> </dl>   | The **Customer Experience Improvement Program**(CEIP) is already open.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |



 

## Remarks

This method always displays the dialog box for the primary service. The Microsoft Exchange Instant Messaging Service (IM) client offers users the option to use Exchange, instead of the default of the Microsoft .NET Messenger Service, as the primary service.

If the primary service is not signed in to, the **Signin** method will not launch the secondary sign-in dialog box for any configured secondary services on any client. The **Signin** API cannot be used to prepopulate the sign-in name or password for the secondary service **Sign In** dialog box or to suppress this dialog box if the credentials are not cached.

The Windows Messenger APIs cannot recall or display the secondary sign-in dialog box independently if the primary service has been signed in to but the secondary service has not. Calling **Signin** in this case will return **MSGR\_E\_ALREADY\_LOGGED\_ON**, and neither the primary nor secondary sign-in dialog boxes will be displayed. To sign in to the secondary service when the primary service has already been signed in, a client user must either choose **Sign In** from the **File** menu or click the **Not signed in to all services** link in the client status bar.

This API also has an operating system dependency. The Credentials Manager component for version 4.0 is included in the Windows XP operating system and handles signing in to the client. Because the Credentials Manager has its own logic for saving passwords, all passwords passed to this API will be ignored. Passwords can be set through user input or Credentials Manager caching only. **NULL** or blank strings passed as user name will cause the Credentials Manager UI to populate the user name based on the one last used and stored in its internal caching strategy. The very first time the **Credentials Manager** dialog box is displayed in the operating system, a new Windows Live ID registration sequence may be invoked in the UI. This is handled by the operating system and cannot be controlled by the Windows Messenger APIs.

The maximum allowable password length depends on the version of the Messenger client. For versions 4.7 and earlier, the maximum password length is 16 characters. For versions 5.0 or later of the Messenger client, the maximum password length increases to 256 characters.

Unless called through scripting, the *bstrSigninName* parameter of this method will partially prepopulate the **Sign In** dialog box, but will not submit credentials to the server automatically, even if both user name and password are provided.

-   If sign-in name and password are given as **NULL** strings, user settings will determine whether the fields are prepopulated. If the user chose to save the password, the dialog box will be populated with previously saved credentials. The Windows XP Credentials Manager UI will potentially cache all last-used credentials in this circumstance. If no cached credentials exist, the fields will be blank.
-   If sign-in name and password are given as blank strings, the behavior is the same as in the previous case.
-   If sign-in name and password are given as non-empty strings, the **Sign In** dialog box launches with fields populated by those strings, even if credentials are cached. Although not recommended, this approach may be useful in cases in which a client handles the provisioning of a brand new service account (that is, the client is prepopulating the dialog box with credentials that were just created and thus could not yet be cached).

Calling this method initially displays the UI but does not perform automatic sign-in. The sign-in initiated by the user through the UI will result in a [**OnSignin**](im-dmessengerevents-onsignin.md) event and a [**OnMyStatusChange**](im-dmessengerevents-onmystatuschange.md) event with **MISTATUS\_LOCAL\_CONNECTING\_TO\_SERVER**, which lasts until the server receives and responds to the protocol-level logon command or the client-side timer window on logon expires. That state lasts until the server of the service receives and responds to the protocol-level logoff command. Otherwise, after 15 seconds without connecting to the server, the client-side timer will cancel the logon attempt and generate a **OnMyStatusChange** event with *mMYStatusOE*=**MISTATUS\_OFFLINE** and *hr*=**MSGR\_E\_LOGON\_TIMEOUT**.

If you do not wish to display a sign-in dialog box to the user, use the [**AutoSignin**](im-imessenger-autosignin.md) method instead. **AutoSignin**requires that the client has access to cached credentials (that is, the user has selected the **Remember My Password** option in the client UI); the user has saved credentials in the Windows XP Credentials Manager UI; or the client has been modified to always save the password independent of operating system or user options.

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



## See also

<dl> <dt>

[**IMessenger**](im-imessenger.md)
</dt> <dt>

[**Signout**](im-imessenger-signout.md)
</dt> </dl>

 

 





