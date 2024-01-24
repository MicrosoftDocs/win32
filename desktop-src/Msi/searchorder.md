---
description: Setting this per-user system policy specifies the order in which the installer searches three types of sources.
ms.assetid: c16a5cbb-d530-4932-944b-af68d0a4018c
title: SearchOrder
ms.topic: article
ms.date: 05/31/2018
---

# SearchOrder

Setting this per-user [system policy](system-policy.md) specifies the order in which the installer searches three types of sources. The types of sources are:

"n" – network

"m" – media (CD-ROM or DVD)

"u" – Uniform Resource Locator (URL)

For example, to search network sources first, media sources second, and URL sources last set this policy to a value of "nmu". To omit searching for a particular source type, leave out the corresponding letter from the value.

If SearchOrder is not set, the default search order is network, media, and then URL.

## Registry Key

**HKEY\_CURRENT\_USER**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_SZ**

## Related topics

<dl> <dt>

[Source Resiliency](source-resiliency.md)
</dt> </dl>

 

 



