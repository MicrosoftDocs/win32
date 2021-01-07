---
description: The Native Wifi API contains functions, structures, and enumerations that support wireless network connectivity and wireless profile management.
ms.assetid: 686f9ccf-5040-44c5-8633-83f12dc46586
title: About the Native Wifi API
ms.topic: article
ms.date: 05/31/2018
---

# About the Native Wifi API

The Native Wifi API contains functions, structures, and enumerations that support wireless network connectivity and wireless profile management. The API can be used for both infrastructure and ad hoc networks. The Wireless Ad Hoc API is a simplified object-oriented interface for creating, managing, and using ad hoc networks.

> [!Note]  
> Ad hoc mode might not be available in future versions of Windows. Starting with Windows 8.1 and Windows Server 2012 R2, use [Wi-Fi Direct](about-the-wi-fi-direct-api.md) instead.

 

The implementation of the Ad Hoc API uses the Native Wifi API. This means that Ad Hoc API calls can trigger Native Wifi notifications, and vice versa.

Mixing Native Wifi API calls and Wireless Ad Hoc API calls is not recommended. Developers should choose a programming approach before designing an application. If your application uses or manages infrastructure networks, you should use the Native Wifi API. If your application requires profile management functionality, you should use the Native Wifi API. Otherwise, you should use the Wireless Ad Hoc API.

## Related topics

<dl> <dt>

[About Native Wifi](about-native-wifi.md)
</dt> <dt>

[Native Wifi API Support on Windows XP](about-wireless-lan-api-for-windows-xp-service-pack-2.md)
</dt> <dt>

[Native Wifi API Permissions](native-wifi-api-permissions.md)
</dt> <dt>

[About the Wireless Ad Hoc API](about-the-wireless-ad-hoc-api.md)
</dt> <dt>

[Download the Windows Vista SDK](https://www.microsoft.com/downloads/details.aspx?FamilyID=f26b1aa4-741a-433a-9be5-fa919850bdbf)
</dt> </dl>

 

 



