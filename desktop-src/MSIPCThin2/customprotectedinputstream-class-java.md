---
title: CustomProtectedInputStream class
description: This class implements a wrapper of the input stream allowing writing of a custom RMS protected output stream.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: AA93DCD7-BA19-48EB-84AE-734CAEE50FFF
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- CustomProtectedInputStream class
topic_type:
- apiref
api_name:
- CustomProtectedInputStream class
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CustomProtectedInputStream class

This class implements a wrapper of the input stream allowing writing of a custom RMS protected output stream. Custom denotes that it is more configurable than the default protected input stream, also **CustomProtectedInputStream** requires a user policy as an input.

## Signature

``` syntax
public class CustomProtectedInputStream extends InputStream
```

**CustomProtectedInputStream** extends Android's base class. For information on base class methods see, [InputStream](http://developer.android.com/reference/java/io/InputStream.mdl).

## Methods



| Name                                                                                               | Description                                                                      |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [**create asynchronous**](customprotectedinputstream-create-method-java.md)<br/>            | Asynchronously creates an input stream for reading protected content.<br/> |
| [**create synchronous**](customprotectedinputstream-create-synchronous-method-java.md)<br/> | Synchronously creates an input stream for reading protected content.<br/>  |
| [**getUserPolicy**](customprotectedinputstream-getuserpolicy-method-java.md)<br/>           | Gets the user policy associated with the stream.<br/>                      |



 

## Defined in

CustomProtectedInputStream.java

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

[Android API Reference](android.md)
</dt> <dt>

[Developer guidance and terms](core-concepts.md)
</dt> <dt>

[Get started](get-started.md)
</dt> </dl>

 

 





