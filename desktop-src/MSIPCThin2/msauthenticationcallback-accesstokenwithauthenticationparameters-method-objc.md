---
title: MSAuthenticationCallback accessTokenWithAuthenticationParameters method
description: Implement this callback method to authenticate you application.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 74FD5865-923E-475A-A8C4-F6B97EEC79A2
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSAuthenticationCallback accessTokenWithAuthenticationParameters method
topic_type:
- apiref
api_name:
- MSAuthenticationCallback accessTokenWithAuthenticationParameters method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSAuthenticationCallback accessTokenWithAuthenticationParameters method

Implement this callback method to authenticate you application.

We recommend that you use the [Azure AD Authentication Library (ADAL)](https://msdn.microsoft.com/library/jj573266.aspx). However, other authentication libraries that support OAuth 2.0 can be used as well.

For more information, see the *Prerequisites* section in the [iOS and OS X Apps](ios-sdk.md) topic under [Get started](get-started.md).

## Signature

``` syntax
- (void)accessTokenWithAuthenticationParameters:(MSAuthenticationParameters *)authenticationParameters completionBlock:(void(^)(NSString *accessToken, NSError *error))completionBlock;
```

## Parameters



| Name                                  | Datatype                                                                                  | Notes |
|---------------------------------------|-------------------------------------------------------------------------------------------|-------|
| *authenticationParameters*<br/> | [**MSAuthenticationParameters**](msauthenticationparameters-class-objc.md) \*<br/> |       |
| *completionBlock*<br/>          | void(^)(**NSString** \*accessToken, **NSError** \*error)<br/>                       |       |



 

## Defined in

MSAuthenticationCallback.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

This method must be implemented by you. The Rights Management SDK 4.2 will use this method via its APIs to authenticate your application.

We recommend that you use the [Azure AD Authentication Library](https://msdn.microsoft.com/library/jj573266.aspx) and, other authentication libraries can be used.

 

 





