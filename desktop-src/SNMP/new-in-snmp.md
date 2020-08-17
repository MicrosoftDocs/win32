---
title: New in SNMP
description: SNMP supports the use of IPv6 starting with Windows Vista.
ms.assetid: 38d71c0a-8de1-45a7-958c-aa44411451bc
ms.topic: article
ms.date: 05/31/2018
---

# New in SNMP

\[SNMP is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [Windows Remote Management](/windows/desktop/WinRM/portal), which is the Microsoft implementation of WS-Man.\]

SNMP supports the use of IPv6 starting with Windows Vista. However, SNMP supports IPv6 only for networks running Windows Server 2008 and Windows Vista. This is because SNMP requires the updated protocol stack available in these operating systems for its IPv6 support.

Unless your network is solely a Windows Server 2008 network, IPv6 communications will fail, even if an IPv6 protocol stack is separately installed on those computers that run earlier versions of Windows. For example, SNMP agents that run on Windows Server 2003, or Windows XP, or Windows 2000, respond only to queries that are made to their IPv4 addresses.

 

 