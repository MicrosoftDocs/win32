---
title: Windows Firewall Profiles
description: When authoring your firewall rules it is best to only plumb your firewall rules to profiles that are appropriate for your scenarios and to modify your rules according to each specific profile.
ms.assetid: 6c0ea258-0cc2-43a0-ade7-1795354f5dce
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Firewall Profiles

When authoring your firewall rules it is best to only plumb your firewall rules to profiles that are appropriate for your scenarios and to modify your rules according to each specific profile.

Windows Firewall offers three firewall profiles: domain, private and public. The domain profile applies to networks where the host system can authenticate to a domain controller. The private profile is a user-assigned profile and is used to designate private or home networks. Lastly, the default profile is the public profile, which is used to designate public networks such as Wi-Fi hotspots at coffee shops, airports, and other locations.

Windows Firewall provides public APIs which can be used to acquire the current profile and to enable firewall rule groups on specific profiles. These APIs should be utilized by all installers to provide the best user experience and seamless integration.

Best practices are to create your rules in all three profiles, but only enable the firewall rule group on the profiles that suit your scenarios. For example, if you are installing a home media sharing application that is only used on a private network then it would be best to create firewall rules in all three profiles, but only enable the firewall rule group containing your rules on the private profile.

If the current profile is not one of the profiles which apply to your scenarios, then inform the user that your firewall rules are not enabled in the current profile. You should also inform the user that the application will not function as expected unless the user moves to a network which has one of the profiles that applies to your scenario or re-categorizes the current network.

Enabling rules that have been created in the public profile by default is not recommended.

## Windows Firewall Profiles - Restrictions per Profile

You may also wish to modify the restrictions on your firewall rules depending on which profile the rules are applied to. For applications and services that are designed to only be accessed by devices or other computers within a home or small business network, it is best to modify the remote address restriction to specify "Local Subnet" only. The same application or service would not have this restriction when used in an enterprise environment. This can be done by adding the remote address restriction to rules that are added to the private and public profiles, while leaving them unrestricted in the domain profile. This remote address restriction should not apply to applications or services that require global Internet connectivity.

 

 




