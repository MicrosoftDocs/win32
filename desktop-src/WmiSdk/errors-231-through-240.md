---
description: Describes WMI SNMP provider errors 231 through 240.
ms.assetid: edb3dabb-6a65-4285-97d3-f7025d3bb5da
ms.tgt_platform: multiple
title: Errors 231 through 240
ms.topic: article
ms.date: 05/31/2018
---

# Errors 231 through 240

Describes WMI SNMP provider errors 231 through 240.

[Fatal Error 232](#fatal-error-232)

[Fatal Error 233](#fatal-error-233)

[Fatal Error 234](#fatal-error-234)

[Fatal Error 236](#fatal-error-236)

## Fatal Error 232

<dl> <dt>

<span id="_232__Fatal____fileName___line___Invocation_of_SNMPv1_SMI_OBJECT-TYPE_disallowed_"></span><span id="_232__fatal____filename___line___invocation_of_snmpv1_smi_object-type_disallowed_"></span><span id="_232__FATAL____FILENAME___LINE___INVOCATION_OF_SNMPV1_SMI_OBJECT-TYPE_DISALLOWED_"></span>**<232, Fatal>:"&lt;fileName&gt;:<line\#>:Invocation of SNMPv1 SMI OBJECT-TYPE disallowed"**
</dt> <dd>

Module syntax error. You have used the SNMPv1-specific **OBJECT-TYPE** invocation in the MIB, but have specified the **/v2c** switch, which requires strict conformance to SNMPv2C syntax.

</dd> </dl>

## Fatal Error 233

<dl> <dt>

<span id="_233__Fatal_____fileName___line____Invocation_of_SNMPv1_SMI_TRAP-TYPE_disallowed_"></span><span id="_233__fatal_____filename___line____invocation_of_snmpv1_smi_trap-type_disallowed_"></span><span id="_233__FATAL_____FILENAME___LINE____INVOCATION_OF_SNMPV1_SMI_TRAP-TYPE_DISALLOWED_"></span>**<233, Fatal>: "&lt;fileName&gt;:<line\#>: Invocation of SNMPv1 SMI TRAP-TYPE disallowed"**
</dt> <dd>

Module syntax error. You have used the SNMPv1-specific **TRAP-TYPE** invocation in the MIB, but have specified the **/v2c** switch, which requires strict conformance to SNMPv2C syntax.

</dd> </dl>

## Fatal Error 234

<dl> <dt>

<span id="_234__Fatal____fileName___line____MODULE-IDENTITY_invocation_is_allowed_only_immediately_after_the_IMPORTS_section_"></span><span id="_234__fatal____filename___line____module-identity_invocation_is_allowed_only_immediately_after_the_imports_section_"></span><span id="_234__FATAL____FILENAME___LINE____MODULE-IDENTITY_INVOCATION_IS_ALLOWED_ONLY_IMMEDIATELY_AFTER_THE_IMPORTS_SECTION_"></span>**<234, Fatal>:"&lt;fileName&gt;:<line\#>: MODULE-IDENTITY invocation is allowed only immediately after the IMPORTS section"**
</dt> <dd>

Module syntax error. The **MODULE-IDENTITY** invocation is misplaced.

</dd> </dl>

## Fatal Error 236

<dl> <dt>

<span id="_236__Fatal_____fileName___line____Number_does_not_fit_into_the_32_bit_representation_used_by_the_compiler_"></span><span id="_236__fatal_____filename___line____number_does_not_fit_into_the_32_bit_representation_used_by_the_compiler_"></span><span id="_236__FATAL_____FILENAME___LINE____NUMBER_DOES_NOT_FIT_INTO_THE_32_BIT_REPRESENTATION_USED_BY_THE_COMPILER_"></span>**<236, Fatal>: "&lt;fileName&gt;:<line\#>: Number does not fit into the 32 bit representation used by the compiler"**
</dt> <dd>

Module syntax error in value assignment. There is a MIB value assignment error in which an integer value is so large that it requires more than 32 bits to represent it.

</dd> </dl>

 

 



