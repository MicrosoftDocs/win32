---
title: UserPolicy class
description: Represents a user policy.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'DA25AB8E-F135-4398-A52F-F581460483A6'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["UserPolicy class"]
topic_type:
- apiref
api_name:
- UserPolicy class
api_type:
- NA
---

# UserPolicy class

Represents a user policy

## Signature

``` syntax
public class UserPolicy implements Serializable
```

## Methods



| Name                                                                                                                                                       | Description                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**accessCheck**](userpolicy-accesscheck-method-java.md)<br/>                                                                                       | Does the user policy has the given right.<br/>                                      |
| [**acquire**](userpolicy-acquire-method-java.md)<br/>                                                                                               | Acquire a **UserPolicy** object based on a serialized content policy.<br/>          |
| [**create(PolicyDescriptor, ...) asynchronous**](userpolicy-create-policydescriptor-method-java.md)<br/>                                            | Asynchronously creates a new **UserPolicy** object from a policy descriptor.<br/>   |
| [**create (PolicyDescriptor, ...) synchronous**](userpolicy-create-policydescriptor-------synchronous-method-java.md)<br/>                          | Synchronously creates a new **UserPolicy** object from a policy descriptor.<br/>    |
| [**create(TemplateDescriptor, ...) asynchronous**](userpolicy-create-templatedescriptor-method-java.md)<br/>                                        | Asynchronously creates a new **UserPolicy** object from a template descriptor.<br/> |
| [**create (TemplateDescriptor, ...) synchronous**](userpolicy-create-templatedescriptor-------synchronous-method-java.md)<br/>                      | Synchronously creates a new **UserPolicy** object from a template descriptor.<br/>  |
| [**doesUseDeprecatedAlgorithm**](userpolicy-doesusedeprecatedalgorithm-method-java.md)<br/>                                                         | Does the policy use [*deprecated algorithms*](terms.md).<br/>                      |
| [**getContentId**](userpolicy-getcontentid-method-java.md)<br/>                                                                                     | Gets the content ID.<br/>                                                           |
| [**getContentValidUntil**](userpolicy-getcontentvaliduntil-method-java.md)<br/>                                                                     | Gets the date until which the content is valid.<br/>                                |
| [**getDescription**](userpolicy-getdescription-method-java.md)<br/>                                                                                 | Gets the content description.<br/>                                                  |
| [**getEncryptedAppData**](userpolicy-getencryptedappdata-method-java.md)<br/>                                                                       | Gets the encrypted application data.<br/>                                           |
| [**getIssuedTo**](userpolicy-getissuedto-method-java.md)<br/>                                                                                       | Gets the user to whom the policy was originally issued.<br/>                        |
| [**getName**](userpolicy-getname-method-java.md)<br/>                                                                                               | Gets the policy name.<br/>                                                          |
| [**getOwner**](userpolicy-getowner-method-java.md)<br/>                                                                                             | Gets the policy owner.<br/>                                                         |
| [**getPolicyDescriptor**](userpolicy-getpolicydescriptor-method-java.md)<br/>                                                                       | Gets the policy descriptor.<br/>                                                    |
| [**getReferrer**](userpolicy-getreferrer-method-java.md)<br/>                                                                                       | Gets the referrer information.<br/>                                                 |
| [**getSerializedContentPolicy**](userpolicy-getserializedcontentpolicy-method-java.md)<br/>                                                         | Gets the serialized content policy.<br/>                                            |
| [**getSignedAppData**](userpolicy-getsignedappdata-method-java.md)<br/>                                                                             | Gets the signed application data.<br/>                                              |
| [**getTemplateDescriptor**](userpolicy-gettemplatedescriptor-method-java.md)<br/>                                                                   | Gets the template descriptor associated with the policy.<br/>                       |
| [**getType**](userpolicy-gettype-method-java.md)<br/>                                                                                               | Gets the type of user policy.<br/>                                                  |
| [**isAllowedAuditedExtract**](userpolicy-isallowedauditedextract-method-java.md)<br/>                                                               | Is audited extract of the policy allowed.<br/>                                      |
| [**isIssuedToOwner**](userpolicy-isissuedtoowner-method-java.md)<br/>                                                                               | Checks if the current user is the same as the original policy owner.<br/>           |
| [**isProtected**](userpolicy-isprotected-method-java.md)<br/>                                                                                       | Checks if the user policy is a protected user policy.<br/>                          |
| [**registerForDocTracking asynchronous**](userpolicy-registerfordoctracking-boolean--sting--authenticationcallback--creationcallback--java.md)<br/> | Asynchronously registers this user policy with the document tracking service.<br/>  |
| [**registerForDocTracking synchronous**](userpolicy-registerfordoctracking-synchronous-method-java.md)<br/>                                         | Synchronously registers this user policy with the document tracking service.<br/>   |
| [**revokeUserPolicy asynchronous**](msipcthin2-userpolicy_revokeuserpolicy_method_java)<br/>                                                         | Asynchronously revokes published content.<br/>                                      |
| [**revokeUserPolicy synchronous**](msipcthin2-userpolicy_revokeuserpolicy_synchronous_method_java)<br/>                                              | Synchronously revokes published content.<br/>                                       |



 

## Defined in

UserPolicy.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Package

com.microsoft.rightsmanagement

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





