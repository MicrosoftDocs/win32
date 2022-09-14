---
description: WMI implements a technique that allows multiple localized versions of the same class to be stored in the repository.
ms.assetid: 01e1cee5-d882-45b6-ac93-68533c2c6c9d
ms.tgt_platform: multiple
title: Localizing WMI Class Information
ms.topic: article
ms.date: 05/31/2018
---

# Localizing WMI Class Information

WMI implements a technique that allows multiple localized versions of the same class to be stored in the repository.

The class definition is separated into the following versions:

-   A language-neutral version that contains only a basic class definition.
-   A language-specific version that contains localized information, such as property descriptions that are specific to a locale.

The language-specific class definitions are stored in a child namespace beneath the namespace that contains a language-neutral basic class definition.

When you request a localized class definition for a specific locale, WMI combines the basic class definition and the localized class information to form a complete localized class. You can get a localized version of a WMI class by specifying a locale when you connect to WMI and setting a flag that indicates that you want localized information. WMI then merges the information from the language-neutral and the language-specific versions of the class definition to form a localized class.

WMI classes that contain localized information are marked with the **Amendment** qualifier and are called amended classes; a class supports localized information if it has this qualifier. You can determine which locale the class has been localized for by checking for another qualifier called [**Locale**](swbemobjectpath-locale.md). The locale qualifier contains a localization identifier (Windows LCID) that identifies a locale. For example, the locale for American English is 0x409. If a qualifier in an amended class contains localized information, it contains the **amended** qualifier flavor.

WMI localization includes the following tasks:

-   [Creating localized class definitions](creating-localized-class-definitions.md)
-   [Compiling localized MOF files](compiling-localized-mof-files.md)
-   [Localizing property values](localizing-property-values.md)
-   [Retrieving amended classes](retrieving-amended-classes.md)

For more information, see [Amended Class Considerations](amended-class-considerations.md).

 

 



