---
title: UserRights.userRights method
description: Instantiates a new UserRights object.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '1256D022-0E7B-49F1-B0A1-DD5FBCAAF4E8'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["UserRights.userRights method"]
topic_type:
- apiref
api_name:
- UserRights.userRights method
api_type:
- NA
---

# UserRights.userRights method

Instantiates a new [**UserRights**](userrights-class-java.md) object.

## Signature

``` syntax
public userRights(Collection<String> users,
                                      Collection<String> rights)
```

## Parameters



| Name                | Datatype                                | Notes                                                                                                                                                                                                                                                                                                                                          |
|---------------------|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *users*<br/>  | **Collection&lt;String&gt;**<br/> | The set of users to whom the rights are granted.<br/>                                                                                                                                                                                                                                                                                    |
| *rights*<br/> | **Collection&lt;String&gt;**<br/> | For more information on managing user rights, see [Built-in Rights Usage Restriction Reference](built-in-rights-usage-restriction-reference.md) as well as [**CommonRights**](commonrights-class-java.md), [**EditableDocumentRights**](editabledocumentrights-class-java.md) and [**EmailRights**](emailrights-class-java.md).<br/> |



 

## Defined in

UserRights.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





