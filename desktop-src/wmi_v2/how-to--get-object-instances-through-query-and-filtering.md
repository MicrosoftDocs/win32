---
title: Getting object instances through querying and filtering
description: This topic provides an overview of how to retrieve the instances of a class from a CIM server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5158AC47-6DA6-4D0C-82F5-4952E5205367
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Getting object instances through querying and filtering

This topic provides an overview of how to retrieve the instances of a class from a CIM server.

In this scenario, a cmdlet retrieves zero, one, or many instances of a class. There are several ways to retrieve class instances from a CIM server.

-   GetInstance
-   QueryInstances
-   EnumerateInstances
-   EnumerateAssociatedInstances

Currently CDXML does not support GetInstance for retrieving a particular instance. Server filtering can be done through QueryInstances; however, CDXML supports WQL queries only.

A GET cmdlet definition based on Enumerate and Query requires the following information.

-   Metadata that describes the cmdlet properties.

    -   Verb
    -   Noun
    -   HelpURI

-   Cmdlet parameters for filtering the results.

    -   Cmdlet parameter Name and Type
    -   Cmdlet parameter attributes (Mandatory, ValueFromPipeline, Position, and so on)
    -   CIM class property used for filtering
    -   Type of filter query expressions to be formed. For example, RegularQuery or MinQuery

-   For each parameter, the form of its query expression can be further specialized into one of the following types:

    -   RegularQuery - Compares an instance property value with the corresponding cmdlet argument using either the equal or like operator.
    -   MinQuery - Compares an instance property value with the corresponding cmdlet argument value using the less than or equal operator.
    -   MaxQuery - Compares an instance property value with the corresponding cmdlet argument value using the greater than or equal operator.
    -   ExcludeQuery - Compares an instance property value with the corresponding cmdlet argument value and filters out instances that match.

The information above applies to the GET cmdlet when working with instance providers; that is, a CIM provider that returns instances through QueryInstance or EnumerateInstances intrinsic operations.

The following CDXML elements are used to describe the information outlined above.

``` syntax
Cmdlet Metadata : <Cmdlet> and <CmdletMetadata> 
Cmdlet Filterting Parameters : <GetCmdletParameters>
```

 

 




