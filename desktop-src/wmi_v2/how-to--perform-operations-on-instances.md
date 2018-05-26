---
title: Performing operations on instances
description: This topic provides an overview of how a cmdlet that corresponds to an instance method, intrinsic or extrinsic, is applied to a set of instances of a class that have been retrieved by using a query constructed based on the query parameters.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4EAB4167-EFB7-4DFA-8671-2055E3F46CCE
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Performing operations on instances

This topic provides an overview of how a cmdlet that corresponds to an instance method, intrinsic or extrinsic, is applied to a set of instances of a class that have been retrieved by using a query constructed based on the query parameters.

A CIM query operation may return 0 or many instances matching the constructed query. After the instances are retrieved, the CIM Instance operation can be performed on those instances. The following table shows a typical mapping between cmdlet verbs and CIM operations.



| PowerShell verb                 | CIM operation                                   |
|---------------------------------|-------------------------------------------------|
| Set/Update<br/>           | ModifyInstance<br/>                       |
| Remove<br/>               | DeleteInstance<br/>                       |
| Other approved verbs<br/> | Extrinsic instance method operations<br/> |



 

A cmdlet definition based on a CIM Instance operation requires the following information.

-   Cmdlet Metadata element.
-   Query Parameters element, which defines the properties and query expressions used to filter the instances.
-   Method elements, which define the mapping between the cmdlet parameters and the corresponding method. For Method elements, you'll also need the following information.

    -   For both extrinsic and intrinsic methods The method name (for intrinsic methods , use cim: as the prefix).
    -   For extrinsic methods Method parameters that are used as cmdlet parameters. (A method can have more parameters than are used by a cmdlet.)
    -   For extrinsic methods Method output.

The following CDXML elements are used to describe the information outlined above.

``` syntax
Cmdlet Metadata : <Cmdlet> and <CmdletMetadata> 
Cmdlet Filterting Parameters : <GetCmdletParameters>
Method invoked by cmdlet : <Method>
```

 

 





