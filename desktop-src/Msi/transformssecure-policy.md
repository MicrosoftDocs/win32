---
description: Setting the TransformsSecure policy to 1 informs the installer that transforms are to be cached locally on the user's computer in a location where the user does not have write access.
ms.assetid: 4fe992ed-1e8c-4ee2-a325-138bdc039e44
title: TransformsSecure Policy
ms.topic: article
ms.date: 05/31/2018
---

# TransformsSecure Policy

Setting the TransformsSecure policy to 1 informs the installer that transforms are to be cached locally on the user's computer in a location where the user does not have write access. Setting this policy is the same as setting the [TRANSFORMSSECURE property](transformssecure.md) except the scope is different. Setting TransformsSecure policy applies to all packages installed to a given computer. Setting the TRANSFORMSSECURE property applies to the package regardless of the computer.

The purpose of this policy is to provide for secure transform storage with traveling users of Windows 2000. Beginning with Windows Server 2003, the default value of this policy is 1.

When this policy is set, a [maintenance installation](maintenance-installation.md) can only use the transform from the secured cache. In the event that the installer finds that the transform is missing on the local computer, the installer attempts to restore the transform. In order for the installer to restore the transform, the secure transform must reside at an authorized source in the installation package's source list. For more information, see [Source Resiliency](source-resiliency.md). The maintenance installation fails if the transform is unavailable or cannot be loaded.

On Windows Server 2003, if this policy is not set, the default behavior is to store the transforms in a secure location. On all versions prior to Windows Server 2003, if the policy is not set, the default behavior is to store the transforms in the users profile.

See also [Secured Transforms](secured-transforms.md) for more information.

Windows Installer interprets the [TransformsAtSource policy](transformsatsource-policy.md) to be the same as the TransformsSecure policy.

## Registry Key

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

## Related topics

<dl> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 



