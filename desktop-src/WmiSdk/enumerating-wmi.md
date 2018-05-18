---
Description: 'Enumeration is the act of moving through a set of objects and possibly modifying each object as you do so.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'fe7e3259-9a7c-4f73-af30-192bbbace1b3'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Enumerating WMI
---

# Enumerating WMI

Enumeration is the act of moving through a set of objects and possibly modifying each object as you do so. For example, you can enumerate through a set of [**Win32\_DiskDrive**](https://msdn.microsoft.com/library/aa394132) objects to find a particular serial number. Note that although you can enumerate any object, WMI only returns objects to which you have security access.

Enumerations of large data sets can require a large amount of resources and degrade performance. For more information, see [Improving Enumeration Performance](improving-enumeration-performance.md). You also can request data with a more specific query. For more information, see [Querying WMI](querying-wmi.md).

The following sections are discussed in this topic:

-   [Enumerating WMI Using PowerShell](#enumerating-wmi-using-powershell)
-   [Enumerating WMI Using C# (Microsoft.Management.Infrastructure)](#enumerating-wmi-using-c-microsoftmanagementinfrastructure)
-   [Enumerating WMI Using C# (System.Management)](#enumerating-wmi-using-c-systemmanagement)
-   [Enumerating WMI Using VBScript](#enumerating-wmi-using-vbscript)
-   [Enumerating WMI Using C++](#enumerating-wmi-using-c-microsoftmanagementinfrastructure)

## Enumerating WMI Using PowerShell

If you do not know the object path for a specific instance, or you want to retrieve all the instances for a specific class, use [Get-WmiObject](https://technet.microsoft.com/library/dd315379.aspx), with the name of the class in the *-class* parameter. If you want to use a query, you can use the *-query* parameter.

The following procedure describes how to enumerate the instances of a class using PowerShell.

**To enumerate the instances of a class using PowerShell**

1.  Enumerate the instances with a call to [Get-WmiObject](https://technet.microsoft.com/library/dd315379.aspx) cmdlet.

    [Get-WmiObject](https://technet.microsoft.com/library/dd315379.aspx) returns a collection of one or more WMI objects, through which you can enumerate. For more information, see [Accessing a Collection](accessing-a-collection.md).

    If you wish to retrieve a WMI class instance in another namespace or on a different computer, specify the computer and namespace in the *-computer* and *-namespace* parameters, respectively. For more information, see [Creating a WMI Script](creating-a-wmi-script.md). This only works if you have the appropriate access privileges. For more information, see [Maintaining WMI Security](maintaining-wmi-security.md) and [Executing Privileged Operations](executing-privileged-operations.md).

2.  Retrieve any individual instances you wish using the collection's members.

The following code example retrieves an PowerShell collection and then displays the size property for all instances of logical drives on the local computer.


```PowerShell
$objCol = get-wmiobject -class "Win32_LogicalDisk"

# Or, alternately
#$objCol = get-wmiobject -Query "SELECT * FROM Win32_LogicalDisk"

foreach ($Drive in $objCol)
{
    if ($Drive.size -ne $null)
    { "Drive " + $Drive.deviceID + " contains " + $Drive.size + " bytes" }
    else
    { "Drive " + $Drive.deviceID + " is not available." }
}
```



## Enumerating WMI Using C# (Microsoft.Management.Infrastructure)

1.  Add a reference to the **Microsoft.Management.Infrastructure** reference assembly. (This assembly ships as part of the [Windows Software Development Kit (SDK) for Windows 8](Http://Go.Microsoft.Com/FWLink/p/?LinkID=306595).)
2.  Add a **using** statement for the **Microsoft.Management.Infrastructure** namespace.

    ```CSharp
    using Microsoft.Management.Infrastructure;
    ```

    

3.  Instantiate a [CimSession](https://msdn.microsoft.com/library/microsoft.management.infrastructure.cimsession.aspx) object. The following snippet uses the standard "localhost" value for the [**CimSession.Create**](Overload:Microsoft.Management.Infrastructure.CimSession.Create) method.

    ```CSharp
    CimSession cimSession = CimSession.Create("localhost");
    ```

    

4.  Call the [**CimSession.QueryInstances**](Microsoft.Management.Infrastructure.CimSession.QueryInstances) method passing the desired CIM namespace and WQL to use. The following snippet will return two instances representing two standard Windows processes where the handle property (representing a process ID, or PID) has a value of either 0 or 4.

    ```CSharp
    IEnumerable<CimInstance> queryInstances =     
      cimSession.QueryInstances(@"root\cimv2", 
                                "WQL", 
                                @"select name from win32_process where handle = 0 or handle = 4");
    ```

    

5.  Loop through the returned [**CimInstance**](Microsoft.Management.Infrastructure.CimInstance) objects.

    ```CSharp
    foreach (CimInstance cimInstance in enumeratedInstances)
    { 
      Console.WriteLine("Process name: {0}", cimInstance.CimInstanceProperties["Name"].Value);  
    }
    ```

    

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



## Enumerating WMI Using C# (System.Management)

If you do not know the object path for a specific instance, or you want to retrieve all the instances for a specific class, use the [ManagementClass](https://msdn.microsoft.com/library/system.management.managementclass.aspx) object to retrieve a [ManagementObjectCollection](https://msdn.microsoft.com/library/system.management.managementobjectcollection.aspx) that contains all instances of a given class in the WMI namespace. Alternately, you can query WMI through a [ManagementObjectSearcher](https://msdn.microsoft.com/library/system.management.managementobjectsearcher.aspx) to obtain the same set of objects.

> [!Note]  
> **System.Management** was the original .NET namespace used to access WMI; however, the APIs in this namespace generally are slower and do not scale as well relative to their more modern **Microsoft.Management.Infrastructure** counterparts.

 

The following procedure describes how to enumerate the instances of a class using C#.

**To enumerate the instances of a class using C#**

1.  Enumerate the instances with a call to [ManagementClass.GetInstances](https://msdn.microsoft.com/library/ysw6xf4d.aspx).

    The [GetInstances](https://msdn.microsoft.com/library/ysw6xf4d.aspx) method returns a collection, or set, of objects through which you can enumerate. For more information, see [Accessing a Collection](accessing-a-collection.md). The returned collection is actually an [ManagementObjectCollection](https://msdn.microsoft.com/library/system.management.managementobjectcollection.aspx) object, so any of the methods of that object can be called.

    If you wish to retrieve a WMI class instance in another namespace or on a different computer, specify the computer and namespace in the *path* parameter. For more information, see [Creating a WMI Script](creating-a-wmi-script.md). This only works if you have the appropriate access privileges. For more information, see [Maintaining WMI Security](maintaining-wmi-security.md) and [Executing Privileged Operations](executing-privileged-operations.md).

2.  Retrieve any individual instances you wish using the collection's members.

The following code example retrieves an C# collection and then displays the size property for all instances of logical drives on the local computer.


```PowerShell
using System.Management;
...

ManagementClass mc = new ManagementClass("Win32_LogicalDisk");
ManagementObjectCollection objCol = mc.GetInstances();

//or, alternately
//ManagementObjectSearcher mgmtObjSearcher = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk");
//ManagementObjectCollection objCol = mgmtObjSearcher.Get();

if (objCol.Count != 0)
{
   foreach (ManagementObject Drive in objCol)
   {
      if (Drive["size"] != null)
      {
         Console.WriteLine("Drive {0} contains {1} bytes.", Drive["deviceID"], Drive["size"]);
      }
      else
      {
         Console.WriteLine("Drive {0} is not available.", Drive["deviceID"]);
      }
   }
}
Console.ReadLine();
```



## Enumerating WMI Using VBScript

If you do not know the object path for a specific instance, or you want to retrieve all the instances for a specific class, use the [**SWbemServices.InstancesOf**](swbemservices-instancesof.md) method to return an [**SWbemObjectSet**](swbemobjectset.md) enumeration of all the instances of a class. Alternatively you can query WMI through [**SWbemServices.ExecQuery**](swbemservices-execquery.md) to obtain the same set of objects.

The following procedure describes how to enumerate the instances of a class using VBScript.

**To enumerate the instances of a class using VBScript**

1.  Enumerate the instances with a call to the [**SWbemServices.InstancesOf**](swbemservices-instancesof.md) method.

    The [**InstancesOf**](swbemservices-instancesof.md) method returns a collection, or set, of objects through which you can enumerate. For more information, see [Accessing a Collection](accessing-a-collection.md). The returned collection is actually an [**SWbemObjectSet**](swbemobjectset.md) object, so any of the methods of that object can be called.

    If you wish to retrieve a WMI class instance in another namespace or on a different computer, specify the computer and namespace in the moniker. For more information, see [Creating a WMI Script](creating-a-wmi-script.md). This only works if you have the appropriate access privileges. For more information, see [Maintaining WMI Security](maintaining-wmi-security.md) and [Executing Privileged Operations](executing-privileged-operations.md).

2.  Retrieve any individual instances you wish using the collections methods.

The following code example retrieves an [**SWbemServices**](swbemservices.md) object and then executes the [**InstancesOf**](swbemservices-instancesof.md) method to display the size property for all instances of logical drives on the local computer.


```VB
Set objCol = GetObject("WinMgmts:").InstancesOf("Win32_LogicalDisk")
For Each Drive In objCol
    If Not IsNull(Drive.Size) Then    
       WScript.Echo ("Drive " & Drive.deviceid & " contains " & Drive.Size & " bytes")
    Else
       WScript.Echo ("Drive " & Drive.deviceid & " is not available.")
    End If
Next
```



## Enumerating WMI Using C++

In addition to performing basic enumeration, you can set several flags and properties to increase the performance of your enumeration. For more information, see [Improving Enumeration Performance](improving-enumeration-performance.md).

**To enumerate an object set in WMI**

1.  Create an [**IEnumWbemClassObject**](ienumwbemclassobject.md) interface describing the set of objects you wish to enumerate.

    An [**IEnumWbemClassObject**](ienumwbemclassobject.md) object contains a list describing a set of WMI objects. You can use the **IEnumWbemClassObject** methods to enumerate forwards, skip objects, begin at the beginning, and copy the enumerator. The following table lists the methods use to create enumerators for different types of WMI objects.

    

    <table>
    <thead>
    <tr class="header">
    <th>Object</th>
    <th>Method</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td>Class</td>
    <td><dl>[<strong>IWbemServices::CreateClassEnum</strong>](iwbemservices-createclassenum.md)<br />
    [<strong>IWbemServices::CreateClassEnumAsync</strong>](iwbemservices-createclassenumasync.md)<br />
    </dl></td>
    </tr>
    <tr class="even">
    <td>Instance</td>
    <td><dl>[<strong>IWbemServices::CreateInstanceEnum</strong>](iwbemservices-createinstanceenum.md)<br />
    [<strong>IWbemServices::CreateInstanceEnumAsync</strong>](iwbemservices-createinstanceenumasync.md)<br />
    </dl></td>
    </tr>
    <tr class="odd">
    <td>Query result</td>
    <td><dl>[<strong>IWbemServices::ExecQuery</strong>](iwbemservices-execquery.md)<br />
    [<strong>IWbemServices::ExecQueryAsync</strong>](iwbemservices-execqueryasync.md)<br />
    </dl></td>
    </tr>
    <tr class="even">
    <td>Event notification</td>
    <td><dl>[<strong>IWbemServices::ExecNotificationQuery</strong>](iwbemservices-execnotificationquery.md)<br />
    [<strong>IWbemServices::ExecNotificationQueryAsync</strong>](iwbemservices-execnotificationqueryasync.md)<br />
    </dl></td>
    </tr>
    </tbody>
    </table>

    

     

2.  Traverse through the returned enumeration using multiple calls to [**IEnumWbemClassObject::Next**](ienumwbemclassobject-next.md) or [**IEnumWbemClassObject::NextAsync**](ienumwbemclassobject-nextasync.md).

For more information, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md).

 

 



