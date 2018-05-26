---
title: Translating the Authored Firewall Policy into API Calls
description: The INetFwRule interface provides access to the properties of a rule. All the examples provided below will make use of it. You should familiarize yourself with it before reading further.
ms.assetid: 516d0dec-bf9d-4c02-952f-3de71327ea50
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Translating the Authored Firewall Policy into API Calls

The [**INetFwRule**](/windows/previous-versions/Netfw/nn-netfw-inetfwrule?branch=master) interface provides access to the properties of a rule. All the examples provided below will make use of it. You should familiarize yourself with it before reading further.

The following table presents the rule properties exposed by [**INetFwRule**](/windows/previous-versions/Netfw/nn-netfw-inetfwrule?branch=master) interface.



| INetFwRule Property | Comment                                                                                        |
|---------------------|------------------------------------------------------------------------------------------------|
| Action              | Accesses the [**Action**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_action?branch=master) property of this rule.                        |
| Enabled             | Accesses the [**Enabled**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_enabled?branch=master) property for this rule.                     |
| ApplicationName     | Accesses the [**ApplicationName**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_applicationname?branch=master) property for this rule.     |
| Description         | Accesses the [**Description**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_description?branch=master) property for this rule.             |
| Direction           | Accesses the [**Direction**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_direction?branch=master) property for this rule.                 |
| EdgeTraversal       | Accesses the [**EdgeTraversal**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_edgetraversal?branch=master) property for this rule.         |
| Grouping            | Accesses the [**Grouping**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_grouping?branch=master) property for this rule.                   |
| IcmpTypesAndCodes   | Accesses the [**IcmpTypesAndCodes**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_icmptypesandcodes?branch=master) property for this rule. |
| Interfaces          | Accesses the [**Interfaces**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_interfaces?branch=master) property for this rule.               |
| InterfaceTypes      | Accesses the [**InterfaceTypes**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_interfacetypes?branch=master) property for this rule.       |
| LocalAddresses      | Accesses the [**LocalAddresses**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_localaddresses?branch=master) property for this rule.       |
| LocalPorts          | Accesses the [**LocalPorts**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_localports?branch=master) property of this rule.                |
| Name                | Accesses the [**Name**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_name?branch=master) property for this rule.                           |
| Profiles            | Accesses the [**Profiles**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_profiles?branch=master) property for this rule.                   |
| Protocol            | Accesses the [**Protocol**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_protocol?branch=master) property for this rule.                   |
| RemoteAddresses     | Accesses the [**RemoteAddresses**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_remoteaddresses?branch=master) property of this rule.      |
| RemotePorts         | Accesses the [**RemotePorts**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_remoteports?branch=master) property for this rule.             |
| ServiceName         | Accesses the [**ServiceName**](/windows/previous-versions/Netfw/nf-netfw-inetfwrule-get_servicename?branch=master) property for this rule.             |



 

 

 




