---
description: Allows client applications to access SNMP information through WMI.
ms.assetid: d9e3fd1d-8320-4407-9a9e-e2eb5dd62fef
ms.tgt_platform: multiple
title: Accessing SNMP Devices
ms.topic: article
ms.date: 05/31/2018
---

# Accessing SNMP Devices

The Simple Network Management Protocol (SNMP) provider allows client applications to access SNMP information through WMI. The [SNMP provider](snmp-provider.md) acts as a gateway to systems and devices that use SNMP for management. Only the management or monitoring computer must be running WMI because it can read from any SNMP-enabled device.

> [!Note]  
> For more information about installing the provider, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 

SNMP Management Information Base (MIB) object variables can be read from and written to, and SNMP traps can be automatically mapped to WMI events, which can be defined for any arbitrary create, delete, or update operations to data beyond the MIB-defined traps. This feature of WMI functions as an extension of standard SNMP capabilities. For more information, see [Monitoring Events](monitoring-events.md).

The tools described in the following topics are designed for use by Windows scripting and C/C++ programmers. Familiarity with WMI, SNMPv1 and SNMPv2C, and a working knowledge of networking and network management concepts are recommended.

For more information about using WMI with SNMP, see [Setting up the WMI SNMP Environment](setting-up-the-wmi-snmp-environment.md).

 

 



