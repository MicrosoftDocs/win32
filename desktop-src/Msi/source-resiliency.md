---
description: Applications that rely on network resources for installation-on-demand are susceptible to source failures if the source location should change for any reason or become damaged.
ms.assetid: 3d6a0524-d5df-4d4c-b861-d4a7da95ce40
title: Source Resiliency
ms.topic: article
ms.date: 05/31/2018
---

# Source Resiliency

Applications that rely on network resources for [installation-on-demand](installation-on-demand.md) are susceptible to source failures if the source location should change for any reason or become damaged. The Windows Installer provides source resiliency for features that are installed on-demand by using a source list. The source list contains the locations searched by the installer for installation packages. The entries in this list can be network locations, Uniform Resource Locators (URLs), or compact discs. If one of these sources fails, the installer can quickly and seamlessly try the next.

The application developer does not need to incorporate any special information into the installer package to ensure source resiliency. Once the application is installed, the installer has the behavior of adding the last successfully used source as an entry in the source list. By default, this source is the location from which the installer package is initially installed, and is the same as the [**SourceDir**](sourcedir.md) property.

A system administrator can change the source list by applying a [transform](merges-and-transforms.md) or by changing the [**SOURCELIST**](sourcelist.md) property from the command line or in the [Property table](property-table.md).

The installer begins searching for a source by checking the most recently used source location in the source list. If this search fails, the installer searches the list of network sources, then media sources, and finally URL sources. System administrators can change this search order using the [SearchOrder](searchorder.md) system policy. If these searches fail, the installer may present a [Browse Dialog](browse-dialog.md) so that the user can search for the source manually. The browse dialog box cannot be displayed if the user interface level is set to None. For details, see [User Interface Levels](user-interface-levels.md).

Commonly, the installer should only display a browse dialog box if the current user is an administrator or if the installation does not require elevated privileges. An administrator can control the display of the browse dialog box to users with the [DisableBrowse](disablebrowse.md) and [AllowLockDownBrowse](allowlockdownbrowse.md) policies. An administrator also controls whether users can install applications from sources located on media by using the [DisableMedia](disablemedia.md) and [AllowLockDownMedia](allowlockdownmedia.md) policies. The use of these policies depends on the Windows Installer version. For details, see the following:

-   [Source Resiliency Policy](source-resiliency-policy-windows-installer-version-2-0.md)

 

 



