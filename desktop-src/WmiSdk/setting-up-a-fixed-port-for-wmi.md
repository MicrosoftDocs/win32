---
description: WMI runs as part of a shared service host with ports assigned through DCOM by default. However, you can set up the WMI service to run as the only process in a separate host and specify a fixed port.
ms.assetid: 62908445-2a43-4a20-a998-e497c6ecf48e
ms.tgt_platform: multiple
title: Setting Up a Fixed Port for WMI
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Setting Up a Fixed Port for WMI

WMI runs as part of a shared service host with ports assigned through DCOM by default. However, you can set up the WMI service to run as the only process in a separate host and specify a fixed port.

The following procedure is an automated setup to allow WMI to have a fixed port. The procedure uses the [**winmgmt**](winmgmt.md) command-line tool.

**To set up a fixed port for WMI**

1.  At the command prompt, type **winmgmt -standalonehost**
2.  Stop the WMI service by typing the command **net stop "Windows Management Instrumentation"**, or use the short name of **net stop winmgmt**
3.  Restart the WMI service again in a new service host by typing **net start "Windows Management Instrumentation"** or **net start winmgmt**
4.  Establish a new port number for the WMI service by typing **netsh firewall add portopening TCP 24158 WMIFixedPort**

To undo any changes you make to WMI, type **winmgmt /sharedhost**, then stop and start the winmgmt service again.

## Examples

For a script that sets up a fixed port for WMI, see the following Scripting Gallery [code sample](https://Gallery.TechNet.Microsoft.Com/Set-WmiSinglePortps1-20fa8389 ).

or a PowerShell code example that enables or disables the WMI port settings, see the [Set-WmiSinglePort](https://Gallery.TechNet.Microsoft.Com/Set-WmiSinglePortps1-20fa8389) example on TechNet Gallery.

## Related topics

<dl> <dt>

[Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md)
</dt> <dt>

[Troubleshooting a Remote WMI Connections](connecting-to-wmi-remotely-starting-with-vista.md)
</dt> <dt>

[Provider Hosting and Security](provider-hosting-and-security.md)
</dt> </dl>

 

 



