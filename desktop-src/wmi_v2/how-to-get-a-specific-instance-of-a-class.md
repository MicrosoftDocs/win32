---
title: How to Get a Specific Instance of a Class (C\ )
description: This topic provides step-by-step instructions for getting a specific (keyed) instance of a specified CIM class using the Windows Management Infrastructure (MI) .NET API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '87CB7DAB-1BF0-40C8-955C-F3D0A0B2012E'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# How to: Get a Specific Instance of a Class (C#)

This topic provides step-by-step instructions for getting a specific (keyed) instance of a specified CIM class using the [Windows Management Infrastructure (MI) .NET API](Http://Go.Microsoft.Com/FWLink/p/?LinkID=308910). In addition to the steps, a full source code example is provided at the end of the topic.

> [!Note]  
> To see the native [MI API](Http://Go.Microsoft.Com/FWLink/p/?LinkID=308914) and Microsoft Visual C++ version of this topic, refer to [How to: Get a Specific Instance of a Class (C/C++)](how-to--get-a-specific-instance-of-a-class--c-c---.md)

 

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

    

4.  Instantiate a [**CimInstance**](Microsoft.Management.Infrastructure.CimInstance) object using the CIM class name. For purposes of this topic, that object will be referred to as the "search instance". The search instance will ultimately contain the key values with which to search for a specific instance of the class passed to the **CimInstance** constructor ([**Win32\_Process**](https://msdn.microsoft.com/library/aa394372), in this example).

    ```CSharp
    CimInstance searchInstance = new CimInstance(cimClassName);
    ```

    

5.  In order to get a specific instance of a class by its key value(s), you must first determine the class's key properties and then specify the desired values for those key properties. The following code instantiates a [**CimClass**](Microsoft.Management.Infrastructure.CimClass) object using the desired class name ([**Win32\_Process**](https://msdn.microsoft.com/library/aa394372), in this example) and then uses a simple LINQ query to obtain all the key properties for that class. (You might need to add a using statement for the **System.Linq** namespace.) This step is optional if you already know the key values and will add them directly in step 7.0

    ```CSharp
    CimClass cimClass = cimSession.GetClass(cimNamespace, cimClassName);
    var keyProperties = from p in cimClass.CimClassProperties 
                        where ((p.Flags & CimFlags.Key) == CimFlags.Key) 
                        select p;
    ```

    

6.  Once the key properties for the desired class have been obtained, you need to get a value for each of the key properties. The following code loops through those key properties, querying the user for a value associated with each key, and adding the **propertyName**/**value** pair to a [Dictionary](Http://Go.Microsoft.Com/FWLink/p/?LinkID=313110) object. This step is optional if you already know the key values and will add them directly in step 7.

    ```CSharp
    Dictionary<string, object> propertyValues = new Dictionary<string, object>();
    foreach (CimPropertyDeclaration keyProperty in keyProperties)
    {
      Console.Write(String.Format("Please type Key value for Property '{0}' of Type:({1}): ",
                                  keyProperty.Name, keyProperty.CimType));
      propertyValues.Add(keyProperty.Name, Console.ReadLine());
    }
    ```

    

7.  Add each property key and value obtained in the previous step to the "search instance".

    ```CSharp
    if (propertyValues != null &amp;&amp; propertyValues.Count > 0)
    {
      foreach (var property in propertyValues)
      {
        searchInstance.CimInstanceProperties.Add(CimProperty.Create(property.Key, property.Value, CimFlags.Key));
      }
    }
    ```

    

8.  Once the "search instance" is populated, call the [**CimSession.GetInstance**](Microsoft.Management.Infrastructure.CimSession.GetInstance) method to retrieve the instanced identified by the specified key values.

    ```CSharp
    if (searchInstance != null)
    {
      CimInstance cimInstance = cimSession.GetInstance(cimNamespace, searchInstance);

      // Use the instance
      Console.WriteLine("Process name: {0}", 
                        cimInstance.CimInstanceProperties["Name"].Value.ToString());
    }
    ```

    

## Example

The following code sample enables the user to specify the desired key for the [**Win32\_Process**](https://msdn.microsoft.com/library/aa394372) class (which represents active processes) on the local machine, and if found, prints the name of process.

> [!Note]  
> In a real application you would define as parameters the computer name ("localhost"), CIM namespace ("root\\cimv2"), and class name ("Win32\_Process"). For purposes of simplicity, these have been hardcoded in this example.

 


```CSharp
using System;
using System.Collections.Generic;
using Microsoft.Management.Infrastructure;
using System.Linq;

public partial class MI
{
    static Dictionary<string, object> GetKeyPropertiesAndValues(CimSession cimSession, string cimNamespace, string cimClassName)
    {
        Dictionary<string, object> propertyValues = new Dictionary<string, object>();

        CimClass cimClass = cimSession.GetClass(cimNamespace, cimClassName);
        var keyProperties = from p in cimClass.CimClassProperties 
                            where ((p.Flags & CimFlags.Key) == CimFlags.Key) 
                            select p;

        foreach (CimPropertyDeclaration keyProperty in keyProperties)
        {
            Console.Write(String.Format("Please type Key value for Property '{0}' of Type:({1}): ",
                                        keyProperty.Name, keyProperty.CimType));
            propertyValues.Add(keyProperty.Name, Console.ReadLine());
        }

        return propertyValues;
    }
    static CimInstance CreateSearchInstance(CimSession cimSession, string cimNamespace, string cimClassName)
    {
        CimInstance searchInstance = new CimInstance(cimClassName);

        Dictionary<string, object> propertyValues = GetKeyPropertiesAndValues(cimSession, cimNamespace, cimClassName);
        if (propertyValues != null &amp;&amp; propertyValues.Count > 0)
        {
            foreach (var property in propertyValues)
            {
                searchInstance.CimInstanceProperties.Add(CimProperty.Create(property.Key, 
                                                                            property.Value, 
                                                                            CimFlags.Key));
            }
        }

        return searchInstance;
    }

    public static void GetInstance()
    {
        string cimNamespace = @"root\cimv2";
        string cimClassName = "Win32_Process";

        try
        {
            CimSession cimSession = CimSession.Create("localhost");
            CimInstance searchInstance = CreateSearchInstance(cimSession, cimNamespace, cimClassName);
            if (searchInstance != null)
            {
                CimInstance cimInstance = cimSession.GetInstance(cimNamespace, searchInstance);

                // Use the instance
                Console.WriteLine("Process name: {0}", 
                                  cimInstance.CimInstanceProperties["Name"].Value.ToString());
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



 

 




