---
description: The OBJECT-TYPE macro contains mandatory and optional clauses that describe the basic characteristics of a MIB object. The SNMP Provider converts an MIB to the corresponding parts of the OBJECT-TYPE macro.
ms.assetid: ad76a4fc-354e-4270-862c-062aa523bf7e
ms.tgt_platform: multiple
title: OBJECT-TYPE Macro
ms.topic: article
ms.date: 05/31/2018
---

# OBJECT-TYPE Macro

The OBJECT-TYPE macro contains mandatory and optional clauses that describe the basic characteristics of a MIB object. The SNMP Provider converts an MIB to the corresponding parts of the OBJECT-TYPE macro.

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 

## Components

<dl> <dt>

<span id="MIB_object"></span><span id="mib_object"></span><span id="MIB_OBJECT"></span>MIB object
</dt> <dd>

Object that contains most of the data in question.

</dd> <dt>

<span id="Object_descriptor"></span><span id="object_descriptor"></span><span id="OBJECT_DESCRIPTOR"></span>Object descriptor
</dt> <dd>

Unique name or object descriptor identifying each MIB object. Each MIB object descriptor maps exactly to a CIM property name. For example, **ifIndex** translates to **ifIndex**.

</dd> <dt>

<span id="SYNTAX_Clause"></span><span id="syntax_clause"></span><span id="SYNTAX_CLAUSE"></span>[SYNTAX Clause](syntax-clause.md)
</dt> <dd>

Defines the data and type of an MIB object.

</dd> <dt>

<span id="INDEX_clause"></span><span id="index_clause"></span><span id="INDEX_CLAUSE"></span>[INDEX clause](index-clause.md)
</dt> <dd>

Defines a key for selecting a unique table row.

</dd> <dt>

<span id="AUGMENTS_clause"></span><span id="augments_clause"></span><span id="AUGMENTS_CLAUSE"></span>AUGMENTS clause
</dt> <dd>

Indicates that the table collection it specifies can be considered an extension of another table collection, and can replace the INDEX clause in SNMPv2. The collections referred to by the AUGMENTS clause can be combined with the other table collection to form one collection. The resulting collection shares the primary key properties specified in the last table collection in the chain.

In this case, the previous mapping rules specified for the INDEX clause are applied to the last table collection in the chain. The collection of objects then maps to one CIM class definition.

</dd> <dt>

<span id="OBJECT-IDENTIFIER_clause"></span><span id="object-identifier_clause"></span><span id="OBJECT-IDENTIFIER_CLAUSE"></span>OBJECT-IDENTIFIER clause
</dt> <dd>

Contains a unique object identifier for an MIB object. This object identifier maps to the CIM property qualifier **object\_identifier**.

</dd> <dt>

<span id="ACCESS_and_MAX-ACCESS_Clauses"></span><span id="access_and_max-access_clauses"></span><span id="ACCESS_AND_MAX-ACCESS_CLAUSES"></span>[ACCESS and MAX-ACCESS Clauses](access-and-max-access-clauses.md)
</dt> <dd>

Define the access rights to the MIB object.

</dd> <dt>

<span id="DESCRIPTION_clause"></span><span id="description_clause"></span><span id="DESCRIPTION_CLAUSE"></span>DESCRIPTION clause
</dt> <dd>

Provides a text description of the object, which maps to the CIM property qualifier **Description**. This clause may be empty.

Each **TABLE** and **ENTRY** object in an SNMP table definition also contains a DESCRIPTION clause, which also may be empty. The TABLE and ENTRY DESCRIPTION clauses are concatenated and the result maps to the CIM class qualifier **Description**.

</dd> <dt>

<span id="STATUS_clause"></span><span id="status_clause"></span><span id="STATUS_CLAUSE"></span>STATUS clause
</dt> <dd>

Indicates whether the object must be supported. When the value of the STATUS clause is **obsolete**, the provider discards the MIB object from the mapping. Otherwise, the STATUS clause maps to the CIM property qualifier **Status**.

For SNMPv1, the preferred value of **Status** is either **mandatory** or **optional**, but the qualifier can contain some other value. For SNMPv2C, the preferred value of **Status** is either **current** or **deprecated**, but the qualifier can contain some other value.

</dd> <dt>

<span id="DEFVAL_clause"></span><span id="defval_clause"></span><span id="DEFVAL_CLAUSE"></span>DEFVAL clause
</dt> <dd>

Assigns a default value to a variable in a logical table row, and maps to the string CIM property qualifier **Defval**.

</dd> <dt>

<span id="REFERENCE_clause"></span><span id="reference_clause"></span><span id="REFERENCE_CLAUSE"></span>REFERENCE clause
</dt> <dd>

Refers to another document that contains more information about the object. This clause maps to the CIM property qualifier **Reference**, which is of type string.

</dd> <dt>

<span id="UNITS_clause"></span><span id="units_clause"></span><span id="UNITS_CLAUSE"></span>UNITS clause
</dt> <dd>

Provides a precise definition of what the object represents. This clause maps to the CIM property qualifier **Units**, which is of type string.

</dd> </dl>

## Remarks

The OBJECT-TYPE macro describes the basic characteristics of an individual MIB object. A set of OBJECT-TYPE macros can be considered as a group of related objects. In SNMPv2C, use the OBJECT-GROUP macro to formally group sets of related objects into a collection. However, there is no formal mechanism for creating collections in SNMPv1. For the purposes of the SNMP Provider, the OBJECT-GROUP macro is ignored, but you can invent grouping relationships and fabricate collections.

 

 



