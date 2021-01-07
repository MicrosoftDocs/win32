---
description: Describes WMI SNMP provider errors 1071 through 1080.
ms.assetid: c9161c96-6839-4b32-b1bd-b40af18ab314
ms.tgt_platform: multiple
title: Errors 1071 through 1080
ms.topic: article
ms.date: 05/31/2018
---

# Errors 1071 through 1080

Describes WMI SNMP provider errors 1071 through 1080.

[Warning 1071](#warning-1071)

[Warning 1072](#warning-1072)

[Fatal Error 1074](#fatal-error-1074)

[Fatal Error 1075](#fatal-error-1075)

[Fatal Error 1077](#fatal-error-1077)

[Fatal Error 1079](#fatal-error-1079)

[Warning 1080](#warning-1080)

## Warning 1071

<dl> <dt>

<span id="_1071__Warning_____fileName__line____Symbol__identifier__not_present_in_imported_module__identifier__"></span><span id="_1071__warning_____filename__line____symbol__identifier__not_present_in_imported_module__identifier__"></span><span id="_1071__WARNING_____FILENAME__LINE____SYMBOL__IDENTIFIER__NOT_PRESENT_IN_IMPORTED_MODULE__IDENTIFIER__"></span>**<1071, Warning>: "<fileName><line\#>: Symbol <identifier> not present in imported module <identifier>"**
</dt> <dd>

Module semantic warning about cross-referencing, specific to neither SNMPv1 nor SNMPv2C. A symbol imported from a module does not resolve to anything in that module. Even though that module is specified in the input, this warning appears.

</dd> </dl>

## Warning 1072

<dl> <dt>

<span id="_1072__Warning_____fileName___line___OBJECT-TYPE__name__is_a_descendant_of_OBJECT-TYPE__name__of_module__name__"></span><span id="_1072__warning_____filename___line___object-type__name__is_a_descendant_of_object-type__name__of_module__name__"></span><span id="_1072__WARNING_____FILENAME___LINE___OBJECT-TYPE__NAME__IS_A_DESCENDANT_OF_OBJECT-TYPE__NAME__OF_MODULE__NAME__"></span><**1072, Warning>: "<fileName>:<line\#> OBJECT-TYPE <name> is a descendant of OBJECT-TYPE <name> of module <name>"**
</dt> <dd>

**OBJECT-TYPE** macro invocation module semantic warning. A scalar object cannot have any descendant objects.

This warning can occur in either SNMPv1 or SNMPv2C.

</dd> </dl>

## Fatal Error 1074

<dl> <dt>

<span id="_1074__Fatal_____fileName___line___SEQUENCE__Conceptual_row__OBJECT-TYPE__name__does_not_have_a_SEQUENCE_OF__Conceptual_table__OBJECT-TYPE_as_its_parent_"></span><span id="_1074__fatal_____filename___line___sequence__conceptual_row__object-type__name__does_not_have_a_sequence_of__conceptual_table__object-type_as_its_parent_"></span><span id="_1074__FATAL_____FILENAME___LINE___SEQUENCE__CONCEPTUAL_ROW__OBJECT-TYPE__NAME__DOES_NOT_HAVE_A_SEQUENCE_OF__CONCEPTUAL_TABLE__OBJECT-TYPE_AS_ITS_PARENT_"></span>**<1074, Fatal>: "<fileName>:<line\#> SEQUENCE (Conceptual row) OBJECT-TYPE <name> does not have a SEQUENCE OF (Conceptual table) OBJECT-TYPE as its parent"**
</dt> <dd>

**OBJECT-TYPE** macro invocation module semantic error. Every row object must have a table object as its parent.

This error can occur in either SNMPv1 or SNMPv2C.

</dd> </dl>

## Fatal Error 1075

<dl> <dt>

<span id="_1075__Fatal____fileName___line____OBJECT-TYPE__name__cannot_be_a_child_of_table_OBJECT-TYPE__name__of_module__name__unless_it_is_in_the_SEQUENCE_of_the_latter_"></span><span id="_1075__fatal____filename___line____object-type__name__cannot_be_a_child_of_table_object-type__name__of_module__name__unless_it_is_in_the_sequence_of_the_latter_"></span><span id="_1075__FATAL____FILENAME___LINE____OBJECT-TYPE__NAME__CANNOT_BE_A_CHILD_OF_TABLE_OBJECT-TYPE__NAME__OF_MODULE__NAME__UNLESS_IT_IS_IN_THE_SEQUENCE_OF_THE_LATTER_"></span>**<1075, Fatal>:"<fileName>:<line\#>: OBJECT-TYPE <name> cannot be a child of table OBJECT-TYPE <name> of module <name> unless it is in the SEQUENCE of the latter"**
</dt> <dd>

**OBJECT-TYPE** macro invocation module semantic error. Every SEQUENCE object must have exactly the same objects that are mentioned in the SEQUENCE type definition as its children. Similarly, every SEQUENCE OF object must have exactly one child.

This error can occur in either SNMPv1 or SNMPv2C.

</dd> </dl>

## Fatal Error 1077

<dl> <dt>

<span id="_1077__Fatal_____fileName___line____The_syntax_of_table_OBJECT-TYPE__name__is_not_the_SEQUENCE_OF_the_syntax_of_the_child_OBJECT-TYPE__name__of_module__name__"></span><span id="_1077__fatal_____filename___line____the_syntax_of_table_object-type__name__is_not_the_sequence_of_the_syntax_of_the_child_object-type__name__of_module__name__"></span><span id="_1077__FATAL_____FILENAME___LINE____THE_SYNTAX_OF_TABLE_OBJECT-TYPE__NAME__IS_NOT_THE_SEQUENCE_OF_THE_SYNTAX_OF_THE_CHILD_OBJECT-TYPE__NAME__OF_MODULE__NAME__"></span>**<1077, Fatal>: "<fileName>:<line\#>: The syntax of table OBJECT-TYPE <name> is not the SEQUENCE OF the syntax of the child OBJECT-TYPE <name> of module <name>"**
</dt> <dd>

**OBJECT-TYPE** macro invocation module semantic error. The syntax clause of a table object must be the "SEQUENCE OF" of the syntax of the row object.

This error can occur in either SNMPv1 or SNMPv2C.

</dd> </dl>

## Fatal Error 1079

<dl> <dt>

<span id="_1079__Fatal___fileName___line____OBJECT-TYPE__name__is_an_extra_child_of_OBJECT-TYPE__name__of_module__name__"></span><span id="_1079__fatal___filename___line____object-type__name__is_an_extra_child_of_object-type__name__of_module__name__"></span><span id="_1079__FATAL___FILENAME___LINE____OBJECT-TYPE__NAME__IS_AN_EXTRA_CHILD_OF_OBJECT-TYPE__NAME__OF_MODULE__NAME__"></span>**<1079, Fatal>:"fileName>:<line\#>: OBJECT-TYPE <name> is an extra child of OBJECT-TYPE <name> of module <name>"**
</dt> <dd>

**OBJECT-TYPE** macro invocation module semantic error. Every SEQUENCE OF object must have exactly one child.

This error can occur in either SNMPv1 or SNMPv2C.

</dd> </dl>

## Warning 1080

<dl> <dt>

<span id="_1080__Warning_____fileName__line____MIB_Module__moduleName___from_which_symbol__symbolName__is_imported__is_not_present_in_input_"></span><span id="_1080__warning_____filename__line____mib_module__modulename___from_which_symbol__symbolname__is_imported__is_not_present_in_input_"></span><span id="_1080__WARNING_____FILENAME__LINE____MIB_MODULE__MODULENAME___FROM_WHICH_SYMBOL__SYMBOLNAME__IS_IMPORTED__IS_NOT_PRESENT_IN_INPUT_"></span>**<1080, Warning>: "<fileName><line\#>: MIB Module <moduleName>, from which symbol <symbolName> is imported, is not present in input"**
</dt> <dd>

Module semantic warning about cross-referencing, specific to neither SNMPv1 nor SNMPv2C. If one of the modules in the IMPORTS section of the main module or a subsidiary module does not exist, but symbols from this module are not referenced, this warning appears.

</dd> </dl>

 

 



