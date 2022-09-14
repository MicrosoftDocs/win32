---
description: An SNMP collection maps to a CIM class and the elements of a collection map to the properties of a CIM class. All generated CIM class definitions must be derived from the SnmpObjectType class.
ms.assetid: e6f82fd6-e3d8-48c5-8c7b-a30a2d502f41
ms.tgt_platform: multiple
title: SNMP Collections
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# SNMP Collections

An SNMP collection maps to a CIM class and the elements of a collection map to the properties of a CIM class. All generated CIM class definitions must be derived from the **SnmpObjectType** class.

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 

The following class definitions parent all generated class definitions:

``` syntax
[abstract]
class SnmpMacro
{
};

[abstract]
class SnmpObjectType:SnmpMacro
{
};
```

## Remarks

The following rules apply when mapping SNMP collections to CIM classes. Unless otherwise specified, these rules apply to both scalar and table collections:

-   The mapping process generates CIM class names by concatenating "SNMP\_", the MIB module identity name, "\_", and the collection's object descriptor.

    For example: **system** translates to **SNMP\_RFC1213\_MIB\_system**, while **ifTable** translates to **SNMP\_RFC1213\_MIB\_ifTable**.

-   In all cases, hyphens (-) in SNMP MIB identifiers map to underscores (\_) in CIM class names.
-   Naming conflicts can occur due to CIM name case-insensitivity. If a naming conflict occurs, the provider chooses one of the conflicting group definitions and ignores the remaining definitions.
-   The identity name of the MIB module that contains the collection maps to the CIM class qualifier **Module\_Name**.
-   The object identifier of the fabricated collection maps to the CIM class qualifier **Group\_Objectid**.
-   The MIB module imports list (obtained from the **MODULE-IDENTITY** macro definition) maps to the CIM class qualifier **module\_imports**. This qualifier contains a comma-separated list of module names.

 

 



