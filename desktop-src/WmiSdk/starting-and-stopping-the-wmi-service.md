---
description: WMI runs as a service with the display name &\#0034;Windows Management Instrumentation&\#0034; and the service name &\#0034;winmgmt&\#0034;.
ms.assetid: 8dff43bf-71d0-4d5a-91bc-6f474186d4ba
ms.tgt_platform: multiple
title: Starting and Stopping the WMI Service
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Starting and Stopping the WMI Service

WMI runs as a service with the display name "Windows Management Instrumentation" and the service name "winmgmt". WMI runs automatically at system startup under the LocalSystem account. If WMI is not running, it automatically starts when the first management application or script requests connection to a WMI namespace.

Several other services are dependent upon the WMI service, depending on the operating system version that the system is running.

## Starting Winmgmt Service

The following procedure describes how to start the WMI service.

**To start Winmgmt Service**

1.  At a command prompt, enter **net** **start** **winmgmt** \[*/<switch>*\].

    For more information about the switches that are available, see [winmgmt](winmgmt.md). You use the built-in Administrator account or an account in the Administrators group running with elevated rights to start the WMI service. For more information, see [User Account Control and WMI](user-account-control-and-wmi.md).

2.  Other services that are dependent on the WMI service, such as SMS Agent Host or Windows Firewall, will not automatically be restarted.

## Stopping Winmgmt Service

The following procedure describes how to stop the WMI Service.

**To stop Winmgmt Service**

1.  At a command prompt, enter **net stop winmgmt**.

2.  Other services that are dependent on the WMI service also halt, such as SMS Agent Host or Windows Firewall.

## Examples

The TechNet Gallery contains the [WMI service watchdog script](https://Gallery.TechNet.Microsoft.Com/WMI-service-watchdog-script-4fab1282), which describes how to programmatically shut down and restart the winmgmt service with PowerShell.

## Related topics

<dl> <dt>

[Using the WMI Command-Line Tools](using-the-wmi-command-line-tools.md)
</dt> </dl>

 

 



