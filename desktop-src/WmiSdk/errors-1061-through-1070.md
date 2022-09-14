---
description: Describes WMI SNMP provider errors 1061 through 1070.
ms.assetid: 1bbd6153-7241-4673-ae17-1caa92b2e6a6
ms.tgt_platform: multiple
title: Errors 1061 through 1070
ms.topic: article
ms.date: 05/31/2018
---

# Errors 1061 through 1070

Describes WMI SNMP provider errors 1061 through 1070.

[Fatal Error 1063](#fatal-error-1063)

[Fatal Error 1064](#fatal-error-1064)

[Fatal Error 1070](#fatal-error-1070)

## Fatal Error 1063

<dl> <dt>

<span id="_1063__Fatal_____fileName__line____Upper_bound_of_SIZE_specification_is_less_than_the_lower_bound_"></span><span id="_1063__fatal_____filename__line____upper_bound_of_size_specification_is_less_than_the_lower_bound_"></span><span id="_1063__FATAL_____FILENAME__LINE____UPPER_BOUND_OF_SIZE_SPECIFICATION_IS_LESS_THAN_THE_LOWER_BOUND_"></span>**<1063, Fatal>: "&lt;fileName&gt;<line\#>: Upper bound of SIZE specification is less than the lower bound"**
</dt> <dd>

Module semantic error in SIZE specification, specific to neither SNMPv1 nor SNMPv2C. The symbol used in a SIZE specification must resolve to OCTET STRING or Opaque. The lower bound of a range or SIZE specification must be no greater than the upper bound.

</dd> </dl>

## Fatal Error 1064

<dl> <dt>

<span id="_1064__Fatal_____fileName___line____SEQUENCE_item__identifier__does_not_resolve_to_an_OBJECT-TYPE_"></span><span id="_1064__fatal_____filename___line____sequence_item__identifier__does_not_resolve_to_an_object-type_"></span><span id="_1064__FATAL_____FILENAME___LINE____SEQUENCE_ITEM__IDENTIFIER__DOES_NOT_RESOLVE_TO_AN_OBJECT-TYPE_"></span>**<1064, Fatal>: "&lt;fileName&gt;:<line\#>: SEQUENCE item &lt;identifier&gt; does not resolve to an OBJECT-TYPE"**
</dt> <dd>

Type assignment module semantic error, specific to neither SNMPv1 nor SNMPv2C. All of the individual elements of a SEQUENCE declaration must resolve to an OBJECT-TYPE.

</dd> </dl>

## Fatal Error 1070

<dl> <dt>

<span id="_1070__Fatal_____fileName__line____MIB_Module__moduleName___from_which_symbol__symbolName__is_imported__is_not_present_in_input_"></span><span id="_1070__fatal_____filename__line____mib_module__modulename___from_which_symbol__symbolname__is_imported__is_not_present_in_input_"></span><span id="_1070__FATAL_____FILENAME__LINE____MIB_MODULE__MODULENAME___FROM_WHICH_SYMBOL__SYMBOLNAME__IS_IMPORTED__IS_NOT_PRESENT_IN_INPUT_"></span>**<1070, Fatal>: "&lt;fileName&gt;<line\#>: MIB Module &lt;moduleName&gt;, from which symbol &lt;symbolName&gt; is imported, is not present in input"**
</dt> <dd>

Module semantic error in cross-referencing, specific to neither SNMPv1 nor SNMPv2C. If one of the modules in the IMPORTS section of the main module or a subsidiary module does not exist and one or more symbols from this module are actually referenced, this fatal error occurs.

</dd> </dl>

 

 



