---
description: You may apply the small update to a local installation of MNP2000 with the sample patch MNPpatch.msp created in Generating a Patch Package.
ms.assetid: 928182ae-5ddb-446f-a9b8-e8b3aa4ce49c
title: Applying a Patch Package to a Local Installation
ms.topic: article
ms.date: 05/31/2018
---

# Applying a Patch Package to a Local Installation

You may apply the small update to a local installation of MNP2000 with the sample patch MNPpatch.msp created in [Generating a Patch Package](generating-a-patch-package.md). The general procedure is discussed in the section [Applying Small Updates by Patching the Local Installation of the Product](applying-small-updates-by-patching-the-local-installation-of-the-product.md).

Install the original MNP2000 product locally on your computer. Verify that this has the error Concert.txt that the small update is to fix. Next launch the installation by entering the following command line.

**msiexec /p MNP2000.msp REINSTALL=ALL REINSTALLMODE=omus**

Reexamine the Concert.txt belonging to MNP2000 to verify that the installer has applied the small update to fix this file.

To apply the small update to an administrative image, see [Applying a Patch Package to an Administrative Installation](applying-a-patch-package-to-an-administrative-installation.md).

[Continue](applying-a-patch-package-to-an-administrative-installation.md)

 

 



