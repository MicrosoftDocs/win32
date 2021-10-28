---
title: wmic
description: The WMI command-line (WMIC) utility provides a command-line interface for WMI.
ms.assetid: a0f5c1e2-9a4d-4c2b-b324-58ec01e67b6e
ms.tgt_platform: multiple
ms.topic: article
ms.date: 09/10/2021
---

# wmic

> [!IMPORTANT]
> The WMI command-line (WMIC) utility is deprecated as of Windows 10, version 21H1, and as of the 21H1 semi-annual channel release of Windows Server. This utility is superseded by Windows PowerShell for WMI (see [Chapter 7&mdash;Working with WMI](/powershell/scripting/learn/ps101/07-working-with-wmi)). This deprecation applies only to the WMI command-line (WMIC) utility; Windows Management Instrumentation (WMI) itself is not affected. Also see [Windows 10 features we're no longer developing](/windows/deployment/planning/windows-10-deprecated-features).

The WMI command-line (WMIC) utility provides a command-line interface for Windows Management Instrumentation (WMI). WMIC is compatible with existing shells and utility commands. The following is a general reference topic for WMIC. For more information and guidelines on how to use WMIC, including additional information on aliases, verbs, switches, and commands, see [Using Windows Management Instrumentation command-line](/previous-versions/windows/it-pro/windows-server-2003/cc779482(v=ws.10)) and [WMIC&mdash;take command-line control over WMI](/previous-versions/windows/it-pro/windows-2000-server/bb742610(v=technet.10)).

## Alias

An alias is a friendly renaming of a class, property, or method that makes WMI easier to use and read. You can determine what aliases are available for WMIC through the **/?** command. You can also determine the aliases for a specific class using the **&lt;className&gt; /?** command. For more information, see [WMIC aliases](/previous-versions/windows/it-pro/windows-server-2003/cc736307(v=ws.10)).

## Switch

A switch is a WMIC option that you can set globally or optionally. For a list of available switches, see [WMIC switches](/previous-versions/windows/it-pro/windows-server-2003/cc787035(v=ws.10)).

## Verbs

To use verbs in WMIC, enter the alias name followed by the verb. If an alias doesn't support a verb, you receive the message "provider is not capable of the attempted operation." For more information, see [WMIC verbs](/previous-versions/windows/it-pro/windows-server-2003/cc784966(v=ws.10)).

Most aliases support the following verbs.

### ASSOC

Returns the result of the `Associators of (<wmi_object>)` query where *<wmi\_object>* is the path of objects returned by the **PATH** or **CLASS** commands. The results are instances associated with the object. When ASSOC is used with an alias, the classes with the class underlying the alias are returned. By default the output is returned in HTML format.

The ASSOC verb has the following switches.

| Switch                         | Description                                                                                                       |
|--------------------------------|-------------------------------------------------------------------------------------------------------------------|
| /RESULTCLASS:&lt;classname&gt; | Returned endpoints associated with the source object must belong to, or be derived from the specified class.      |
| /RESULTROLE:&lt;rolename&gt;   | Returned endpoints must play a specific role in associations with the source object.                              |
| /ASSOCCLASS:&lt;assocclass&gt; | Returned endpoints must be associated with the source through the specified class, or one of its derived classes. |

Example: **OS ASSOC**

### CALL

Executes a method.

Example: **SERVICE WHERE CAPTION='TELNET' CALL STARTSERVICE**

> [!NOTE]  
> To determine the methods available for a given class, use **/?**. For example, **SERVICE WHERE CAPTION='TELNET' CALL /?** lists the available functions for the service class.

### CREATE

Creates a new instance, and sets the property values. CREATE can't be used to create a new class.

Example: **ENVIRONMENT CREATE NAME="TEMP"; VARIABLEVALUE="NEW"**

### DELETE

Deletes the current instance or set of instances. DELETE can be used to delete a class.

Example: **PROCESS WHERE NAME="CALC.EXE" DELETE**

### GET

Retrieve specific property values.

GET has the following switches.

| Switch                               | Description                                                                                                                                |
|--------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| /VALUE                               | Output is formatted with each value listed on a separate line and with the name of the property.                                           |
| /ALL                                 | Output is formatted as a table.                                                                                                            |
| /TRANSLATE:&lt;translation table&gt; | Translate the output using the translation table named by the command. The translation tables BasicXml and NoComma are included with WMIC. |
| /EVERY:&lt;interval&gt;              | Repeat the command every &lt;interval&gt; seconds.                                                                                         |
| /FORMAT:&lt;format specifier&gt;     | Specifies a key word or XSL file name to format the data.                                                                                  |

Example: **PROCESS GET NAME**

### LIST

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
| /TRANSLATE:&lt;translation table&gt; | Translate the output using the translation table named by the command. The translation tables BasicXml and NoComma are included with WMIC. |
| /EVERY:&lt;interval&gt;              | Repeat the command every &lt;interval&gt; seconds.                                                                                         |
| /FORMAT:&lt;format specifier&gt;     | Specifies a key word or XSL file name to format the data.                                                                                  |

Example: **PROCESS LIST BRIEF**

### SET

Assigns values to properties. Example: **ENVIRONMENT SET NAME="TEMP"**, **VARIABLEVALUE="NEW"**

## Switches

Global switches are used to set defaults for the WMIC environment. You can view the current value of the conditions set by these switches by entering the **CONTEXT** command.

### /NAMESPACE

Namespace the alias uses typically. The default is root\\cimv2.

Example: **/NAMESPACE:\\\\root**

### /ROLE

Namespace WMIC typically looks in for aliases and other WMIC information.

Example: **/ROLE:\\\\root**

### /NODE

Computer names, comma delimited. All commands are synchronously executed against all computers listed in this value. File names must be prefixed with &. Computer names within a file must be comma delimited or on separate lines.

### /IMPLEVEL

Impersonation level.

Example: **/IMPLEVEL:Anonymous**

### /AUTHLEVEL

Authentication level.

Example: **/AUTHLEVEL:Pkt**

### /LOCALE

Locale.

Example: **/LOCALE:MS\_411**

### /PRIVILEGES

Enable or disable all privileges.

Example: **/PRIVILEGES:ENABLE** or **/PRIVILEGES:DISABLE**

### /TRACE

Display the success or failure of all functions used to execute WMIC commands.

Example: **/TRACE:ON** or **/TRACE:OFF**

### /RECORD

Records all output to an XML file. Output is also displayed at the command prompt.

Example: **/RECORD:***MyOutput.xml*

### /INTERACTIVE

Typically, delete commands are confirmed.

Example: **/INTERACTIVE:ON** or **/INTERACTIVE:OFF**

### /FAILFAST **on**\|**off**\|*TimeoutInMilliseconds*

If ON, the /NODE computers are pinged before sending WMIC commands to them. If a computer doesn't respond, then the WMIC commands are not sent to it.

Example: "/FAILFAST:ON" or "/FAILFAST:OFF"

**WMIC /FAILFAST:1000**

### /USER

User name used by WMIC when accessing the /NODE computers or computers specified in the aliases. You are prompted for the password. A user name can't be used with the local computer.

Example: **/USER:***JSMITH*

### /PASSWORD

Password used by WMIC when accessing the /NODE computers. The password is visible at the command line.

Example: **/PASSWORD:***password*

### /OUTPUT

Specifies a mode for all output redirection. Output doesn't appear at the command line and the destination is cleared before output begins. Valid values are STDOUT, CLIPBOARD or a file name.

Example: **/OUTPUT:CLIPBOARD**

### /APPEND

Specifies a mode for all output redirection. Output doesn't appear at the command line and the destination is not cleared before output begins and output is appended to the end of the current contents of the destination. Valid values are STDOUT, CLIPBOARD or a file name.

Example: **/APPEND:CLIPBOARD**

### /AGGREGATE

Used with the **LIST** and **GET /EVERY** switch. If AGGREGATE is ON, LIST and GET display their results when all computers in the /NODE have either responded or timed out. If AGGREGATE is OFF, LIST and GET display their results as soon as they are received.

Example: **/AGGREGATE:OFF** or **/AGGREGATE:ON**

## Commands

The following WMIC commands are available at all times. For more information, see [WMIC commands](/previous-versions/windows/it-pro/windows-server-2003/cc779647(v=ws.10)).

### CLASS

Escape from the default alias mode of WMIC to access classes in the WMI schema directly. For more information on available WMI classes, see [WMI classes](wmi-classes.md).

Example: **WMIC /OUTPUT:c:\\ClassOutput.htm CLASS Win32\_SoundDevice**

### PATH

Escape from the default alias mode of WMIC to access instances in the WMI schema directly.

Example: **WMIC /OUTPUT:c:\\PathOutput.txt PATH Win32\_SoundDevice GET /VALUE**

### CONTEXT

Display the current values of all global switches.

Example: **WMIC CONTEXT**

### QUIT

Exit from WMIC.

Example: **WMIC QUIT**

### EXIT

Exit from WMIC.

Example: **WMIC EXIT**

## Requirements

| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |

