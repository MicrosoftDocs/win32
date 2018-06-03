---
title: CustomProtectedOutputStream.getEncryptedContentLength method
description: Gets the calculated size of the encrypted content.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 1D9F641A-394E-435B-A486-B6E581B011AC
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- CustomProtectedOutputStream.getEncryptedContentLength method
topic_type:
- apiref
api_name:
- CustomProtectedOutputStream.getEncryptedContentLength method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CustomProtectedOutputStream.getEncryptedContentLength method

Gets the calculated size of the encrypted content.

## Signature

``` syntax
static public long getEncryptedContentLength(long decryptedContentLength, 
                                        UserPolicy userPolicy) throws InvalidParameterException
```

## Parameters



| Name                                | Datatype                                               | Notes                                      |
|-------------------------------------|--------------------------------------------------------|--------------------------------------------|
| *decryptedContentLength*<br/> | **long**<br/>                                    | Must be greater then 0 (zero). <br/> |
| *userPolicy*<br/>             | [**UserPolicy**](userpolicy-class-java.md)<br/> |                                            |



 

## Returns

A **long**

## Defined in

CustomProtectedOutputStream.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





