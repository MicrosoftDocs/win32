---
description: Describes WMI SNMP provider errors 1021 through 1033.
ms.assetid: fc638d0f-20f4-46d0-a36a-c3898415f35c
ms.tgt_platform: multiple
title: Errors 1021 through 1030
ms.topic: article
ms.date: 05/31/2018
---

# Errors 1021 through 1030

Describes WMI SNMP provider errors 1021 through 1033.

[Fatal Error 1021](#fatal-error-1021)

[Fatal Error 1022](#fatal-error-1022)

[Fatal Error 1023](#fatal-error-1023)

[Fatal Error 1024](#fatal-error-1024)

[Fatal Error 1025](#fatal-error-1025)

[Fatal Error 1026](#fatal-error-1026)

[Warning 1027](#warning-1027)

[Fatal Error 1028](#fatal-error-1028)

[Fatal Error 1029](#fatal-error-1029)

[Fatal Error 1030](#fatal-error-1030)

## Fatal Error 1021

<dl> <dt>

<span id="_1021__Fatal_____fileName__line____Identifier__identifier__in_the_VARIABLES_clause_of_TRAP-TYPE_does_not_resolve_to_a_scalar_OBJECT-TYPE_"></span><span id="_1021__fatal_____filename__line____identifier__identifier__in_the_variables_clause_of_trap-type_does_not_resolve_to_a_scalar_object-type_"></span><span id="_1021__FATAL_____FILENAME__LINE____IDENTIFIER__IDENTIFIER__IN_THE_VARIABLES_CLAUSE_OF_TRAP-TYPE_DOES_NOT_RESOLVE_TO_A_SCALAR_OBJECT-TYPE_"></span>**<1021, Fatal>: "&lt;fileName&gt;<line\#>: Identifier &lt;identifier&gt; in the VARIABLES clause of TRAP-TYPE does not resolve to a scalar OBJECT-TYPE"**
</dt> <dd>

**TRAP-TYPE** macro invocation, SNMPv1-specific module semantic error. Each item in the list of variables used in the VARIABLES clause of a **TRAP-TYPE** macro invocation must resolve to the name of a scalar OBJECT-TYPE instance.

</dd> </dl>

## Fatal Error 1022

<dl> <dt>

<span id="_1022__Fatal_____fileName__line____Value_does_not_resolve_to_type__type__"></span><span id="_1022__fatal_____filename__line____value_does_not_resolve_to_type__type__"></span><span id="_1022__FATAL_____FILENAME__LINE____VALUE_DOES_NOT_RESOLVE_TO_TYPE__TYPE__"></span>**<1022, Fatal>: "&lt;fileName&gt;<line\#>: Value does not resolve to type &lt;type&gt;"**
</dt> <dd>

Value assignment module semantic error, specific to neither SNMPv1 nor SNMPv2C. The value on the RHS of an INTEGER, **NULL**, OCTET STRING, or OBJECT IDENTIFIER value assignment is of the wrong type.

</dd> </dl>

## Fatal Error 1023

<dl> <dt>

<span id="_1023__Fatal_____fileName__line____Identifier__identifier__does_not_resolve_to_the_type__identifier__"></span><span id="_1023__fatal_____filename__line____identifier__identifier__does_not_resolve_to_the_type__identifier__"></span><span id="_1023__FATAL_____FILENAME__LINE____IDENTIFIER__IDENTIFIER__DOES_NOT_RESOLVE_TO_THE_TYPE__IDENTIFIER__"></span>**<1023, Fatal>: "&lt;fileName&gt;<line\#>: Identifier &lt;identifier&gt; does not resolve to the type &lt;identifier&gt;"**
</dt> <dd>

Value assignment module semantic error, specific to neither SNMPv1 nor SNMPv2C. A symbol (value reference) on the RHS of an INTEGER, **NULL**, OCTET STRING, or OBJECT IDENTIFIER value assignment does not resolve to the right type.

</dd> </dl>

## Fatal Error 1024

<dl> <dt>

<span id="_1024__Fatal_____fileName__line____Negative_integer_in_OID_value_definition_"></span><span id="_1024__fatal_____filename__line____negative_integer_in_oid_value_definition_"></span><span id="_1024__FATAL_____FILENAME__LINE____NEGATIVE_INTEGER_IN_OID_VALUE_DEFINITION_"></span>**<1024, Fatal>: "&lt;fileName&gt;<line\#>: Negative integer in OID value definition"**
</dt> <dd>

Value assignment module semantic error, specific to neither SNMPv1 nor SNMPv2C. All values in an OID component list must be non-negative (preferably positive) integers.

</dd> </dl>

## Fatal Error 1025

<dl> <dt>

<span id="_1025__Fatal____Identifier__identifier__in_OID_value_does_not_resolve_to_a_positive_integer_"></span><span id="_1025__fatal____identifier__identifier__in_oid_value_does_not_resolve_to_a_positive_integer_"></span><span id="_1025__FATAL____IDENTIFIER__IDENTIFIER__IN_OID_VALUE_DOES_NOT_RESOLVE_TO_A_POSITIVE_INTEGER_"></span>**<1025, Fatal>: "Identifier &lt;identifier&gt; in OID value does not resolve to a positive integer"**
</dt> <dd>

Value assignment module semantic error, specific to neither SNMPv1 nor SNMPv2C. All values in an OID component list must be non-negative (preferably positive) integers.

</dd> </dl>

## Fatal Error 1026

<dl> <dt>

<span id="_1026__Fatal_____fileName__line____Identifier__identifier__in_OID_value_neither_resolves_to_an_OID_value_nor_a_positive_integer_"></span><span id="_1026__fatal_____filename__line____identifier__identifier__in_oid_value_neither_resolves_to_an_oid_value_nor_a_positive_integer_"></span><span id="_1026__FATAL_____FILENAME__LINE____IDENTIFIER__IDENTIFIER__IN_OID_VALUE_NEITHER_RESOLVES_TO_AN_OID_VALUE_NOR_A_POSITIVE_INTEGER_"></span>**<1026, Fatal>: "&lt;fileName&gt;<line\#>: Identifier &lt;identifier&gt; in OID value neither resolves to an OID value nor a positive integer"**
</dt> <dd>

Value assignment module semantic error, specific to neither SNMPv1 nor SNMPv2C. The first component used in an OID value must resolve to an OID value or an INTEGER.

</dd> </dl>

## Warning 1027

<dl> <dt>

<span id="_1027__Warning_____fileName__line____Imported_symbol__identifier__unused_"></span><span id="_1027__warning_____filename__line____imported_symbol__identifier__unused_"></span><span id="_1027__WARNING_____FILENAME__LINE____IMPORTED_SYMBOL__IDENTIFIER__UNUSED_"></span>**<1027, Warning>: "&lt;fileName&gt;<line\#>: Imported symbol &lt;identifier&gt; unused"**
</dt> <dd>

IMPORTS section module semantic warning, specific to neither SNMPv1 nor SNMPv2C. A warning is issued for every unused imported symbol.

</dd> </dl>

## Fatal Error 1028

<dl> <dt>

<span id="_1028__Fatal____Module__identifier__not_imported_in_the_IMPORTS_section_"></span><span id="_1028__fatal____module__identifier__not_imported_in_the_imports_section_"></span><span id="_1028__FATAL____MODULE__IDENTIFIER__NOT_IMPORTED_IN_THE_IMPORTS_SECTION_"></span>**<1028, Fatal>: "Module &lt;identifier&gt; not imported in the IMPORTS section"**
</dt> <dd>

IMPORTS section module semantic error, specific to neither SNMPv1 nor SNMPv2C. A module name used in referencing a symbol must either be present in the IMPORTS clause, or be the name of the current module.

</dd> </dl>

## Fatal Error 1029

<dl> <dt>

<span id="_1029__Fatal_____fileName__line____Current_module__identifier__cannot_be_imported_"></span><span id="_1029__fatal_____filename__line____current_module__identifier__cannot_be_imported_"></span><span id="_1029__FATAL_____FILENAME__LINE____CURRENT_MODULE__IDENTIFIER__CANNOT_BE_IMPORTED_"></span>**<1029, Fatal>: "&lt;fileName&gt;<line\#>: Current module &lt;identifier&gt; cannot be imported"**
</dt> <dd>

IMPORTS section module semantic error, specific to neither SNMPv1 nor SNMPv2C. The name of the current module also figures in the IMPORTS list.

</dd> </dl>

## Fatal Error 1030

<dl> <dt>

<span id="_1030__Fatal____fileName__line____Symbol__identifier__not_imported_from_Module__identifier__"></span><span id="_1030__fatal____filename__line____symbol__identifier__not_imported_from_module__identifier__"></span><span id="_1030__FATAL____FILENAME__LINE____SYMBOL__IDENTIFIER__NOT_IMPORTED_FROM_MODULE__IDENTIFIER__"></span>**<1030, Fatal>:"&lt;fileName&gt;<line\#>: Symbol &lt;identifier&gt; not imported from Module &lt;identifier&gt;"**
</dt> <dd>

IMPORTS section module semantic error, specific to neither SNMPv1 nor SNMPv2C. You have used the "Module.Symbol" notation, but the symbol has not been imported from the specified module in the IMPORTS section.

</dd> </dl>

 

 



