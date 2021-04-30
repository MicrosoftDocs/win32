---
description: Starting with Windows Vista, the WMI service does not use the WMI Log Files. Instead, it uses Event Tracing for Windows (ETW) and events are available through Event Viewer or the Wevtutil command-line tool.
ms.assetid: bb6401e8-caf7-4f39-ab64-b7532723ce9a
ms.tgt_platform: multiple
title: Tracing WMI Activity
ms.topic: article
ms.date: 05/31/2018
---

# Tracing WMI Activity

Starting with Windows Vista, the WMI service does not use the [WMI Log Files](wmi-log-files.md). Instead, it uses [Event Tracing for Windows (ETW)](/windows/desktop/ETW/event-tracing-portal) and events are available through **Event Viewer** or the Wevtutil command-line tool.

The following sections are discussed in this topic:

-   [Obtaining WMI Events Through Event Viewer](#obtaining-wmi-events-through-event-viewer)
-   [Enabling WMI Tracing at Command Prompt](#enabling-wmi-tracing-at-command-prompt)
-   [Using WPP-based WMI Tracing](#using-wpp-based-wmi-tracing)
-   [Related topics](#related-topics)

## Obtaining WMI Events Through Event Viewer

The WMITracing.log file contains the events that WMI traces. However, this is a binary file. To see these events in a format readable by humans, use the **Event Viewer**.

By default, WMI events are not traced. This procedure describes how to use **Event Viewer** to enable WMI event tracing and locate WMI events. You can do the same operations through the wevtutil command-line tool.

**To view WMI Events in Event Viewer**

1.  Open **Event Viewer**. On the **View** menu, click **Show Analytic and Debug Logs**. Locate the **Trace** channel log for WMI under Applications and Service Logs \| Microsoft \| Windows \| WMI Activity.
2.  Right-click the **Trace** log and select **Log Properties**. Click the **Enable Logging** check box to start the WMI event tracing. For more information about channels, see [Event Logs and Channels in Windows Event Log](/previous-versions//aa385225(v=vs.85)).
3.  WMI events appear in the event window for **WMI-Activity**. Double-click an event in the list to see the detailed information. You can view an event in **XML View** or in **Friendly View** format.

The **Event ID** field displays a value that contains the following information.

<dl> <dt>

<span id="Event_1"></span><span id="event_1"></span><span id="EVENT_1"></span>Event 1
</dt> <dd>

Start of the event sequence for a specific operation. One occurrence for each sequence.

The event fields for an Event 1 are:

-   **GroupOperationID** is a unique identifier that is used for all events reported for a specific client.
-   **OperationId** indicates the operation sequence.
-   **Operation** specifies the connection or request to WMI.
-   **User** indicates the account that makes a request to WMI by running a script or through CIM Studio.
-   **Namespace** shows the WMI namespace to which the connection is made.

For example, a script may request all the instances of a WMI class, such as [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service). The first operation may be a connection to WMI.

</dd> <dt>

<span id="Event_2"></span><span id="event_2"></span><span id="EVENT_2"></span>Event 2
</dt> <dd>

Events that make up the operation. One or more occurrences in the sequence.

The event fields for an Event 2 are:

-   **GroupOperationID** indicates the sequence in which the event occurs.
-   **GroupOperationID** indicates the sequence in which the event occurs.
-   **ProviderName** indicates the name of the provider which supplies the data.
-   **Path** is the WMI path to the object.

For example, the operation may be an enumeration of [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service).

</dd> <dt>

<span id="Event_3"></span><span id="event_3"></span><span id="EVENT_3"></span>Event 3
</dt> <dd>

End of the event sequence for a specific operation. One occurrence for each sequence.

Only the **GroupOperationID** is shown.

</dd> </dl>

## Enabling WMI Tracing at Command Prompt

You can also enable WMI event tracing through the Wevtutil command-line tool. Use the following command: **Wevtutil.exe sl Microsoft-Windows-WMI-Activity/Trace /e:true**. The WMI event source is Microsoft-Windows-WMI. For more information about Wevtutil.exe, see [About Windows Event Log](/previous-versions//aa382610(v=vs.85)).

## Using WPP-based WMI Tracing

In Windows operating systems starting with Windows Vista, WMI creates an active trace channel during the boot process. The name of the channel is WMI\_Trace\_Session. Only errors are logged to the channel.

The Windows software trace preprocessor (WPP) records information in a binary file. To read the file, you must first translate it into a readable, text format. You use a tool called tracefmt.exe from the [Windows Driver Kit (WDK)](https://www.microsoft.com/whdc/DevTools/WDK/WDKpkg.mspx) to do the translation. The tool requires information stored in some associated files. The files are located in the %SystemRoot%\\System32\\wbem\\tmf directory and have a .tmf file name extension. The tool actually requires a single .tmf file . You make that single file by concatenating all of the .tmf files into another .tmf file. For more information about .tmf files, see [Trace Message Format File](/windows-hardware/drivers/devtest/trace-message-format-file).

After installing the [Windows Driver Kit (WDK)](https://www.microsoft.com/whdc/DevTools/WDK/WDKpkg.mspx) to get the tracelog.exe and tracefmt.exe command-line tools, perform the following steps to collect a WPP-based WMI trace.

**To view a WPP-based WMI trace**

1.  To create the single .tmf file, open an elevated Command Prompt window and navigate to the %SystemRoot%\\System32\\wbem\\tmf directory.

2.  Type **copy /y %SystemRoot%\\System32\\wbem\\tmf\\\*.tmf %SystemRoot%\\System32\\wbem\\tmf\\wmi.tmf**. This will create a file named wmi.tmf that includes the contents of all of the other .tmf files.

3.  Type **tracelog -flush WMI\_Trace\_Session**. This will flush the WPP buffers on the disk.
4.  Type **set TRACE\_FORMAT\_PREFIX = \[%9!d!\]%8!04X!.%3!04X!.%3!04X!::%4!s!\[%1!s!\](%!COMPNAME!:%!FUNC !:%2!s!)**. The tracefmt tool adds some default information to each trace message. You can configure what information is included by setting the TRACE\_FORMAT\_PREFIX environment variable. To learn about the syntax used, see [Trace Message Prefix](https://msdn.microsoft.com/library/aa139695.aspx).
5.  Type **tracefmt -tmf %systemroot%\\system32\\wbem\\tmf\\wmi.tmf -o OUTPUT.TXT %systemroot%\\system32\\wbem\\logs\\WMITracing.log**. This performs the translation from binary format to readable text format.
6.  Type **notepad %systemroot%\\system32\\wbem\\tmf\\OUTPUT.TXT**. This will open the trace file in Notepad.

The following are some other WPP-related tasks you might need to perform.

**To stop WPP-based WMI tracing**

-   Type **tracelog -stop WMI\_Trace\_Session**.

**To start WPP-based WMI tracing**

-   Type **tracelog -start WMI\_Trace\_Session -guid \#1FF6B227-2CA7-40f9-9A66-980EADAA602E -rt -level 5 -flag 0x7 -f MYTRACE.BIN**

**Windows Vista:** By default, WPP-based WMI tracing is set to level 2 which includes only error messages. To include informational messages as well, set the level to 4. All areas of WMI are traced by default. There are three distinct areas that can be traced: Core (flag=0x1), ESS (flag=0x2) and Prov (flag=0x4). In the start command above, **flag 0x7** causes all three areas to be traced.

**Windows 7:** By default, WPP-based WMI tracing is disabled and set to level 0. To use WPP-based WMI tracing, this feature must be enabled and set to either level 2 for error messages or level 4 for both error and informational messages.

**To list all WPP trace sessions**

-   Type **tracelog -l**.

**To list info about the WMI WPP trace session**

-   Type **tracelog -l \| findstr /i "wmi\_trace"**.

**To view the WMI WPP trace session parameters**

-   Type **tracelog -q WMI\_Trace\_Session**.

## Related topics

<dl> <dt>

[WMI Troubleshooting](wmi-troubleshooting.md)
</dt> <dt>

[WMI Log Files](wmi-log-files.md)
</dt> </dl>

 

 
