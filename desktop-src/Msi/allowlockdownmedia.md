---
description: Setting the value of this per-machine system policy to &\#0034;1&\#0034;, enables nonadministrative users to install managed applications from sources stored on media, such as a CD-ROM.
ms.assetid: 9eac7520-0ba3-4529-a80b-010447a5b5e7
title: AllowLockdownMedia
ms.topic: article
ms.date: 05/31/2018
---

# AllowLockdownMedia

Setting the value of this per-machine [system policy](system-policy.md) to "1", enables nonadministrative users to install [*managed applications*](m-gly.md) from sources stored on media, such as a CD-ROM. See [Source Resiliency](source-resiliency.md). For example, if this policy is set, a nonadministrative user may use a media source to install assigned or published applications or applications being installed for all users. Setting this policy also enables nonadministrative users to run programs at LocalSystem privileges during an elevated installation.

The default value of this policy is 1 only on computers running Windows Vista and that are not joined to a domain. The default on other computers is that nonadministrative users cannot install managed applications from a source located on media.

Because this policy enables users that are not an administrator to install with privileges they do not have by default, before setting this policy you should consider whether it provides an appropriate level of security for your user. The default setting is recommended to ensure a secure environment.

For more information about securing installations and using digital certificates see [Guidelines for Authoring Secure Installations](guidelines-for-authoring-secure-installations.md) and [Digital Signatures and Windows Installer](digital-signatures-and-windows-installer.md) and [Downloading an Installation from the Internet](downloading-an-installation-from-the-internet.md).

## Registry Key

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

## Remarks

Setting this policy also enables nonadministrative users to run arbitrary programs at LocalSystem privileges if they have a Windows Installer package that installs or launches those programs.

## Related topics

<dl> <dt>

[Source Resiliency](source-resiliency.md)
</dt> <dt>

[AllowLockdownBrowse](allowlockdownbrowse.md)
</dt> </dl>

 

 



