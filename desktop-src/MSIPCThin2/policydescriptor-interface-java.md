---
title: PolicyDescriptor class
description: Information associated with a users custom policy.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 85F0C28F-8B6F-451F-9F24-FD9B477B90EE
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- PolicyDescriptor class
topic_type:
- apiref
api_name:
- PolicyDescriptor class
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PolicyDescriptor class

Information associated with a user's custom policy.

## Signature

``` syntax
public class PolicyDescriptor implements Serializable
```

## Methods



| Name                                                                                                                         | Description                                                    |
|------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| [**createPolicyDescriptorFromUserRights**](policydescriptor-createpolicydescriptorfromuserrights-method-java.md)<br/> | Creates a new **PolicyDescriptor** from user rights<br/> |
| [**createPolicyDescriptorFromUserRoles**](policydescriptor-createpolicydescriptorfromuserroles-method-java.md)<br/>   | Creates a new **PolicyDescriptor** from user roles<br/>  |
| [**getContentValidUntil**](policydescriptor-getcontentvaliduntil-method-java.md)<br/>                                 | Gets the date that the content is valid until<br/>       |
| [**getDescription**](policydescriptor-getdescription-method-java.md)<br/>                                             | Gets the policy description<br/>                         |
| [**getEncryptedAppData**](policydescriptor-getencryptedappdata-method-java.md)<br/>                                   | Gets the encrypted application data<br/>                 |
| [**getLicenseMetadata**](policydescriptor-getlicensemetadata-java.md)<br/>                                            | Gets the license metadata object.<br/>                   |
| [**getName**](policydescriptor-getname-method-java.md)<br/>                                                           | Gets the policy's name<br/>                              |
| [**getOfflineCacheLifetimeInDays**](policydescriptor-getlicensevaliditytimeintervalindays-method-java.md)<br/>        | Gets the time a user policy can be cached offline<br/>   |
| [**getReferrer**](policydescriptor-getreferrer-method-java.md)<br/>                                                   | Gets the optional referrer<br/>                          |
| [**getSignedAppData**](policydescriptor-getsignedappdata-method.md)<br/>                                              | Gets the signed application data<br/>                    |
| [**getUserRightsList**](policydescriptor-getuserrightslist-method-java.md)<br/>                                       | Gets the user's rights list<br/>                         |
| [**getUserRolesList**](policydescriptor-getuserroleslist-method-java.md)<br/>                                         | Gets the user's roles list<br/>                          |
| [**setContentValidUntil**](policydescriptor-setcontentvaliduntil-method-java.md)<br/>                                 | Sets the date that the content is valid until<br/>       |
| [**setDescription**](policydescriptor-setdescription-method-java.md)<br/>                                             | Sets the policy description<br/>                         |
| [**setEncryptedAppData**](policydescriptor-setencryptedappdata-method-java.md)<br/>                                   | Sets the encrypted application data<br/>                 |
| [**setLicenseMetadata**](policydescriptor-setlicensemetadata-java.md)<br/>                                            | Sets the license metadata object.<br/>                   |
| [**setName**](policydescriptor-setname-method-java.md)<br/>                                                           | Sets the policy's name<br/>                              |
| [**setOfflineCacheLifetimeInDays**](policydescriptor-setlicensevaliditytimeintervalindays-method-java.md)<br/>        | Sets the number of days the license is valid<br/>        |
| [**setSignedAppData**](policydescriptor-setsignedappdata-method-java.md)<br/>                                         | Sets the signed application data.<br/>                   |
| [**setReferrer**](policydescriptor-setreferrer-method-java.md)<br/>                                                   | Sets the referrer information<br/>                       |



 

## Defined in

PolicyDescriptor.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Package

com.microsoft.rightsmanagement

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





