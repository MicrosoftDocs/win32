---
Description: 'In a distributed model, the client often cannot receive exceptions that occur in the service. However, HPC sessions do provide exception propagation, making it possible for service faults to be caught and processed by the client application.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'eae4bfaa-6048-4f56-bb6d-54cd89c7f93a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Handling Exceptions in an HPC Session
---

# Handling Exceptions in an HPC Session

In a distributed model, the client often cannot receive exceptions that occur in the service. However, HPC sessions do provide exception propagation, making it possible for service faults to be caught and processed by the client application.

To enable exception propagation, include the following attribute on the class declaration that implements the service.

`[ServiceBehavior(IncludeExceptionDetailInFaults = true)]`

For example,


```CSharp
    [ServiceBehavior(IncludeExceptionDetailInFaults = true)]
    public class EchoService : IEchoService
    {
        . . .
    }
```



 

 



