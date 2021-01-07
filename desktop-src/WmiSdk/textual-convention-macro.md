---
description: SNMP textual conventions map to CIM-defined types.
ms.assetid: 73bb6c22-0a68-4a4b-8de2-8326ec67a059
ms.tgt_platform: multiple
title: TEXTUAL-CONVENTION Macro
ms.topic: article
ms.date: 05/31/2018
---

# TEXTUAL-CONVENTION Macro

SNMP textual conventions map to CIM-defined types.

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 

The following mapping rules apply to SNMP textual conventions:

-   The named type definition in the SYNTAX clause maps verbatim to the CIM property qualifier **object\_syntax**.
-   Use the following table to map textual conventions when the SYNTAX clause explicitly refers to a textual convention of a SNMPv2C TEXTUAL-CONVENTION macro, or refers to an implied textual convention. The default value is always **NULL**.



| Textual convention | CIM variant type | CIM qualifier                                                                                                                                                        |
|--------------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DateAndTime        | **VT\_BSTR**     | **textual\_convention**: DateAndTime<br/> **encoding**: OCTETSTRING<br/> **object\_syntax**: DateAndTime<br/> **cimtype**: string<br/>       |
| Displaystring      | **VT\_BSTR**     | **textual\_convention**: Displaystring<br/> **encoding**: OCTETSTRING<br/> **object\_syntax**: Displaystring<br/> **cimtype**: string<br/>   |
| MacAddress         | **VT\_BSTR**     | **textual\_convention**: MacAddress<br/> **encoding**: OCTETSTRING<br/> **object\_syntax**: MacAddress<br/> **cimtype**: string<br/>         |
| PhysAddress        | **VT\_BSTR**     | **textual\_convention**: PhysAddress<br/> **encoding**: OCTETSTRING<br/> **object\_syntax**: PhysAddress<br/> **cimtype**: string<br/>       |
| SnmpUDPAddress     | **VT\_BSTR**     | **textual\_convention**: SnmpUDPAddress<br/> **encoding**: OCTETSTRING<br/> **object\_syntax**: SnmpUDPAddress<br/> **cimtype**: string<br/> |
| SnmpOSIAddress     | **VT\_BSTR**     | **textual\_convention**: SnmpOSIAddress<br/> **encoding**: OCTETSTRING<br/> **object\_syntax**: SnmpOSIAddress<br/> **cimtype**: string<br/> |
| SnmpIPXAddress     | **VT\_BSTR**     | **textual\_convention**: SnmpIPXAddress<br/> **encoding**: OCTETSTRING<br/> **object\_syntax**: SnmpIPXAddress<br/> **cimtype**: string<br/> |



 

-   The CIM-defined variant type and the CIM property qualifiers **textual\_convention**, **encoding**, **object\_syntax**, and **cimtype** map using the underlying primitive type.
-   The DISPLAY-HINT clause of the SNMPv2C TEXTUAL-CONVENTION macro maps verbatim to the CIM property qualifier **display\_hint**. This qualifier is not generated if there is no TEXTUAL-CONVENTION macro, or the macro does not contain a DISPLAY-HINT clause.

## Example Code

The following example describes an SNMPv1 textual convention.

``` syntax
myNamedType ::= DISPLAYSTRING (SIZE (0..127))

myNamedProperty OBJECT-TYPE
SYNTAX  myNamedType
ACCESS read-only
STATUS MANDATORY
DESCRIPTION ""
```

This example generates the following CIM qualifiers.

``` syntax
object_syntax("myNamedType"),
textual_convention("DISPLAYSTRING"),
encoding("OCTETSTRING"),
variable_length("0..127")
```

The following example describes an SNMPv2 textual convention.

``` syntax
myDisplaystring ::= TEXTUAL-CONVENTION
DISPLAY-HINT "255a"
STATUS current
DESCRIPTION "" 
SYNTAX OCTET STRING (SIZE (0..127))

myNamedProperty OBJECT-TYPE
SYNTAX  myDisplaystring
MAX-ACCESS read-only
STATUS current
DESCRIPTION ""
```

This example generates the following CIM qualifiers.

``` syntax
object_syntax("myDisplaystring"),
textual_convention("OCTETSTRING"),
encoding("OCTETSTRING"),
display_hint("255a"),
variable_length("0..127")
```

 

 




