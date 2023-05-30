---
description: Learn how to start and stop Windows Management Instrumentation, along with other services that depend on it.
ms.assetid: 8dff43bf-71d0-4d5a-91bc-6f474186d4ba
ms.tgt_platform: multiple
title: Starting and stopping the WMI service
ms.topic: article
ms.date: 02/09/2023
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Starting and stopping WMI service

Windows Management Instrumentation (WMI) runs as a service with the display name **Windows Management Instrumentation** and the service name **winmgmt**. WMI runs automatically at system startup under the *LocalSystem* account. If WMI isn't running, it automatically starts when the first management application or script requests connection to a WMI namespace.

Several other services depend on the WMI service, based on the operating system version that the system is running.

## Start winmgmt service

The following procedure describes how to start the WMI service:

1. At a command prompt, enter `net start winmgmt [/<switch>]`.

    For more information about the switches that are available, see [winmgmt](winmgmt.md). You use the built-in Administrator account or an account in the Administrators group running with elevated rights to start the WMI service. For more information, see [User Account Control and WMI](user-account-control-and-wmi.md).

2. Other services that are dependent on the WMI service, such as SMS Agent Host or Windows Firewall, don't automatically restart.

## Stop winmgmt service

The following procedure describes how to stop the WMI service:

1. At a command prompt, enter `net stop winmgmt`.

2. Other services that are dependent on the WMI service also halt, such as SMS Agent Host or Windows Firewall.

## See also

[Using the WMI command-line tools](using-the-wmi-command-line-tools.md)
