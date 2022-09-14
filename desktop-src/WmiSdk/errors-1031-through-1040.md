---
description: Describes WMI SNMP provider errors 1031 through 1040.
ms.assetid: 5fc519ac-ae05-4daf-a681-7935190f1d46
ms.tgt_platform: multiple
title: Errors 1031 through 1040
ms.topic: article
ms.date: 05/31/2018
---

# Errors 1031 through 1040

Describes WMI SNMP provider errors 1031 through 1040.

[Warning 1031](#warning-1031)

[Fatal Error 1032](#fatal-error-1032)

[Fatal Error 1033](#fatal-error-1033)

[Warning 1034](#warning-1034)

[Warning 1036](#warning-1036)

[Fatal Error 1037](#fatal-error-1037)

[Fatal Error 1038](#fatal-error-1038)

[Fatal Error 1039](#fatal-error-1039)

[Fatal Error 1040](#fatal-error-1040)

## Warning 1031

<dl> <dt>

<span id="_1031__Warning_____fileName___line____Standard_symbol__identifier__should_be_imported_from_module__identifier_._Assuming_the_standard_definition._"></span><span id="_1031__warning_____filename___line____standard_symbol__identifier__should_be_imported_from_module__identifier_._assuming_the_standard_definition._"></span><span id="_1031__WARNING_____FILENAME___LINE____STANDARD_SYMBOL__IDENTIFIER__SHOULD_BE_IMPORTED_FROM_MODULE__IDENTIFIER_._ASSUMING_THE_STANDARD_DEFINITION._"></span>**<1031, Warning>: "&lt;fileName&gt;:<line\#>: Standard symbol &lt;identifier&gt; should be imported from module &lt;identifier&gt;. Assuming the standard definition."**
</dt> <dd>

IMPORTS section module semantic warning, specific to neither SNMPv1 nor SNMPv2C. If an SNMP identifier known to the compiler is in the IMPORTS section, then the module from which it is imported must be one of the standard modules.

Certain commonly used IMPORTS are "assumed knowledge" on the part of the compiler. It is unnecessary for the compiler to require access to other information modules to resolve these.

The built-in SNMPv1 and SNMPv2C IMPORTS are described in the following tables.

</dd> </dl>

**Built-in SNMPv1 IMPORTS**



| Import Class | Module      | Instances                                                           |
|--------------|-------------|---------------------------------------------------------------------|
| ASN.1 Value  | RFC1155-SMI | Internet, directory, management, experimental, private, enterprises |
|              | RFC1213-MIB | MIB-II and IP, interfaces, transmission                             |
| ASN.1 Type   | RFC1155-SMI | NetworkAddress, IpAddress, Counter, Gauge, TimeTicks, Opaque        |
|              | RFC1213-MIB | DisplayString, PhysAddress                                          |
| ASN.1 Macro  | RFC-1212    | OBJECT-TYPE                                                         |
|              | RFC-1215    | TRAP-TYPE                                                           |



 

**Built-in SNMPv2C IMPORTS**



| Import Class       | Module      | Instances                                                                                                                                                                                                      |
|--------------------|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ASN.1 Value        | SNMPv2-SMI  | org, dod, Internet, directory, mgmt, mib-2, transmission, experimental, private, enterprises, security, snmpv2, snmpDomains, snmpProxys, snmpModules                                                           |
|                    | SNMPv2-TM   | rfc1157Proxy                                                                                                                                                                                                   |
| Object Identity    | SNMPv2-SMI  | zeroDotZero                                                                                                                                                                                                    |
|                    | SNMPv2-TM   | snmpUDPDomain, snmpCLNSDomain, smnpCONSDomain, snmpDDPDomain, snmpIPXDomain, rfc1157Domain                                                                                                                     |
| ASN.1 Type         | SNMPv2-SMI  | Integer32, IpAddress, Counter32, TimeTicks, Opaque, Counter64, Unsigned32, Gauge32                                                                                                                             |
| ASN.1 Macro        | SNMPv2-SMI  | MODULE-IDENTITY, OBJECT-IDENTITY, OBJECT-TYPE, NOTIFICATION-TYPE                                                                                                                                               |
|                    | SNMPv2-CONF | OBJECT-GROUP, NOTIFICATION-GROUP, MODULE-COMPLIANCE, AGENT-CAPABILITIES                                                                                                                                        |
|                    | SNMPv2-TC   | TEXTUAL-CONVENTION                                                                                                                                                                                             |
| Textual Convention | SNMPv2-TC   | DisplayString, PhysAddress, MacAddress, TruthValue, TestAndIncr, AutonomousType, InstancePointer, VariablePointer, RowPointer, RowStatus, TimeStamp, TimeInterval, DateAndTime, StorageType, Tdomain, Taddress |
|                    | SNMPv2-TM   | SnmpUDPAddress, SnmpOSIAddress, SnmpNBPAddress, SnmpIPXAddress                                                                                                                                                 |



 

## Fatal Error 1032

<dl> <dt>

<span id="_1032__Fatal_____fileName__line____Duplicate_value__value__in_enumeration_"></span><span id="_1032__fatal_____filename__line____duplicate_value__value__in_enumeration_"></span><span id="_1032__FATAL_____FILENAME__LINE____DUPLICATE_VALUE__VALUE__IN_ENUMERATION_"></span>**<1032, Fatal>: "&lt;fileName&gt;<line\#>: Duplicate value &lt;value&gt; in enumeration"**
</dt> <dd>

Module semantic error in an enumeration, specific to neither SNMPv1 nor SNMPv2C. There must not be any duplicate values. The <line\#> parameter is the position of the recurrence of the name/value.

</dd> </dl>

## Fatal Error 1033

<dl> <dt>

<span id="_1033__Fatal_____fileName__line____Duplicate_name__identifier__in_enumeration_"></span><span id="_1033__fatal_____filename__line____duplicate_name__identifier__in_enumeration_"></span><span id="_1033__FATAL_____FILENAME__LINE____DUPLICATE_NAME__IDENTIFIER__IN_ENUMERATION_"></span>**<1033, Fatal>: "&lt;fileName&gt;<line\#>: Duplicate name &lt;identifier&gt; in enumeration"**
</dt> <dd>

Module semantic error in an enumeration, specific to neither SNMPv1 nor SNMPv2C. There must not be any duplicate names. The <line\#> parameter is the position of the recurrence of the name/value.

</dd> </dl>

## Warning 1034

<dl> <dt>

<span id="_1034__Warning_____fileName__line____A_value_of_0_disallowed_in_an_enumeration_"></span><span id="_1034__warning_____filename__line____a_value_of_0_disallowed_in_an_enumeration_"></span><span id="_1034__WARNING_____FILENAME__LINE____A_VALUE_OF_0_DISALLOWED_IN_AN_ENUMERATION_"></span>**<1034, Warning>: "&lt;fileName&gt;<line\#>: A value of 0 disallowed in an enumeration"**
</dt> <dd>

Module semantic warning in an enumeration, specific to neither SNMPv1 nor SNMPv2C. It is recommended that a named value of zero not be used in an enumeration.

</dd> </dl>

## Warning 1036

<dl> <dt>

<span id="_1036__Warning____fileName__line____Value_in_enumeration_does_not_resolve_to_a_positive_integer_"></span><span id="_1036__warning____filename__line____value_in_enumeration_does_not_resolve_to_a_positive_integer_"></span><span id="_1036__WARNING____FILENAME__LINE____VALUE_IN_ENUMERATION_DOES_NOT_RESOLVE_TO_A_POSITIVE_INTEGER_"></span>**<1036, Warning> "&lt;fileName&gt;<line\#>: Value in enumeration does not resolve to a positive integer"**
</dt> <dd>

Module semantic warning in an enumeration, specific to neither SNMPv1 nor SNMPv2C. A negative value is not allowed in an enumeration.

</dd> </dl>

## Fatal Error 1037

<dl> <dt>

<span id="_1037__Fatal_____fileName__line____Identifier__identifier__does_not_resolve_to_OCTET_STRING_or_Opaque_types_"></span><span id="_1037__fatal_____filename__line____identifier__identifier__does_not_resolve_to_octet_string_or_opaque_types_"></span><span id="_1037__FATAL_____FILENAME__LINE____IDENTIFIER__IDENTIFIER__DOES_NOT_RESOLVE_TO_OCTET_STRING_OR_OPAQUE_TYPES_"></span>**<1037, Fatal>: "&lt;fileName&gt;<line\#>: Identifier &lt;identifier&gt; does not resolve to OCTET STRING or Opaque types"**
</dt> <dd>

Module semantic error in SIZE specification, specific to neither SNMPv1 nor SNMPv2C. The symbol used in a SIZE specification must resolve to OCTET STRING or Opaque.

</dd> </dl>

## Fatal Error 1038

<dl> <dt>

<span id="_1038__Fatal_____fileName__line____Identifier__identifier__does_not_resolve_an_INTEGER_or_Gauge_type_"></span><span id="_1038__fatal_____filename__line____identifier__identifier__does_not_resolve_an_integer_or_gauge_type_"></span><span id="_1038__FATAL_____FILENAME__LINE____IDENTIFIER__IDENTIFIER__DOES_NOT_RESOLVE_AN_INTEGER_OR_GAUGE_TYPE_"></span>**<1038, Fatal>: "&lt;fileName&gt;<line\#>: Identifier &lt;identifier&gt; does not resolve an INTEGER or Gauge type"**
</dt> <dd>

Module semantic error in range specification. This error can occur in either SNMPv1 or SNMPv2C.

In SNMPv1, the symbol used in a Range specification must resolve to INTEGER or Gauge.

In SNMPv2C, the symbol used in a Range specification must resolve to INTEGER, Gauge32, Integer32, or Unsigned32.

</dd> </dl>

## Fatal Error 1039

<dl> <dt>

<span id="_1039__Fatal___fileName__line____Negative_value_used_in_SIZE_specification_"></span><span id="_1039__fatal___filename__line____negative_value_used_in_size_specification_"></span><span id="_1039__FATAL___FILENAME__LINE____NEGATIVE_VALUE_USED_IN_SIZE_SPECIFICATION_"></span>**<1039, Fatal>:&lt;fileName&gt;<line\#>: Negative value used in SIZE specification"**
</dt> <dd>

Module semantic error in SIZE specification, specific to neither SNMPv1 nor SNMPv2C. Any value used in specifying the SIZE must be non-negative.

</dd> </dl>

## Fatal Error 1040

<dl> <dt>

<span id="_1040__Fatal_____fileName__line____Identifier__identifier__in_SIZE_specification_does_not_resolve_to_a_non-negative_integral_value_"></span><span id="_1040__fatal_____filename__line____identifier__identifier__in_size_specification_does_not_resolve_to_a_non-negative_integral_value_"></span><span id="_1040__FATAL_____FILENAME__LINE____IDENTIFIER__IDENTIFIER__IN_SIZE_SPECIFICATION_DOES_NOT_RESOLVE_TO_A_NON-NEGATIVE_INTEGRAL_VALUE_"></span>**<1040, Fatal>: "&lt;fileName&gt;<line\#>: Identifier &lt;identifier&gt; in SIZE specification does not resolve to a non-negative integral value"**
</dt> <dd>

Module semantic error in range or size specification, specific to neither SNMPv1 nor SNMPv2C. Any symbol used in specifying a value in a SIZE specification resolves to a non-negative value.

</dd> </dl>

 

 



