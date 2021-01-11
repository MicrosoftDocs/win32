---
description: WMI uses Event Tracing (ETW) and events can be obtained through the Event Viewer user interface or the Wevtutil command line tool. For more information, see Tracing WMI Activity.
ms.assetid: 315b8355-03b9-40f9-a6c1-29a49f5a2cd8
ms.tgt_platform: multiple
title: WMI Log Files
ms.topic: article
ms.date: 05/31/2018
---

# WMI Log Files

WMI uses [Event Tracing](/windows/desktop/ETW/event-tracing-portal) (ETW) and events can be obtained through the **Event Viewer** user interface or the Wevtutil command line tool. For more information, see [Tracing WMI Activity](tracing-wmi-activity.md).

-   [Event Tracing Instead of Text Logs](#event-tracing-instead-of-text-logs)
-   [WMI Log Files](#wmi-log-files)
-   [Related topics](#related-topics)

## Event Tracing Instead of Text Logs

WMI service activity is recorded in the WMITracing.log file. For more information about enabling WMI event tracing and accessing the WMITracing.log file, see [Tracing WMI Activity](tracing-wmi-activity.md). Windows Driver Model (WDM) providers continue to log in the Wbemprov.log file.

## WMI Log Files

The WMI service and some providers write text log files to record events.

<dl> <dt>

<span id="WMI_Provider_Log_Files"></span><span id="wmi_provider_log_files"></span><span id="WMI_PROVIDER_LOG_FILES"></span>[WMI Provider Log Files](wmi-provider-log-files.md)
</dt> <dd>

WMI providers also may maintain logs. Which log files appear on a system depends on which providers are installed.

</dd> </dl>

## Related topics

<dl> <dt>

[WMI Reference](wmi-reference.md)
</dt> <dt>

[Tracing WMI Activity](tracing-wmi-activity.md)
</dt> <dt>

[Logging WMI Activity](logging-wmi-activity.md)
</dt> </dl>

 

 
