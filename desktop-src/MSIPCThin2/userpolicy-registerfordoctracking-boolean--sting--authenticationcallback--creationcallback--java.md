---
title: UserPolicy.registerForDocTracking asynchronous method
description: Asynchronously registers this user policy with the document tracking service.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: CC3559DB-467B-440B-9A73-43504CF13C81
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- UserPolicy.registerForDocTracking asynchronous method
topic_type:
- apiref
api_name:
- UserPolicy.registerForDocTracking asynchronous method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserPolicy.registerForDocTracking asynchronous method

Asynchronously registers this user policy with the document tracking service.

## Signature

``` syntax
public static IAsyncControl RegisterForDocTracking(
                                                   boolean sendRegistrationNotificationMail,
                                                   String userId,                            
                                                   AuthenticationRequestCallback authenticationContext,
                                                   CreationCallBack<Boolean> callback) 
                              throws InvalidParameterException
```

## Parameters



| Name                                          | Datatype                                                                                         | Notes                                                                                |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| *sendRegistrationNotificationMail*<br/> | **boolean**<br/>                                                                           | True or False<br/>                                                             |
| *userId*<br/>                           | **String**<br/>                                                                            | The email address of the user to be notified of document tracking events.<br/> |
| *authenticationContext*<br/>            | [**AuthenticationRequestCallback**](authenticationrequestcallback-interface-java.md)<br/> |                                                                                      |
| *callback*<br/>                         | CreationCallback&lt;**boolean**&gt;<br/>                                                   |                                                                                      |



 

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



 

 

 





