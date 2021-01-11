---
description: Describes WMI SNMP provider errors 1041 through 1050.
ms.assetid: e7e70fb3-12c6-40b1-91a4-c550e8210c09
ms.tgt_platform: multiple
title: Errors 1041 through 1050
ms.topic: article
ms.date: 05/31/2018
---

# Errors 1041 through 1050

Describes WMI SNMP provider errors 1041 through 1050.

[Fatal Error 1041](#fatal-error-1041)

[Fatal Error 1042](#fatal-error-1042)

[Warning 1043](#warning-1043)

[Fatal Error 1044](#fatal-error-1044)

[Warning 1045](#warning-1045)

[Warning 1046](#warning-1046)

[Warning 1047](#warning-1047)

[Warning 1048](#warning-1048)

[Fatal Error 1049](#fatal-error-1049)

## Fatal Error 1041

<dl> <dt>

<span id="_1041__Fatal_____fileName__line____Identifier__identifier__in_range_specification_does_not_resolve_to_an_integral_value_"></span><span id="_1041__fatal_____filename__line____identifier__identifier__in_range_specification_does_not_resolve_to_an_integral_value_"></span><span id="_1041__FATAL_____FILENAME__LINE____IDENTIFIER__IDENTIFIER__IN_RANGE_SPECIFICATION_DOES_NOT_RESOLVE_TO_AN_INTEGRAL_VALUE_"></span>**<1041, Fatal>: "<fileName><line\#>: Identifier <identifier> in range specification does not resolve to an integral value"**
</dt> <dd>

Module semantic error in range or size specification, specific to neither SNMPv1 nor SNMPv2C. The symbol used in a SIZE specification must resolve to OCTET STRING or Opaque. Any value used in specifying a range must be an integer.

</dd> </dl>

## Fatal Error 1042

<dl> <dt>

<span id="_1042__Fatal_____fileName__line____Upper_bound_of_range_specification_is_less_than_the_lower_bound_"></span><span id="_1042__fatal_____filename__line____upper_bound_of_range_specification_is_less_than_the_lower_bound_"></span><span id="_1042__FATAL_____FILENAME__LINE____UPPER_BOUND_OF_RANGE_SPECIFICATION_IS_LESS_THAN_THE_LOWER_BOUND_"></span>**<1042, Fatal>: "<fileName><line\#>: Upper bound of range specification is less than the lower bound"**
</dt> <dd>

Module semantic error in range or size specification, specific to neither SNMPv1 nor SNMPv2C. The symbol used in a SIZE specification must resolve to OCTET STRING or Opaque. The lower bound of a range or SIZE specification must be no greater than the upper bound.

</dd> </dl>

## Warning 1043

<dl> <dt>

<span id="_1043__Warning_____fileName___line____OBJECT-TYPE_with_SYNTAX__SEQUENCE___should_have_an_ACCESS_clause__not-accessible_"></span><span id="_1043__warning_____filename___line____object-type_with_syntax__sequence___should_have_an_access_clause__not-accessible_"></span><span id="_1043__WARNING_____FILENAME___LINE____OBJECT-TYPE_WITH_SYNTAX__SEQUENCE___SHOULD_HAVE_AN_ACCESS_CLAUSE__NOT-ACCESSIBLE_"></span>**<1043, Warning>: "<fileName>:<line\#>: OBJECT-TYPE with SYNTAX "SEQUENCE", should have an ACCESS clause "not-accessible"**
</dt> <dd>

**OBJECT-TYPE** macro invocation module semantic warning. A table or conceptual row (SEQUENCE OF or SEQUENCE object types, respectively) must be "not-accessible."

This warning can occur in either SNMPv1 or SNMPv2C.

</dd> </dl>

## Fatal Error 1044

<dl> <dt>

<span id="_1044__Fatal_____fileName__line____Redefinition_of_symbol__identifier__"></span><span id="_1044__fatal_____filename__line____redefinition_of_symbol__identifier__"></span><span id="_1044__FATAL_____FILENAME__LINE____REDEFINITION_OF_SYMBOL__IDENTIFIER__"></span>**<1044, Fatal>: "<fileName><line\#>: Redefinition of symbol <identifier>"**
</dt> <dd>

Module semantic error, specific to neither SNMPv1 nor SNMPv2C. Redefinition of object descriptors, macro invocations, and ASN.1 types cause an error.

</dd> </dl>

## Warning 1045

<dl> <dt>

<span id="_1045__Warning_____fileName__lineReference_to_standard_symbol__symbolName__assumed_to_be_for_the_definition_as_in__moduleName_._Use_the__module.symbol__notations__if_you_want_to_refer_to_the_definition_in_the_current_module_"></span><span id="_1045__warning_____filename__linereference_to_standard_symbol__symbolname__assumed_to_be_for_the_definition_as_in__modulename_._use_the__module.symbol__notations__if_you_want_to_refer_to_the_definition_in_the_current_module_"></span><span id="_1045__WARNING_____FILENAME__LINEREFERENCE_TO_STANDARD_SYMBOL__SYMBOLNAME__ASSUMED_TO_BE_FOR_THE_DEFINITION_AS_IN__MODULENAME_._USE_THE__MODULE.SYMBOL__NOTATIONS__IF_YOU_WANT_TO_REFER_TO_THE_DEFINITION_IN_THE_CURRENT_MODULE_"></span>**<1045, Warning>: "<fileName><lineReference to standard symbol <symbolName> assumed to be for the definition as in <moduleName>. Use the "module.symbol" notations, if you want to refer to the definition in the current module"**
</dt> <dd>

Module semantic warning, specific to neither SNMPv1 nor SNMPv2C. A symbol known to the compiler has been redefined, and is being referenced. The compiler assumes the standard definition of the symbol. Therefore, to use a redefinition of the standard symbol, you must use the "Module.Symbol" notation.

</dd> </dl>

## Warning 1046

<dl> <dt>

<span id="_1046__Warning_____fileName__line_____symbol__undefined._Assuming_standard_definition_"></span><span id="_1046__warning_____filename__line_____symbol__undefined._assuming_standard_definition_"></span><span id="_1046__WARNING_____FILENAME__LINE_____SYMBOL__UNDEFINED._ASSUMING_STANDARD_DEFINITION_"></span>**<1046, Warning>: "<fileName><line\#>: <symbol> undefined. Assuming standard definition"**
</dt> <dd>

Module semantic warning, specific to neither SNMPv1 nor SNMPv2C. A symbol known to the compiler must not be redefined or used without being imported.

</dd> </dl>

## Warning 1047

<dl> <dt>

<span id="_1047__Warning_____fileName__line____Type_definition__symbol__defined_but_not_referenced_"></span><span id="_1047__warning_____filename__line____type_definition__symbol__defined_but_not_referenced_"></span><span id="_1047__WARNING_____FILENAME__LINE____TYPE_DEFINITION__SYMBOL__DEFINED_BUT_NOT_REFERENCED_"></span>**<1047, Warning>: "<fileName><line\#>: Type definition <symbol> defined but not referenced"**
</dt> <dd>

Module semantic warning, specific to neither SNMPv1 nor SNMPv2C. All value assignments and type definitions must be referenced somewhere.

</dd> </dl>

## Warning 1048

<dl> <dt>

<span id="_1048__Warning_____fileName__line____Value_definition__symbol__defined_but_not_referenced_"></span><span id="_1048__warning_____filename__line____value_definition__symbol__defined_but_not_referenced_"></span><span id="_1048__WARNING_____FILENAME__LINE____VALUE_DEFINITION__SYMBOL__DEFINED_BUT_NOT_REFERENCED_"></span>**<1048, Warning>: "<fileName><line\#>: Value definition <symbol> defined but not referenced"**
</dt> <dd>

Module semantic warning, specific to neither SNMPv1 nor SNMPv2C. All value assignments and type definitions must be referenced somewhere.

</dd> </dl>

## Fatal Error 1049

<dl> <dt>

<span id="_1049__Fatal_____fileName___line____DEFVAL_clause_not_allowed_for_OBJECT-TYPE_with_SYNTAX_NetworkAddress_"></span><span id="_1049__fatal_____filename___line____defval_clause_not_allowed_for_object-type_with_syntax_networkaddress_"></span><span id="_1049__FATAL_____FILENAME___LINE____DEFVAL_CLAUSE_NOT_ALLOWED_FOR_OBJECT-TYPE_WITH_SYNTAX_NETWORKADDRESS_"></span>**<1049, Fatal>: "<fileName>:<line\#>: DEFVAL clause not allowed for OBJECT-TYPE with SYNTAX NetworkAddress"**
</dt> <dd>

**OBJECT-TYPE** macro invocation SNMPv1-specific module semantic error. The DEFVAL clause is not allowed for an OBJECT-TYPE whose SYNTAX clause resolves to NetworkAddress.

</dd> </dl>

 

 



