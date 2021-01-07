---
description: If this per-user system policy is set to &\#0034;1&\#0034;; the installer searches for transform files in the root of any network sources in the source list for the product. By default, transforms are stored in the Application Data folder of a user's profile.
ms.assetid: 24881078-1610-4a37-a52d-fcabd78e1738
title: TransformsAtSource Policy
ms.topic: article
ms.date: 05/31/2018
---

# TransformsAtSource Policy

If this per-user [system policy](system-policy.md) is set to "1"; the installer searches for transform files in the root of any network sources in the source list for the product. By default, transforms are stored in the Application Data folder of a user's profile.

Windows Installer interprets the TransformsAtSource policy to be the same as the [TransformsSecure policy](transformssecure-policy.md).

## Registry Key

**HKEY\_CURRENT\_USER**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_SZ**

 

 



