---
title: Server Graphical Shell restrictions
description: Server apps must be able to run without the Server Graphical Shell
ms.assetid: 8F531497-B64D-4E79-AD7A-790EFDC6ADFE
ms.topic: article
ms.date: 05/31/2018
---

# Server apps must be able to run without the Server Graphical Shell

## Platform

**Servers** – Windows Server 2012 

## Description

Server Graphical Shell, the feature that includes Windows Explorer and Internet Explorer, is installed by default on “Server with a GUI” installations of Windows Server 2012. The Server Graphical Shell feature can be uninstalled in order to reduce the potential servicing and performance footprint, thereby limiting the number of reboots that the server may incur, while still allowing management tools to be run locally on the server.

After an administrator uninstalls the Server Graphical Shell, the server is in the Minimal Server Interface configuration:

![server graphical shell interface configuration](images/minimalserverinterface.png)

Administrators can then opt to run in the Minimal Server Interface configuration (which includes a set of local management tools), as the default, rather than in the Server with a GUI configuration. This allows local monitoring and management, while reducing both resource usage and frequency of servicing.

Administrators can reinstall Server Graphical Shell later if they need the functionality within it. (Administrators can also start from a Server Core install, and “build up” to the Minimal Server Interface configuration using the Features On Demand functionality.)

Server apps must be capable of running in the Minimal Server Interface configuration to take advantage of the reduced resource utilization and servicing footprint. This capability can be achieved by allowing the administrator to choose not to install parts of the app that needs the Server Graphical Shell, or by detecting the presence of Server Graphical Shell and disabling some aspects of the app.

The Minimal Server Interface has a reduced resource and servicing footprint because many APIs and binaries that are included in the Server Graphical Shell are not available in this configuration. Where appropriate, server apps should also allow remote administration (preferably via Windows PowerShell Remoting) from another Windows Server or Windows Client installation. This enables better centralized administration of one or more machines in the Minimal Server Interface configuration, or of machines in an even lower footprint configuration such as Server Core.

## Manifestation

If an app requires any of the APIs or binaries that are not available in the Minimal Server Interface configuration, it may not display properly on the screen and/or be unusable.

## Mitigation

Server app developers should identify those parts of their apps that require any of the removed APIs or binaries and include info for the server administrator identifying the parts of the app that won’t run properly when using the Minimal Server Interface. If those parts of the app can be optionally installed or are not absolutely required for product functionality, the app can still be installed and run under the Minimal Server Interface configuration.

If the app cannot be used at all without the Server Graphical Shell, this limitation should be documented and the server administrator should be instructed to install the Server Graphical Shell. (If adding to a Server Core installation, this might require adding features using Features On Demand.) In addition, the app should check on startup that all required files are available, as the Server Graphical Shell can be uninstalled at any time before or after the installation of the app.

## Solution

Rely on the smallest possible set of dependencies, and modularize apps so that the core app functionality can work without requiring more heavyweight user interface components installed. Develop apps that do not require any of the removed APIs or binaries, and rely instead on the functionality contained within the Minimal Server Interface or Server Core. This will reduce maintenance requirements while improving performance and user satisfaction.

Where there are parts of an app that might add significant functionality when the Server Graphical Shell is available, app developers can:

-   Allow these additional features making use of Server Graphical Shell to be optionally installed, so they can be omitted from installations on a Minimal Server Interface configuration
-   Detect the presence of Server Graphical Shell and adapt the app behavior

App developers should also ensure that server apps are remotely manageable where possible and appropriate.

## Detecting Minimal Server Interface and Server Core

Windows Server will install a corresponding registry value for each server level installed. You can query for the existence of these keys to determine if the Server Graphical Shell or Minimal Server Interface features are installed and enabled.

HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Server\\ServerLevels:



|   &nbsp;         | Server Core | Minimal Server Interface | Server Graphical Shell |
|------------------|-------------|--------------------------|------------------------|
| ServerCore=1     | X           | X                        | X                      |
| Server-GuiMgmt=1 |             | X                        | X                      |
| ServerGuiShell=1 |             |                          | X                      |



 

An “X” in the table above means that registry key will be present when the corresponding feature is installed.

Note that these server levels are additive; if the Server Graphical Shell is installed, so is the Minimal Server Interface and Server Core. In that case, both registry keys will be present.

## Tests

Inspect your app code for requirements that use any of the removed APIs and binaries. After you have removed any instances of these from “core application” binaries, test your app in an environment that does not include the Server Graphical Shell. Tools such as the Process Monitor might help with this.

If you cannot completely discontinue use of these APIs and binaries, ensure that your app fails gracefully when run on Minimal Server Interface or Server Core.

## Resources

-   [Existing Server Core docs on MSDN](/previous-versions/windows/desktop/legacy/ms723891(v=vs.85))

 

 