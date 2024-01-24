---
description: 'Before putting data into the registry, an application should divide the data into two categories: computer-specific data and user-specific data.'
ms.assetid: 470d00c1-5975-4a58-9a78-fbed7326a60c
title: Categories of Data
ms.topic: article
ms.date: 05/31/2018
---

# Categories of Data

Before putting data into the registry, an application should divide the data into two categories: computer-specific data and user-specific data. By making this distinction, an application can support multiple users, and yet locate user-specific data over a network and use that data in different locations, allowing location-independent user profile data. (A user profile is a set of configuration data saved for every user.)

When the application is installed, it should record the computer-specific data under the **HKEY\_LOCAL\_MACHINE** key. In particular, it should create keys for the company name, product name, and version number, as shown in the following example:

**HKEY\_LOCAL\_MACHINE\\Software\\***MyCompany\\MyProduct\\1.0*

If the application supports COM, it should record that data under **HKEY\_LOCAL\_MACHINE\\Software\\Classes**.

An application should record user-specific data under the **HKEY\_CURRENT\_USER** key, as shown in the following example:

**HKEY\_CURRENT\_USER\\Software\\***MyCompany\\MyProduct\\1.0*

 

 



