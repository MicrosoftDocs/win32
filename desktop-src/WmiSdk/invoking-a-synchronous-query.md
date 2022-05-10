---
description: A synchronous query is a query that maintains control over the process of your application for the duration of the query.
ms.assetid: 628e9a31-7b0d-4099-bfa5-56330bb4eb6b
ms.tgt_platform: multiple
title: Invoking a Synchronous Query
ms.topic: article
ms.date: 05/31/2018
---

# Invoking a Synchronous Query

A synchronous query is a query that maintains control over the process of your application for the duration of the query. A synchronous query requires a single interface call, and is therefore more simple than an asynchronous call. However, a synchronous query has the potential of locking up your application for large queries or queries over a network.

The following procedure describes how to issue a synchronous data query using PowerShell.

**To issue a synchronous data query in PowerShell**

-   Describe your query to WMI using the WMI [Get-WmiObject](/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-5.1) cmdlet and the *-query* parameter. The cmdlet returns either a single object, or a collection of objects, depending on how many objects fit the query.

    ```PowerShell
    Get-WmiObject -query "SELECT * FROM Win32_logicalDisk WHERE DeviceID = 'C:'"
    ```

    

The following procedure describes how to issue a synchronous data query using C#.

**To issue a synchronous data query in C# (Microsoft.Management.Infrastructure)**

1.  Describe your query to WMI using CimSession.QueryInstances. This method returns a collection of CimInstance objects.

    ```CSharp
    using Microsoft.Management.Infrastructure;
    ...
    string Namespace = @"root\cimv2";
    string diskDriveQuery = "SELECT * FROM Win32_LogicalDisk";
    CimSession mySession = CimSession.Create("localhost");
    IEnumerable<CimInstance> queryInstances = mySession.QueryInstances(Namespace, "WQL", diskDriveQuery);
    ```

    

2.  Use standard C# language collection techniques to access each returned object.

    ```CSharp
    foreach (CimInstance drive in queryInstances)
    {
       Console.WriteLine(drive.CimInstanceProperties["DeviceID"]);
    }
    ```

    

The following procedure describes how to issue a synchronous data query using C#.

**To issue a synchronous data query in C# (System.Management)**

1.  Create the query with a [ManagementObjectSearcher](/dotnet/api/system.management.managementobjectsearcher) object, and retrieve the information with a call to [ManagementObjectSearcher.Get](/dotnet/api/system.management.managementobjectsearcher.get#System_Management_ManagementObjectSearcher_Get).

    This method returns a [ManagementObjectCollection](/dotnet/api/system.management.managementobjectcollection) object.

    ```CSharp
    using System.Management;
    ...
    ManagementObjectSearcher mgmtObjSearcher = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk");
    ManagementObjectCollection objCol = mgmtObjSearcher.Get();
    ```

    

2.  Use standard C# language collection techniques to access each returned object.

    ```CSharp
    foreach (ManagementObject drive in objCol)
    {
       Console.WriteLine(drive["DeviceID"]);
    }
    ```

    

The following procedure describes how to issue a synchronous data query using VBScript.

**To issue a synchronous data query in VBScript**

1.  Describe your query to WMI using [**SWbemServices.ExecQuery**](swbemservices-execquery.md). This method returns an [**SWbemObjectSet**](swbemobjectset.md).

    ```VB
    GetObject("winmgmts:").ExecQuery _
            ("Select * from Win32_Service where State='Stopped'")
    ```

    

2.  Use standard scripting language [collection](accessing-a-collection.md) techniques to access each returned object.

    ```VB
    for each Service in _ 
        GetObject("winmgmts:").ExecQuery _
            ("Select * from Win32_Service where State='Stopped'")
        WScript.Echo "  "& Service.DisplayName & " [", Service.Name, "]"
    next
    ```

    

The following procedure describes how to issue a synchronous data query using C++.

**To issue a synchronous query in C++**

1.  Describe your query to WMI through a call to [**IWbemServices::ExecQuery**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execquery).

    The [**ExecQuery**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execquery) method takes a WQL search string as a parameter that describes your query. WMI performs the query and returns an [**IEnumWbemClassObject**](/windows/desktop/api/Wbemcli/nn-wbemcli-ienumwbemclassobject) interface pointer. Through the **IEnumWbemClassObject** interface, you can access the classes or instances that make up the result set.

2.  After you receive your query, you can enumerate your query with a call to [**IEnumWbemClassObject::Next**](/windows/desktop/api/Wbemcli/nf-wbemcli-ienumwbemclassobject-next). For more information, see [Enumerating WMI](enumerating-wmi.md).

    The following code example requires the following references and \#include statements to compile correctly.

    ```C++
    #include <wbemidl.h>
    #include <iostream>
    using namespace std;
    ```

    

    The following code example describes how to query for the objects that represent the users and groups in WMI.

    ```C++
    void ExecQuerySync(IWbemServices *pSvc)
    {
        // Query for all users and groups.

        BSTR Language = SysAllocString(L"WQL");
        BSTR Query = SysAllocString(L"SELECT * FROM __Namespace");

        // Initialize the IEnumWbemClassObject pointer.
        IEnumWbemClassObject *pEnum = 0;

        // Issue the query.
        HRESULT hRes = pSvc->ExecQuery(
            Language,
            Query,
            WBEM_FLAG_FORWARD_ONLY,         // Flags
            0,                              // Context
            &pEnum
            );

        SysFreeString(Query);
        SysFreeString(Language);

        if (hRes != 0)
        {
            printf("Error\n");
            return;
        }
        
        ULONG uTotal = 0;

        // Retrieve the objects in the result set.
        for (;;)
        {
            IWbemClassObject *pObj = 0;
            ULONG uReturned = 0;

            hRes = pEnum->Next(
                0,                  // Time out
                1,                  // One object
                &pObj,
                &uReturned
                );

            uTotal += uReturned;

            if (uReturned == 0)
                break;

            // Use the object.
            
            // ...
            
            // Release it.
            // ===========
            
            pObj->Release();    // Release objects not owned.            
        }

        // All done.
        pEnum->Release();
    }
    ```

    

 

 
