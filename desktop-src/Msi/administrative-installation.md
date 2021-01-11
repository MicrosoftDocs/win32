---
description: The Windows Installer can perform an administrative installation of an application or product to a network for use by a workgroup.
ms.assetid: 5840cfab-a127-4b1f-a7af-a2d8e2786928
title: Administrative Installation
ms.topic: article
ms.date: 05/31/2018
---

# Administrative Installation

The Windows Installer can perform an administrative installation of an application or product to a network for use by a workgroup. An administrative installation installs a source image of the application onto the network that is similar to a source image on a CD-ROM. Users in a workgroup who have access to this administrative image can then install the product from this source. A user must first install the product from the network to run the application. The user can choose to run-from-source when he installs and the installer uses most of the product's file directly from the network.

Administrators can run an administrative installation from the command line by using the /a [command line option](command-line-options.md).

The [ADMIN action](admin-action.md) is the top-level action used to initiate an administrative installation. When this action is executed the installer calls the actions in the [AdminExecuteSequence](adminexecutesequence-table.md) and [AdminUISequence](adminuisequence-table.md) tables to perform the administrative installation.

The [**AdminProperties**](adminproperties.md) property is a semicolon delimited list of properties that are set at the time of an administration installation. The installer uses these properties during a post administration installation of the application from the administrative image.

Users who do not have continuous access to the network may install an application from an administrative image and then at times have to rely on media, such as CD-ROM disks, as their backup source. In these cases the length of the file names in the administrative image and on the media must match. Both must use long file names or both must use short file names. For example, a CD-ROM that only supports short file names could provide both the original media for installing the administrative image and a backup source.

If the [**SHORTFILENAMES**](shortfilenames.md) property is set during an administrative installation, this property may need to be set again by a user subsequently applying a patch to the administrative image. When using Windows Installer to apply the patch, the installer automatically sets the **SHORTFILENAMES** property if the administrative image uses short file names.

If an administrator uses a package having a [**Word Count Summary**](word-count-summary.md) property of 2 or 3 to perform an administrative installation, users of the administrative image cannot automatically reinstall from the original media source. If the administrative image becomes unavailable, users who have installed from the administrative image are prevented from reverting to the original media.

The application of [*transforms*](t-gly.md) during the creation of an administrative image has no valid effect. To make a customized version of a product available to a work group, apply the transform during the installation of the product from the administrative image.

During an administrative installation, the installer creates a source image for all features in the product except those feature with 0 in the Level column of the [Feature table](feature-table.md).

 

 



