---
title: Guidelines for Working with Multiple Profiles
description: Best practices that will help you avoid common errors when working with multiple profiles.
ms.assetid: 3105c6d0-813c-499d-b585-8c5d9fa15414
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Guidelines for Working with Multiple Profiles

The following list includes best practices that will help you avoid common errors when working with multiple profiles.

-   Always assume that more than one firewall profile could be active at a given time.
-   Do not pass a bitmask returned by [**get\_CurrentProfileTypes()**](/windows/previous-versions/Netfw/nf-netfw-inetfwpolicy2-get_currentprofiletypes?branch=master) to a function such as [**put\_FirewallEnabled()**](/windows/previous-versions/Netfw/nf-netfw-inetfwprofile-get_firewallenabled?branch=master) which does not support bitmask.
-   Do not try to compare the bitmask returned by [**get\_CurrentProfileTypes()**](/windows/previous-versions/Netfw/nf-netfw-inetfwpolicy2-get_currentprofiletypes?branch=master) to a specific profile value.
-   Do not cast the bitmask by [**get\_CurrentProfileTypes()**](/windows/previous-versions/Netfw/nf-netfw-inetfwpolicy2-get_currentprofiletypes?branch=master) to the enumerated type [**NET\_FW\_PROFILE\_TYPE2**](/windows/previous-versions/Icftypes/ne-icftypes-net_fw_profile_type2_?branch=master).
-   Make sure to properly handle S\_FALSE as a possible return value from functions such as [**LocalPolicyModifyState()**](/windows/previous-versions/Netfw/?branch=master), [**get\_IsRuleGroupCurrentlyEnabled()**](/windows/previous-versions/Netfw/nf-netfw-inetfwpolicy2-get_isrulegroupcurrentlyenabled?branch=master), and [**IsRuleGroupEnabled()**](/windows/previous-versions/Netfw/nf-netfw-inetfwpolicy2-isrulegroupenabled?branch=master).

For an example that illustrates working with multiple profiles, see [Working with Multiple Profiles](working-with-multiple-profiles.md).

 

 




