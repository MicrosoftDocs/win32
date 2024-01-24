---
description: In general, each Active Directory object maps to exactly one WMI instance.
ms.assetid: c6c7f3c3-7174-4278-bf40-d99ed8bd0c8d
ms.tgt_platform: multiple
title: Mapping Active Directory Instances
ms.topic: article
ms.date: 05/31/2018
---

# Mapping Active Directory Instances

In general, each Active Directory object maps to exactly one WMI instance. The WMI class corresponding to the WMI instance is the same as the class provided by the class provider from the corresponding Active Directory class. The key property **ADSIPath** of each instance is filled in with the ADSI path of the object.

The following sections are discussed in this topic:

-   [Mapping Namespaces](#mapping-namespaces)
-   [Mapping Attribute Values](#mapping-attribute-values)
-   [Mapping Instance Associations](#mapping-instance-associations)

> [!Note]  
> For more information about support and installation of this component on a specific operating system, see [Operating System Availability of WMI Components](operating-system-availability-of-wmi-components.md).

 

## Mapping Namespaces

Each of the namespaces in ADSI map one-to-one to namespaces in the WMI \\root\\directory namespace. The name of the WMI namespace is the same as the **ProgId** value of the Directory Services provider that provides the namespace. Specifically, Active Directory maps to the \\LDAP namespace in the \\root\\directory namespace. WMI creates the \\LDAP namespace as a part of the class provider registration process.

## Mapping Attribute Values

The following table lists the mapping between each attribute of an Active Directory object and a WMI property.



| Active Directory syntax | WMI data type                                 | WMI property value                                                        |
|-------------------------|-----------------------------------------------|---------------------------------------------------------------------------|
| Access-Point            | **CIM\_STRING**                               | Mapped from the value of the string.                                      |
| Boolean                 | **CIM\_BOOLEAN**                              | Mapped directly to the appropriate Boolean value.                         |
| Case Insensitive String | **CIM\_STRING**                               | Mapped from the value of the string.                                      |
| Case Sensitive String   | **CIM\_STRING**                               | Mapped from the value of the string.                                      |
| Distinguished Name      | **CIM\_STRING**                               | Mapped from the value of the string.                                      |
| DN-Binary               | Embedded object of class **DN\_With\_Binary** | Mapped to instances of the **DN\_With\_String** class.                    |
| DN-String               | Embedded object of class **DN\_With\_String** | Mapped to instances of the **DN\_With\_String** class.                    |
| Enumeration             | **CIM\_SINT32**                               | Mapped directly to the integer value.                                     |
| IA5-String              | **CIM\_STRING**                               | Mapped from the value of the string.                                      |
| Integer                 | **CIM\_SINT32**                               | Mapped directly to the integer value.                                     |
| NT Security Descriptor  | Embedded object of Class **Uint8Array**       | Mapped to instances of the **Uint8Array** class.                          |
| Numeric String          | **CIM\_STRING**                               | Mapped from the value of the string.                                      |
| Object Id               | **CIM\_STRING**                               | Mapped from the string representation of the OID; for example, "1.3.3.4". |
| Octet String            | Embedded object of Class **Uint8Array**       | Mapped to instances of the **Uint8Array** class.                          |
| OR Name                 | **CIM\_STRING**                               | Mapped from the value of the string.                                      |
| Presentation-Address    | **CIM\_STRING**                               | Mapped from the value of the string.                                      |
| Print Case String       | **CIM\_STRING**                               | Mapped from the value of the string.                                      |
| Replica Link            | Embedded object of class **Uint8Array**       | Mapped to instances of the **Uint8Array** class.                          |
| SID                     | Embedded object of Class **Uint8Array**       | Mapped to instances of the **Uint8Array** class.                          |
| Time                    | **CIM\_DATETIME**                             | Converted to the CIM\_DATETIME representation and mapped.                 |
| Undefined               | N/A                                           | N/A                                                                       |
| Unicode String          | **CIM\_STRING**                               | Mapped from the value of the string.                                      |
| UTC Coded Time          | **CIM\_DATETIME**                             | Converted to the CIM\_DATETIME representation and mapped.                 |



 

For more information about **Uint8Array** and **DN\_With\_Binary**, see [Mapping Attributes](mapping-active-directory-classes.md).

## Mapping Instance Associations

The Directory Services provider maps the different container relationships in Active Directory using instances of the [**DS\_LDAP\_Instance\_Containment**](/previous-versions/windows/desktop/dsprov/ds-ldap-instance-containment) class.

 

 
