---
title: Translating the Authored Firewall Policy into API Calls
description: The INetFwRule interface provides access to the properties of a rule. All the examples provided below will make use of it. You should familiarize yourself with it before reading further.
ms.assetid: 516d0dec-bf9d-4c02-952f-3de71327ea50
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Translating the Authored Firewall Policy into API Calls

The [**INetFwRule**](/previous-versions/windows/desktop/api/Netfw/nn-netfw-inetfwrule) interface provides access to the properties of a rule. All the examples provided below will make use of it. You should familiarize yourself with it before reading further.

The following table presents the rule properties exposed by [**INetFwRule**](/previous-versions/windows/desktop/api/Netfw/nn-netfw-inetfwrule) interface.



| INetFwRule Property | Comment                                                                                        |
|---------------------|------------------------------------------------------------------------------------------------|
| Action              | Accesses the [**Action**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_action) property of this rule.                        |
| Enabled             | Accesses the [**Enabled**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_enabled) property for this rule.                     |
| ApplicationName     | Accesses the [**ApplicationName**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_applicationname) property for this rule.     |
| Description         | Accesses the [**Description**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_description) property for this rule.             |
| Direction           | Accesses the [**Direction**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_direction) property for this rule.                 |
| EdgeTraversal       | Accesses the [**EdgeTraversal**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_edgetraversal) property for this rule.         |
| Grouping            | Accesses the [**Grouping**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_grouping) property for this rule.                   |
| IcmpTypesAndCodes   | Accesses the [**IcmpTypesAndCodes**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_icmptypesandcodes) property for this rule. |
| Interfaces          | Accesses the [**Interfaces**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_interfaces) property for this rule.               |
| InterfaceTypes      | Accesses the [**InterfaceTypes**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_interfacetypes) property for this rule.       |
| LocalAddresses      | Accesses the [**LocalAddresses**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_localaddresses) property for this rule.       |
| LocalPorts          | Accesses the [**LocalPorts**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_localports) property of this rule.                |
| Name                | Accesses the [**Name**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_name) property for this rule.                           |
| Profiles            | Accesses the [**Profiles**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_profiles) property for this rule.                   |
| Protocol            | Accesses the [**Protocol**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_protocol) property for this rule.                   |
| RemoteAddresses     | Accesses the [**RemoteAddresses**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_remoteaddresses) property of this rule.      |
| RemotePorts         | Accesses the [**RemotePorts**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_remoteports) property for this rule.             |
| ServiceName         | Accesses the [**ServiceName**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwrule-get_servicename) property for this rule.             |



 

 

 




