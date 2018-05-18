---
title: Checking the Effective Firewall Status
description: Firewall status is determined by a combination of two levels of control.
ms.assetid: 'c2a6f57d-e05b-4143-90ad-39ca32d66c66'
keywords: ["Checking the Effective Firewall Status"]
---

# Checking the Effective Firewall Status

Firewall status is determined by a combination of two levels of control. Global operation mode determines whether the firewall is enabled and whether exceptions are allowed. Interface operation mode determines whether a specific interface is firewalled when the firewall is enabled. To find the current status of the firewall, first check the global operation mode, and then check the mode on the interface of interest.

To check the global operation mode, use the [**FirewallEnabled**](inetfwprofile-firewallenabled.md) property of the [**INetFwProfile**](inetfwprofile.md) object to find out if the firewall is enabled. Use the [**ExceptionsNotAllowed**](inetfwprofile-exceptionsnotallowed.md) property of the **INetFwProfile** object to find out if exceptions are allowed.

To check the interface operation mode, use the [**InternetFirewallEnabled**](inetsharingconfiguration-get-internetfirewallenabled.md) property of the [**INetSharingConfiguration**](inetsharingconfiguration.md) object.

The following table lists the resulting system state as a combination of the global operation mode and the operation mode of a specific interface.



| Global Operation Mode              | Interface Operation Mode | Resultant Firewall Status |
|------------------------------------|--------------------------|---------------------------|
| Enabled                            | Enabled                  | Enabled                   |
| Not Enabled                        | Not Enabled              | Not Enabled               |
| Not Enabled                        | Enabled                  | Not Enabled               |
| Enabled                            | Not Enabled              | Not Enabled               |
| Exceptions Not Allowed AND Enabled | Enabled                  | Enabled                   |
| Exceptions Not Allowed AND Enabled | Not Enabled              | Enabled                   |



 

 

 




