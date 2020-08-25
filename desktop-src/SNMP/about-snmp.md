---
title: About SNMP
description: SNMP uses a distributed architecture consisting of managers and agents.
ms.assetid: 55be55a8-1968-4373-a969-f7e03b75a824
keywords:
- SNMP, About
ms.topic: article
ms.date: 05/31/2018
---

# About SNMP

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](/windows/desktop/WinRM/portal), which is the Microsoft implementation of WS-Man.\]

SNMP uses a distributed architecture consisting of managers and agents. An agent is an SNMP application that responds to queries from SNMP manager applications. The SNMP agent is responsible for retrieving and updating local management information based on the requests of the SNMP manager. The agent also notifies registered managers when significant events or traps occur. A manager is an SNMP application that generates queries to SNMP agent applications and receives traps from SNMP agent applications.

On computers running Microsoft Windows XP/Windows 2000/Windows NT, the SNMP agent is implemented by the SNMP service (SNMP.EXE). The SNMP manager is typically a third-party SNMP management console application. The management console application does not need to run on the same host as the SNMP agent. To use the information the Microsoft SNMP service provides, you need at least one SNMP management console application. The system includes libraries that support SNMP management console applications, but it does not include an SNMP management console application at this time.

 

 