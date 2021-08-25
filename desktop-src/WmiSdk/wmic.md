---
description: The WMI command-line (WMIC) utility provides a command-line interface for WMI.
ms.assetid: a0f5c1e2-9a4d-4c2b-b324-58ec01e67b6e
ms.tgt_platform: multiple
title: wmic
ms.topic: article
ms.date: 05/31/2018
---

# wmic

The WMI command-line (WMIC) utility provides a command-line interface for Windows Management Instrumentation (WMI). WMIC is compatible with existing shells and utility commands. The following is a general reference topic for WMIC. For more information and guidelines on how to use WMIC, including additional information on aliases, verbs, switches, and commands, see [Using Windows Management Instrumentation Command-line](/previous-versions/windows/it-pro/windows-server-2003/cc779482(v=ws.10)) and [WMIC - Take Command-line Control over WMI](/previous-versions/windows/it-pro/windows-2000-server/bb742610(v=technet.10)).

## Alias

An alias is a friendly renaming of a class, property, or method that makes WMI easier to use and read. You can determine what aliases are available for WMIC through the **/?** command. You can also determine the aliases for a specific class using the **&lt;className&gt; /?** command. For more information, see [WMIC Aliases](/previous-versions/windows/it-pro/windows-server-2003/cc736307(v=ws.10)).

## Switch

A switch is a WMIC option you can set globally or optionally. For a list of available switches, see [WMIC Switches](/previous-versions/windows/it-pro/windows-server-2003/cc787035(v=ws.10)).

## Verbs

To use verbs in WMIC, enter the alias name followed by the verb. If an alias does not support a verb, you receive the message "provider is not capable of the attempted operation." For more information, see [WMIC Verbs](/previous-versions/windows/it-pro/windows-server-2003/cc784966(v=ws.10)).

Most aliases support the following verbs.

<dl> <dt>

<span id="ASSOC"></span><span id="assoc"></span>ASSOC
</dt> <dd>

Returns the result of the `Associators of (<wmi_object>)` query where *<wmi\_object>* is the path of objects returned by the **PATH** or **CLASS** commands. The results are instances associated with the object. When ASSOC is used with an alias, the classes with the class underlying the alias are returned. By default the output is returned in HTML format.

The ASSOC verb has the following switches.



| Switch                         | Description                                                                                                       |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------|
| /RESULTCLASS:&lt;classname&gt; | Returned endpoints associated with the source object must belong to, or be derived from the specified class.      |
| /RESULTROLE:&lt;rolename&gt;   | Returned endpoints must play a specific role in associations with the source object.                              |
| /ASSOCCLASS:&lt;assocclass&gt; | Returned endpoints must be associated with the source through the specified class, or one of its derived classes. |



 

Example: **OS ASSOC**

</dd> <dt>

<span id="CALL"></span><span id="call"></span>CALL
</dt> <dd>

Executes a method.

Example: **SERVICE WHERE CAPTION='TELNET' CALL STARTSERVICE**

> [!Note]  
> To determine the methods available for a given class, use **/?**. For example, **SERVICE WHERE CAPTION='TELNET' CALL /?** lists the available functions for the service class.

 

</dd> <dt>

<span id="CREATE"></span><span id="create"></span>CREATE
</dt> <dd>

Creates a new instance and sets the property values. CREATE cannot be used to create a new class.

Example: **ENVIRONMENT CREATE NAME="TEMP"; VARIABLEVALUE="NEW"**

</dd> <dt>

<span id="DELETE"></span><span id="delete"></span>DELETE
</dt> <dd>

Deletes the current instance or set of instances. DELETE can be used to delete a class.

Example: **PROCESS WHERE NAME="CALC.EXE" DELETE**

</dd> <dt>

<span id="GET"></span><span id="get"></span>GET
</dt> <dd>

Retrieve specific property values.

GET has the following switches.



| Switch                               | Description                                                                                                                                |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| /VALUE                               | Output is formatted with each value listed on a separate line and with the name of the property.                                           |
| /ALL                                 | Output is formatted as a table.                                                                                                            |
| /TRANSLATE:<translation table> | Translate the output using the translation table named by the command. The translation tables BasicXml and NoComma are included with WMIC. |
| /EVERY:&lt;interval&gt;              | Repeat the command every &lt;interval&gt; seconds.                                                                                         |
| /FORMAT:<format specifier>     | Specifies a key word or XSL file name to format the data.                                                                                  |



 

Example: **PROCESS GET NAME**

</dd> <dt>

<span id="LIST"></span><span id="list"></span>LIST
</dt> <dd>

Shows data. LIST is the default verb.

LIST has the following adverbs.



| Adverb   | Description                                                  |
|----------|--------------------------------------------------------------|
| BRIEF    | Core set of the properties.                                  |
| FULL     | Full set of properties. This is the default adverb for LIST. |
| INSTANCE | Instance paths only.                                         |
| STATUS   | Status of the objects.                                       |
| SYSTEM   | System properties.                                           |



 

LIST has the following switches.



| Switch                               | Description                                                                                                                                |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| /TRANSLATE:<translation table> | Translate the output using the translation table named by the command. The translation tables BasicXml and NoComma are included with WMIC. |
| /EVERY:&lt;interval&gt;              | Repeat the command every &lt;interval&gt; seconds.                                                                                         |
| /FORMAT:<format specifier>     | Specifies a key word or XSL file name to format the data.                                                                                  |



 

Example: **PROCESS LIST BRIEF**

</dd> <dt>

<span id="SET"></span><span id="set"></span>SET
</dt> <dd>

Assigns values to properties. Example: **ENVIRONMENT SET NAME="TEMP"**, **VARIABLEVALUE="NEW"**

</dd> </dl>

## Switches

Global switches are used to set defaults for the WMIC environment. You can view the current value of the conditions set by these switches by entering the **CONTEXT** command.

<dl> <dt>

<span id="_NAMESPACE"></span><span id="_namespace"></span>/NAMESPACE
</dt> <dd>

Namespace the alias uses typically. The default is root\\cimv2.

Example: **/NAMESPACE:\\\\root**

</dd> <dt>

<span id="_ROLE"></span><span id="_role"></span>/ROLE
</dt> <dd>

Namespace WMIC typically looks in for aliases and other WMIC information.

Example: **/ROLE:\\\\root**

</dd> <dt>

<span id="_NODE"></span><span id="_node"></span>/NODE
</dt> <dd>

Computer names, comma delimited. All commands are synchronously executed against all computers listed in this value. File names must be prefixed with &. Computer names within a file must be comma delimited or on separate lines.

</dd> <dt>

<span id="_IMPLEVEL"></span><span id="_implevel"></span>/IMPLEVEL
</dt> <dd>

Impersonation level.

Example: **/IMPLEVEL:Anonymous**

</dd> <dt>

<span id="_AUTHLEVEL"></span><span id="_authlevel"></span>/AUTHLEVEL
</dt> <dd>

Authentication level.

Example: **/AUTHLEVEL:Pkt**

</dd> <dt>

<span id="_LOCALE"></span><span id="_locale"></span>/LOCALE
</dt> <dd>

Locale.

Example: **/LOCALE:MS\_411**

</dd> <dt>

<span id="_PRIVILEGES"></span><span id="_privileges"></span>/PRIVILEGES
</dt> <dd>

Enable or disable all privileges.

Example: **/PRIVILEGES:ENABLE** or **/PRIVILEGES:DISABLE**

</dd> <dt>

<span id="_TRACE"></span><span id="_trace"></span>/TRACE
</dt> <dd>

Display the success or failure of all functions used to execute WMIC commands.

Example: **/TRACE:ON** or **/TRACE:OFF**

</dd> <dt>

<span id="_RECORD"></span><span id="_record"></span>/RECORD
</dt> <dd>

Records all output to an XML file. Output is also displayed at the command prompt.

Example: **/RECORD:***MyOutput.xml*

</dd> <dt>

<span id="_INTERACTIVE"></span><span id="_interactive"></span>/INTERACTIVE
</dt> <dd>

Typically, delete commands are confirmed.

Example: **/INTERACTIVE:ON** or **/INTERACTIVE:OFF**

</dd> <dt>

<span id="_FAILFAST_on_off_TimeoutInMilliseconds"></span><span id="_failfast_on_off_timeoutinmilliseconds"></span><span id="_FAILFAST_ON_OFF_TIMEOUTINMILLISECONDS"></span>/FAILFAST **on**\|**off**\|*TimeoutInMilliseconds*
</dt> <dd>

If ON the /NODE computers are pinged before sending WMIC commands to them. If a computer does not respond the WMIC commands are not sent to it.

Example: "/FAILFAST:ON" or "/FAILFAST:OFF"

**WMIC /FAILFAST:1000**

</dd> <dt>

<span id="_USER"></span><span id="_user"></span>/USER
</dt> <dd>

User name used by WMIC when accessing the /NODE computers or computers specified in the aliases. You are prompted for the password. A user name cannot be used with the local computer.

Example: **/USER:***JSMITH*

</dd> <dt>

<span id="_PASSWORD"></span><span id="_password"></span>/PASSWORD
</dt> <dd>

Password used by WMIC when accessing the /NODE computers. The password is visible at the command line.

Example: **/PASSWORD:***password*

</dd> <dt>

<span id="_OUTPUT"></span><span id="_output"></span>/OUTPUT
</dt> <dd>

Specifies a mode for all output redirection. Output does not appear at the command line and the destination is cleared before output begins. Valid values are STDOUT, CLIPBOARD or a file name.

Example: **/OUTPUT:CLIPBOARD**

</dd> <dt>

<span id="_APPEND"></span><span id="_append"></span>/APPEND
</dt> <dd>

Specifies a mode for all output redirection. Output does not appear at the command line and the destination is not cleared before output begins and output is appended to the end of the current contents of the destination. Valid values are STDOUT, CLIPBOARD or a file name.

Example: **/APPEND:CLIPBOARD**

</dd> <dt>

<span id="_AGGREGATE"></span><span id="_aggregate"></span>/AGGREGATE
</dt> <dd>

Used with the **LIST** and **GET /EVERY** switch. If AGGREGATE is ON, LIST and GET display their results when all computers in the /NODE have either responded or timed out. If AGGREGATE is OFF, LIST and GET display their results as soon as they are received.

Example: **/AGGREGATE:OFF** or **/AGGREGATE:ON**

</dd> </dl>

## Commands

The following WMIC commands are available at all times. For more information, see [WMIC Commands](/previous-versions/windows/it-pro/windows-server-2003/cc779647(v=ws.10)).

<dl> <dt>

<span id="CLASS"></span><span id="class"></span>CLASS
</dt> <dd>

Escape from the default alias mode of WMIC to access classes in the WMI schema directly. For more information on available WMI classes, see [WMI Classes](wmi-classes.md).

Example: **WMIC /OUTPUT:c:\\ClassOutput.htm CLASS Win32\_SoundDevice**

</dd> <dt>

<span id="PATH"></span><span id="path"></span>PATH
</dt> <dd>

Escape from the default alias mode of WMIC to access instances in the WMI schema directly.

Example: **WMIC /OUTPUT:c:\\PathOutput.txt PATH Win32\_SoundDevice GET /VALUE**

</dd> <dt>

<span id="CONTEXT"></span><span id="context"></span>CONTEXT
</dt> <dd>

Display the current values of all global switches.

Example: **WMIC CONTEXT**

</dd> <dt>

<span id="QUIT"></span><span id="quit"></span>QUIT
</dt> <dd>

Exit from WMIC.

Example: **WMIC QUIT**

</dd> <dt>

<span id="EXIT"></span><span id="exit"></span>EXIT
</dt> <dd>

Exit from WMIC.

Example: **WMIC EXIT**

</dd> </dl>

## Examples

The [Script for setting IP/Subnet/Gateway/DNS using wmic](https://Gallery.TechNet.Microsoft.Com/Batch-per-settare-487c1b3f) sample on TechNet Gallery describes how to modify and update IP, Subnet, Gateway, and DNS settings.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |



 

