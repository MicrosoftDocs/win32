---
title: Guidelines for Working with Multiple Profiles
description: Best practices that will help you avoid common errors when working with multiple profiles.
ms.assetid: '3105c6d0-813c-499d-b585-8c5d9fa15414'
---

# Guidelines for Working with Multiple Profiles

The following list includes best practices that will help you avoid common errors when working with multiple profiles.

-   Always assume that more than one firewall profile could be active at a given time.
-   Do not pass a bitmask returned by [**get\_CurrentProfileTypes()**](inetfwpolicy2-currentprofiletypes.md) to a function such as [**put\_FirewallEnabled()**](inetfwprofile-firewallenabled.md) which does not support bitmask.
-   Do not try to compare the bitmask returned by [**get\_CurrentProfileTypes()**](inetfwpolicy2-currentprofiletypes.md) to a specific profile value.
-   Do not cast the bitmask by [**get\_CurrentProfileTypes()**](inetfwpolicy2-currentprofiletypes.md) to the enumerated type [**NET\_FW\_PROFILE\_TYPE2**](net-fw-profile-type2.md).
-   Make sure to properly handle S\_FALSE as a possible return value from functions such as [**LocalPolicyModifyState()**](inetfwpolicy2-localpolicymodifystate.md), [**get\_IsRuleGroupCurrentlyEnabled()**](inetfwpolicy2-isrulegroupcurrentlyenabled.md), and [**IsRuleGroupEnabled()**](inetfwpolicy2-isrulegroupenabled.md).

For an example that illustrates working with multiple profiles, see [Working with Multiple Profiles](working-with-multiple-profiles.md).

 

 




