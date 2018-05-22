---
title: How to Enumerate All Instances of a Class (C\ )
description: This topic provides step-by-step instructions for enumerating the instances of a specified CIM class using the Windows Management Infrastructure (MI) .NET API. In addition to the steps, a full source code example is provided at the end of the topic.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '08197FE4-E7A9-4AE6-890E-55AEBBF047BC'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# How to: Enumerate All Instances of a Class (C#)

This topic provides step-by-step instructions for enumerating the instances of a specified CIM class using the [Windows Management Infrastructure (MI) .NET API](Http://Go.Microsoft.Com/FWLink/p/?LinkID=308910). In addition to the steps, a full source code example is provided at the end of the topic.

> [!Note]  
> To see the native [MI API](Http://Go.Microsoft.Com/FWLink/p/?LinkID=308914) and Microsoft Visual C++ version of this topic, refer to [How to: Enumerate All Instances of a Class (C/C++)](how-to--enumerate-all-instances-of-a-class.md)

 

## Step-by-step Instructions

1.  Add a reference to the **Microsoft.Management.Infrastructure** reference assembly. (This assembly ships as part of the [Windows Software Development Kit (SDK) for Windows 8](Http://Go.Microsoft.Com/FWLink/p/?LinkID=306595).)
2.  Add a **using** statement for the **Microsoft.Management.Infrastructure** namespace.

    ```CSharp
    using Microsoft.Management.Infrastructure;
    ```

    

3.  Instantiate a [CimSession](https://msdn.microsoft.com/library/microsoft.management.infrastructure.cimsession.aspx) object. The following snippet uses the standard "localhost" value for the [**CimSession.Create**](Overload:Microsoft.Management.Infrastructure.CimSession.Create) method.

    ```CSharp
    CimSession cimSession = CimSession.Create("localhost");
    ```

    

4.  Call the [**CimSession.EnumerateInstances**](Microsoft.Management.Infrastructure.CimSession.EnumerateInstances) method passing the desired CIM namespace and class whose instances you want to enumerate. The following snippet enumerates the instances of the [**Win32\_Process**](https://msdn.microsoft.com/library/aa394372) class. (You'll need to add a using statement for the **System.Collections.Generic** namespace so that the compiler can locate the [IEnumerable](Http://Go.Microsoft.Com/FWLink/p/?LinkID=313091) type information.)

    ```CSharp
    IEnumerable<CimInstance> enumeratedInstances = 
      cimSession.EnumerateInstances(@"root\cimv2", "Win32_Process");
    ```

    

5.  Loop through the returned [**CimInstance**](Microsoft.Management.Infrastructure.CimInstance) objects.

    ```CSharp
    foreach (CimInstance cimInstance in enumeratedInstances)
    { /* access desired CimInstance members */ }
    ```

    

## Example

The following code sample enumerates all instances of the [**Win32\_Process**](https://msdn.microsoft.com/library/aa394372) class (which represents active processes) on the local machine, and prints the name of each process.

> [!Note]  
> In a real application you would define as parameters the computer name ("localhost"), CIM namespace ("root\\cimv2"), and class name ("Win32\_Process"). For purposes of simplicity, these have been hardcoded in this example.

 


```CSharp
using System;
using System.Collections.Generic;
using Microsoft.Management.Infrastructure;

public partial class MI
{
    public static void EnumerateInstances()
    {
        try
        {
            CimSession cimSession = CimSession.Create("localhost");
            IEnumerable<CimInstance> enumeratedInstances = 
                cimSession.EnumerateInstances(@"root\cimv2", "Win32_Process");
            foreach (CimInstance cimInstance in enumeratedInstances)
            {
                Console.WriteLine("{0}", cimInstance.CimInstanceProperties["Name"].Value.ToString());
            }
        }
        catch (CimException ex) 
        { 
            // Handle the exception as appropriate.
            // This example prints the message.
            Console.WriteLine(ex.Message); 
        }
    }
}
```



 

 




