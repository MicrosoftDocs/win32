---
description: Event identifiers uniquely identify a particular event.
ms.assetid: 83a84db4-572b-48bd-bc0f-071b2089a5ca
title: Event Identifiers (Event Logging)
ms.topic: article
ms.date: 05/31/2018
---

# Event Identifiers (Event Logging)

Event identifiers uniquely identify a particular event. Each [event source](event-sources.md) can define its own numbered events and the description strings to which they are mapped in its message file. Event viewers can present these strings to the user. They should help the user understand what went wrong and suggest what actions to take. Direct the description at users solving their own problems, not at administrators or support technicians. For more information, see [Error Message Guidelines](/windows/desktop/Debug/error-message-guidelines).

## Format

The following diagram illustrates the format of an event identifier.

``` syntax
  3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
  1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
 +---+-+-+-----------------------+-------------------------------+
 |Sev|C|R|     Facility          |               Code            |
 +---+-+-+-----------------------+-------------------------------+
```

<dl> <dt>

<span id="Sev"></span><span id="sev"></span><span id="SEV"></span>Sev
</dt> <dd>

Severity. The severity is defined as follows:

<dl> <dd>00 - Success</dd> <dd>01 - Informational</dd> <dd>10 - Warning</dd> <dd>11 - Error</dd> </dl> </dd> <dt>

<span id="C"></span><span id="c"></span>C
</dt> <dd>

Customer bit. This bit is defined as follows:

<dl> <dd>0 - System code</dd> <dd>1 - Customer code</dd> </dl> </dd> <dt>

<span id="R"></span><span id="r"></span>R
</dt> <dd>

Reserved bit.

</dd> <dt>

<span id="Facility"></span><span id="facility"></span><span id="FACILITY"></span>Facility
</dt> <dd>

Facility code. This value can be FACILITY\_NULL.

</dd> <dt>

<span id="Code"></span><span id="code"></span><span id="CODE"></span>Code
</dt> <dd>

Status code for the facility.

</dd> </dl>

## Message Definitions

Messages are defined in the event message file. The description strings in the event message file are indexed by event identifier, enabling Event Viewer to display event-specific text for any event based on the event identifier. All descriptions are localized and language dependent. For more information on building a message file, see [Message Text Files](message-text-files.md).

The description strings may contain insertion string placeholders, of the form %*n*, where %1 indicates the first insertion string, and so on. For example, the following is a sample entry in the .mc file:

``` syntax
MessageId=0x4
Severity=Error
Facility=System
SymbolicName=MSG_CMD_DELETE
Language=English
File %1 contains %2, which is in error.
.
```

In this case, the buffer returned by [**ReadEventLog**](/windows/desktop/api/Winbase/nf-winbase-readeventloga) contains insertion strings. The **NumStrings** member of the [**EVENTLOGRECORD**](/windows/desktop/api/Winnt/ns-winnt-eventlogrecord) structure indicates the number of insertion strings. The **StringOffset** member of the **EVENTLOGRECORD** structure indicates the location of the first insertion string in the buffer. You can pass an array of DWORD\_PTRs that point to the address each string in the buffer when calling the [**FormatMessage**](/windows/desktop/api/winbase/nf-winbase-formatmessage) function and it will insert the strings into the message.

The description string can also contain placeholders for parameter strings from the parameter message file. The placeholders are of the form %%*n*, where %%1 is replaced by the parameter string with the identifier of 1, and so on. However, it is up to you to insert the parameter strings into the message string that [**FormatMessage**](/windows/desktop/api/winbase/nf-winbase-formatmessage) returns. Typically, you call **FormatMessage** to get the message string for the event. You then parse the message string for %%*n* parameters. If the message contains one or more parameters, load the **ParameterMessageFile** registry value for the source. For each parameter in the message string, get the identifier and pass it to **FormatMessage** to get the parameter string. Replace the parameter in the message string with the parameter string that **FormatMessage** returned.

## Insertion Strings

Insertion strings are optional language-independent strings used to fill in values for placeholders in description strings. Because the strings are not localized, it is critical that these placeholders be used only to represent language-independent strings such as numeric values, file names, user names, and so on. The string length must not exceed 32 kilobytes - 1 characters.

Avoid using several strings to create a larger description. An insertion string should be treated as data, not text. For example, in the following example, pszString1 and pszString2 should not be used as insertion strings for pszDescription.

``` syntax
LPSTR pszString1 = "successfully"; 
LPSTR pszString2 = "not"; 
LPSTR pszDescription = "The user was %1 added to the database.";
```

In the following example, it is appropriate to use either pszString1 or pszString2 for the insertion string in pszDescription.

``` syntax
LPSTR pszString1 = "c:\\testapp1.c"; 
LPSTR pszString2 = "c:\\testapp2.c"; 
LPSTR pszDescription = "Access denied. Attempted to open the file %1."
```

 

 
