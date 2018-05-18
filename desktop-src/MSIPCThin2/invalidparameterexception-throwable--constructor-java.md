---
title: InvalidParameterException(String, String, Throwable) constructor
description: Initializes a new instance of the InvalidParameterException class with a passed in message and tag and, the specified inner exception.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'e5240e62-2e50-4f87-ac7e-5776c7380095'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["InvalidParameterException(String, String, Throwable) constructor"]
topic_type:
- apiref
api_name:
- InvalidParameterException(String, String, Throwable) constructor
api_type:
- NA
---

# InvalidParameterException(String, String, Throwable) constructor

Initializes a new instance of the [**InvalidParameterException**](invalidparameterexception-class-java.md) class with a passed in message and tag and, the specified inner exception.

> [!Note]  
> The message is precise and just revealing enough to pinpoint the invalid parameter which will assist you to find mistakes in your code.

 

## Signature

``` syntax
public InvalidParameterException(Sting tag, String message, Throwable e)
```

## Parameters



| Name                 | Datatype                 | Description                     |
|----------------------|--------------------------|---------------------------------|
| *tag*<br/>     | **String**<br/>    | The tag to log with.<br/> |
| *message*<br/> | **String**<br/>    |                                 |
| *e*<br/>       | **Throwable**<br/> | The inner exception.<br/> |



 

## Returns

[**InvalidParameterException**](invalidparameterexception-class-java.md)

## Defined in

InvalidParameterException.java

 

 





