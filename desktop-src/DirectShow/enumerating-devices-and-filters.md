---
description: Enumerating Devices and Filters
ms.assetid: 334bba2a-7477-4115-9ce0-d4495c1fc290
title: Enumerating Devices and Filters
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Devices and Filters

Sometimes an application needs to locate a particular filter on the user's system. For example, a video capture application might display a list of available capture devices. Because DirectShow uses a component-based architecture, you cannot know at design time which filters are installed on the user's system. This is particularly true for filters that represent hardware devices. DirectShow provides two components that locate registered filters:

-   The [System Device Enumerator](system-device-enumerator.md) finds filters by their category.
-   The [Filter Mapper](filter-mapper.md) finds filters according to search criteria supplied by the application.

The enumerators discussed in this section follow the standard form used by COM enumeration interfaces. For more information, see the "IEnumXXXX" topic in the Microsoft Platform Software Development Kit (SDK).

This section contains the following topics:

-   [Using the System Device Enumerator](using-the-system-device-enumerator.md)
-   [Using the Filter Mapper](using-the-filter-mapper.md)

## Related topics

<dl> <dt>

[Basic DirectShow Tasks](basic-directshow-tasks.md)
</dt> </dl>

 

 



