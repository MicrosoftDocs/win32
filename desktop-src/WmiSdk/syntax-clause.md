---
description: Contains a SYNTAX clause that defines the data and type for the MIB object.
ms.assetid: 24c483c8-db50-492f-9c2e-72620395331a
ms.tgt_platform: multiple
title: SYNTAX Clause
ms.topic: article
ms.date: 05/31/2018
---

# SYNTAX Clause

The [OBJECT-TYPE](object-type-macro.md) macro contains a SYNTAX clause that defines the data and type for the MIB object. While the SNMP Provider observes general rules for mapping SYNTAX clauses, the provider also follows rules specific to several data types.

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 

The following mapping rules apply to all of the data types described in the table below:

-   The textual representation of the SYNTAX clause maps to the CIM property qualifier **textual\_convention**.
-   The named type definition in the SYNTAX clause maps to the CIM property qualifier **object\_syntax**. This mapping differs depending on the data type. For more information, see the mapping descriptions.
-   The SNMP type used when encoding SNMPv1 and SNMPv2C protocol frames maps to the CIM property qualifier **encoding**.
-   The CIM property qualifier **cimtype** contains the textual representation that formats the underlying CIM protocol value.

The following table lists data types that have specific rules that govern the provider mapping behavior.



| SNMP data type                                     | Description                                                                                                                                                                                                                                      |
|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Primitive type](#primitive-type)                  | One of the basic data types defined in the Structure of Management Information (SMI) documents RFC 1213 and RFC 1903.                                                                                                                            |
| [Textual convention](textual-convention-macro.md) | Type definition generated through the explicit use of the SNMPv2C **TEXTUAL-CONVENTION** macro or generated through the use of a named type. A textual convention assigns a name and, in some cases, a range of values to an existing data type. |
| [Named type](#named-type)                          | Named reference to a primitive type, textual convention, or constrained type.                                                                                                                                                                    |
| [Constrained type](#constrained-type)              | Primitive type, named type, or textual convention that has been constrained by some subtyping mechanism defined in the SMI documents RFC 1213 and RFC 1903.                                                                                      |



 

## Primitive Type

The primitive type is one of the basic data types defined in the Structure of Management Information (SMI) documents RFC 1213 and RFC 1903. SNMP primitive types map to CIM-defined types. The following table lists the mapping that occurs when the SYNTAX clause explicitly refers to a primitive type for SNMPv1. The **textual\_convention**, **encoding**, and **object\_syntax** qualifiers are always the same as the MIB type and the default value is always **NULL**.



| MIB type         | CIM variant type | cimtype value |
|------------------|------------------|---------------|
| INTEGER          | VT\_I4           | **sint32**    |
| OCTETSTRING      | VT\_BSTR         | **string**    |
| OBJECTIDENTIFIER | VT\_BSTR         | **string**    |
| NULL             | VT\_NULL         | Not supported |
| IpAddress        | VT\_BSTR         | **string**    |
| Counter          | VT\_I4           | **uint32**    |
| Gauge            | VT\_I4           | **uint32**    |
| TimeTicks        | VT\_I4           | **uint32**    |
| Opaque           | VT\_BSTR         | **string**    |
| NetworkAddress   | VT\_BSTR         | **string**    |



 

The provider ignores the OBJECT-TYPE macro when the SYNTAX clause refers to **NULL**, either explicitly or through a named type assignment. The following table lists the mapping that occurs when the SYNTAX clause explicitly refers to a primitive type for SNMPv2. The **textual\_convention**, **encoding**, and **object\_syntax** qualifiers are always the same as the MIB type and the default value is always **NULL**.



| MIB type          | CIM variant type | cimtype value |
|-------------------|------------------|---------------|
| INTEGER           | VT\_I4           | **sint32**    |
| OCTET STRING      | VT\_BSTR         | **string**    |
| OBJECT IDENTIFIER | VT\_BSTR         | **string**    |
| IpAddress         | VT\_BSTR         | **string**    |
| Counter32         | VT\_I4           | **uint32**    |
| Gauge32           | VT\_I4           | **uint32**    |
| Unsigned32        | VT\_I4           | **uint32**    |
| Integer32         | VT\_I4           | **sint32**    |
| Counter64         | VT\_BSTR         | **uint64**    |
| TimeTicks         | VT\_I4           | **uint32**    |
| Opaque            | VT\_BSTR         | **string**    |



 

## Named Type

SNMP named types map to CIM-defined types. When the SYNTAX clause refers to a [primitive type](#primitive-type), [textual convention](textual-convention-macro.md), or [constrained type](#constrained-type) through a type assignment derivation, use the those types to determine which mapping procedures apply.

-   If, through derivation of the type assignment rules, you encounter a constrained type definition:

    -   And if, through further derivation, you encounter one of the textual conventions listed in [TEXTUAL-CONVENTION Macro](textual-convention-macro.md), then apply the mapping rules for constrained types and textual conventions.
    -   Otherwise, if you encounter one of the primitive types listed in either primitive type table, apply the mapping rules for primitive types and constrained types.

-   If you encounter one of the textual conventions listed in [TEXTUAL\_CONVENTION Macro](textual-convention-macro.md), apply the mapping rules for textual conventions.
-   If you encounter one of the primitive types listed in either primitive type table, apply the mapping rules for primitive types.

> [!Note]  
> Classes containing property types that do not conform to the mapping described above are not valid. In this case, the provider returns an error if and when the provider requests the retrieval of a class definition while executing an instance retrieval function.

 

## Constrained Type

A constrained type is a primitive type, named type, or textual convention that has been constrained by some subtyping mechanism defined in the SMI documents RFC 1213 and RFC 1903. When subtyping occurs, additional CIM qualifiers are required to specify the subtype values. The named-type definition in the SYNTAX clause maps verbatim to the CIM property qualifier **object\_syntax** up to, but not including the constraints of the subtype.

Subtypes may follow any of the following formats:

-   Enumerated INTEGER

    The CIM property qualifier **enumeration** specifies the enumerated values. This qualifier is represented as a string containing a comma-separated list of signed 32-bit integer values. The following table lists the mapping types. The default value is always **NULL**.



| Constrained MIB type | CIM variant type | CIM qualifiers                                                                                                        |
|----------------------|------------------|-----------------------------------------------------------------------------------------------------------------------|
| Enumerated INTEGER   | VT\_BSTR         | **textual\_convention**: enumeratedinteger<br/> **encoding**: INTEGER<br/> **cimtype**: string<br/> |



 

-   BITS

    The CIM property qualifier **bits** specifies the enumerated values. This qualifier is represented as a string containing a comma-separated list of signed 32-bit integer values. The following table lists the mapping types. The default value is always **NULL**.



| Constrained MIB type | CIM variant type      | CIM qualifiers                                                                                               |
|----------------------|-----------------------|--------------------------------------------------------------------------------------------------------------|
| BITS                 | VT\_ARRAY \| VT\_BSTR | **textual\_convention**: bits<br/> **encoding**: OCTETSTRING<br/> **cimtype**: string<br/> |



 

-   Variable-length

    When the SYNTAX clause refers to a primitive type, named type, or textual convention that is subtyped as a variable-length OCTET STRING or Opaque, the CIM property qualifier **variable\_length** specifies the minimum, maximum, and fixed-length values associated with the type definition. This qualifier is implemented as a string in the following format where the variable-length values are represented as unsigned 32-bit integers.

    ``` syntax
    (((0.9) .. (0.9)) | (0.9))(, (((0.9) .. (0.9)) | (0.9)))*
    ```

-   Fixed-length

    When the SYNTAX clause refers to a primitive type, named type, or textual convention that is subtyped as a fixed-length OCTET STRING or Opaque, the CIM property qualifier **fixed\_length** specifies the fixed-length value. This qualifier is represented as an unsigned 32-bit integer value.

-   Range

    When the SYNTAX clause refers to a primitive type, named type, or textual convention that is subtyped as a ranged or fixed-value INTEGER or Gauge, the CIM property qualifier **variable\_value** specifies the ranged and fixed values associated with the type definition. This qualifier is implemented as a string in the following format where the range and fixed-length values are represented as unsigned 32-bit integers.

    ``` syntax
    (((0.9)..(0.9))|(0.9))(,(((0.9)..(0.9))|(0.9)))*
    ```

## Example Code

The following example describes an enumerated INTEGER subtype.

``` syntax
Status := INTEGER {
up(1),
down(2),
testing(3)
}
```

This example maps to:

``` syntax
enumeration("up(1),down(2),testing(3)")
```

The following code example describes a BITS subtype.

``` syntax
Status := BITS {
up(1),
down(2), 
testing(3)
}
```

The following code example maps to:

``` syntax
bits("up(1),down(2),testing(3)")
```

The following code example describes a variable-length subtype.

``` syntax
MySnmpOSIAddress ::=  TEXTUAL-CONVENTION

    DISPLAY-HINT    "*1x:/1x:"
    STATUS        current
    DESCRIPTION
            "Represents an OSI transport-address:

            octets    contents         encoding
              1        length of NSAP   'n' as an unsigned-integer
                                        (either 0 or from 3 to 20)
              2..(n+1)  NSAP          concrete binary representation
              (n+2)..m  TSEL             string of (up to 64) octets
            "
    SYNTAX         OCTET STRING (SIZE (1|4..85))
```

This example maps to:

``` syntax
display_hint("*1x:/1x:"),
encoding("OCTETSTRING"),
textual_convention("OCTETSTRING"),
variable_length ("1,4..85")
```

The following example describes a fixed-length subtype.

``` syntax
IPXADDRESS := OCTET STRING (SIZE (6))
```

This example maps to:

``` syntax
fixed_length(6)
```

The following example describes a range subtype.

``` syntax
Status := INTEGER (10..20|8)
```

This example maps to:

``` syntax
variable_value("10..20,8")
```

 

 




