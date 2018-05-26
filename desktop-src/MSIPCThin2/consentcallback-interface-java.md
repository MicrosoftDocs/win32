---
title: ConsentCallback interface
description: Interface for managing consent.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 128CEBB0-FB86-432A-B759-C02E571B8AAA
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- ConsentCallback interface
topic_type:
- apiref
api_name:
- ConsentCallback interface
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ConsentCallback interface

Interface for managing consent. Your application should implement this interface's method and pass it to the Rights Management SDK 4.2 APIs that perform consent.

## Signature

``` syntax
public interface ConsentCallback
```

## Methods



| Name                                                                  | Description                                                                       |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**consents**](conscentcallback-conscents-method-java.md)<br/> | Callback provided by SDK to get back user's consent preference results<br/> |



 

## Defined in

ConsentCallback.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Package

com.microsoft.rightsmanagement

## Thread Safety

Members of this class are not guaranteed to be thread safe.

## See also

<dl> <dt>

[**ConsentCallback consents method**](conscentcallback-conscents-method-java.md)
</dt> </dl>

 

 





