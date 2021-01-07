---
description: Describes WMI SNMP provider errors 1091 through 1100.
ms.assetid: 9b7db4fc-8ae8-46f7-a40f-e4401a335c5d
ms.tgt_platform: multiple
title: Errors 1091 through 1100
ms.topic: article
ms.date: 05/31/2018
---

# Errors 1091 through 1100

Describes WMI SNMP provider errors 1091 through 1100.

[Warning 1091](#warning-1091)

[Fatal Error 1092](#fatal-error-1092)

[Fatal Error 1093](#fatal-error-1093)

[Fatal Error 1094](#fatal-error-1094)

[Fatal Error 1095](#fatal-error-1095)

[Fatal Error 1097](#fatal-error-1097)

[Fatal Error 1098](#fatal-error-1098)

[Fatal Error 1099](#fatal-error-1099)

## Warning 1091

<dl> <dt>

<span id="_1091__Warning_____fileName___line___IMPLIED_clause_is_not_allowed_for_fixed_size_objects_"></span><span id="_1091__warning_____filename___line___implied_clause_is_not_allowed_for_fixed_size_objects_"></span><span id="_1091__WARNING_____FILENAME___LINE___IMPLIED_CLAUSE_IS_NOT_ALLOWED_FOR_FIXED_SIZE_OBJECTS_"></span>**<1091, Warning>: "<fileName>:<line\#> IMPLIED clause is not allowed for fixed size objects"**
</dt> <dd>

**OBJECT-TYPE** macro invocation SNMPv2C-specific module semantic warning. The IMPLIED keyword can only be present for an object having a variable-length syntax, such as an OBJECT IDENTIFIER or variable-length OCTET STRING, in the INDEX clause.

</dd> </dl>

## Fatal Error 1092

<dl> <dt>

<span id="_1092__Fatal_____fileName___line___IMPLIED_clause_not_allowed_for_potentially_zero-length_objects_"></span><span id="_1092__fatal_____filename___line___implied_clause_not_allowed_for_potentially_zero-length_objects_"></span><span id="_1092__FATAL_____FILENAME___LINE___IMPLIED_CLAUSE_NOT_ALLOWED_FOR_POTENTIALLY_ZERO-LENGTH_OBJECTS_"></span>**<1092, Fatal>: "<fileName>:<line\#> IMPLIED clause not allowed for potentially zero-length objects"**
</dt> <dd>

**OBJECT-TYPE** macro invocation SNMPv2C-specific module semantic error. The IMPLIED clause cannot be used on a variable-length object if that object can have a zero length.

</dd> </dl>

## Fatal Error 1093

<dl> <dt>

<span id="_1093._Fatal_____fileName__line____Only_the_type__INTEGER__can_be_enumerated_according_to_the_V1_SMI_"></span><span id="_1093._fatal_____filename__line____only_the_type__integer__can_be_enumerated_according_to_the_v1_smi_"></span><span id="_1093._FATAL_____FILENAME__LINE____ONLY_THE_TYPE__INTEGER__CAN_BE_ENUMERATED_ACCORDING_TO_THE_V1_SMI_"></span>**<1093. Fatal>: "<fileName><line\#>: Only the type "INTEGER" can be enumerated according to the V1 SMI"**
</dt> <dd>

Type assignment, SNMPv1-specific module semantic error. An SNMPv1 MIB enumeration can use only the type INTEGER.

</dd> </dl>

## Fatal Error 1094

<dl> <dt>

<span id="_1094._Fatal_____fileName__line____The_type_used_in_the_enumeration_does_not_resolve_to_one_of_the_allowed_types_"></span><span id="_1094._fatal_____filename__line____the_type_used_in_the_enumeration_does_not_resolve_to_one_of_the_allowed_types_"></span><span id="_1094._FATAL_____FILENAME__LINE____THE_TYPE_USED_IN_THE_ENUMERATION_DOES_NOT_RESOLVE_TO_ONE_OF_THE_ALLOWED_TYPES_"></span>**<1094. Fatal>: "<fileName><line\#>: The type used in the enumeration does not resolve to one of the allowed types"**
</dt> <dd>

Type assignment, SNMPv2C-specific module semantic error. The type used in an enumeration must be INTEGER or an equivalent type, or another enumeration.

</dd> </dl>

## Fatal Error 1095

<dl> <dt>

<span id="_1095._Fatal_____fileName__line____Enumeration_member_is_not_a_member_of_the_parent_enumeration_"></span><span id="_1095._fatal_____filename__line____enumeration_member_is_not_a_member_of_the_parent_enumeration_"></span><span id="_1095._FATAL_____FILENAME__LINE____ENUMERATION_MEMBER_IS_NOT_A_MEMBER_OF_THE_PARENT_ENUMERATION_"></span>**<1095. Fatal>: "<fileName><line\#>: Enumeration member is not a member of the parent enumeration"**
</dt> <dd>

Type assignment, SNMPv2C-specific module semantic error. If another enumeration is used, its set of items must be a subset of the parent enumeration's set of items.

</dd> </dl>

## Fatal Error 1097

<dl> <dt>

<span id="_1097__Fatal_____fileName__line____identifier__name__does_not_resolve_to_an_integer_value_"></span><span id="_1097__fatal_____filename__line____identifier__name__does_not_resolve_to_an_integer_value_"></span><span id="_1097__FATAL_____FILENAME__LINE____IDENTIFIER__NAME__DOES_NOT_RESOLVE_TO_AN_INTEGER_VALUE_"></span>**<1097, Fatal>: "<fileName><line\#>: identifier <name> does not resolve to an integer value"**
</dt> <dd>

Type assignment, SNMPv2C-specific module semantic error. The values in the BITS type must be integer values.

</dd> </dl>

## Fatal Error 1098

<dl> <dt>

<span id="_1098__Fatal_____fileName__line____Duplicate_value__value__in_BITS_construct_"></span><span id="_1098__fatal_____filename__line____duplicate_value__value__in_bits_construct_"></span><span id="_1098__FATAL_____FILENAME__LINE____DUPLICATE_VALUE__VALUE__IN_BITS_CONSTRUCT_"></span>**<1098, Fatal>: "<fileName><line\#>: Duplicate value <value> in BITS construct"**
</dt> <dd>

Type assignment, SNMPv2C-specific module semantic error. There must be no duplicate names and values in a BITS construct. The <line\#> parameter is the position of the recurrence of the name/value.

</dd> </dl>

## Fatal Error 1099

<dl> <dt>

<span id="_1099__Fatal_____fileName__line____Duplicate_name__identifier__in_BITS_construct_"></span><span id="_1099__fatal_____filename__line____duplicate_name__identifier__in_bits_construct_"></span><span id="_1099__FATAL_____FILENAME__LINE____DUPLICATE_NAME__IDENTIFIER__IN_BITS_CONSTRUCT_"></span>**<1099, Fatal>: "<fileName><line\#>: Duplicate name <identifier> in BITS construct"**
</dt> <dd>

Type assignment, SNMPv2C-specific module semantic error. There must be no duplicate names and values in a BITS construct. The <line\#> parameter is the position of the recurrence of the name/value.

</dd> </dl>

 

 



