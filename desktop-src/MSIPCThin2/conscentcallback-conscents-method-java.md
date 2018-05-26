---
title: ConsentCallback consents method
description: Callback to be provided by you to know when and which consent notifications to display to user.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 0B8CE14C-B42F-4772-B06C-4A71754F6DE6
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- ConsentCallback consents method
topic_type:
- apiref
api_name:
- ConsentCallback consents method
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ConsentCallback consents method

Callback to be provided by you to know when and which consent notifications to display to user.

## Signature

``` syntax
public void consents(Collection<Consent> consents, 
                     ConsentCompletionCallback consentCompletionCallback
                     );
```

## Parameters



| Name                                   | Datatype                                                                            | Notes |
|----------------------------------------|-------------------------------------------------------------------------------------|-------|
| *consents*<br/>                  | Collection&lt;[**Consent**](consent-class-java.md)&gt;<br/>                  |       |
| *consentCompletionCallback*<br/> | [**ConsentCompletionCallback**](consentcompletioncallback-interface.md)<br/> |       |



 

## Defined in

ConsentCallback.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





