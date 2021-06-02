---
description: Control of Winsock Tracing
ms.assetid: b079bdfc-b192-451c-967d-dcefa94b7ec7
title: Control of Winsock Tracing
ms.topic: article
ms.date: 05/31/2018
---

# Control of Winsock Tracing

Winsock tracing can be controlled by using either of the following methods:

-   Command-line tools

    Two command-line tools are included with Windows Vista and Windows Server 2008 that are used to control tracing and convert the binary trace log file to readable text.

    The **logman.exe** tool is used to start or stop Winsock tracing.

    The **tracerpt.exe** tool is used to convert the binary trace log file to a readable text file.

-   Event Viewer

    The Event Viewer on Windows Vista and later can also be used to enable Winsock tracing. The Event Viewer is accessible under the Administrative Tools from the Start menu.

## Using logman and tracert

Winsock network event tracing is disabled by default on Windows Vista and later.

The following command starts Winsock network event tracing on a computer, sets the name of event trace session to mywinsocksession, and sends output to a binary log file called winsocklogfile.etl:

**logman start -ets mywinsocksession -o winsocklogfile.etl -p Microsoft-Windows-Winsock-AFD**

Log files are created in the current directory with filenames of the form winsocklogfile\_000001.etl

The following command stops the above Winsock tracing on a computer for the session named mywinsocksession:

**logman stop -ets mywinsocksession**

A binary log file will be written to the location specified by the –o parameter. To translate the binary file into a readable text file, **tracerpt.exe** is used:

**tracerpt.exe <name of the .etl file> –o winsocktracelog.txt**

If an output file containing xml rather than plain text is preferred, the following command is used:

**tracerpt.exe <name of the .etl file> –o winsocktracelog.xml –of xml**

Winsock catalog change tracing is enabled by default on Windows Vista and later.

> [!Note]  
> Layered Service Providers are deprecated. Starting with Windows 8 and Windows Server 2012, use [Windows Filtering Platform](../fwp/windows-filtering-platform-start-page.md).

 

The following command starts Winsock Catalog Change tracing for layered service providers (LSPs) on a computer, sets the name of event trace session to mywinsockcatalogsession, and sends output to a binary log file called winsockcataloglogfile.etl:

**logman start -ets mywinsockcatalogsession -o winsockcataloglogfile.etl -p Microsoft-Windows-Winsock-WS2HELP**

Log files are created in the current directory with filenames of the form winsockcataloglogfile\_000001.etl

The following command stops the above Winsock tracing on a computer for the session named mysession:

**logman stop -ets mywinsockcatalogsession**

A binary log file will be written to the location specified by the –o parameter. To translate the binary file into a readable text file, **tracerpt.exe** is used:

**tracerpt.exe <name of the .etl file> –o winsockcatalogtracelog.txt**

If an output file containing xml rather than plain text is preferred, the following command is used:

**tracerpt.exe <name of the .etl file> –o winsockcatalogtracelog.xml –of xml**

## Using Event Viewer to Start Winsock Network Event Tracing

When you open Event Viewer, the left pane contains the list of events. Open **Applications and Services Logs** and navigate to **Microsoft\\Windows\\Winsock Network Event** as the source and select **Operational**.

In the Action pane, select **Log Properties** and check the **Enable Logging** check box. Once logging is enabled, you can also change the size of the log file if this is needed.

Winsock network event tracing is now enabled and all you need to do is hit the Refresh action to update the list of events that have been logged. To stop logging, simply uncheck the same radio button.

You may need to increase the log size depending on how many events you want to see. One drawback to using the Event Viewer for Winsock tracing is that it does not load all the string resources so the messages displayed in the Description field (once you select an event) is sometimes hard to read (an argument that should be formatted as hex will be displayed in decimal, for example). However, you can select the **Details** tab in the event description which shows the raw XML log entry which usually has easier to understand arguments.

## Using Event Viewer to Start Winsock Catalog Change Tracing

When you open Event Viewer, the left pane contains the list of events. Open **Applications and Services Logs** and navigate to **Microsoft\\Windows\\Winsock Catalog Change** as the source and select **Operational**.

In the Action pane, select **Log Properties** and check the **Enable Logging** check box. Once logging is enabled, you can also change the size of the log file if this is needed.

Winsock catalog change tracing is now enabled and all you need to do is hit the Refresh action to update the list of events that have been logged. To stop logging, simply uncheck the same radio button.

You may need to increase the log size depending on how many events you want to see. One drawback to using the Event Viewer for Winsock tracing is that it does not load all the string resources so the messages displayed in the Description field (once you select an event) is sometimes hard to read (an argument that should be formatted as hex will be displayed in decimal, for example). However, you can select the **Details** tab in the event description which shows the raw XML log entry which usually has easier to understand arguments.

## Interpreting Winsock Tracing Logs

All Winsock tracing events in a log contain two types of information:

-   System
-   EventData

The system information contains the logging level, the time the log entry was created, the event ID that represents the event type, the execution Process ID, the execution Thread ID, and other system information. A log level of 4 in Winsock tracing represents information event logging. A log level of 5 in Winsock tracing represents verbose event logging.

The execution process ID and thread ID in the system information indicates the process and thread that was running when the event occurred. In many cases, this will represent a kernel or worker thread and process, not a user-mode thread and or the process of the application. So this field is normally not very useful.

Each Winsock tracing event type has a unique event ID in the system section of the logged data. These event IDs can easily be used to filter a log file for specific Winsock tracing events.

The eventdata contains information specific to the event type.

The Process parameter in the eventdata information is the kernel EPROCESS structure address for the process, not the actual PID. To match an event to the user mode PID, take the Process value from the eventdata information from any log entry and look earlier in the log for a socket creation event with the Process value. Once a match is found, the last parameter in the socket creation event data is the user-mode Process ID that created the socket.

An Address parameter in the eventdata information is returned in some Winsock tracing events. An Address parameter represents an IP address, but it is displayed in the text file created by the **tracerpt.exe** tool or in Event Viewer as raw bytes or a number. IPv6 addresses are displayed in hexadecimal, so they are more easily understood. IPv4 addresses are displayed as a large decimal number. Developers will need to manually convert the raw bytes of an IPv4 address to the more familiar IPv4 dotted-decimal address notation to be better able to interpret the value.

An Error parameter in the eventdata is returned in some Winsock tracing events. An Error parameter is of the form of an NTSTATUS or HRESULT error code. This error parameter is displayed in the text file created by the **tracerpt.exe** tool or in Event Viewer as a decimal number. Developers will need to manually convert the decimal number to a hex number in order to better interpret the error code in some cases.

## Related topics

<dl> <dt>

[Winsock Tracing](winsock-tracing.md)
</dt> <dt>

[Winsock Catalog Change Tracing Details](winsock-layered-service-provider-tracing-event-details.md)
</dt> <dt>

[Winsock Network Event Tracing Details](winsock-tracing-event-details.md)
</dt> <dt>

[Winsock Tracing Levels](winsock-tracing-levels.md)
</dt> </dl>

 

 
