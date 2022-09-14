---
description: WMI has several types of class and property qualifiers. Qualifiers can also have modifying flavors.
ms.assetid: b889df69-327b-40d0-bbd7-a33d7924f3e1
ms.tgt_platform: multiple
title: WMI Qualifiers
ms.topic: article
ms.date: 05/31/2018
---

# WMI Qualifiers

WMI has several types of class and property [*qualifiers*](gloss-q.md). Qualifiers can also have modifying [*flavors*](gloss-f.md). The following types of qualifiers and flavors are used in WMI.

The name of each qualifier appears with its data type and an indicator of whether the qualifier can be applied to a class, instance, property, or method. For qualifiers such as **Association** (discussed under [Meta Qualifiers](meta-qualifiers.md)), there is an implied usage rule that the meta qualifier must also be present. For example, the implicit usage rule for the **Aggregation** qualifiers is that the **Association** qualifier must also be present.



| Qualifier type                              | Description                                                                                                                           |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [Meta](meta-qualifiers.md)                 | Refines the definition of meta-constructs by clarifying the actual usage of a class or property declaration.                          |
| [Optional](optional-qualifiers.md)         | Addresses situations not common to all CIM-compliant implementations.                                                                 |
| [Qualifier Flavors](qualifier-flavors.md)  | Provides more information about a qualifier, such as whether a derived class or instance can override the qualifier's original value. |
| [Standard](standard-qualifiers.md)         | Supports the descriptions that all CIM-compliant implementations must handle.                                                         |
| [WMI-specific](wmi-specific-qualifiers.md) | Describes qualifiers specific to WMI, such as performance counter class qualifiers.                                                   |



 

For more information on applying qualifiers to your WMI classes, see [Adding a Qualifier](adding-a-qualifier.md). To see how to examine qualifiers on existing WMI classes, see the example code below.

## Example

The following PowerShell code, taken from the [TechNet gallery](https://Gallery.TechNet.Microsoft.Com/Get-WMI-Class-qualifiers-239970e7), describes how to retrieve qualifiers from a WMI class.


```PowerShell
Function Get-WMIClassesWithQualifiers 
{ 
 Param([string]$qualifier = "dynamic", 
  [string]$namespace = "root\cimv2") 
 $classes = Gwmi -list -namespace $namespace 
 foreach($class in $classes) 
 { 
  $query = "select * from meta_class where __this isa ""$($class.name)"" " 
  $a = gwmi -Query $query -Namespace $namespace |  
  select -Property __class, qualifiers 
   if($a.qualifiers | % { $_ | ? { $_.name -match "$qualifier" }}) 
    { $a.__class } 
  } #end foreach $class 
} 
```



 

 



