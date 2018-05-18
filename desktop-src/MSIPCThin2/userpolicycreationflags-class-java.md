---
title: UserPolicyCreationFlags class
description: Option flags for creating user policies.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'FCBE4ECF-BE2C-439B-8A1F-6EFEF44266D6'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["UserPolicyCreationFlags class"]
topic_type:
- apiref
api_name:
- UserPolicyCreationFlags class
api_type:
- NA
---

# UserPolicyCreationFlags class

Option flags for creating user policies.

## Signature

``` syntax
public class UserPolicyCreationFlags
```

## Properties



| Name                                         | Signature                                                             | Notes                                                                                          |
|----------------------------------------------|-----------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| **NONE**<br/>                          | public static final int NONE = 0;<br/>                          |                                                                                                |
| **ALLOW\_AUDITED\_EXTRACTION** <br/>   | public static final int ALLOW\_AUDITED\_EXTRACTION = 1;<br/>    | Specifies whether the content can be opened in a non-RMS aware application or not. <br/> |
| **PREFER\_DEPRECATED\_ALGORITHM**<br/> | public static final int PREFER\_DEPRECATED\_ALGORITHM = 2;<br/> | Specifies whether [*deprecated algorithms*](terms.md) (ECB) is preferred or not.<br/>   |



 

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

 

 





