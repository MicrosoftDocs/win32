---
description: Describes WMI SNMP provider errors 1051 through 1060.
ms.assetid: 789cc5b6-e3ef-4f66-8dec-6970d6df1fe9
ms.tgt_platform: multiple
title: Errors 1051 through 1060
ms.topic: article
ms.date: 05/31/2018
---

# Errors 1051 through 1060

Describes WMI SNMP provider errors 1051 through 1060.

[Fatal Error 1051](#fatal-error-1051)

[Fatal Error 1054](#fatal-error-1054)

[Fatal Error 1055](#fatal-error-1055)

## Fatal Error 1051

<dl> <dt>

<span id="_1051__Fatal_____fileName___line____Ambiguous_reference_to_symbol__identifier__"></span><span id="_1051__fatal_____filename___line____ambiguous_reference_to_symbol__identifier__"></span><span id="_1051__FATAL_____FILENAME___LINE____AMBIGUOUS_REFERENCE_TO_SYMBOL__IDENTIFIER__"></span>**<1051, Fatal>: "<fileName>:<line\#>: Ambiguous reference to symbol <identifier>"**
</dt> <dd>

IMPORTS section module semantic error, specific to neither SNMPv1 nor SNMPv2C. Each object descriptor corresponding to an object in an Internet Standard MIB must be unique. Since enterprise MIBs can have common object descriptors, such descriptors imported from two modules must be used unambiguously in the MIB module by using the notation "module.descriptor."

</dd> </dl>

## Fatal Error 1054

<dl> <dt>

<span id="_1054__Fatal_____fileName___line_____identifier__in_INDEX_clause_does_not_resolve_to_one_of_the_allowed_types_"></span><span id="_1054__fatal_____filename___line_____identifier__in_index_clause_does_not_resolve_to_one_of_the_allowed_types_"></span><span id="_1054__FATAL_____FILENAME___LINE_____IDENTIFIER__IN_INDEX_CLAUSE_DOES_NOT_RESOLVE_TO_ONE_OF_THE_ALLOWED_TYPES_"></span>**<1054, Fatal>: "<fileName>:<line\#>: <identifier> in INDEX clause does not resolve to one of the allowed types"**
</dt> <dd>

**OBJECT-TYPE** macro invocation module semantic error. The type of an object in the INDEX clause, or any type specified in the INDEX clause, must resolve to a scalar type, that is, a non-SEQUENCE or non-SEQUENCE OF type. Any type specified in the INDEX clause must also resolve to one of these.

This error can occur in either SNMPv1 or SNMPv2C.

</dd> </dl>

## Fatal Error 1055

<dl> <dt>

<span id="_1055__Fatal____fileName___line____SYNTAX_of_INDEX_OBJECT-TYPE__identifier___does_not_resolve_to_one_of_the_allowed_types_"></span><span id="_1055__fatal____filename___line____syntax_of_index_object-type__identifier___does_not_resolve_to_one_of_the_allowed_types_"></span><span id="_1055__FATAL____FILENAME___LINE____SYNTAX_OF_INDEX_OBJECT-TYPE__IDENTIFIER___DOES_NOT_RESOLVE_TO_ONE_OF_THE_ALLOWED_TYPES_"></span>**<1055, Fatal>:"<fileName>:<line\#>: SYNTAX of INDEX OBJECT-TYPE <identifier>, does not resolve to one of the allowed types"**
</dt> <dd>

**OBJECT-TYPE** macro invocation module semantic error. The type of an object in the INDEX clause, or any type specified in the INDEX clause, must resolve to a scalar type, that is, a non-SEQUENCE or non-SEQUENCE OF type.

This error can occur in either SNMPv1 or SNMPv2C.

</dd> </dl>

 

 



