---
description: WMI defines a set of system properties that are associated with all classes and instances of classes in addition to class-specific properties.
ms.assetid: ea8ca4e4-9969-48fc-9b9f-5a5c8442006d
ms.tgt_platform: multiple
title: CIM System Properties for MIB Objects
ms.topic: article
ms.date: 05/31/2018
---

# CIM System Properties for MIB Objects

WMI defines a set of system properties that are associated with all classes and instances of classes in addition to class-specific properties.

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 

The SNMP Provider uses the following CIM system properties when mapping MIB object definitions to CIM class definitions. Mandatory properties must be present for the SNMP Provider to fully resolve a group object. Failure to define a mandatory property returns an error.



<table>
<thead>
<tr class="header">
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>__CLASS</strong></td>
<td><strong>string</strong>Mandatory<br/> For instances, the class to which the object belongs. For classes, this is the class name.<br/></td>
</tr>
<tr class="even">
<td><strong>__DYNASTY</strong></td>
<td><strong>string</strong>Optional<br/> Name of the class that is the ultimate base class for the current object (not its immediate parent class).<br/></td>
</tr>
<tr class="odd">
<td><strong>__GENUS</strong></td>
<td><strong>uint32</strong>Mandatory<br/> Type of object. Values are:<br/> <dl> 1 = class<br />
2 = instance<br />
</dl></td>
</tr>
<tr class="even">
<td><strong>__NAMESPACE</strong></td>
<td><strong>string</strong>Mandatory<br/> Namespace where the object is located.<br/></td>
</tr>
<tr class="odd">
<td><strong>__PATH</strong></td>
<td><strong>string</strong>Mandatory<br/> Absolute path to the object.<br/></td>
</tr>
<tr class="even">
<td><strong>__PROPERTYCOUNT</strong></td>
<td><strong>uint32</strong>Mandatory<br/> Number of non-system properties defined for the object.<br/></td>
</tr>
<tr class="odd">
<td><strong>__RELPATH</strong></td>
<td><strong>string</strong>Mandatory<br/> Relative path to the object.<br/></td>
</tr>
<tr class="even">
<td><strong>__SERVER</strong></td>
<td><strong>string</strong>Mandatory<br/> Server supplying the object.<br/></td>
</tr>
<tr class="odd">
<td><strong>__SUPERCLASS</strong></td>
<td><strong>string</strong>Optional<br/> Immediate parent class of the object.<br/></td>
</tr>
</tbody>
</table>



 

 

 




