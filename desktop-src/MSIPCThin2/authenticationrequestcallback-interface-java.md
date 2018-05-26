---
title: AuthenticationRequestCallback interface
description: AuthenticationRequestCallback interface definition.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 1C29304E-9EE4-4305-AA1A-4BC543DB9285
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- AuthenticationRequestCallback interface
topic_type:
- apiref
api_name:
- AuthenticationRequestCallback interface
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AuthenticationRequestCallback interface

**AuthenticationRequestCallback** interface definition. This interface is implemented by you and used by the SDK to retrieve an access token.

We recommend that you use the [Azure AD Authentication Library (ADAL)](https://msdn.microsoft.com/library/jj573266.aspx). However, other authentication libraries that support OAuth 2.0 can be used as well. For more information, see the *Prerequisites* section in the [Android Apps](android-sdk.md) topic under [Get started](get-started.md).

## Signature

``` syntax
public interface AuthenticationRequestCallback
```

## Methods



| Name                                                                              | Description                               |
|-----------------------------------------------------------------------------------|-------------------------------------------|
| [**getToken**](authenticationrequestcallback-gettoken-method-java.md)<br/> | Gets the authentication token.<br/> |



 

## Defined in

AuthenticationRequestCallback.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Package

com.microsoft.rightsmanagement

## Thread Safety

Members of this class are not guaranteed to be thread safe.

## See also

<dl> <dt>

[Android API Reference](android.md)
</dt> <dt>

[**CreationCallback&lt;T&gt;**](creationcallback-t--interface-java.md)
</dt> <dt>

[Azure AD Authentication Library](https://msdn.microsoft.com/library/jj573266.aspx)
</dt> </dl>

 

 





