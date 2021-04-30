---
description: The most common means of updating a WMI class instance is to update the entire instance at once.
ms.assetid: fca5f102-0823-4900-b147-9b29ca036607
ms.tgt_platform: multiple
title: Updating an Entire Instance
ms.topic: article
ms.date: 05/31/2018
---

# Updating an Entire Instance

The most common means of updating a WMI class instance is to update the entire instance at once. By updating an entire instance, WMI does not have to parse the instance into individual properties and send them to your application. Instead, WMI can simply send you the entire instance. When you finish, WMI can then copy your entire changed instance over the original instance.

The following procedure describes how to modify or update an instance using PowerShell.

**To modify or update an instance using PowerShell**

1.  Retrieve a local copy of the object with a call to Get-WmiObject.

    ```PowerShell
    $mySettings = get-WMIObject Win32_WmiSetting
    ```

    

2.  If necessary, view the properties of the object with a call to the Properties collection.

    Although not required, you may wish to know the value of the property before you change it.

    ```PowerShell
    $mySettings.Properties
    ```

    

3.  Make any changes to the local object properties.

    Doing so changes only the local copy. To save your changes to WMI, you must place the entire copy back into the WMI repository.

    ```PowerShell
    $mySettings.LoggingLevel = 1
    ```

    

4.  Place the object back into the WMI repository using a call to the Put method.

    ```PowerShell
    $mySettings.Put()
    ```

    

The following procedure describes how to modify or update an instance using C#.

**To modify or update an instance using C# (Microsoft.Management.Infrastructure)**

1.  Retrieve a local copy of the object with a call to [CimSession.GetInstance](/previous-versions/windows/desktop/wmi_v2/mi-managed-api/hh832585(v=vs.85)), as described in [Retrieving a WMI Instance](retrieving-an-instance.md).

    ```CSharp
    using Microsoft.Management.Infrastructure;
    ...
    string Namespace = @"root\cimv2";
    string className = "win32_logicalDisk";

    CimInstance diskDrive = new CimInstance(className, Namespace);
    diskDrive.CimInstanceProperties.Add(CimProperty.Create("DeviceID", "C:", CimFlags.Key));

    CimSession session = CimSession.Create("localhost");
    CimInstance myDisk = session.GetInstance(Namespace, diskDrive);
    ```

    

2.  If necessary, view the properties of the object with a call to the Properties collection.

    Although not required, you may wish to know the value of the property before you change it.

    ```CSharp
    foreach (CimProperty property in myDisk.CimInstanceProperties)
    {
       Console.WriteLine(property.ToString());
    }

    Console.ReadLine();
    ```

    

3.  Make any changes to the local object properties.

    Doing so changes only the local copy. To save your changes to WMI, you must place the entire copy back into the WMI repository.

    ```CSharp
    myDisk.CimInstanceProperties["VolumeName"].Value = "NewName";
    ```

    

4.  Place the object back into the WMI repository using a call to [CimSession.ModifyInstance](/previous-versions/windows/desktop/wmi_v2/mi-managed-api/hh832593(v=vs.85)).

    ```CSharp
    session.ModifyInstance(Namespace,myDisk);
    ```

    

The following procedure describes how to modify or update an instance using PowerShell.

> [!Note]  
> **System.Management** was the original .NET namespace used to access WMI; however, the APIs in this namespace generally are slower and do not scale as well relative to their more modern **Microsoft.Management.Infrastructure** counterparts.

 

**To modify or update an instance using C# (Microsoft.Management)**

1.  Retrieve a local copy of the object with a call to [ManagementObject.Get](/dotnet/api/system.management.managementobject.get#System_Management_ManagementObject_Get).

    ```CSharp
    using System.Management;
    ...
    ManagementObject myDisk = new ManagementObject("Win32_LogicalDisk.DeviceID='C:'");
    myDisk.Get();
    ```

    

2.  If necessary, view the properties of the object with a call to the Properties collection.

    Although not required, you may wish to know the value of the property before you change it.

    ```CSharp
    foreach (PropertyData property in myDisk.Properties)
    {
       Console.WriteLine(property.Name + " " + property.Value);
    }

    Console.ReadLine();
    ```

    

3.  Make any changes to the local object properties.

    Doing so changes only the local copy. To save your changes to WMI, you must place the entire copy back into the WMI repository.

    ```CSharp
    myDisk["VolumeName"] = "newName";
    ```

    

4.  Place the object back into the WMI repository using a call to the [ManagementObject.Put](/dotnet/api/system.management.managementobject.put#System_Management_ManagementObject_Put) or method.

    ```CSharp
    myDisk.Put();
    ```

    

The following procedure describes how to modify or update an instance using VBScript.

**To modify or update an instance using VBScript**

1.  Retrieve a local copy of the object with a call to **GetObject**.
2.  If necessary, view the properties of the object with a call to the [**Properties\_**](swbemobject-properties-.md) method.

    Although not required, you may wish to know the value of the property before you change it.

3.  Make any changes to the object properties with a call to the [**SWbemProperty.Value**](swbemproperty-value.md) method.

    The **Value** method changes only the local copy. To save your changes to WMI, you must place the entire copy back into the WMI repository.

4.  Place the object back into the WMI repository with a call the [**SWbemObject.Put\_**](swbemobject-put-.md) or [**SWbemObject.PutAsync\_**](swbemobject-putasync-.md) methods.

As the names imply, [**Put\_**](swbemobject-put-.md) updates synchronously while [**PutAsync\_**](swbemobject-putasync-.md) updates asynchronously. Either method copies over the original instance with your modified instance. However, to take advantage of asynchronous processing, you must create an [**SWbemSink**](swbemsink.md) object. For more information, see [Calling a method](calling-a-method.md).

The following procedure describes how to modify or update an instance using C++.

**To modify or update an instance using C++**

1.  Retrieve a local copy of the instance with a call to [**IWbemServices::GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject) or [**IWbemServices::GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync).
2.  If necessary, view the properties of the object with a call to [**IWbemClassObject::Get**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-get).

    Although not required, you may wish to know the value of the property before you change it.

3.  Make any necessary changes to the copy with a call to [**IWbemClassObject::Put**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemclassobject-put).

    The **Put** method changes only the local copy. To save your changes to WMI, you must place the entire copy back into the WMI repository.

4.  Place your copy back into the WMI repository with a call the [**IWbemServices::PutInstance**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putinstance) or [**IWbemServices::PutInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync) methods.

    As the names imply, **PutInstance** updates synchronously while [**PutInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync) updates asynchronously. Either method copies over the original instance with your modified instance. However, to take advantage of asynchronous processing, you must implement the [**IWbemObjectSink**](iwbemobjectsink.md) interface.

    You should be aware that an update operation on an instance belonging to a class hierarchy might not succeed due to an error involving another class in the hierarchy. WMI calls the [**PutInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync) method of each of the providers responsible for the classes from which the class owning the original instance derives. If any of these providers fail, the original update request fails. For more information, see the Remarks section of [**PutInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync).

For more information, see [Calling a Provider Method](calling-a-provider-method.md).

> [!Note]  
> Because the callback to the sink might not be returned at the same authentication level as the client requires, it is recommended that you use semisynchronous instead of asynchronous communication. For more information, see [Calling a Method](calling-a-method.md).

 

 

 
