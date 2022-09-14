---
description: If this per-user system policy is set to &\#0034;1&\#0034;, users and administrators running a maintenance installation of one product are prevented from using the Browse Dialog to browse media sources, such as CD-ROM, for the sources of other installable products.
ms.assetid: 275a6d43-ecf8-4146-82eb-3b42b25b9a80
title: DisableMedia
ms.topic: article
ms.date: 05/31/2018
---

# DisableMedia

If this per-user [system policy](system-policy.md) is set to "1", users and administrators running a maintenance installation of one product are prevented from using the Browse Dialog to browse media sources, such as CD-ROM, for the sources of other installable products. Browsing for other products is prevented regardless of whether the installation is done with elevated privileges. It is still possible for the user to reinstall the product from media if the user has a correctly labeled media source.

## Registry Key

**HKEY\_CURRENT\_USER**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

## Remarks

Note that the [**DISABLEMEDIA**](-disablemedia.md) property has a different effect than the DisableMedia policy. Setting the DisableMedia system policy, only disables browsing to media sources. Setting the **DISABLEMEDIA** property prevents the installer from registering any media source, such as a CD-ROM, as a valid source for the product. If browsing is enabled however, a user may still browse to a media source.

## Related topics

<dl> <dt>

[Source Resiliency](source-resiliency.md)
</dt> </dl>

 

 



