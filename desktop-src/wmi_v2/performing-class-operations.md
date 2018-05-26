---
title: Performing class operations
description: This topic provides an overview of performing class operations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: E8A5F14E-F3B5-4195-A373-11C079135834
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Performing class operations

This topic provides an overview of performing class operations.

Class operations - also known as static methods in MOF - are different than instance operations and cmdlets mapped to static methods are defined in a different section of the CDXML file than those mapped to instance methods. The two main differences are the following.

-   Static methods do not have query parameters because they cannot be applied to instances.
-   It is possible to map a single cmdlet to multiple static methods by creating a separate parameter set for each method.

A cmdlet definition for invoking a static method has the following elements.

-   The name of the method.
-   The method parameters. Each parameter appears as a cmdlet parameter. (A method can have more parameters than are used by a cmdlet.)
-   The method output.

A separate static method can be called for each parameter set of the cmdlet. This is not possible with cmdlets that are mapped to instance methods.

The following CDXML elements are used to describe the information outlined above.

``` syntax
Cmdlet Metatadata: <Cmdlet> and <CmdletMetadata>
Method Signature: <Method>
```

 

 




