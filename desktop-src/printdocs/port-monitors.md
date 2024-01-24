---
description: Once a device driver has converted an entire journal file into raw device commands, the file of converted commands is passed back to the spooler.
ms.assetid: 149e44d0-052a-48ba-8f65-59eab193c785
title: Port Monitors
ms.topic: article
ms.date: 05/31/2018
---

# Port Monitors

Once a device driver has converted an entire journal file into raw device commands, the file of converted commands is passed back to the spooler. The spooler sends these low-level commands to a monitor. A port monitor is a .dll that passes the raw device commands over the network, through a parallel port, or through a serial port to the printer device. Custom port monitors can be installed to support passing device data through other communication ports.

Use the following functions to work with port monitors.



| Function                               | Description                                                                         |
|----------------------------------------|-------------------------------------------------------------------------------------|
| [**AddMonitor**](addmonitor.md)       | Installs a local port monitor and links the configuration, data, and monitor files. |
| [**DeleteMonitor**](deletemonitor.md) | Removes a port monitor added by the [**AddMonitor**](addmonitor.md) function.      |
| [**EnumMonitors**](enummonitors.md)   | Enumerates the port monitors installed on a specified server.                       |



 

 

 



