---
description: Describes WMI SNMP provider errors 1101 through 1110.
ms.assetid: ffb3da80-0ffa-4f05-a35e-c51dba38a7fe
ms.tgt_platform: multiple
title: Errors 1101 through 1110
ms.topic: article
ms.date: 05/31/2018
---

# Errors 1101 through 1110

Describes WMI SNMP provider errors 1101 through 1110.

[Fatal Error 1101](#fatal-error-1101)

## Fatal Error 1101

<dl> <dt>

<span id="_1101__Fatal_____fileName__line____The_length_of_the_range_is_too_long_for_the_compiler__Does_not_fit_into_4_bytes__"></span><span id="_1101__fatal_____filename__line____the_length_of_the_range_is_too_long_for_the_compiler__does_not_fit_into_4_bytes__"></span><span id="_1101__FATAL_____FILENAME__LINE____THE_LENGTH_OF_THE_RANGE_IS_TOO_LONG_FOR_THE_COMPILER__DOES_NOT_FIT_INTO_4_BYTES__"></span>**<1101, Fatal>: "&lt;fileName&gt;<line\#>: The length of the range is too long for the compiler (Does not fit into 4 bytes)"**
</dt> <dd>

Module semantic error in range or size specification, specific to neither SNMPv1 nor SNMPv2C. The size of a set of ranges must be less than 2³². The size of a set of ranges is defined as the difference between the largest value and the smallest value in the set.

</dd> </dl>

 

 



