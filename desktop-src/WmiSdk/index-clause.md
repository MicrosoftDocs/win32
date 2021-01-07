---
description: Specifies a key to select a unique row in a scalar or table collection.
ms.assetid: 3c4edae0-55be-4804-b5fe-07458b918365
ms.tgt_platform: multiple
title: INDEX Clause
ms.topic: article
ms.date: 05/31/2018
---

# INDEX Clause

The INDEX clause specifies a key to select a unique row in a scalar or table collection. The SNMP Provider maps to a different type of CIM class depending on the type of table the SNMP device uses. Because a key can be more than one type of object, the provider uses different mapping rules depending on the type of object within the key. For more information, see [INDEX Clause Data Types](#index-clause-data-types).

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 

A scalar collection maps to a CIM singleton class: that is, a class that can have only one instance. Because there is no need to uniquely identify one instance from another, a singleton class does not designate one or more properties as the key. Classes generated from scalar collections:

-   Do not contain **Key** property qualifiers.
-   Do contain the standard CIM class qualifier **Singleton**, which is of type **Bool**.

A table collection maps to a CIM class that can have more than one instance. As a result, the CIM class definition must contain at least one property that defines the object key; that is, a property that uniquely identifies an instance of the class. The INDEX clause of a table collection's [OBJECT-TYPE](object-type-macro.md) macro specifies the collection's set of key properties. The following mapping rules apply:

-   The CIM qualifier **Key**, type **Bool**, defines a key property.
-   The ordering of the INDEX information within the table collection defines the ordering of the keys within the CIM class definition.

    The CIM qualifier **Key\_Order** defines the ordering of the keys. This qualifier is an unsigned 32-bit integer value which, for the purposes of the MOF qualifier syntax, must be converted to a signed 32-bit integer value using the twos-complement operation.

Currently, the mapping of the SNMPv2C INDEX clause does not handle the use of the **IMPLIED** qualifier. A CIM class definition is not generated in this case.

## INDEX Clause Data Types

Because of the flexibility of the INDEX clause within the [OBJECT-TYPE](object-type-macro.md) macro, the specification of keyed properties is not straightforward. Instead, you should consider the possibilities that the INDEX clause may contain one or more of the following data types:

-   Internally accessible **indexobject** value

    The **indexobject** value is a named value that refers to a MIB object definition appearing in the conceptual row of the same table that contains the INDEX clause. The MIB object definition referred to in the INDEX clause maps to a key property of the CIM class definition.

-   Externally accessible **indexobject** value

    In this case, **indexobject** is a named value that refers to a MIB object definition appearing in the conceptual row of a different table.

-   Accessible **indextype** value

    The **indextype** value is a named type that refers to one of the following data types: **INTEGER**, **OCTET STRING**, **OBJECT IDENTIFIER**, **NetworkAddress**, or **IpAddress**. If the INDEX clause contains an MIB-type reference, the following mapping rules apply:

    -   The MIB object referred to maps to a key property of the CIM class definition. Its type syntax is based on the **indextype** value specified, which maps to CIM property qualifiers using the standard [SYNTAX clause](syntax-clause.md) mapping procedures.
    -   The mapping process generates a unique property name by concatenating the MIB table object descriptor, an underscore (\_), and the rank order of the INDEX clause **indextype** value. For example, the property name for the third component **indextype** of the MIB table **enterpriseIfTable** is **enterpriseIfTable\_3**.
    -   The CIM property is annotated with the **Virtual\_Key** qualifier. This qualifier specifies that the SNMP Provider should calculate the value of the property based on the superset of instance information associated with all of the accessible MIB object definitions in the class definition.
    -   The CIM class definition must contain at least one property that does not have an associated **Virtual\_Key** qualifier; failure to specify this property invalidates the class definition.

-   Fixed-length subtype

    When the INDEX clause of an SNMP table collection contains an SNMP-supported type that is subtyped as a fixed-length OCTET STRING, the CIM property qualifier **Fixed\_Length** must be used to specify this value.

 

 



