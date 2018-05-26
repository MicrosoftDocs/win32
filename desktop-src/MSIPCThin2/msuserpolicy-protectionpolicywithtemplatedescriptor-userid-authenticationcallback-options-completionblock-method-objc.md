---
title: MSUserPolicy userPolicyWithTemplateDescriptor userId authenticationCallback options completionBlock method
description: This method creates a user policy based on the supplied template descriptor.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 3C475D5C-B1BE-4D69-B6C7-C4D160FDA7EE
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSUserPolicy userPolicyWithTemplateDescriptor userId authenticationCallback options completionBlock method
topic_type:
- apiref
api_name:
- MSUserPolicy userPolicyWithTemplateDescriptor userId authenticationCallback options completionBlock method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSUserPolicy userPolicyWithTemplateDescriptor:userId:authenticationCallback:options:completionBlock method

This method creates a user policy based on the supplied template descriptor. The following method should be invoked from the main thread.

## Signature

``` syntax
+ (MSAsyncControl *)userPolicyWithTemplateDescriptor:(MSTemplateDescriptor *)templateDescriptor
                                              userId:(NSString *)userId
                                       signedAppData:(NSDictionary *)signedAppData
                                     licenseMetadata:(MSLicenseMetadata*)licenseMetadata
                              authenticationCallback:(id<MSAuthenticationCallback>)authenticationCallback
                                             options:(MSUserPolicyCreationOptions)options
                                     completionBlock:(void(^)(MSUserPolicy *userPolicy, NSError *error))completionBlock;
```

## Parameters



| Name                                | Datatype                                                                                                   | Notes                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *templateDescriptor*<br/>     | [**MSTemplateDescriptor**](mstemplatedescriptor-interface-objc.md) \*<br/>                          | Required. The object which defines the template used to create the policy.<br/>                                                                                                                                                                                                                                                                |
| *userId*<br/>                 | **NSString** \*<br/>                                                                                 | The email address of the user for whom the templates are being retrieved. <br/> This email address will be used to discover the RMS service instance (either AD RMS server or Azure RMS) that the user's organization is using. <br/>                                                                                                    |
| *authenticationCallback*<br/> | id&lt;[**MSAuthenticationCallback**](msauthenticationcallback-protocol-objc.md)&gt;) \*<br/>        | Callback method to be used for authorization.<br/>                                                                                                                                                                                                                                                                                             |
| *signedAppData*<br/>          | **NSDictionary** \*<br/>                                                                             |                                                                                                                                                                                                                                                                                                                                                      |
| *licenseMetaData*<br/>        | [**MSLicenseMetadata**](mslicensemetadata-class-objc.md) \*<br/>                                    | If you want to enable document tracking, it must be initialized before creating the [**MSUserPolicy**](msuserpolicy-interface-objc.md) with the [**MSTemplateDescriptor**](mstemplatedescriptor-interface-objc.md) object.<br/> For more information, see [**How to: Use document tracking**](how-to--use-document-tracking.md).<br/> |
| *options*<br/>                | [**MSUserPolicyCreationOptions**](msprotectionpolicycreationoptions-enum-objc.md)<br/>              | Options for creating protection policy object (see [**MSUserPolicyCreationOptions**](msprotectionpolicycreationoptions-enum-objc.md))<br/>                                                                                                                                                                                                    |
| *completionBlock*<br/>        | void(^)([**MSUserPolicy**](msuserpolicy-interface-objc.md) \* userPolicy, **NSError** \*error)<br/> | The created user policy.<br/>                                                                                                                                                                                                                                                                                                                  |



 

## Returns

A pointer to an [**MSAsyncControl**](msasynccontrol-class.md) object.

## Defined in

MSUserPolicy.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

If you want to use the **document tracking** feature, the **licenseMetadata** property must be initialized prior to creating the [**MSUserPolicy**](msuserpolicy-interface-objc.md) and you will need to register with the document tracking service via a call to [**registerForDocTracking:userId:authenticationCallback:completionBlock**](msuserpolicy-registerfordoctracking-userid-authenticationcallback-completionblock-method-objc.md), otherwise this parameter can be left uninitialized (nil) and the call to **registerForDocTracking:userId:authenticationCallback:completionBlock** on the **MSUserPolicy** can be skipped.

An example usage of this method:


```
[MSUserPolicy userPolicyWithTemplateDescriptor:[templates objectAtIndex:0]
                                        userId:@"user@domain.com"
                        authenticationCallback:authenticationCallback
                                 signedAppData:appData
                               licenseMetadata:docTrackingData
                                       options:None
                               completionBlock:^(MSUserPolicy *userPolicy, NSError *error)
```



 

 





