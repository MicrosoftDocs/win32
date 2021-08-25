---
title: Tracing
description: Tracing uses Event Tracing for Windows (ETW).
ms.assetid: b008bae2-9423-4e72-ae03-9cd50f73d812
keywords:
- Tracing Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Tracing

Tracing uses Event Tracing for Windows (ETW). To take advantage of the tracing tools available with Windows Server 2008 R2, install the Microsoft Windows SDK from the [MSDN Downloads](https://www.microsoft.com/download/details.aspx?id=8279) site.


There are three tracing levels supported:

-   Verbose (all available traces).
-   Info (informational traces).
-   Error (error traces).

The following events are traced:

-   Any errors (Level=Error, Level=Info or Level=Verbose).
-   Entry/Exit of an API (Level=Info or Level=Verbose).
-   Start and completion of any IO (Level=Info or Level=Verbose)
-   Exchanged SOAP messages (Level=Verbose, available on Windows 2003 SP1 and later)

## Generating and Viewing WWSAPI Traces

WWSAPI uses the manifest based events on Windows Vista and above. As a result, the tracing experience has some differences based on the operating system version. Generating ETW traces can be done by using the in-box ETW tools on all supported platforms. However viewing the ETW traces in a nice format requires custom tools on Windows XP SP2 and Windows 2003 SP1. There are few different ways of collecting and viewing WWSAPI ETW event traces depending on the operating system version.

## Enabling and Viewing WWSAPI traces in Event Viewer (works on Windows Vista and above)

-   Run eventvwr.msc from command line or run menu.
-   Click the view link on the Actions pane on the right and enable Show Analytic and Debug logs option.
-   Browse to Application and Service Logs\\Microsoft\\Windows\\WebServices providers on the left pane.
-   Right click the Tracing provider and select Enable log.
-   Run your scenario.
-   When you refresh the event viewer page, you should start seeing the WWSAPI tracing entries.

## Enabling and Viewing WWSAPI traces using Wstrace.bat Script (works on XPSP2 and above)

The wstrace.bat batch file provides a convenient way to:

-   Create a trace log
-   Delete a trace log
-   Enable and disable tracing
-   Update the tracing level (info/error/verbose)
-   Converting trace logs to CSV files

The batch file uses logman.exe for all commands, with the exception of converting the logs to CSV file, which requires a custom tool (wstracedump.exe).

## Using tracing commands

The following command creates a log that uses info, error or verbose level. This command requires elevated privileges.

**wstrace.bat create \[info \| error \| verbose\]**

The following command deletes the log. This command requires elevated privileges.

**wstrace.bat delete**

The following command enables tracing. You must first create a log.

**wstrace.bat on**

The tracing level (info, error or verbose) can be modified as follows:

**wstrace.bat update \[info \| error \| verbose\]**

To dump the trace output, use the following command:

**wstrace.bat dump > temp.csv**

The events will be dumped to the CSV file until Ctrl-C is pressed or tracing is disabled.

## Tracing File format

The CSV files created by wstrace.bat are simple comma-separated-variable text files. These files may be opened in Excel, Notepad, etc.

The columns of the file are as follows:

-   TimeStamp - Time stamp of when the event was recorded
-   ProcessID - ULONG ID of the process recording the event
-   ThreadID - ULONG ID of the thread recording the event
-   Event - Enumerated value of the event type may be ("api enter" \| "api pending" \| "api ExitSyncSuccess" \| "api ExitSyncFailure" \| "api ExitAsyncSuccess" \| "api ExitAsyncFailure" \| "io started" \| "io completed" \| "io failed" \| "error" \| "received message start" \| "received message" \| "received message stop" \| "sending message start" \| "sending message" \| "sending message stop")
-   Operation - The name of the operation being invoked. Typically this maps to the API being called.
-   Error - Optional HRESULT error number
-   Info - Optional information about the event

## Collecting WWSAPI ETW Trace File using ETW tools (works on XPSP2 and above)

Enabling ETW tracing for WWSAPI

**logman start wstrace -bs 64 -ft 1 -rt -p Microsoft-Windows-WebServices \[flags \[level\]\] \[-o &lt;EtlLogFileName&gt;\] -ets**

to create and start the ETW tracing session. Logman.exe is an in-box ETW tool available on all supported platforms. Note that you need to use Microsoft\_Windows\_WebServices as the provider name on XPSP2 and W2K3. You can run logman query providers to see the list of registered providers. Microsoft-Windows-WebServices (or Microsoft\_Windows\_WebServices) provider should be listed unless it is not registered. The provider is normally registered during setup. However it can also be manually registered by running wevtutil.exe im &lt;ManifestFileName&gt; (on Windows Vista and Later) or mofcomp.exe &lt;MofFileName&gt; (on XPSP2 and W2K3).

Flags can be used to filter the traces by their kind. It can be OR'd value of the following trace kinds. If not supplied, all trace kinds are enabled.

-   0x1 - API entry/exit traces.
-   0x2 - Error traces.
-   0x4 - IO traces.
-   0x8 - SOAP message traces.
-   0x10 - Binary message traces.

Level can be used to filter the traces by their level. It should be one of the following values. If not supplied, all trace levels are enabled.

-   0x1 - Fatal traces.
-   0x2 - Error traces.
-   0x3 - Warning traces.
-   0x4 - Informational traces.
-   0x5 - Verbose traces.

EtlLogFileName is the path to the ETW event log file to be created (use .etl extension). If not provided, ETW will pick a random name which can be queried later. This file should not reside on user's profile directory. ETW event log file (.etl file) is in binary format. It can be consumed by ETW applications, but it is not in human readable format. Next step describes how to view its content.

Run your scenario

Collecting ETW event log file.

**logman stop wstrace -ets**

to stop the ETW tracing session. This is when ETW stops logging the events. ETW event log file (specified in EtlLogFileName parameter) is ready to consume. It can either be viewed locally (instructions are given below) or sent to the product group for investigation.

End to end example using ETW tools:

**logman start wstrace -bs 64 -ft 1 -rt -p Microsoft-Windows-WebServices -o mytrace.etl -ets**

**echo .. run your scenario..**

**logman stop wstrace -ets**

**tracerpt mytrace.etl -o mytrace.xml**

**wstrace.htm**

**echo .. use mytrace.xml and wstrace.xsl in the opened page ..**

## Viewing WWSAPI ETW Trace File traces using wstracedump.exe tool (works on Windows XP and above)

Wstracedump.exe is a custom developed ETW consumer tool which processes events in the WWSAPI ETW trace file and produces human readable output. It can produce output from all supported platforms. See its usage (wstracedump.exe -?) for more information.

## Viewing WWSAPI ETW Trace File traces using ETW tools (works on Windows Vista and above)

Tracerpt.exe is the tool to view the content of an ETW event log file and available on all supported platforms. It can be used to generate CSV, EVTX or XML dump files from an ETW event log file. However the generated output file has human readable traces only on Windows Vista and later. These instructions describes how to generate the XML dump file and use it along with an xsl file to display the traces in a nice format (xsl file is very trivial and may be altered if different formats are desired).

-   Run

    **tracerpt &lt;EtlLogFileName&gt; -o &lt;OutputXMLFileName&gt;**

    to create an XML dump from the binary ETL file (tracerpt.exe creates the output file in XML format by default. Run tracerpt -? To see other available formats).

-   At this point, you can see the tracing information in the XML file. Additionally, you can open the wstrace.htm file and use the xml dump file and the wstrace.xsl file to see the traces in a nicer format. Note that the files need to be on the local machine to be able to use this html file on IE.

## Security

When enabling tracing, administrators should take into account that it consumes additional disk space and computation power. A malicious client or application may exhaust system resources unless tracing settings are configured with reasonable limits. When using message tracing feature, messages carrying sensitive information such as credentials, personal information, etc. may be persisted to the disk or be viewed by anyone who has access to the system event viewer. As a mitigation to this issue, tracing can be enabled by System or Administrator users on Windows 2003 and later. Message tracing is disabled on Windows XP on which any user can turn tracing on.

The following enumeration is used with tracing:

-   [**WS\_TRACE\_API**](/windows/desktop/api/WebServices/ne-webservices-ws_trace_api)

 

 




