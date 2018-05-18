---
title: MSUserPolicy registerForDocTracking userId authenticationCallback completionBlock method
description: Registers this policy with the document tracking service. See Remarks section for further details.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '2FAE51F2-68EB-4876-B073-4C803074EBC9'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSUserPolicy registerForDocTracking userId authenticationCallback completionBlock method"]
topic_type:
- apiref
api_name:
- MSUserPolicy registerForDocTracking userId authenticationCallback completionBlock method
api_type:
- NA
---

# MSUserPolicy registerForDocTracking:userId:authenticationCallback:completionBlock method

Registers this policy with the document tracking service. See **Remarks** section for further details.

For more information, see [**How to: Use document tracking**](how-to--use-document-tracking.md).

## Signature

``` syntax
- (MSAsyncControl *)
    registerForDocTracking:(BOOL) sendRegistrationNotificationMail 
                                   userId:(NSString *)userId
                   authenticationCallback:(id<MSAuthenticationCallback>)authenticationCallback                                                    
                          completionBlock:(void(^)(BOOL success, NSError *error))completionBlock;
```

## Parameters



| Name                                          | Datatype                                                                                        | Notes                                                                         |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| *sendRegistrationNotificationMail*<br/> | **BOOL**<br/>                                                                             | True or False<br/>                                                      |
| *userId*<br/>                           | **NSString** \*<br/>                                                                      | The id of the registering user in the form - **userid@domain.ext**<br/> |
| *authenticationCallback*<br/>           | id&lt;[**MSAuthenticationCallback**](msauthenticationcallback-protocol-objc.md)&gt;<br/> |                                                                               |
| *completionBlock*<br/>                  | void(^)(**BOOL** success, **NSError** \*error)<br/>                                       |                                                                               |



 

## Returns

A pointer to an [**MSAsyncControl**](msasynccontrol-class.md) object.

## Defined in

MSUserPolicy.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

Document tracking is currently only supported for Rights Management Services On-line scenarios. In order to conditionally register licenses based on this, we will use service discovery to determine whether or not registration is supported.

-   In the case of a [**MSMutableProtectedData**](msmutableprotecteddata-interface-objc.md) object, obtained after binding the user policy to a file, will have the [**MSUserPolicy**](msuserpolicy-interface-objc.md) object within, we will not be able to register for on premises scenarios.
-   In the case of Microsoft Office using the [**MSProtector**](msprotector-class-objc.md) class for buffer based protection, the [**MSUserPolicy**](msuserpolicy-interface-objc.md) object in that class will be used to register the license.

If this method is called without setting up the corresponding [**MSLicenseMetadata**](mslicensemetadata-class-objc.md) or there is a registration error with the service, there is no adverse effect and an SDK error will be produced.

Because this method is asynchronous, the returned [**MSAsyncControl**](msasynccontrol-class.md) object can be used to cancel the request if needed.

 

 





