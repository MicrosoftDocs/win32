---
title: PolicyAcquisitionFlags class
description: Defines modes for consuming protected content.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'D332F590-974F-41EF-B994-F79B2C1BC655'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["PolicyAcquisitionFlags class"]
topic_type:
- apiref
api_name:
- PolicyAcquisitionFlags class
api_type:
- NA
---

# PolicyAcquisitionFlags class

Defines modes for consuming protected content.

## Signature

``` syntax
public final class PolicyAcquisitionFlags
```

## Properties



| Name                         | Signature                                             | Notes                                                                                                                                                                                                                                      |
|------------------------------|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **NONE**<br/>          | public static final int NONE = 0;<br/>          | When specified, the SDK will attempt to perform the operation silently, and without using the network. <br/> If it fails to run without the network it will attempt to access the network.<br/>                                |
| **OFFLINE\_ONLY**<br/> | public static final int OFFLINE\_ONLY = 1;<br/> | When specified, the SDK will attempt to perform the operation silently, without using the network. <br/> If it fails to run without the the network it will throw the **OfflineOnlyRequiresInternetException** exception.<br/> |



 

## Defined in

PolicyAcquisitionFlags.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Package

com.microsoft.rightsmanagement

## Remarks

For more information about the built-in rights and the usage restrictions associated with them that apps should observe, see [Built-in Rights Usage Restriction Reference](built-in-rights-usage-restriction-reference.md).

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





