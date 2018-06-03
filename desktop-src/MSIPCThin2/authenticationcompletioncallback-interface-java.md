---
title: AuthenticationCompletionCallback interface
description: An interface provided the SDK used to return an access token to the SDK from the application using it.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: E62B5D35-0BBE-413C-80A3-4D56007AA04B
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- AuthenticationCompletionCallback interface
topic_type:
- apiref
api_name:
- AuthenticationCompletionCallback interface
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AuthenticationCompletionCallback interface

An interface provided the SDK used to return an access token to the SDK from the application using it. We recommend that you use the [Azure AD Authentication Library](https://msdn.microsoft.com/library/jj573266.aspx) and other authentication libraries can be used.

## Signature

``` syntax
public interface AuthenticationCompletionCallback
```

## Methods



| Name                                                                                   | Description                                                 |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [**onCancel**](authenticationcompletioncallback-oncancel-method-java.md)<br/>   | Called if authentication was cancelled<br/>           |
| [**onFailure**](authenticationcompletioncallback-onfailure-method-java.md)<br/> | Should be called if authentication has failed<br/>    |
| [**onSuccess**](authenticationcompletioncallback-onsuccess-method-java.md)<br/> | Callback to asynchronously pass the access token<br/> |



 

## Defined in

AuthenticationCompletionCallback.java

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

[Azure AD Authentication Library](https://msdn.microsoft.com/library/jj573266.aspx)
</dt> </dl>

 

 





