---
title: Windows Remote Management
description: Windows Remote Management (Windows Remote Management) is the Microsoft implementation of WS-Management Protocol, a standard SOAP-based, firewall-friendly protocol that allows hardware and operating systems, from different vendors, to interoperate.
ms.assetid: 6429e748-e0bf-431a-8989-db5b211665d5
ms.tgt_platform: multiple
keywords:
- Windows Remote Management (WinRM), Start Page
- WS-Management
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbOrient
api_name: 
api_type: 
api_location: 
---

# Windows Remote Management

## Purpose

Windows Remote Management (WinRM) is the Microsoft implementation of [WS-Management Protocol](ws-management-protocol.md), a standard Simple Object Access Protocol (SOAP)-based, firewall-friendly protocol that allows hardware and operating systems, from different vendors, to interoperate.

The WS-Management protocol specification provides a common way for systems to access and exchange management information across an IT infrastructure. WinRM and [*Intelligent Platform Management Interface (IPMI)*](windows-remote-management-glossary.md), along with the [Event Collector](https://go.microsoft.com/fwlink/p/?linkid=84396#event-collector) are components of the [Windows Hardware Management](https://go.microsoft.com/fwlink/p/?linkid=45204) features.

## Where applicable

You can use WinRM scripting objects, the WinRM command-line tool, or the Windows Remote Shell command line tool WinRS to obtain management data from local and remote computers that may have [*baseboard management controllers (BMCs)*](windows-remote-management-glossary.md). If the computer runs a Windows-based operating system version that includes WinRM, the management data is supplied by [Windows Management Instrumentation (WMI)](https://docs.microsoft.com/windows/desktop/WmiSdk/wmi-start-page).

You can also obtain hardware and system data from WS-Management protocol implementations running on operating systems other than Windows in your enterprise. WinRM establishes a session with a remote computer through the SOAP-based WS-Management protocol rather than a connection through DCOM, as WMI does. Data returned to WS-Management protocol are formatted in XML rather than in objects.

The [Intelligent Platform Management Interface (IPMI)](https://docs.microsoft.com/previous-versions/windows/desktop/ipmiprv/ipmi-provider) WMI provider is a standard WMI provider with classes that obtain BMC sensor data from computers with appropriate hardware. IPMI data can be accessed using the WinRM scripting API, the WMI [Scripting](https://docs.microsoft.com/windows/desktop/WmiSdk/scripting-api-for-wmi), or [COM](https://docs.microsoft.com/windows/desktop/WmiSdk/com-api-for-wmi) APIs.

## Developer audience

The developer audience is the IT Pro who writes scripts to automate the management of servers or the ISV developer obtaining data for management applications.

## Run-time requirements

WinRM is part of the operating system. However, to obtain data from remote computers, you must configure a WinRM [*listener*](windows-remote-management-glossary.md#l). For more information, see [Installation and Configuration for Windows Remote Management](installation-and-configuration-for-windows-remote-management.md). If a BMC is detected at system startup, then the IPMI provider loads; otherwise, the WinRM scripting objects and the WinRM command-line tool are still available.

## In this section

<dl> <dt>

[About Windows Remote Management](about-windows-remote-management.md)
</dt> <dd>

Link to public WS-Management protocol specification, WinRM architecture, relationship to WMI, hardware management with the IPMI provider, configuration and installation.

</dd> <dt>

[Using Windows Remote Management](using-windows-remote-management.md)
</dt> <dd>

Getting started using the WinRM scripting API and hardware management.

</dd> <dt>

[Windows Remote Management Reference](windows-remote-management-reference.md)
</dt> <dd>

List of scripting interfaces defined by Microsoft Web Services for Management (WS-Management) Automation and class definitions of the WMI classes created by the IPMI provider and classes that communicate with the IPMI driver to obtain [baseboard management controller (BMC)](windows-remote-management-glossary.md) data.

</dd> </dl>

 

 




