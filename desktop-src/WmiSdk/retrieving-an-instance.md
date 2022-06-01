---
description: Retrieving an instance is one of the most common retrieval procedures you are likely to perform in WMI.
ms.assetid: c3258783-ffcd-4c40-aaf2-7c65617cf9f8
ms.tgt_platform: multiple
title: Retrieving a WMI Instance
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving a WMI Instance

Retrieving an instance is one of the most common retrieval procedures you are likely to perform in WMI. You can retrieve an existing instance or create a new unnamed instance. The WMI path to the existing instance is a required parameter. For more information, see [Describing the Location of a WMI Object](describing-the-location-of-a-wmi-object.md).

> [!Note]  
> When providing an instance, a provider may be unable to provide a value for certain properties. Unless otherwise stated in the property description, you cannot infer any meaning from an empty value. This is not to be confused with a string which has a **NULL** value. In this case, the value is populated. It is empty but has a value: **NULL**.

 

Retrieve a local copy of the instance with a call to the PowerShell [Get-WmiObject](/powershell/module/microsoft.powershell.management/get-wmiobject) cmdlet.

**To retrieve an instance of a WMI class using PowerShell**

-   You can retrieve specific instances using the *-class* and *-filter* parameters.

    ```PowerShell
    Get-WmiObject -query "SELECT * FROM Win32_logicalDisk WHERE DeviceID = 'C:'"
    ```

    

You can retrieve a WMI instance using C# by creating a search object using [CimInstance](/previous-versions/windows/desktop/wmi_v2/mi-managed-api/hh832336(v=vs.85)), and then filling it with the relevant key values, and then searching for that object with a [CimSession.GetInstance](/previous-versions/windows/desktop/wmi_v2/mi-managed-api/hh832585(v=vs.85)) call.

**To retrieve an instance of a WMI class using C# (Microsoft.Management.Infrastructure)**

1.  Using the [Microsoft.Management.Infrastructure](/previous-versions/windows/desktop/wmi_v2/mi-managed-api/hh832958(v=vs.85)) namespace, create a new [CimInstance](/previous-versions/windows/desktop/wmi_v2/mi-managed-api/hh832336(v=vs.85)) object with the relevant class name and namespace.

    ```CSharp
    using Microsoft.Management.Infrastructure;
    ...
    string Namespace = @"root\cimv2";
    string className = "Win32_LogicalDisk";

    CimInstance myDrive = new CimInstance(className, Namespace);
    ```

    

2.  Create a [CimProperty](/previous-versions/windows/desktop/wmi_v2/mi-managed-api/hh832461(v=vs.85)) that contains the name and value of the key property of the instance you wish to search for, and add that property to your class object.

    ```CSharp
    myDrive.CimInstanceProperties.Add(CimProperty.Create("DeviceID", "C:", CimFlags.Key));
    ```

    

3.  Retrieve the object from WMI with a [CimSession.GetInstance](/previous-versions/windows/desktop/wmi_v2/mi-managed-api/hh832585(v=vs.85)) call.

    ```CSharp
    CimSession mySession = CimSession.Create("localhost");
    CimInstance searchInstance = mySession.GetInstance(Namespace, myDrive);
    ```

    

You can retrieve either a specific WMI class instance, or a collection of WMI class instances, using classes in the [System.Management](/dotnet/api/system.management) namespace.

> [!Note]  
> **System.Management** was the original .NET namespace used to access WMI; however, the APIs in this namespace generally are slower and do not scale as well relative to their more modern **Microsoft.Management.Infrastructure** counterparts.

 

**To retrieve an instance of a WMI class using C# (System.Management)**

1.  Retrieve a local copy of a specific instance by creating a new [ManagementObject](/dotnet/api/system.management.managementobject), with the name and specific instance value passed in though the *ManagementPath* parameter. You can then retrieve the instance data by explicitly calling [ManagementObject.Get](/dotnet/api/system.management.managementobject.get#System_Management_ManagementObject_Get).

    ```CSharp
    using System.Management;
    ...
    ManagementObject objInst = new ManagementObject("Win32_LogicalDisk.DeviceID='C:'");
    objInst.Get();
    ```

    

2.  Alternately, you can retrieve all instances of a WMI class by searching for them with a [ManagementObjectSearcher](/dotnet/api/system.management.managementobjectsearcher), and then enumerating through the returned [ManagementObjectCollection](/dotnet/api/system.management.managementobjectcollection).

    ```CSharp
    using System.Management;
    ...
    ManagementObjectSearcher mgmtObjSearcher = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk");
    ManagementObjectCollection colDisks = mgmtObjSearcher.Get();

    foreach (ManagementObject objDisk in colDisks)
    {
       Console.WriteLine("Device ID : {0}", objDisk["DeviceID"]);
    }

    Console.ReadLine();
    ```

    

    You can implicitly call the **Get** method by accessing the instance. For more information, see [Retrieving Part of a WMI Instance](retrieving-part-of-an-instance.md).

Retrieve a local copy of the instance with a call to the VBScript [**GetObject**](https://msdn.microsoft.com/library/e9waz863(v=VS.71).aspx) method.

**To retrieve an instance of a WMI class using VBScript**

-   Call [**GetObject**](https://msdn.microsoft.com/library/e9waz863(v=VS.71).aspx) with the object path of the instance as shown in the following example.

    ```VB
    Set objinst = GetObject("WinMgmts:Win32_LogicalDisk='C:'")
    ```

    

    Retrieving a specific instance requires giving a name as part of the object path.

In C++, call [**IWbemServices::GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject).

**To retrieve an instance of a WMI class using C++**

-   Retrieve a local copy of the instance with a call to [**IWbemServices::GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject) or [**IWbemServices::GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync). The WMI path to the object must be included.

    As the name implies, [**GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync) retrieves the instance asynchronously, while [**GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject) retrieves the instance synchronously. If you want to use asynchronous retrieval, you must implement the [**IWbemObjectSink**](iwbemobjectsink.md) interface.

## Examples

For a VBScript example to use as a template to retrieve class and instance information, see the [WMI Template Script](https://Gallery.TechNet.Microsoft.Com/aded1ef3-d2af-4821-8a92-b5c22ca2ecd8) example on TechNet Gallery. This particular example uses GetObject to retrieve the WMI Service.

 

 
