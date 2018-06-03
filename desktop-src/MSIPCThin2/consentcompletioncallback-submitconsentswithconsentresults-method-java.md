---
title: ConsentCompletionCallback submitConsentsWithConsentResults method
description: Callback provided by SDK to get back user's consent preference results.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: D7B7E8AE-10BC-4935-A18F-38DE92420A50
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- ConsentCompletionCallback submitConsentsWithConsentResults method
topic_type:
- apiref
api_name:
- ConsentCompletionCallback submitConsentsWithConsentResults method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ConsentCompletionCallback submitConsentsWithConsentResults method

Callback provided by SDK to get back user's consent preference results.

## Signature

``` syntax
public void submitConsentsWithConsentResults(Collection<Consent> consents) 
  throws ProtectionException;
```

## Parameters



| Name                  | Datatype                                                           | Notes |
|-----------------------|--------------------------------------------------------------------|-------|
| *consents*<br/> | Collection&lt;[**Consent**](consent-class-java.md)&gt;<br/> |       |



 

## Defined in

ConsentCompletionCallback.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 





