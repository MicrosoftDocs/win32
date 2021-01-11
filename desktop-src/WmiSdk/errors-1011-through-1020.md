---
description: Describes WMI SNMP provider errors 1011 through 1020.
ms.assetid: 5151a110-1532-48cc-832a-2cee21853b6b
ms.tgt_platform: multiple
title: Errors 1011 through 1020
ms.topic: article
ms.date: 05/31/2018
---

# Errors 1011 through 1020

Describes WMI SNMP provider errors 1011 through 1020.

[Fatal Error 1011](#fatal-error-1011)

[Fatal Error 1012](#fatal-error-1012)

[Fatal Error 1013](#fatal-error-1013)

[Warning 1014](#warning-1014)

[Fatal Error 1015](#fatal-error-1015)

[Fatal Error 1016](#fatal-error-1016)

[Fatal Error 1018](#fatal-error-1018)

[Fatal Error 1020](#fatal-error-1020)

## Fatal Error 1011

<dl> <dt>

<span id="_1011__Fatal_____fileName___line___the_SYNTAX_of_member__identifier__of_SEQUENCE___identifier___differs_from_the_SYNTAX_clause_of_the_OBJECT-TYPE_"></span><span id="_1011__fatal_____filename___line___the_syntax_of_member__identifier__of_sequence___identifier___differs_from_the_syntax_clause_of_the_object-type_"></span><span id="_1011__FATAL_____FILENAME___LINE___THE_SYNTAX_OF_MEMBER__IDENTIFIER__OF_SEQUENCE___IDENTIFIER___DIFFERS_FROM_THE_SYNTAX_CLAUSE_OF_THE_OBJECT-TYPE_"></span>**<1011, Fatal>: "<fileName>:<line\#> the SYNTAX of member <identifier> of SEQUENCE, <identifier>, differs from the SYNTAX clause of the OBJECT-TYPE"**
</dt> <dd>

**OBJECT-TYPE** macro invocation module semantic error. An element of a SEQUENCE must be same as the type in the SYNTAX clause of the OBJECT-TYPE definition. The <line\#> parameter is the line of the SYNTAX clause of the OBJECT-TYPE definition.

This error can occur in either SNMPv1 or SNMPv2C.

</dd> </dl>

## Fatal Error 1012

<dl> <dt>

<span id="_1012__Fatal_____fileName___line___An_INDEX_or_AUGMENTS_clause_is_required_only_for_SEQUENCE_OBJECT-TYPES_"></span><span id="_1012__fatal_____filename___line___an_index_or_augments_clause_is_required_only_for_sequence_object-types_"></span><span id="_1012__FATAL_____FILENAME___LINE___AN_INDEX_OR_AUGMENTS_CLAUSE_IS_REQUIRED_ONLY_FOR_SEQUENCE_OBJECT-TYPES_"></span>**<1012, Fatal>: "<fileName>:<line\#> An INDEX or AUGMENTS clause is required only for SEQUENCE OBJECT-TYPES"**
</dt> <dd>

**OBJECT-TYPE** macro invocation module semantic error. An INDEX clause must only be present in an OBJECT-TYPE definition whose SYNTAX resolves to a SEQUENCE type.

This error can occur when compiling either an SNMPv1 or SNMPv2C MIB.

</dd> </dl>

## Fatal Error 1013

<dl> <dt>

<span id="_1013__Fatal_____fileName__line_____identifier__should_resolve_to_a_SEQUENCE_type_"></span><span id="_1013__fatal_____filename__line_____identifier__should_resolve_to_a_sequence_type_"></span><span id="_1013__FATAL_____FILENAME__LINE_____IDENTIFIER__SHOULD_RESOLVE_TO_A_SEQUENCE_TYPE_"></span>**<1013, Fatal>: "<fileName><line\#>: <identifier> should resolve to a SEQUENCE type"**
</dt> <dd>

**OBJECT-TYPE** macro invocation module semantic error. A type used in the "SEQUENCE OF" construct must resolve to a SEQUENCE type.

This error can occur in either SNMPv1 or SNMPv2C.

</dd> </dl>

## Warning 1014

<dl> <dt>

<span id="_1014__Warning_____fileName___line____Sub-identifier_of_value_0_not_recommended_in_OIDs_"></span><span id="_1014__warning_____filename___line____sub-identifier_of_value_0_not_recommended_in_oids_"></span><span id="_1014__WARNING_____FILENAME___LINE____SUB-IDENTIFIER_OF_VALUE_0_NOT_RECOMMENDED_IN_OIDS_"></span>**<1014, Warning>: "<fileName>:<line\#>: Sub-identifier of value 0 not recommended in OIDs"**
</dt> <dd>

**OBJECT-TYPE** macro invocation module semantic warning. It is recommended that no object in an Internet Standard MIB use a sub-identifier of zero in its OBJECT IDENTIFIER.

This warning can occur in either SNMPv1 or SNMPv2C.

</dd> </dl>

## Fatal Error 1015

<dl> <dt>

<span id="_1015__Fatal_____fileName___line____OBJECT-TYPEs__identifier__from_module__identifier__and__identifier__from_module__identifier__are_assigned_the_same_OID_values_"></span><span id="_1015__fatal_____filename___line____object-types__identifier__from_module__identifier__and__identifier__from_module__identifier__are_assigned_the_same_oid_values_"></span><span id="_1015__FATAL_____FILENAME___LINE____OBJECT-TYPES__IDENTIFIER__FROM_MODULE__IDENTIFIER__AND__IDENTIFIER__FROM_MODULE__IDENTIFIER__ARE_ASSIGNED_THE_SAME_OID_VALUES_"></span>**<1015, Fatal>: "<fileName>:<line\#>: OBJECT-TYPEs <identifier> from module <identifier> and <identifier> from module <identifier> are assigned the same OID values"**
</dt> <dd>

**OBJECT-TYPE** macro invocation module semantic error. Two **OBJECT-TYPE** invocations (in the same or different modules) must not be assigned the same Object Identifier value.

This error can occur in either SNMPv1 or SNMPv2C.

</dd> </dl>

## Fatal Error 1016

<dl> <dt>

<span id="_1016__Fatal_____fileName___line____Value_in_the_DEFVAL_clause_does_not_match_the_type_in_the_SYNTAX_clause_"></span><span id="_1016__fatal_____filename___line____value_in_the_defval_clause_does_not_match_the_type_in_the_syntax_clause_"></span><span id="_1016__FATAL_____FILENAME___LINE____VALUE_IN_THE_DEFVAL_CLAUSE_DOES_NOT_MATCH_THE_TYPE_IN_THE_SYNTAX_CLAUSE_"></span>**<1016, Fatal>: "<fileName>:<line\#>: Value in the DEFVAL clause does not match the type in the SYNTAX clause"**
</dt> <dd>

**OBJECT-TYPE** macro invocation module semantic error. A value in a DEFVAL clause must be a value of the type mentioned in the SYNTAX clause.

This error can occur in either SNMPv1 or SNMPv2C.

</dd> </dl>

## Fatal Error 1018

<dl> <dt>

<span id="_1018__Fatal_____fileName__line_____symbol__in_ENTERPRISE_clause_of_TRAP-TYPE_does_not_resolve_to_an_OID_value_"></span><span id="_1018__fatal_____filename__line_____symbol__in_enterprise_clause_of_trap-type_does_not_resolve_to_an_oid_value_"></span><span id="_1018__FATAL_____FILENAME__LINE_____SYMBOL__IN_ENTERPRISE_CLAUSE_OF_TRAP-TYPE_DOES_NOT_RESOLVE_TO_AN_OID_VALUE_"></span>**<1018, Fatal>: "<fileName><line\#>: <symbol> in ENTERPRISE clause of TRAP-TYPE does not resolve to an OID value"**
</dt> <dd>

**TRAP-TYPE** macro invocation, SNMPv1-specific module semantic error. The symbol used in the ENTERPRISE clause of a **TRAP-TYPE** macro invocation must resolve to an Object Identifier value.

</dd> </dl>

## Fatal Error 1020

<dl> <dt>

<span id="_1020__Fatal_____fileName__line____Value_assigned_to_TRAP-TYPE__identifier__does_not_resolve_to_a_positive_integer_"></span><span id="_1020__fatal_____filename__line____value_assigned_to_trap-type__identifier__does_not_resolve_to_a_positive_integer_"></span><span id="_1020__FATAL_____FILENAME__LINE____VALUE_ASSIGNED_TO_TRAP-TYPE__IDENTIFIER__DOES_NOT_RESOLVE_TO_A_POSITIVE_INTEGER_"></span>**<1020, Fatal>: "<fileName><line\#>: Value assigned to TRAP-TYPE <identifier> does not resolve to a positive integer"**
</dt> <dd>

**TRAP-TYPE** macro invocation, SNMPv1-specific module semantic error. A symbol used in specifying the trap value does not resolve to a positive integer.

</dd> </dl>

 

 



