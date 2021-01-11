---
description: About the ACM Architecture
ms.assetid: 4a5c0085-0e7b-424d-9205-5ec39518a088
title: About the ACM Architecture
ms.topic: article
ms.date: 05/31/2018
---

# About the ACM Architecture

The Auto Configuration Module (ACM) is the new wireless configuration component for Windows Vista. Windows XP with Service Pack 3 (SP3) and Wireless LAN API for Windows XP with Service Pack 2 (SP2) use the Wireless Zero Configuration (WZC) service instead.

The ACM scans networks periodically and uses an iterative process to select and connect to the most preferred network in the range, if that network has an interface enabled for auto-connection. The ACM also saves and retrieves network profiles, which contain ACM, Media Specific Module (MSM), security, and independent hardware vendor (IHV) settings. These network profiles are for auto configuration.

Auto configuration supports both global and per-interface settings and network profiles. The global settings and network profiles are configured if the machine has joined a domain with a group policy object (GPO) either at the domain level or the organizational unit (OU) level in the Active Directory (AD) hierarchy. These group policy settings and profiles are read-only, applied to each 802.11 interface in the system, and always take precedence over the per-interface and per-user settings and network profiles. The group policy profiles are placed at the top of the preferred network profile list on each 802.11 network interface.

The ACM architecture is extensible. IHVs can implement proprietary wireless functionality without altering the provided native 802.11 framework. The exposed IHV control functions and structures enable this extensibility.

## Related topics

<dl> <dt>

[About Native Wifi](about-native-wifi.md)
</dt> </dl>

 

 



