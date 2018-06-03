---
title: Roles class
description: Roles for protecting documents.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: D58ABB15-7084-45D2-BD17-E7979F81ACB8
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- Roles class
topic_type:
- apiref
api_name:
- Roles class
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Roles class

Roles for protecting documents.

## Signature

``` syntax
public final class Roles
```

## Properties



| Name                    | Signature                                                            | Description                                                                                  |
|-------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| **VIEWER**<br/>   | `    public final static String VIEWER = "VIEWER";`<br/>       | User will only be able to view the document. They cannot edit, copy, or print it.<br/> |
| **REVIEWER**<br/> | `    public final static String REVIEWER = "REVIEWER";`<br/>   | User will be able to view and edit the document. They cannot copy or print it.<br/>    |
| **AUTHOR**<br/>   | `    public final static String AUTHOR = "AUTHOR";`<br/>       | User will be able to view, edit, copy, and print the document.<br/>                    |
| **COOWNER**<br/>  | `        public final static String COOWNER = "COOWNER";`<br/> | User will have all permissions<br/>                                                    |



 

## Defined in

Roles.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Package

com.microsoft.rightsmanagement

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 





