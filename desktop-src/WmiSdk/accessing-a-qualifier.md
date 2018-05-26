---
Description: A qualifier is a tag that provides more information about a WMI object, method, or property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 53a307da-2e81-4361-876a-16b51484512e
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Accessing a WMI Qualifier
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Accessing a WMI Qualifier

A qualifier is a tag that provides more information about a WMI object, method, or property. At times, you may need to access the data stored in a qualifier. For example, a common task is to determine if a provider implements a method by attempting to retrieve the **Implemented** qualifier for that method. For more information, see [WMI Qualifiers](wmi-qualifiers.md) and [Adding a Qualifier](adding-a-qualifier.md).

You can retrieve the qualifiers on a WMI object in PowerShell by first retrieving the object, and then examining the qualifiers as you would any other property.

**To retrieve a qualifier using PowerShell**

-   Retrieve the object whose qualifiers you want to view using [Get-WmiObject](https://technet.microsoft.com/library/dd315379.aspx), and then access the qualifiers through the **Qualifiers** property:

    ```PowerShell
    $myDisk = get-wmiObject Win32_LogicalDisk
    $myDisk.qualifiers

    #or

    get-wmiObject Win32_LogicalDisk | format-list qualifiers

    #or

    $myDisk = get-wmiObject Win32_LogicalDisk
    foreach ($qual in $myDisk.Qualifiers)
    { $qual }
    ```

    

    For more information, see [Retrieving a WMI Instance](retrieving-an-instance.md).

You can retrieve the qualifiers on a WMI instance in C# by first retrieving the object, and then examining the qualifiers as a collection.

**To retrieve a qualifier using C# (Microsoft.System.Management)**

1.  Retrieve the class whose qualifiers you want to view by creating a CimInstance object, using the specified class name and namespace.

    ```CSharp
    using Microsoft.Management.Infrastructure;
    ...
    CimSession mySession = CimSession.Create("localhost");
    CimInstance diskDrive = new CimInstance(className, Namespace);
    diskDrive.CimInstanceProperties.Add(CimProperty.Create("DeviceID", "C:", CimFlags.Key));
    CimInstance myDrive = mySession.GetInstance(Namespace, diskDrive);
    ```

    

    For more information, see [Retrieving a WMI Instance](retrieving-an-instance.md).

2.  You can retrieve the class qualifiers from the [CimInstance.CimClass.CimClassQualifiers](https://msdn.microsoft.com/library/microsoft.management.infrastructure.cimclass.cimclassqualifiers.aspx), the property qualifiers from [CimInstance.CimClass.CimClassProperties](https://msdn.microsoft.com/library/microsoft.management.infrastructure.cimclass.cimclassproperties.aspx), and the method qualifiers from [CimInstance.CimClass.CimClassMethods](https://msdn.microsoft.com/library/microsoft.management.infrastructure.cimclass.cimclassmethods.aspx).

    ```CSharp
    Console.WriteLine("Class: " + myDrive.ToString());
    foreach (CimQualifier qualifier in myDrive.CimClass.CimClassQualifiers)
    {
       Console.WriteLine("     " + qualifier.Name.ToString() + ": " + qualifier.Value.ToString());
    }

    foreach (CimPropertyDeclaration property in myDrive.CimClass.CimClassProperties)
    {
       Console.WriteLine(property.Name.ToString());
       foreach (CimQualifier qualifier in property.Qualifiers)
       {
          Console.WriteLine("     " + qualifier.Name.ToString() + ": " + qualifier.Value.ToString());
       }
    }

    foreach (CimMethodDeclaration method in myDrive.CimClass.CimClassMethods)
    {
       Console.WriteLine(method.Name.ToString());
       foreach (CimQualifier qualifier in method.Qualifiers)
       {
          Console.WriteLine("     " + qualifier.Name.ToString() + ": " + qualifier.Value.ToString());
       }
    }
    ```

    

    For more information, see [Retrieving a WMI Instance](retrieving-an-instance.md).

You can retrieve the qualifiers on a WMI object in C# by first retrieving the object, and then examining the qualifiers as a collection.

> [!Note]  
> **System.Management** was the original .NET namespace used to access WMI; however, the APIs in this namespace generally are slower and do not scale as well relative to their more modern **Microsoft.Management.Infrastructure** counterparts.

 

**To retrieve a qualifier using C# (System.Management)**

1.  Retrieve the object whose qualifiers you want to view using [ManagementObject](https://msdn.microsoft.com/library/system.management.managementobject.aspx).

    ```CSharp
    using System.Management;
    ...
    ManagementObject myDisk = new ManagementObject("Win32_LogicalDisk.DeviceID='C:'");
    ```

    

    For more information, see [Retrieving a WMI Instance](retrieving-an-instance.md).

2.  Place the qualifiers into a [QualifierDataCollection](https://msdn.microsoft.com/library/system.management.qualifierdatacollection.aspx), and enumerate through the [QualifierData](https://msdn.microsoft.com/library/system.management.qualifierdata.aspx) values.

    ```CSharp
    
    QualifierDataCollection myQualifiers = myDisk.Qualifiers;
    foreach (QualifierData qd in myQualifiers)
    {
       Console.WriteLine(qd.Name + ": " + qd.Value);
    }
    Console.ReadLine();
    ```

    

    For more information, see [Retrieving a WMI Instance](retrieving-an-instance.md).

The following procedure describes how to retrieve a qualifier using VBScript.

**To retrieve a qualifier using VBScript**

1.  Retrieve the object whose qualifiers you want to view, as shown in the following example:

    ```VB
    Set Process = GetObject("winmgmts:Win32_Process")
    ```

    

    The most common way to retrieve an object is by using the [**GetObject**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-getobject?branch=master) method. For more information, see [Retrieving a WMI Instance](retrieving-an-instance.md).

2.  Access the qualifiers of the object through the [**SWbemObject.Qualifiers\_**](swbemobject-qualifiers-.md) property, as shown in the following example:

    ```VB
    for each Qualifier in Process.Qualifiers_
        WScript.Echo " " & Qualifier.Name
    next
    ```

    

The following code example describes how to access all the qualifiers on a [**Win32\_Process**](https://msdn.microsoft.com/library/aa394372) object.


```VB
On Error Resume Next
Set Process = GetObject("winmgmts:Win32_Process")
WScript.Echo ""
WScript.Echo "Class name is", Process.Path_.Class

'Get the qualifiers
WScript.Echo ""
WScript.Echo "Qualifiers:"
WScript.Echo ""
for each Qualifier in Process.Qualifiers_
    WScript.Echo " " & Qualifier.Name
next

if Err <> 0 Then
    WScript.Echo Err.Description
    Err.Clear
End if
```



The following procedure describes how to retrieve a qualifier using C++.

**To retrieve a qualifier using C++**

1.  Retrieve the object whose qualifiers you want to view.

    The most common way to retrieve an object is by using a call to [**GetObject**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-getobject?branch=master) or [**GetObjectAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-getobjectasync?branch=master). For more information, see [Retrieving WMI Class or Instance Data](retrieving-class-or-instance-data.md).

2.  Retrieve the qualifier set for a given property with a call to [**IWbemClassObject::GetPropertyQualifierSet**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-getpropertyqualifierset?branch=master) or [**IWbemClassObject::GetMethodQualifierSet**](/windows/win32/WbemCli/nf-wbemcli-iwbemclassobject-getmethodqualifierset?branch=master) methods.

3.  Access the qualifiers of the object through the returned [**IWbemQualifierSet**](/windows/win32/Wbemcli/nn-wbemcli-iwbemqualifierset?branch=master) interface.

## Examples

For more information on retrieving qualifiers, see the [Get-WmiClassMethodsAndWritableWmiProperties](https://Gallery.TechNet.Microsoft.Com/10670e14-4cf1-4ce5-99d0-fc4ca80dac2c) PowerShell code sample on the TechNet Gallery.

 

 



