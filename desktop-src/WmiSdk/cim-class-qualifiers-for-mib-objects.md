---
description: The SNMP Provider uses the following CIM class qualifiers when mapping MIB object definitions to CIM class definitions.
ms.assetid: 458167dc-562e-47b8-8760-797ae13f9459
ms.tgt_platform: multiple
title: CIM Class Qualifiers for MIB Objects
ms.topic: article
ms.date: 05/31/2018
---

# CIM Class Qualifiers for MIB Objects

The SNMP Provider uses the following CIM class qualifiers when mapping MIB object definitions to CIM class definitions. A mandatory qualifier must be present for the SNMP Provider to fully resolve a group object. Failure to define a mandatory qualifier returns an error. Specifying an illegal qualifier value also returns an error.

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 



| Qualifier           | Description                                                                                                                             |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Description**     | **string**Optional<br/> Description of the class.<br/>                                                                      |
| **Group\_Objectid** | **string**Mandatory, if the class is for the SNMP class provider.<br/> Object identifier of the fabricated collection.<br/> |
| **Module\_Imports** | **string**Optional<br/> Comma-separated list of MIB module names used to resolve imports.<br/>                              |
| **Module\_Name**    | **string**Optional<br/> Identity name of a MIB module.<br/>                                                                 |
| **Reference**       | **string**Optional<br/> Refers to another document that contains more information about the class.<br/>                     |
| **Singleton**       | **Bool**Mandatory for classes mapped from scalar collections.<br/> Indicates a class that can only have one instance.<br/>  |



 

 

 




