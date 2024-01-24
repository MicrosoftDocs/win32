---
description: The SNMP Provider uses the following CIM property qualifiers when mapping MIB object definitions to CIM class definitions.
ms.assetid: 6e858e7e-5c46-4350-9696-c5efa1252c00
ms.tgt_platform: multiple
title: CIM Property Qualifiers for MIB Objects
ms.topic: article
ms.date: 05/31/2018
---

# CIM Property Qualifiers for MIB Objects

The SNMP Provider uses the following CIM property qualifiers when mapping MIB object definitions to CIM class definitions. A mandatory qualifier must be present for the SNMP Provider to fully resolve a MIB object. Failure to define a mandatory qualifier returns an error. Specifying an illegal qualifier value also returns an error.

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 



| Qualifier                          | Description                                                                                                                                                                                            |
|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Bits**                           | **string**Mandatory, if the **Textual\_Convention** qualifier does not equal BITS.<br/> Enumerated values for the subtype definition of a bit.<br/>                                        |
| **Cimtype**                        | **string**Mandatory<br/> CIM textual representation that formats an underlying CIM protocol value.<br/>                                                                                    |
| **Defval**                         | **string**Optional<br/> Object's default value.<br/>                                                                                                                                       |
| **Description**                    | **string**Optional<br/> Description of the object.<br/>                                                                                                                                    |
| **Display\_Hint**                  | **string**Optional<br/> Manner in which the object's data should appear to a user.<br/>                                                                                                    |
| **Encoding**                       | **string**Optional<br/> SNMP type used when encoding SNMPv1 and SNMPv2C protocol frames.<br/>                                                                                              |
| **Enumeration**                    | **string**Mandatory, if the **Textual\_Convention** qualifier does not equal ENUMERATEDINTEGER.<br/> Enumerated values for an enumerated integer subtype definition.<br/>                  |
| **Fixed\_Length**                  | **uint32**Optional<br/> Fixed-length value.<br/>                                                                                                                                           |
| [**Key**](standard-qualifiers.md) | **Bool**Optional<br/> Key property of a class definition.<br/>                                                                                                                             |
| **Key\_Order**                     | **uint32**Optional, unless [**Key**](standard-qualifiers.md) is specified.<br/> Order of the key property in the class definition.<br/>                                                   |
| **Name**                           | **string**Mandatory<br/> Implicit name of the property. Note that this qualifier is not explicitly defined.<br/>                                                                           |
| **Object\_Identifier**             | **string**Mandatory<br/> Object's MIB object identifier.<br/>                                                                                                                              |
| **Object\_Syntax**                 | **string**Optional<br/> Object's named type definition.<br/>                                                                                                                               |
| **Read**                           | **Bool**Optional (at least one of **Read** or **Write** must be specified)<br/> Grants read access to the object.<br/>                                                                     |
| **Reference**                      | **string**Optional<br/> Refers to another document that contains more information about the object.<br/>                                                                                   |
| **Status**                         | **string**Optional<br/> Indicates whether the object must be supported.<br/>                                                                                                               |
| **Textual\_Convention**            | **string**Mandatory<br/> Textual representation of the SYNTAX clause of the MIB [OBJECT-TYPE](object-type-macro.md) macro.<br/>                                                           |
| **Units**                          | **string**Optional<br/> Precise definition of what the object represents.<br/>                                                                                                             |
| **Variable\_Length**               | **string**Optional<br/> Minimum, maximum, and fixed-length values associated with the object's type definition.<br/>                                                                       |
| **Variable\_Value**                | **string**Optional<br/> Ranged and fixed values associated with the object's type definition.<br/>                                                                                         |
| **Virtual\_Key**                   | **Bool**Optional<br/> Indicates that the property's value should be based on the superset of instance information associated with all accessible MIB objects in the class definition.<br/> |
| **Write**                          | **Bool**Optional (at least one of **Read** or **Write** must be specified)<br/> Grants write access to the object.<br/>                                                                    |



 

 

 




