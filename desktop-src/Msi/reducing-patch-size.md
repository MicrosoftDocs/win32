---
description: Beginning with Windows Installer version 3.0, patch authors can use the product baseline cached by the installer to more easily service applications with smaller delta patches.
ms.assetid: ab5b193d-79ce-4ed4-af53-89a4197197c1
title: Reducing Patch Size
ms.topic: article
ms.date: 05/31/2018
---

# Reducing Patch Size

Beginning with Windows Installer version 3.0, patch authors can use the product baseline cached by the installer to more easily service applications with smaller delta patches. In many cases, a [*delta patch*](d-gly.md) that delivers servicing information to an application can be significantly smaller than a full-file patch or installation package that delivers the same information.

**Windows Installer 2.0:** Not supported. Beginning with Windows Installer 3.0, the installer selectively saves baseline information about files when they are updated.

Windows Installer provides three methods for updating and servicing applications: [small updates](small-updates.md), [minor upgrades](minor-upgrades.md), and [major upgrades](major-upgrades.md). A small update is also referred to as a quick fix engineering (QFE) update, and a minor upgrade is also referred to as a service pack (SP) update. A typical major upgrade removes a previous application and installs a new application. Windows Installer can deliver servicing information to applications as an [installation package](installation-package.md) (.msi file) or as a [patch package](patch-packages.md) (.msp file).

A Windows Installer patch package that delivers servicing information for a small update or minor upgrade is generally much smaller than the equivalent installation package that delivers the same servicing information. It is recommended that patch packages be used for the distribution of small and minor upgrades. It is recommended that an installation package be used for the distribution of a major upgrade.

Windows Installer patches (.msp files) can be generated from either full files or from file differences (also called file deltas.) A Windows Installer patch generated from file deltas can be much smaller than the equivalent full-file patch. All versions of the Windows Installer can use both full-file patches or delta patches.

Beginning with Windows Installer version 3.0, the installer selectively saves baseline information about files when they are updated. Information about the original base application (the RTM version) and the most recent minor upgrade (service pack) are saved in a private location when the application is installed or receives a minor upgrade.

The installer does the following to minimize the size of the baseline cache:

-   No more than two baselines are maintained for each application: a baseline of the file as originally released (RTM) and a baseline of the file at the most recent minor upgrade (service pack.)
-   A file is not added to the cache until it is patched. The baseline cache is copy-on-write.
-   If the application has never been updated, there are no files in the baseline cache.
-   When the application's last servicing was a minor upgrade (service pack) the application is at a baseline level and at most two copies of a file can be present on the computer. One copy of the file is in the target directory of the installation. The other copy can be in the RTM baseline cache.
-   When the application's last servicing was a small update (QFE) the application is not at a baseline level and at most three copies of a file can be present on the computer. The first copy of the file is in the target directory of the installation. The second copy of the file is in the RTM baseline cache. The last copy of the file is in the most recent baseline cache.
-   The application's baseline cache is removed when the product is uninstalled.

Beginning with Windows Installer version 3.0, the installer can use the baseline cache when patches are applied to the application. The baseline information can be used to apply a delta patch or to revert a file to a previous version during a patch uninstall. This can enable patch authors to benefit from smaller delta patches. If the installer finds that the delta patch cannot be applied to the target file, the installer can attempt to use a file saved in the baseline cache as a starting point. The installer only resorts to requesting the original installation source after trying all the possibilities in the cache.

Adherence to the following guidelines can help patch authors use Windows Installer version 3.0 patches and the baseline cache to create smaller delta patches:

-   Author patches that include the [MsiPatchSequence table](msipatchsequence-table.md). This table is required to use the baseline cache and is available beginning with Windows Installer version 3.0.
-   Do not set policy that prevents baseline caching. The value of the [MaxPatchCacheSize](maxpatchcachesize.md) policy specifies the maximum percentage of disk space that can be used. If the MaxPatchCacheSize policy is set to 0, no additional files are saved in the baseline cache. If the policy is not set, the default is that a maximum of 10% of the disk space can be used. If the total size of the cache reaches the maximum percentage of disk space, no additional files are saved. The policy does not affect files that have already been saved. Even when caching is disabled, the installer can use existing product baseline caches.
-   If the first patch applied includes the [MsiPatchSequence table](msipatchsequence-table.md), caching is enabled for the application.
-   If any patch in the servicing transaction does not include the [MsiPatchSequence table](msipatchsequence-table.md), caching is enabled for the application only if a minor upgrade patch (service pack) that includes the MsiPatchSequence table is successfully applied to the product.
-   Generate the patch package using patch creation tools such as [Msimsp.exe](msimsp-exe.md) and [PATCHWIZ.DLL](patchwiz-dll.md).
-   Always target patches for the RTM version of the application or a minor upgrade (service pack) version of the application. The targets specified in the [TargetImages table](targetimages-table-patchwiz-dll-.md) of the Patch Creation Properties (PCP) file should be product check points defined by the first three fields of the [**ProductVersion**](productversion.md) property.
-   Never target patches at small update images. The targets for building the patch should not include previous small update upgrade images.

 

 



