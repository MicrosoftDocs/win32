---
title: Using Windows Remote Management
description: Windows Remote Management is intended to improve hardware management in a network environment with various devices running a variety of operating systems.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6ee2b238-5bc2-4274-b7ca-49dbc728d8f1
ms.prod: windows-server-dev
ms.technology: windows-remote-management
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Using Windows Remote Management

Windows Remote Management is intended to improve hardware management in a network environment with various devices running a variety of operating systems. The entire design of the service is focused on monitoring and managing remote computers by implementing an interoperable standard protocol.

Because the [WinRM Scripting API](winrm-scripting-api.md) and the [WinRM C++ API](winrm-c---api.md) implement and closely model the operations defined for the WS-Management protocol, scripts and applications receive streams of XML in response to requests. Input parameters to method calls must be constructed in XML. You can use the methods of the [MSXML](http://go.microsoft.com/fwlink/p/?linkid=57523) API to display or construct XML strings. For an example, see [Displaying XML Output from WinRM Scripts](displaying-xml-output-from-winrm-scripts.md).

The following list includes topics that describe how to use WinRM scripting:

-   [Detecting Whether a Remote Computer Supports WS-Management Protocol](detecting-whether-a-remote-computer-supports-ws-management-protocol.md)
-   [Obtaining Data from the Local Computer](obtaining-data-from-the-local-computer.md)
-   [Obtaining Data from a Remote Computer](obtaining-data-from-a-remote-computer.md)
-   [Enumerating or Listing All the Instances of a Resource](enumerating-or-listing-all-instances-of-a-resource.md)
-   [Querying for Specific Instances of a Resource](querying-for-specific-instances-of-a-resource.md)
-   [Displaying XML Output from WinRM Scripts](displaying-xml-output-from-winrm-scripts.md)

## Tracing WinRM Activity

Because WinRM obtains data through [Windows Management Instrumentation (WMI)](https://msdn.microsoft.com/library/aa394582), you can trace WMI activity that results from WinRM messages. Starting with Windows Vista, the WMI service no longer uses the [WMI Log Files](https://msdn.microsoft.com/library/aa394564). Instead it uses [Event Tracing](https://msdn.microsoft.com/library/windows/desktop/bb968803) (ETW) and events are available through the **Event Viewer** UI or the Evtutil command line tool.

## Related topics

<dl> <dt>

[Windows Remote Management](portal.md)
</dt> <dt>

[About Windows Remote Management](about-windows-remote-management.md)
</dt> <dt>

[Windows Remote Management Reference](windows-remote-management-reference.md)
</dt> <dt>

[Scripting in Windows Remote Management](scripting-in-windows-remote-management.md)
</dt> </dl>

 

 




