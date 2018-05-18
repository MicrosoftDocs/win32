---
title: UserPolicy.create(TemplateDescriptor, ...) asynchronous method
description: Asynchronously creates a new UserPolicy object from a template descriptor.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '202E8E74-0D9B-4832-95E9-16771A1D8EDF'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["UserPolicy.create(TemplateDescriptor, ...) asynchronous method"]
topic_type:
- apiref
api_name:
- UserPolicy.create(TemplateDescriptor, ...) asynchronous method
api_type:
- NA
---

# UserPolicy.create(TemplateDescriptor, ...) asynchronous method

Asynchronously creates a new [**UserPolicy**](userpolicy-class-java.md) object from a template descriptor.

## Signature

``` syntax
public static IAsyncControl create(
                                     TemplateDescriptor templateDescriptor,
                                     String userId,
                                     AuthenticationRequestCallback authenticationContext,
                                     int userPolicyCreationFlags,
                                     Map<String,String> signedAppData,
                                     LicenseMetadata licenseMetadata,
                                     CreationCallback<UserPolicy> callback)  
                              throws InvalidParameterException
```

## Parameters



| Name                                 | Datatype                                                                                         | Notes                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *templateDescriptor*<br/>      | [**TemplateDescriptor**](templatedescriptor-class-java.md)<br/>                           |                                                                                                                                                                                                                                                                                                                                      |
| *userId*<br/>                  | **String**<br/>                                                                            | A unique user identifier such as an email address.<br/> This *userId* is used to discover the RMS service instance (either ADRMS server or Azure RMS) that the user's organization is using. *userId* is used for caching user policy as well for offline usage.<br/>                                                    |
| *authenticationContext*<br/>   | [**AuthenticationRequestCallback**](authenticationrequestcallback-interface-java.md)<br/> |                                                                                                                                                                                                                                                                                                                                      |
| *userPolicyCreationFlags*<br/> | **int**<br/>                                                                               | For more information, see [**UserPolicyCreationFlags**](userpolicycreationflags-class-java.md))<br/>                                                                                                                                                                                                                          |
| *signedAppData*<br/>           | **Map&lt;String,String&gt;**<br/>                                                          |                                                                                                                                                                                                                                                                                                                                      |
| *licenseMetaData*<br/>         | [**LicenseMetadata**](licensemetadata-interface-java.md)<br/>                             | If you want to enable document tracking, it must be initialized before creating the [**UserPolicy**](userpolicy-class-java.md) with the [**TemplateDescriptor**](templatedescriptor-class-java.md) object.<br/> For more information, see [**How to: Use document tracking**](how-to--use-document-tracking.md).<br/> |
| *callback*<br/>                | CreationCallback&lt;[**UserPolicy**](userpolicy-class-java.md)&gt;&gt; <br/>              |                                                                                                                                                                                                                                                                                                                                      |



 

## Throws

[**InvalidParameterException**](invalidparameterexception-class-java.md)

## Returns

A [**IAsyncControl**](iasynccontrol-interface.md)

## Defined in

UserPolicy.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





