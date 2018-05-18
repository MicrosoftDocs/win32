---
title: MSUserPolicy userPolicyWithSerializedPolicy userId authenticationCallback consentCallback options completionBlock method
description: Creates a protection policy based on the supplied serialized policy parameter.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '33C0A9D1-D29D-4BE4-8A87-4F22BD5A5BDD'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSUserPolicy userPolicyWithSerializedPolicy userId authenticationCallback consentCallback options completionBlock method"]
topic_type:
- apiref
api_name:
- MSUserPolicy userPolicyWithSerializedPolicy userId authenticationCallback consentCallback options completionBlock method
api_type:
- NA
---

# MSUserPolicy userPolicyWithSerializedPolicy:userId:authenticationCallback:consentCallback options:completionBlock method

Creates a protection policy based on the supplied serialized policy parameter. The following method should be invoked from your application's main thread.

## Signature

``` syntax
+ (MSAsyncControl *)userPolicyWithSerializedPolicy:(NSData *)serializedPolicy 
                                            userId:(NSString *)userId
                            authenticationCallback:(id<MSAuthenticationCallback>)authenticationCallback
                                   consentCallback:(id<MSConsentCallback>)consentCallback
                                           options:(MSPolicyAcquisitionOptions)options
                                   completionBlock:(void(^)(MSUserPolicy *userPolicy, NSError *error))completionBlock;
```

## Parameters



| Name                                | Datatype                                                                                                  | Notes                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *serializedPolicy*<br/>       | **NSData** \*<br/>                                                                                  | Required. The policy to be consumed<br/>                                                                                                                                                                                                                                                                                                                                                                                    |
| *userId*<br/>                 | **NSString** \*<br/>                                                                                | The email address of the user that is trying to consume the protected content. This email address will be used to determine which policy object to use from the offline cache. If a policy object for this user is not found in the offline cache then this API will go online (if allowed) to get the policy object. <br/> If null is passed, the first policy object found in the offline cache will be used. <br/> |
| *authenticationCallback*<br/> | id&lt;[**MSAuthenticationCallback**](msauthenticationcallback-protocol-objc.md)&gt;<br/>           |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| *consentCallback*<br/>        | id&lt;[**MSConsentCallback**](https://msdn.microsoft.com/library/windows/desktop/dn833525)&gt;<br/>                 |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| *options*<br/>                | [**MSPolicyAcquisitionOptions**](mspolicyacquisitionoptions-enum-objc.md)<br/>                     | Options for creating user policy object. For more information, see [**MSPolicyAcquisitionOptions**](mspolicyacquisitionoptions-enum-objc.md)<br/>.                                                                                                                                                                                                                                                                         |
| *completionBlock*<br/>        | void(^)([**MSUserPolicy**](msuserpolicy-interface-objc.md) \*userPolicy, **NSError** \*error)<br/> | The created protection policy.<br/>                                                                                                                                                                                                                                                                                                                                                                                         |



 

## Returns

A pointer to an [**MSAsyncControl**](msasynccontrol-class.md) object.

## Defined in

MSUserPolicy.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

This example code snip demonstrates how to convert the embedded serialized policy within an MS Office document to a concrete [**MSUserPolicy**](msuserpolicy-interface-objc.md) given the current user, using the email parameter.


```
+ (void)sampleConsumptionWithSerializedLicense:(NSData *)serializedData authenticationCallback:(id<MSAuthenticationCallback>)authenticationCallback
{
    MSAsyncControl *asyncControl = [MSUserPolicy userPolicyWithSerializedPolicy:serializedData
                                                                         userId:@"user@domain.com"
                                                         authenticationCallback:authenticationCallback
                                                                        options:default
                                                                completionBlock:^(MSUserPolicy *userPolicy, NSError *error)
                                    {
                                        // use userPolicy (Note: will be nil on error)
                                    }];
}
```



 

 





