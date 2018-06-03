---
title: Checking the Effective Firewall Status
description: Firewall status is determined by a combination of two levels of control.
ms.assetid: c2a6f57d-e05b-4143-90ad-39ca32d66c66
keywords:
- Checking the Effective Firewall Status
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Checking the Effective Firewall Status

Firewall status is determined by a combination of two levels of control. Global operation mode determines whether the firewall is enabled and whether exceptions are allowed. Interface operation mode determines whether a specific interface is firewalled when the firewall is enabled. To find the current status of the firewall, first check the global operation mode, and then check the mode on the interface of interest.

To check the global operation mode, use the [**FirewallEnabled**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwprofile-get_firewallenabled) property of the [**INetFwProfile**](/previous-versions/windows/desktop/api/Netfw/nn-netfw-inetfwprofile) object to find out if the firewall is enabled. Use the [**ExceptionsNotAllowed**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwprofile-get_exceptionsnotallowed) property of the **INetFwProfile** object to find out if exceptions are allowed.

To check the interface operation mode, use the [**InternetFirewallEnabled**](/previous-versions/windows/desktop/api/NetCon/nf-netcon-inetsharingconfiguration-get_internetfirewallenabled) property of the [**INetSharingConfiguration**](/previous-versions/windows/desktop/api/NetCon/nn-netcon-inetsharingconfiguration) object.

The following table lists the resulting system state as a combination of the global operation mode and the operation mode of a specific interface.



| Global Operation Mode              | Interface Operation Mode | Resultant Firewall Status |
|------------------------------------|--------------------------|---------------------------|
| Enabled                            | Enabled                  | Enabled                   |
| Not Enabled                        | Not Enabled              | Not Enabled               |
| Not Enabled                        | Enabled                  | Not Enabled               |
| Enabled                            | Not Enabled              | Not Enabled               |
| Exceptions Not Allowed AND Enabled | Enabled                  | Enabled                   |
| Exceptions Not Allowed AND Enabled | Not Enabled              | Enabled                   |



 

 

 




