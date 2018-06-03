---
title: UserPolicy.registerForDocTracking synchronous method
description: Asynchronously registers this user policy with the document tracking service.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 9022FB7F-D6C0-4C0C-91E6-743A94975115
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- UserPolicy.registerForDocTracking synchronous method
topic_type:
- apiref
api_name:
- UserPolicy.registerForDocTracking synchronous method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UserPolicy.registerForDocTracking synchronous method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Asynchronously registers this user policy with the document tracking service.

## Signature

``` syntax
public boolean registerForDocTracking(
                                      boolean sendRegistrationNotificationMail,
                                      String userId,
                                      AuthenticationRequestCallback authenticationContext,
                                      final Context applicationContext) 
                              throws ProtectionException
```

## Parameters



| Name                                          | Datatype                                                                                         | Notes                                                                                |
|-----------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| *sendRegistrationNotificationMail*<br/> | **boolean**<br/>                                                                           | True or False<br/>                                                             |
| *userId*<br/>                           | **String**<br/>                                                                            | The email address of the user to be notified of document tracking events.<br/> |
| *authenticationContext*<br/>            | [**AuthenticationRequestCallback**](authenticationrequestcallback-interface-java.md)<br/> |                                                                                      |
| *applicationContext*<br/>               | **Context**<br/>                                                                           |                                                                                      |



 

## Throws

[**ProtectionException**](protectionexception-class-java.md)

## Returns

**boolean**

## Defined in

UserPolicy.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





