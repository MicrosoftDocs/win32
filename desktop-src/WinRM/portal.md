---
title: Windows Remote Management
description: Windows Remote Management (WinRM) is the Microsoft implementation of the WS-Management Protocol, which is a standard SOAP-based, firewall-friendly protocol that allows interoperation between hardware and operating systems from different vendors.
ms.assetid: 6429e748-e0bf-431a-8989-db5b211665d5
ms.tgt_platform: multiple
keywords:
- Windows Remote Management (WinRM), Start Page
- WS-Management
ms.topic: article
ms.date: 02/16/2023
topic_type: 
- kbOrient
api_name: 
api_type: 
api_location: 
---

# Windows Remote Management

Windows Remote Management (WinRM) is the Microsoft implementation of the [WS-Management protocol](ws-management-protocol.md), which is a standard Simple Object Access Protocol (SOAP)-based, firewall-friendly protocol that allows interoperation between hardware and operating systems from different vendors.

The WS-Management protocol specification provides a common way for systems to access and exchange management information across an IT infrastructure. WinRM and the [Intelligent Platform Management Interface (IPMI)](windows-remote-management-glossary.md#i) standard, along with the [Event Collector service](/previous-versions/windows/it-pro/windows-server-2003/cc785056(v=ws.10)#event-collector) are components of the set of features known as [Hardware management](/previous-versions/windows/it-pro/windows-server-2003/cc785056(v=ws.10)).

## Who is WinRM for?

The intended audience for Windows Remote Management is IT professionals&mdash;who write scripts to automate the management of servers&mdash;and independent software vendor (ISV) developers, who want to obtain data for management applications.

## Where can I use WinRM?

To obtain management data from local and remote computers that might have [baseboard management controllers (BMCs)](windows-remote-management-glossary.md), you can use: WinRM scripting objects; the WinRM command-line tool; or the Windows Remote Shell (WinRS) command-line tool. If the computer runs a Windows-based operating system version that includes WinRM, then the management data is supplied by [Windows Management Instrumentation (WMI)](/windows/win32/WmiSdk/wmi-start-page).

You can also obtain hardware and system data from WS-Management protocol implementations running on operating systems other than Windows in your enterprise. WinRM establishes a session with a remote computer through the SOAP-based WS-Management protocol rather than a connection through DCOM, as WMI does. Data returned using the WS-Management protocol is formatted in XML instead of as objects.

The [Intelligent Platform Management Interface (IPMI)](/previous-versions/windows/desktop/ipmiprv/ipmi-provider) WMI provider is a standard WMI provider with classes that obtain BMC sensor data from computers with the appropriate hardware. You can access IPMI data by using: the WinRM scripting API; WMI [scripting](/windows/desktop/WmiSdk/scripting-api-for-wmi); or [COM](/windows/desktop/WmiSdk/com-api-for-wmi) APIs.

## Run-time requirements

WinRM is part of the operating system. However, to obtain data from remote computers, you must configure a WinRM [listener](windows-remote-management-glossary.md#l). For more information, see [Installation and configuration for Windows Remote Management](installation-and-configuration-for-windows-remote-management.md). If a BMC is detected at system startup, then the IPMI provider loads; but even if not, the WinRM scripting objects and the WinRM command-line tool are still available.

## See also

- [About Windows Remote Management](about-windows-remote-management.md)

  A collection of articles about: the public Microsoft Web Services for Management (WS-Management) protocol specification; WinRM architecture; relationship to WMI; hardware management with the IPMI provider; and WinRM configuration and installation.

- [Use Windows Remote Management](using-windows-remote-management.md)

  A collection of articles about how to use the WinRM scripting API to manage hardware.

- [Windows Remote Management reference](windows-remote-management-reference.md)

  Contains the scripting interfaces defined by WS-Management automation. Also contains class definitions of the WMI classes created by the IPMI provider and classes that communicate with the IPMI driver to obtain [baseboard management controller (BMC)](windows-remote-management-glossary.md#b) data.
