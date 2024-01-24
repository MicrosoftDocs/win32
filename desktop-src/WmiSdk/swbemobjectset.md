---
description: An SWbemObjectSet object is a collection of SWbemObject objects. For more information, see Accessing a Collection. This object cannot be created by the VBScript CreateObject call.
ms.assetid: 00f5317e-eb8e-42f9-bada-963e11aadda4
ms.tgt_platform: multiple
title: SWbemObjectSet object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemObjectSet
- ISWbemObjectSet
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemObjectSet object

An **SWbemObjectSet** object is a collection of [**SWbemObject**](swbemobject.md) objects. For more information, see [Accessing a Collection](accessing-a-collection.md). This object cannot be created by the VBScript **CreateObject** call.

You can get an **SWbemObjectSet** object by calling any of the following methods or their asynchronous equivalents:

-   [**SWbemObject.Associators\_**](swbemobject-associators-.md)
-   [**SWbemObject.Instances\_**](swbemobject-instances-.md)
-   [**SWbemObject.References\_**](swbemobject-references-.md)
-   [**SWbemObject.Subclasses\_**](swbemobject-subclasses-.md)
-   [**SWbemServices.AssociatorsOf**](swbemservices-associatorsof.md)
-   [**SWbemServices.ExecQuery**](swbemservices-execquery.md)
-   [**SWbemServices.InstancesOf**](swbemservices-instancesof.md)
-   [**SWbemServices.ReferencesTo**](swbemservices-referencesto.md)
-   [**SWbemServices.SubclassesOf**](swbemservices-subclassesof.md)

> [!Note]  
> The **SWbemObjectSet** object does not support the optional **Add** and **Remove** collection methods.

 

> [!Note]  
> Because the call-back to the sink might not be returned at the same authentication level as the client requires, it is recommended that you use semisynchronous instead of asynchronous communication. For more information, see [Calling a Method](calling-a-method.md).

 

## Members

The **SWbemObjectSet** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SWbemObjectSet** object has these methods.



| Method                              | Description                                                                                                                      |
|:------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| [**Item**](swbemobjectset-item.md) | Retrieves an [**SWbemObject**](swbemobject.md) object from the collection. This is the default method of the object.<br/> |
| [**ItemIndex**](swbemobjectset-itemindex.md) | Retrieves the [**SWbemObject**](swbemobject.md) object associated with the specified index into the collection.<br/> |



 

### Properties

The **SWbemObjectSet** object has these properties.



| Property                                                  | Access type          | Description                                              |
|:----------------------------------------------------------|:---------------------|:---------------------------------------------------------|
| [**Count**](swbemobjectset-count.md)<br/>          | Read-only<br/> | The number of items in the collection.<br/>        |
| [**Security\_**](swbemobjectset-security-.md)<br/> | Read-only<br/> | Used to read or change the security settings.<br/> |



 

## Remarks

An **SWbemObjectSet** is a collection of zero or more [**SWbemObject**](swbemobject.md) objects. Each **SWbemObject** in a **SWbemObjectSet** can represent one of two things:

-   An instance of a WMI-managed resource.
-   An instance of a class definition.

The most common use of this class in WMI is as the return value for an [**ExecQuery**](/windows/desktop/api/Provider/nf-provider-provider-execquery) or [**InstancesOf**](swbemservices-instancesof.md) call, as described in the following code sample:


```VB
strComputer = "."
Set objSWbemServices = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")
Set colServices = objSWbemServices.ExecQuery("SELECT State FROM Win32_Service")
For Each objService In colServices
    Wscript.Echo objService.Name, objService.State
Next
```



For the most part, the only thing you will ever do with an **SWbemObjectSet** is enumerate all the objects contained within the collection itself. However, **SWbemObjectSet** does include a property Count that can be useful in system administration scripting. As the name implies, Count tells you the number of items in the collection. For example, this script retrieves a collection of all the services installed on a computer and then echoes the total number of services found:

For more information on how to use this class, see [Enumerating WMI](enumerating-wmi.md).

## Examples

The following VBScript code sample illustrates how **SWbemObjectSet** collections are manipulated.


```VB
On Error Resume Next

Set Disks = GetObject("winmgmts:").InstancesOf ("CIM_LogicalDisk")

WScript.Echo "There are", Disks.Count, " Disks"

Set Disk = Disks("Win32_LogicalDisk.DeviceID=""C:""")
WScript.Echo Disk.Path_.Path

if Err <> 0 Then
 WScript.Echo Err.Description
 Err.Clear
End if
```



The following Perl code sample illustrates how **SWbemObjectSet** collections are manipulated.


```
use strict;
use Win32::OLE;

my ($disks,$disk);

eval { $disks = Win32::OLE->GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\.\\root\\cimv2")->
   InstancesOf("CIM_LogicalDisk"); };
unless($@)
{
 print "\nThere are ", $disks->{Count}, " Disks \n";

 eval { $disk = $disks->Item("Win32_LogicalDisk.DeviceID=\"C:\""); };
 unless($@)
 {
  print $disk->{Path_}->{Path}, "\n";
 }
 else
 {
  print STDERR Win32::OLE->LastError, "\n";
 }
}
else
{
 print STDERR Win32::OLE->LastError, "\n";
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemObjectSet<br/>                                                        |
| IID<br/>                      | IID\_ISWbemObjectSet<br/>                                                         |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

 




