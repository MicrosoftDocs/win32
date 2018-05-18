---
title: MSAuthenticationCallback protocol
description: Protocol for getting an access token.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '62E538A0-ECFB-4582-BA4B-184CEEE56E08'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSAuthenticationCallback protocol"]
topic_type:
- apiref
api_name:
- MSAuthenticationCallback protocol
api_type:
- NA
---

# MSAuthenticationCallback protocol

Protocol for getting an access token. Your application should implement this protocol and pass it to the Rights Management SDK 4.2 APIs that perform authentication.

We recommend that you use the [Azure AD Authentication Library (ADAL)](https://msdn.microsoft.com/library/jj573266.aspx). However, other authentication libraries that support OAuth 2.0 can be used as well. For more information, see the *Prerequisites* section in the [iOS and OS X Apps](ios-sdk.md) topic under [Get started](get-started.md).

## Signature

``` syntax
@protocol MSAuthenticationCallback <NSObject>
```

## Methods



| Name                                                                                                                                       | Description                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [**accessTokenWithAuthenticationParameters**](msauthenticationcallback-accesstokenwithauthenticationparameters-method-objc.md)<br/> | Implement this callback method to authenticate you application.<br/> |



 

## Defined in

MSAuthenticationCallback.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





