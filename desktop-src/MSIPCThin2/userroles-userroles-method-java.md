---
title: UserRoles.userRoles method
description: Instantiates a new UserRoles object.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '26CF97A3-51D0-47EC-948F-8E74E159C688'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["UserRoles.userRoles method"]
topic_type:
- apiref
api_name:
- UserRoles.userRoles method
api_type:
- NA
---

# UserRoles.userRoles method

Instantiates a new [**UserRoles**](userroles-class-java.md) object.

## Signature

``` syntax
public UserRoles(Collection<String> users,
                                      Collection<String> roles)
```

## Parameters



| Name               | Datatype                                | Notes                                                                        |
|--------------------|-----------------------------------------|------------------------------------------------------------------------------|
| *users*<br/> | **Collection&lt;String&gt;**<br/> | Set of users to whom the roles are assigned.<br/>                      |
| *roles*<br/> | **Collection&lt;String&gt;**<br/> | Use the role types defined in [**Roles**](roles-class-java.md). <br/> |



 

## Defined in

UserRoles.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





