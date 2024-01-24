---
description: Event logs store records of significant events on behalf of the system and applications running on the system.
ms.assetid: 58a6569a-2775-4687-bf99-579fa4153191
title: Logging Guidelines
ms.topic: article
ms.date: 05/31/2018
---

# Logging Guidelines

Event logs store records of significant events on behalf of the system and applications running on the system. Because the logging functions are general purpose, you must decide what information is appropriate to log. Generally, you should log only information that could be useful in diagnosing a hardware or software problem. Event logging is not intended to be used as a tracing tool.

## Choosing Events to Log

The following are examples of cases in which event logging can be helpful:

-   Resource problems. Logging a Warning event when memory allocation fails can help indicate the cause of a low-memory situation.
-   Hardware problems. If a device driver encounters a disk controller time-out, a power failure in a parallel port, or a data error from a network or serial card, the device driver can log information about these events to help the system administrator diagnose hardware problems.
-   Bad sectors. If a disk driver encounters a bad sector, it may be able to read from or write to the sector after retrying the operation, but the sector will go bad eventually. If the disk driver can proceed, it should log a Warning event; otherwise, it should log an Error event. If a file system driver finds a large number of bad sectors and fixes them, logging Warning events might help an administrator determine that the disk may be about to fail.
-   Information events. A server application (such as a database server) records a user logging on, opening a database, or starting a file transfer. The server can also log other events such as errors (cannot access file, host process disconnected, and so on), database corruption, or whether a file transfer was successful.

## Writing Messages

Messages should make sense to administrators and users who are trying to troubleshoot a problem. A message should contain all the information needed to understand what caused the problem and how to correct it.

Avoid writing a cryptic message such as "A driver packet received from the I/O subsystem was invalid. The data is the packet."A better message would indicate that the driver in question is functioning properly, but is logging incorrectly formatted packets. It could go on to say that a Unicode version of the driver is needed to correct the problem. For more information about writing good error messages, see [Error Message Guidelines](/windows/desktop/Debug/error-message-guidelines).

Do not use tabs or commas in the message text, because event logs can be saved as comma or tab-separated text files. Many organizations import these files into databases, and the extra formatting characters will require manual manipulation.

When using UNC names, or other links that contain spaces, enclose the name in angle brackets. For example, <\\\\*sharename*\\*servername*>. You can write a URL to the end of the message that points the user to related help material. The URL must be a fully qualified DNS host name. For example, you could append the following text to your messages: "For additional information on this message, please visit our support site at https://www.microsoft.com/Support/ProdRedirect/ContentSearch.asp." The link would lead to an ASP page that redirects the user to content relating to the error message. It would parse additional parameters (passed when the URL is clicked) to determine where to redirect the user.

The arguments passed to the [**ReportEvent**](/windows/desktop/api/Winbase/nf-winbase-reporteventa) function are appended to the URL as follows:

``` syntax
strHTTPQuery += L"?EvtSrc=" + _strEscapedSource;
strHTTPQuery += L"&EvtCat=" + _strEscapedCategory;
strHTTPQuery += L"&EvtID=" + _strEscapedEventID;
strHTTPQuery += L"&EvtCatID=" + _strEscapedCategoryID;
strHTTPQuery += L"&EvtType=" + _strEscapedType;
strHTTPQuery += L"&EvtTypeID=" + _strEscapedTypeID;
strHTTPQuery += L"&EvtRptTime=" + _strEscapedDateAndTime;
strHTTPQuery += L"&EvtTZBias=" + _strEscapedTimeZoneBias;
```

If the company name, product name, product version, file name, and file version from the message DLL header for the event source are valid, they are also appended to the URL:

``` syntax
ADD_VER_STR(L"CoName",   _strEscapedCompanyName);
ADD_VER_STR(L"ProdName", _strEscapedProductName);
ADD_VER_STR(L"ProdVer",  _strEscapedProductVersion);
ADD_VER_STR(L"FileName", _strEscapedFileName);
ADD_VER_STR(L"FileVer",  _strEscapedFileVersion);
```

## Reducing Overhead

Event logging consumes resources such as disk space and processor time. The amount of disk space that an event log requires and the overhead for an application that logs events depend on how much information you choose to log. This is why it is important to log only essential information. It is also good to place event logging calls in an error path in the code rather than in the main code path, which would reduce performance.

The amount of disk space required for each event log record includes the members of the [**EVENTLOGRECORD**](/windows/desktop/api/Winnt/ns-winnt-eventlogrecord) structure. This is a variable length structure; strings and binary data are stored following the structure.

 

 
