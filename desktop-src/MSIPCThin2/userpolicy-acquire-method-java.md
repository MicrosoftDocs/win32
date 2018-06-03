---
title: UserPolicy.acquire asynchronous method
description: Asynchronously acquires a UserPolicy object based on a serialized content policy.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 83998009-0E55-4B1E-8F33-5AEC66865A4C
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- UserPolicy.acquire asynchronous method
topic_type:
- apiref
api_name:
- UserPolicy.acquire asynchronous method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UserPolicy.acquire asynchronous method

Asynchronously acquires a [**UserPolicy**](userpolicy-class-java.md) object based on a serialized content policy.

## Signature

``` syntax
public static IAsyncControl acquire(byte[] serializedContentPolicy,
                                    String userId,
                                    AuthenticationRequestCallback authenticationCallback,
                                    ConsentCallback consentCallback,
                                    int policyAcquisitionFlags,
                                    CreationCallback<UserPolicy> callback) 
                             throws InvalidParameterException
```

## Parameters



| Name                                 | Datatype                                                                                         | Notes                                                                                                                                                                                                                                                                                                                                                                                               |
|--------------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *serializedContentPolicy*<br/> | **byte**\[\]<br/>                                                                          | A serialized content policy<br/>                                                                                                                                                                                                                                                                                                                                                              |
| *userId*<br/>                  | **String**<br/>                                                                            | Optional.<br/> A *userId* is used for caching a user policy for offline usage. For multiple user scenarios, caller must supply a *userId*.<br/> If *userId* is null, then the user policy is cached without *userId* and is retrievable with null *userId* as well. A null *userId* also retrieves any matching offline user policy cached without *userId* or any *userId*.<br/> |
| *authenticationCallback*<br/>  | [**AuthenticationRequestCallback**](authenticationrequestcallback-interface-java.md)<br/> |                                                                                                                                                                                                                                                                                                                                                                                                     |
| *consentCallback*<br/>         | [**ConsentCallback**](https://msdn.microsoft.com/library/windows/desktop/dn833503)<br/>                     |                                                                                                                                                                                                                                                                                                                                                                                                     |
| *policyAcquisitionFlags*<br/>  | **int**<br/>                                                                               | For more information, see [**PolicyAcquisitionFlags**](policyacquisitionflags-class-java.md)<br/>                                                                                                                                                                                                                                                                                            |
| *callback*<br/>                | CreationCallback&lt;[**UserPolicy**](userpolicy-class-java.md)&gt;&gt;<br/>               | Completion callback<br/>                                                                                                                                                                                                                                                                                                                                                                      |



 

## Throws

[**InvalidParameterException**](invalidparameterexception-class-java.md)

## Returns

[**IAsyncControl**](iasynccontrol-interface.md)

## Defined in

UserPolicy.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





