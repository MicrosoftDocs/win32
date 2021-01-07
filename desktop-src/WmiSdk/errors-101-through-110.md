---
description: Describes WMI SNMP provider errors 101 through 110.
ms.assetid: baa64233-eb19-4f52-836b-5bdf4a23ae4f
ms.tgt_platform: multiple
title: Errors 101 through 110
ms.topic: article
ms.date: 05/31/2018
---

# Errors 101 through 110

Describes WMI SNMP provider errors 101 through 110.

[Fatal Error 101](#fatal-error-101)

[Fatal Error 102](#fatal-error-102)

[Fatal Error 103](#fatal-error-103)

[Fatal Error 104](#fatal-error-104)

[Fatal Error 105](#fatal-error-105)

[Fatal Error 106](#fatal-error-106)

[Fatal Error 107](#fatal-error-107)

[Fatal Error 108](#fatal-error-108)

[Fatal Error 109](#fatal-error-109)

[Warning 110](#warning-110)

## Fatal Error 101

<dl> <dt>

<span id="_101__Fatal____Usage_"></span><span id="_101__fatal____usage_"></span><span id="_101__FATAL____USAGE_"></span>**<101, Fatal>: "Usage:**
</dt> <dd></dd> <dt>

<span id="smi2smir__DiagnosticArgs___VersionArgs___CommandArgs_"></span><span id="smi2smir__diagnosticargs___versionargs___commandargs_"></span><span id="SMI2SMIR__DIAGNOSTICARGS___VERSIONARGS___COMMANDARGS_"></span>**smi2smir <DiagnosticArgs> <VersionArgs> <CommandArgs>**
</dt> <dd></dd> <dt>

<span id="smi2smir__DiagnosticArgs___RegistryArgs_"></span><span id="smi2smir__diagnosticargs___registryargs_"></span><span id="SMI2SMIR__DIAGNOSTICARGS___REGISTRYARGS_"></span>**smi2smir <DiagnosticArgs> <RegistryArgs>**
</dt> <dd></dd> <dt>

<span id="smi2smir__HelpArgs__"></span><span id="smi2smir__helpargs__"></span><span id="SMI2SMIR__HELPARGS__"></span>**smi2smir <HelpArgs>"**
</dt> <dd>

Command-line syntax error. This is followed by an explanation of the switches.

</dd> </dl>

## Fatal Error 102

<dl> <dt>

<span id="_102__Fatal___Invalid_argument_on_command_line_after__last_correct_argument__"></span><span id="_102__fatal___invalid_argument_on_command_line_after__last_correct_argument__"></span><span id="_102__FATAL___INVALID_ARGUMENT_ON_COMMAND_LINE_AFTER__LAST_CORRECT_ARGUMENT__"></span>**<102, Fatal>:"Invalid argument on command line after <last correct argument>"**
</dt> <dd>

Command-line syntax error. There are some extra arguments or a switch is not valid on the command line. The <last correct argument> parameter refers to the last argument that was read correctly on the command line, and can possibly be smi2smir, which is the name of the executable file for the SNMP module information compiler.

</dd> </dl>

## Fatal Error 103

<dl> <dt>

<span id="_103__Fatal____Diagnostic_Level_not_specified_for_the__m_switch_"></span><span id="_103__fatal____diagnostic_level_not_specified_for_the__m_switch_"></span><span id="_103__FATAL____DIAGNOSTIC_LEVEL_NOT_SPECIFIED_FOR_THE__M_SWITCH_"></span>**<103, Fatal>: "Diagnostic Level not specified for the /m switch"**
</dt> <dd>

Command-line syntax error. If you specify the **/m** switch, you must also specify a diagnostic level of 0, 1, or 2.

</dd> </dl>

## Fatal Error 104

<dl> <dt>

<span id="_104__Fatal____Diagnostic_Level_must_be_0__1_or_2_for_the__m_switch_"></span><span id="_104__fatal____diagnostic_level_must_be_0__1_or_2_for_the__m_switch_"></span><span id="_104__FATAL____DIAGNOSTIC_LEVEL_MUST_BE_0__1_OR_2_FOR_THE__M_SWITCH_"></span>**<104, Fatal>: "Diagnostic Level must be 0, 1 or 2 for the /m switch"**
</dt> <dd>

Command-line syntax error. If you specify the **/m** switch, you must also specify a diagnostic level of 0, 1, or 2.

</dd> </dl>

## Fatal Error 105

<dl> <dt>

<span id="_105__Fatal____Maximum_diagnostic_count_missing_after_the__c_switch_"></span><span id="_105__fatal____maximum_diagnostic_count_missing_after_the__c_switch_"></span><span id="_105__FATAL____MAXIMUM_DIAGNOSTIC_COUNT_MISSING_AFTER_THE__C_SWITCH_"></span>**<105, Fatal>: "Maximum diagnostic count missing after the /c switch"**
</dt> <dd>

Command-line syntax error. If you specify the **/c** switch, you must also specify a non-negative integer as the maximum count.

</dd> </dl>

## Fatal Error 106

<dl> <dt>

<span id="_106__Fatal_____argument__is_not_a_valid_diagnostic_count_"></span><span id="_106__fatal_____argument__is_not_a_valid_diagnostic_count_"></span><span id="_106__FATAL_____ARGUMENT__IS_NOT_A_VALID_DIAGNOSTIC_COUNT_"></span>**<106, Fatal>: "<argument> is not a valid diagnostic count"**
</dt> <dd>

Command-line syntax error. If you specify the **/c** switch, you must also specify a non-negative integer as the maximum count.

</dd> </dl>

## Fatal Error 107

<dl> <dt>

<span id="_107__Fatal____File_Name_s__missing_"></span><span id="_107__fatal____file_name_s__missing_"></span><span id="_107__FATAL____FILE_NAME_S__MISSING_"></span>**<107, Fatal>: "File Name(s) missing"**
</dt> <dd>

Command-line semantic error. One or more file names must be specified on the command line for the given combination of switches.

</dd> </dl>

## Fatal Error 108

<dl> <dt>

<span id="_108__Fatal____No_command_argument_specified_"></span><span id="_108__fatal____no_command_argument_specified_"></span><span id="_108__FATAL____NO_COMMAND_ARGUMENT_SPECIFIED_"></span>**<108, Fatal>: "No command argument specified"**
</dt> <dd>

Command-line syntax error. Some action must be specified on the command line.

</dd> </dl>

## Fatal Error 109

<dl> <dt>

<span id="_109__Fatal____Module_name_missing_"></span><span id="_109__fatal____module_name_missing_"></span><span id="_109__FATAL____MODULE_NAME_MISSING_"></span>**<109, Fatal>: "Module name missing"**
</dt> <dd>

Command-line syntax error.

</dd> </dl>

## Warning 110

<dl> <dt>

<span id="_110__Warning____No_include_path_specified_after_the__i_switch_"></span><span id="_110__warning____no_include_path_specified_after_the__i_switch_"></span><span id="_110__WARNING____NO_INCLUDE_PATH_SPECIFIED_AFTER_THE__I_SWITCH_"></span>**<110, Warning>: "No include path specified after the /i switch"**
</dt> <dd>

Command-line syntax warning. If you specify the **/i** switch, you must also specify the path to included files.

</dd> </dl>

## Related topics

<dl> <dt>

[Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md)
</dt> </dl>

 

 



