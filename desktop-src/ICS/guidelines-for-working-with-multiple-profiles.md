---
title: Guidelines for Working with Multiple Profiles
description: Best practices that will help you avoid common errors when working with multiple profiles.
ms.assetid: 3105c6d0-813c-499d-b585-8c5d9fa15414
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Guidelines for Working with Multiple Profiles

The following list includes best practices that will help you avoid common errors when working with multiple profiles.

-   Always assume that more than one firewall profile could be active at a given time.
-   Do not pass a bitmask returned by [**get\_CurrentProfileTypes()**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwpolicy2-get_currentprofiletypes) to a function such as [**put\_FirewallEnabled()**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwprofile-get_firewallenabled) which does not support bitmask.
-   Do not try to compare the bitmask returned by [**get\_CurrentProfileTypes()**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwpolicy2-get_currentprofiletypes) to a specific profile value.
-   Do not cast the bitmask by [**get\_CurrentProfileTypes()**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwpolicy2-get_currentprofiletypes) to the enumerated type [**NET\_FW\_PROFILE\_TYPE2**](/previous-versions/windows/desktop/api/Icftypes/ne-icftypes-net_fw_profile_type2_).
-   Make sure to properly handle S\_FALSE as a possible return value from functions such as [**LocalPolicyModifyState()**](/previous-versions/windows/desktop/api/Netfw/), [**get\_IsRuleGroupCurrentlyEnabled()**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwpolicy2-get_isrulegroupcurrentlyenabled), and [**IsRuleGroupEnabled()**](/previous-versions/windows/desktop/api/Netfw/nf-netfw-inetfwpolicy2-isrulegroupenabled).

For an example that illustrates working with multiple profiles, see [Working with Multiple Profiles](working-with-multiple-profiles.md).

 

 




