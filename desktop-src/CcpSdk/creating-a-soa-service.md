---
Description: 'A service is an interface that includes the ServiceContract attribute. The interface must expose at least one member that includes the OperationContract attribute.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ae527364-4251-4a82-80e0-213ee3ad2092'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Creating a SOA Service
---

# Creating a SOA Service

A service is an interface that includes the **ServiceContract** attribute. The interface must expose at least one member that includes the **OperationContract** attribute.

The following example shows a simple service implementation. For information on creating a client that sends requests to the service, see [Creating a SOA Client](creating-a-soa-client.md).


```CSharp
using System;
using System.Collections.Generic;
using System.Text;
using System.Diagnostics;
using System.ServiceModel;

namespace EchoService
{
    // Interface that defines the service.

    [ServiceContract]
    public interface IEchoService
    {
        [OperationContract]
        string Echo(string input);
    }

    // Class that implements the service interface.

    [ServiceBehavior(IncludeExceptionDetailInFaults = true)]
    public class EchoService : IEchoService
    {
        public string Echo(string input)
        {
            return Environment.MachineName + ": " + input;
        }
    }
}
```



 

 



