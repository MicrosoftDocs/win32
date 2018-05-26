---
title: CommonRights class
description: Rights that are supported by all applications.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 2e7225f6-8ef3-490e-a438-7c1f957221eb
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- CommonRights class
topic_type:
- apiref
api_name:
- CommonRights class
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CommonRights class

Rights that are supported by all applications.

## Signature

``` syntax
public final class CommonRights
```

## Properties



| Name                 | Signature                                                                                                                 | Description                                                                                                                |
|----------------------|---------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| **Owner**<br/> | `public final static String Owner = "OWNER";`<br/>                                                                  | Specifies a right that represents content ownership. This right grants full control over the protected content.<br/> |
| **View**<br/>  | `public final static String View = "VIEW";`<br/>                                                                    | Specifies a right that allows viewing of protected content.<br/>                                                     |
| **ALL**<br/>   | `public final static Collection<String> ALL = Collections.unmodifiableCollection(Arrays.asList(Owner, View));`<br/> | Specifies all the rights (Owner and View)<br/>                                                                       |



 

## Defined in

CommonRights.java

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

 

 





