---
title: Checking the Effective Firewall Status
description: Firewall status is determined by a combination of two levels of control.
ms.assetid: c2a6f57d-e05b-4143-90ad-39ca32d66c66
keywords:
- Checking the Effective Firewall Status
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Checking the Effective Firewall Status

Firewall status is determined by a combination of two levels of control. Global operation mode determines whether the firewall is enabled and whether exceptions are allowed. Interface operation mode determines whether a specific interface is firewalled when the firewall is enabled. To find the current status of the firewall, first check the global operation mode, and then check the mode on the interface of interest.

To check the global operation mode, use the [**FirewallEnabled**](/windows/previous-versions/Netfw/nf-netfw-inetfwprofile-get_firewallenabled?branch=master) property of the [**INetFwProfile**](/windows/previous-versions/Netfw/nn-netfw-inetfwprofile?branch=master) object to find out if the firewall is enabled. Use the [**ExceptionsNotAllowed**](/windows/previous-versions/Netfw/nf-netfw-inetfwprofile-get_exceptionsnotallowed?branch=master) property of the **INetFwProfile** object to find out if exceptions are allowed.

To check the interface operation mode, use the [**InternetFirewallEnabled**](/windows/previous-versions/NetCon/nf-netcon-inetsharingconfiguration-get_internetfirewallenabled?branch=master) property of the [**INetSharingConfiguration**](/windows/previous-versions/NetCon/nn-netcon-inetsharingconfiguration?branch=master) object.

The following table lists the resulting system state as a combination of the global operation mode and the operation mode of a specific interface.



| Global Operation Mode              | Interface Operation Mode | Resultant Firewall Status |
|------------------------------------|--------------------------|---------------------------|
| Enabled                            | Enabled                  | Enabled                   |
| Not Enabled                        | Not Enabled              | Not Enabled               |
| Not Enabled                        | Enabled                  | Not Enabled               |
| Enabled                            | Not Enabled              | Not Enabled               |
| Exceptions Not Allowed AND Enabled | Enabled                  | Enabled                   |
| Exceptions Not Allowed AND Enabled | Not Enabled              | Enabled                   |



 

 

 




