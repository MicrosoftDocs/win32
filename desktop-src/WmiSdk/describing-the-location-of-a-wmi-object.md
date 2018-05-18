---
Description: 'Conceptually similar to a Uniform Resource Locator (URL), a WMI object path is a string that uniquely identifies the namespace on a server, a class within a namespace, or instances of a class.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '7a390541-609d-4b97-b91c-1a41d21ec17d'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Describing the Location of a WMI Object
---

# Describing the Location of a WMI Object

Conceptually similar to a Uniform Resource Locator (URL), a WMI object path is a string that uniquely identifies the namespace on a server, a class within a namespace, or instances of a class. An object path is hierarchical, and contains several elements that describe the location of the object in question. Like file paths, WMI object paths can be described in full or specified as a relative path.

The namespace of a WMI object is listed on the WMI reference page. For example, the location of most of the classes supported by the [CIMWin32 WMI Providers](https://msdn.microsoft.com/library/dn792179) are located in the \\root\\cimv2 namespace. The following PowerShell code describes a call to retrieve the [**Win32\_ComputerSystem**](https://msdn.microsoft.com/library/aa394102) object on your local machine:

`Get-WmiObject -Class Win32_ComputerSystem -Namespace "root\cimv2" -ComputerName "."`

Alternately, a specific instance of [**Win32\_LogicalDisk**](https://msdn.microsoft.com/library/aa394173) may have the following path from the [**SWbemObject.Path\_**](swbemobject-path-.md) property.

`\\Machine1\root\cimv2:Win32_LogicalDisk.DeviceID="C:"`

The following example shows the relative path to this instance, as seen by displaying the [**Relpath**](swbemobjectpath-relpath.md) property of the [**SWbemObjectPath**](swbemobjectpath.md) object returned by the call to [**SWbemObject.Path\_**](swbemobject-path-.md).

`Win32_LogicalDisk.DeviceID="A:"`

Note that **DeviceID** is the key property of the [**Win32\_LogicalDisk**](https://msdn.microsoft.com/library/aa394173) class.

## C++

The following table lists object path types and the associated methods that require object paths.



<table>
<thead>
<tr class="header">
<th>Object path type</th>
<th>Method</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Namespace](describing-a-wmi-namespace-object-path.md)</td>
<td><dl>[<strong>IWbemServices::OpenNamespace</strong>](iwbemservices-opennamespace.md)<br />
</dl></td>
</tr>
<tr class="even">
<td>[Class](describing-a-class-object-path.md)</td>
<td><dl>[<strong>IWbemServices::ExecMethod</strong>](iwbemservices-execmethod.md)<br />
[<strong>IWbemServices::ExecMethodAsync</strong>](iwbemservices-execmethodasync.md)<br />
</dl></td>
</tr>
<tr class="odd">
<td>[Class](describing-a-class-object-path.md) or [Instance](describing-an-instance-object-path.md)</td>
<td><dl>[<strong>IWbemServices::GetObject</strong>](iwbemservices-getobject.md)<br />
[<strong>IWbemServices::GetObjectAsync</strong>](iwbemservices-getobjectasync.md)<br />
</dl></td>
</tr>
<tr class="even">
<td>[Instance](describing-an-instance-object-path.md)</td>
<td><dl>[<strong>IWbemServices::DeleteInstance</strong>](iwbemservices-deleteinstance.md)<br />
[<strong>IWbemServices::DeleteInstanceAsync</strong>](iwbemservices-deleteinstanceasync.md)<br />
</dl></td>
</tr>
</tbody>
</table>



 

## Script

Object paths can be constructed in several ways:

-   Retrieve the property of a method that returns an [**SWbemObjectPath**](swbemobjectpath.md) object.
-   Retrieve the [**SWbemObject.Path\_**](swbemobject-path-.md) property.
-   Create a string variable that contains the object path.

The following table lists the scripting objects that require object paths.



<table>
<thead>
<tr class="header">
<th>Scripting object</th>
<th>Method</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>SWbemServices</strong>](swbemservices.md)</td>
<td><dl>[<strong>AssociatorsOf</strong>](swbemservices-associatorsof.md)<br />
[<strong>AssociatorsOfAsync</strong>](swbemservices-associatorsofasync.md)<br />
[<strong>Delete</strong>](swbemservices-delete.md)<br />
[<strong>DeleteAsync</strong>](swbemservices-deleteasync.md)<br />
[<strong>ExecMethod</strong>](swbemservices-execmethod.md)<br />
[<strong>ExecMethodAsync</strong>](swbemservices-execmethodasync.md)<br />
[<strong>Get</strong>](swbemservices-get.md)<br />
[<strong>GetAsync</strong>](swbemservices-getasync.md)<br />
[<strong>ReferencesTo</strong>](swbemservices-referencesto.md)<br />
[<strong>ReferencesToAsync</strong>](swbemservices-referencestoasync.md)<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>SWbemObjectSet</strong>](swbemobjectset.md)</td>
<td><dl>[<strong>Item</strong>](swbemobjectset-item.md)<br />
</dl></td>
</tr>
</tbody>
</table>



 

 

 



