---
title: How to Query for Specific Instances of a Class (C\ )
description: This topic provides step-by-step instructions for querying instances of a class with WQL (WMI Query Language) using the Windows Management Infrastructure (MI) .NET API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 607010ED-7ADE-420B-873E-F9DF0ECE6B40
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to: Query for Specific Instances of a Class (C#)

This topic provides step-by-step instructions for querying instances of a class with [WQL (WMI Query Language)](Http://Go.Microsoft.Com/FWLink/p/?LinkID=313225) using the [Windows Management Infrastructure (MI) .NET API](Http://Go.Microsoft.Com/FWLink/p/?LinkID=308910). In addition to the steps, a full source code example is provided at the end of the topic.

> [!Note]  
> To see the native [MI API](Http://Go.Microsoft.Com/FWLink/p/?LinkID=308914) and Microsoft Visual C++ version of this topic, refer to [How to: Query for Specific Instances of a Class (C/C++)](how-to--query-for-specific-instances-of-a-class--c-c---.md)

 

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

    

4.  Call the [**CimSession.QueryInstances**](https://www.bing.com/search?q=**CimSession.QueryInstances**) method passing the desired CIM namespace and WQL to use. The following snippet will return two instances representing two standard Windows processes where the handle property (representing a process ID, or PID) has a value of either 0 or 4.

    ```CSharp
    IEnumerable<CimInstance> queryInstances =     
      cimSession.QueryInstances(@"root\cimv2", 
                                "WQL", 
                                @"select name from win32_process where handle = 0 or handle = 4");
    ```

    

5.  Loop through the returned [**CimInstance**](https://www.bing.com/search?q=**CimInstance**) objects.

    ```CSharp
    foreach (CimInstance cimInstance in enumeratedInstances)
    { 
      Console.WriteLine("Process name: {0}", cimInstance.CimInstanceProperties["Name"].Value);  
    }
    ```

    

## Example

The following code sample enumerates all instances of the [**Win32\_Process**](https://msdn.microsoft.com/library/aa394372) class (which represents active processes) on the local machine, and prints the name of each process.

> [!Note]  
> In a real application you would define as parameters the computer name ("localhost") and CIM namespace ("root\\cimv2"). For purposes of simplicity, these have been hardcoded in this example.

 


```CSharp
using System;
using System.Collections.Generic;
using Microsoft.Management.Infrastructure;

public partial class MI
{
    static void PrintCimInstance(CimInstance cimInstance)
    {
        Console.ForegroundColor = ConsoleColor.Blue;
        Console.WriteLine("{0} properties", cimInstance.CimSystemProperties.ClassName);
        Console.ResetColor();

        Console.WriteLine(String.Format("{0,-5}{1,-30}{2,-15}{3,-10}", 
                                        "Key?", "Property", "Type", "Value"));

        foreach (var enumeratedProperty in cimInstance.CimInstanceProperties)
        {
            bool isKey = ((enumeratedProperty.Flags & CimFlags.Key) == CimFlags.Key);

            if (enumeratedProperty.Value != null)
            {
                Console.WriteLine(
                    "{0,-5}{1,-30}{2,-15}{3,-10}",
                    isKey == true ? "Y" : string.Empty,
                    enumeratedProperty.Name,
                    enumeratedProperty.CimType,
                    enumeratedProperty.Value);
            }
        }
        Console.WriteLine();
    }

    public static void QueryInstance(string query)
    {
        try
        {
            CimSession cimSession = CimSession.Create("localhost");

            IEnumerable<CimInstance> queryInstances = 
              cimSession.QueryInstances(@"root\cimv2", "WQL", query);
            foreach (CimInstance cimInstance in queryInstances)
            {
                //Use the current instance. This example prints the instance. 
                PrintCimInstance(cimInstance);
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

<span codelanguage="CSharp"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C#</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>using System;

namespace MIClientManaged
{
    class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                Console.Write(&quot;Enter WQL (x = Quit): &quot;);
                string query = Console.ReadLine().ToUpper();
                if (query.CompareTo(&quot;X&quot;) == 0) break;
                MI.QueryInstance(query);
            }
        }
    }
}</code></pre></td>
</tr>
</tbody>
</table>



 

 




