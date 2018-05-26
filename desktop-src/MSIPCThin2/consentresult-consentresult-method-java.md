---
title: ConsentResult ConsentResult method
description: Instantiates a new ConsentResult.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: BF0C0EF9-CEF1-472A-97D6-18C47AA6F153
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- ConsentResult ConsentResult method
topic_type:
- apiref
api_name:
- ConsentResult ConsentResult method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ConsentResult ConsentResult method

Instantiates a new [**ConsentResult**](consentresult-interface-java.md).

## Signature

``` syntax
public ConsentResult(   boolean accepted, 
                      boolean showAgain, 
                      String userId)
```

## Parameters



| Name                   | Datatype               | Notes                                                                 |
|------------------------|------------------------|-----------------------------------------------------------------------|
| *accepted*<br/>  | **Boolean**<br/> | True if user accepted , False otherwise<br/>                    |
| *showAgain*<br/> | **Boolean**<br/> | False if user checked don't show me again , True otherwise<br/> |
| *userId*<br/>    | **String**<br/>  |                                                                       |



 

## Defined in

ConsentResult.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





