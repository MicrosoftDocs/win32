---
title: MSPolicyDescriptor class
description: Information for describing a policy.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: A96FD245-E075-4E53-A529-1DC8C359AE33
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSPolicyDescriptor class
topic_type:
- apiref
api_name:
- MSPolicyDescriptor class
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSPolicyDescriptor class

Information for describing a policy. Inherits from **MSSecureCodableObject**.

## Signature

``` syntax
@interface MSPolicyDescriptor : MSSecureCodableObject
```

## Methods



| Name                                                                                                      | Description                                      |
|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [**initWithUserRights**](mspolicydescriptor-initwithuserrights-userrightslist-method-objc.md)<br/> | Add user rights for the custom policy<br/> |
| [**initWithUserRoles**](mspolicydescriptor-initwithuserroles-objc.md)<br/>                         | Add user roles for the custom policy<br/>  |



 

## Properties



| Name                                                                                                         | Description                              |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------|
| [**licenseMetadata**](mspolicydescriptor-licensemetadata-property-objc.md)<br/>                       | Document tracking information<br/> |
| [**policyName**](mspolicydescriptor-name-property-objc.md)<br/>                                       | Policy name<br/>                   |
| [**policyDescription**](mspolicydescriptor-description-property-objc.md)<br/>                         | Policy description<br/>            |
| [**userRightsList**](mspolicydescriptor-userrightslist-property-objc.md)<br/>                         | Rights granted to users<br/>       |
| [**userRolesList**](mspolicydescriptor-userroleslist-property-objc.md)<br/>                           | Roles granted to users<br/>        |
| [**referrer**](mspolicydescriptor-referrer-property-objc.md)<br/>                                     | Referral info<br/>                 |
| [**contentValidUntil**](mspolicydescriptor-contentvaliduntil-property-objc.md)<br/>                   | Validity time<br/>                 |
| [**offlineCacheLifetimeInDays**](mspolicydescriptor-offlinecachelifetimeindays-property-objc.md)<br/> | Interval time<br/>                 |
| [**encryptedAppData**](mspolicydescriptor-encryptedappdata-property-objc.md)<br/>                     | App specific data, encrypted<br/>  |
| [**signedAppData**](mspolicydescriptor-signedappdata-property-objc.md)<br/>                           | App specific data, signed<br/>     |



 

## Defined in

MSPolicyDescriptor.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





