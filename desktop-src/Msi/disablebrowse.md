---
description: Setting the value of this per-machine system policy to &\#0034;1&\#0034; prevents nonadministrative users from using a Browse Dialog to locate sources of managed applications stored on media, such as CD-ROM.
ms.assetid: 51806a4c-4ae5-42e9-9d58-8032108164cb
title: DisableBrowse
ms.topic: article
ms.date: 05/31/2018
---

# DisableBrowse

Setting the value of this per-machine [system policy](system-policy.md) to "1" prevents nonadministrative users from using a [Browse Dialog](browse-dialog.md) to locate sources of [*managed applications*](m-gly.md) stored on media, such as CD-ROM. The "Use feature from:" combo box for direct input is locked and the "Browse..." button is disabled. For more details on source browsing, see [source resiliency](source-resiliency.md).

DisableBrowse overrides AllowLockdownBrowse and prevents browsing even if AllowLockdownBrowse is set.

## Registry Key

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

## Remarks

In some cases with DisableBrowse set, a nonadministrative user may still be capable of installing managed applications from sources on correctly labeled media. Setting the DisableBrowse policy only disables the capability to browse to sources. It can be used to prevent a nonadministrative user from browsing to a new source during an install-on-demand installation, reinstallation, or repair. If [AllowLockdownMedia](allowlockdownmedia.md) is set, the nonadministrative user could still install a managed application from correctly labeled media.

DisableBrowse prevents the nonadministrative user from browsing to a new media location or any other source location. For details of how to secure media sources of managed applications see [Source Resiliency](source-resiliency.md).

For information about the interaction of this policy with installation sources, see [Managing Installation Sources](managing-installation-sources.md).

 

 



