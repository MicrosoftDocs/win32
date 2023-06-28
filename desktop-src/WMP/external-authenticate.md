---
title: External.authenticate method
description: The authenticate method initiates an attempt to authenticate the user.
ms.assetid: db4cd2c6-b735-40b1-af96-82a40bda9d97
keywords:
- authenticate method Windows Media Player
- authenticate method Windows Media Player , External class
- External class Windows Media Player , authenticate method
topic_type:
- apiref
api_name:
- External.authenticate
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# External.authenticate method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **authenticate** method initiates an attempt to authenticate the user.

## Syntax


```JScript
External.authenticate(
  AuthenticationIndex
)
```



## Parameters

<dl> <dt>

*AuthenticationIndex* \[in\]
</dt> <dd>

**Number** (**long**) that specifies the index of an authentication-success webpage.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Certain links on a discovery page have targets that should be displayed only after the user has been authenticated. The discovery page, Windows Media Player, and the online store's plug-in use the following steps to authenticate the user and display the target webpage:

1.  Script on a discovery page calls the *External*.**authenticate** method.
2.  Windows Media Player displays a dialog box to obtain a user name and password.
3.  Windows Media Player calls [IWMPContentPartner::Authenticate](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-authenticate), which initiates the authentication attempt and returns immediately.
4.  When the authentication attempt is complete, the online store's plug-in calls [IWMPContentPartnerCallback::Notify](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartnercallback-notify), passing wmpcnAuthResult and a Boolean value that indicates whether the attempt was successful.
5.  If the authentication attempt was successful, Windows Media Player calls [IWMPContentPartner::GetItemInfo](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getiteminfo), passing g\_szItemInfo\_AuthenticationSuccessURL, to obtain the URL of an authentication-success webpage. In this call, Windows Media Player passes the same index that the discovery page passed to the *External*.**authenticate** method.
6.  Windows Media Player displays the authentication-success webpage.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11<br/>                                                 |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.attemptLogin**](external-attemptlogin.md)
</dt> <dt>

[**External.userLoggedIn**](external-userloggedin.md)
</dt> </dl>

 

 





