---
description: Conceptually similar to a Uniform Resource Locator (URL), a WMI object path is a string that uniquely identifies the namespace on a server, a class within a namespace, or instances of a class.
ms.assetid: 7a390541-609d-4b97-b91c-1a41d21ec17d
ms.tgt_platform: multiple
title: Describing the Location of a WMI Object
ms.topic: article
ms.date: 05/31/2018
---

# Describing the Location of a WMI Object

Conceptually similar to a Uniform Resource Locator (URL), a WMI object path is a string that uniquely identifies the namespace on a server, a class within a namespace, or instances of a class. An object path is hierarchical, and contains several elements that describe the location of the object in question. Like file paths, WMI object paths can be described in full or specified as a relative path.

The namespace of a WMI object is listed on the WMI reference page. For example, the location of most of the classes supported by the [CIMWin32 WMI Providers](/windows/desktop/CIMWin32Prov/cimwin32-wmi-providers) are located in the \\root\\cimv2 namespace. The following PowerShell code describes a call to retrieve the [**Win32\_ComputerSystem**](/windows/desktop/CIMWin32Prov/win32-computersystem) object on your local machine:

`Get-WmiObject -Class Win32_ComputerSystem -Namespace "root\cimv2" -ComputerName "."`

Alternately, a specific instance of [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) may have the following path from the [**SWbemObject.Path\_**](swbemobject-path-.md) property.

`\\Machine1\root\cimv2:Win32_LogicalDisk.DeviceID="C:"`

The following example shows the relative path to this instance, as seen by displaying the [**Relpath**](swbemobjectpath-relpath.md) property of the [**SWbemObjectPath**](swbemobjectpath.md) object returned by the call to [**SWbemObject.Path\_**](swbemobject-path-.md).

`Win32_LogicalDisk.DeviceID="A:"`

Note that **DeviceID** is the key property of the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class.

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
<td><a href="describing-a-wmi-namespace-object-path.md">Namespace</a></td>
<td><dl><a href="/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-opennamespace"><strong>IWbemServices::OpenNamespace</strong></a><br />
</dl></td>
</tr>
<tr class="even">
<td><a href="describing-a-class-object-path.md">Class</a></td>
<td><dl><a href="/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethod"><strong>IWbemServices::ExecMethod</strong></a><br />
[<strong>IWbemServices::ExecMethodAsync</strong>](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethodasync)<br />
</dl></td>
</tr>
<tr class="odd">
<td><a href="describing-a-class-object-path.md">Class</a> or <a href="describing-an-instance-object-path.md">Instance</a></td>
<td><dl><a href="/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject"><strong>IWbemServices::GetObject</strong></a><br />
[<strong>IWbemServices::GetObjectAsync</strong>](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync)<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="describing-an-instance-object-path.md">Instance</a></td>
<td><dl><a href="/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteinstance"><strong>IWbemServices::DeleteInstance</strong></a><br />
[<strong>IWbemServices::DeleteInstanceAsync</strong>](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-deleteinstanceasync)<br />
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
<td><a href="swbemservices.md"><strong>SWbemServices</strong></a></td>
<td><dl><a href="swbemservices-associatorsof.md"><strong>AssociatorsOf</strong></a><br />
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
<td><a href="swbemobjectset.md"><strong>SWbemObjectSet</strong></a></td>
<td><dl><a href="swbemobjectset-item.md"><strong>Item</strong></a><br />
</dl></td>
</tr>
</tbody>
</table>



 

 

 
