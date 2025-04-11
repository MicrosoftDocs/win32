---
title: Categories of data
description: 'Before putting data into the registry, an application should divide the data into two categories: computer-specific data and user-specific data.'
ms.assetid: 470d00c1-5975-4a58-9a78-fbed7326a60c
ms.topic: concept-article
ms.date: 01/30/2025
---

# Categories of data

Before storing data in the registry, your app should divide the data into two categories: computer-specific data and user-specific data. By making this distinction, your app can support multiple users, and yet locate user-specific data over a network and use that data in different locations, allowing location-independent user profile data. A user profile is a set of configuration data saved for every user.

When your app is installed, it should record the computer-specific data under the **HKEY\_LOCAL\_MACHINE** key. In particular, it should create keys for the company name, product name, and version number, as shown in the following example:

HKEY\_LOCAL\_MACHINE\\Software\\MyCompany\\MyProduct\\1.0

If your app supports COM, then it should record that data under **HKEY\_LOCAL\_MACHINE\\Software\\Classes**.

Your app should record user-specific data under the **HKEY\_CURRENT\_USER** key, as shown in the following example:

HKEY\_CURRENT\_USER\\Software\\MyCompany\\MyProduct\\1.0
