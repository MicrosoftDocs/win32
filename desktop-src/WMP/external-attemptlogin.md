---
title: External.attemptLogin method
description: The attemptLogin method displays a dialog box so the user can attempt to log in to the online store.
ms.assetid: 04fe476f-6d0e-4faa-9e4a-f87bed782205
keywords:
- attemptLogin method Windows Media Player
- attemptLogin method Windows Media Player , External class
- External class Windows Media Player , attemptLogin method
topic_type:
- apiref
api_name:
- External.attemptLogin
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# External.attemptLogin method

The **attemptLogin** method displays a dialog box so the user can attempt to log in to the online store.

## Syntax


```JScript
External.attemptLogin()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

If the log-in attempt results in a change of log-in status, Windows Media Player raises the [OnLoginChange](external-onloginchange-event.md) event.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.OnLoginChange Event**](external-onloginchange-event.md)
</dt> <dt>

[**External.userLoggedIn**](external-userloggedin.md)
</dt> <dt>

[**IWMPContentPartner::Login**](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-login)
</dt> <dt>

[**Managing Login**](managing-login.md)
</dt> </dl>

 

 





