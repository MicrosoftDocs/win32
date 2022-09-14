---
title: Configuring SNMP Group Policy
description: If you use the Microsoft Management Console (MMC) snap-in for Group Policy to administer registry-based policy settings that apply to SNMP, one or more of the following subkeys may exist.
ms.assetid: de21d2f5-3337-47ba-afcf-347e289873d3
ms.topic: article
ms.date: 05/31/2018
---

# Configuring SNMP Group Policy

If you use the Microsoft Management Console (MMC) snap-in for Group Policy to administer registry-based policy settings that apply to SNMP, one or more of the following subkeys may exist.

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Policies**\\**SNMP**\\**Parameters**\\**ValidCommunities**

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Policies**\\**SNMP**\\**Parameters**\\**PermittedManagers**

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Policies**\\**SNMP**\\**Parameters**\\**TrapConfiguration**

Typically, only members of the Administrators local group can access the following registry subkeys that store configuration data for the SNMP service:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**SNMP**\\**Parameters**\\**ValidCommunities**

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**SNMP**\\**Parameters**\\**PermittedManagers**

For more information about registry-based policy settings, see [About Group Policy](/previous-versions/windows/desktop/Policy/about-group-policy).

 

 