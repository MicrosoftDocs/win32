---
description: If this per-machine system policy is set to a value greater than 0, Windows Installer saves older versions of files in a cache when a patch is applied to an application.
ms.assetid: 986cd521-6907-420d-a2e9-5e0da0069834
title: MaxPatchCacheSize
ms.topic: article
ms.date: 05/31/2018
---

# MaxPatchCacheSize

If this per-machine [system policy](system-policy.md) is set to a value greater than 0, Windows Installer saves older versions of files in a cache when a patch is applied to an application. Caching can increase the performance of future installations that otherwise need to obtain the old files from a original application source.

The value of the MaxPatchCacheSize policy is the maximum percentage of disk space that the installer can use for the cache of old files. For example, a value of 20 specifies no more than 20% be used. If the total size of the cache reaches the specified percentage of disk space, no additional files are saved to the cache. The policy does not affect files that have already been saved.

If the value of the MaxPatchCacheSize policy is set to 0, no additional files are saved.

If the MaxPatchCacheSize policy is not set, the default value is 10 and a maximum of 10% of the disk space can be used to save old files.

## Registry Key

**HKEY\_LOCAL\_MACHINE**\\**Software**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**

## Data Type

**REG\_DWORD**

## Related topics

<dl> <dt>

[Not Supported in Windows Installer 2.0 and earlier](not-supported-in-windows-installer-version-2-0.md)
</dt> </dl>

 

 



