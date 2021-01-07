---
description: An administrative installation creates a source image of an application or product on a network.
ms.assetid: 40755461-317f-4764-aaa2-6b8471d52f55
title: Applying Small Updates by Patching an Administrative Image
ms.topic: article
ms.date: 05/31/2018
---

# Applying Small Updates by Patching an Administrative Image

An [administrative installation](administrative-installation.md) creates a source image of an application or product on a network. Users in a workgroup who have access to this administrative image can install the product from this source. Updating the application for this workgroup is done in two steps:

-   First, the small update patch can be applied to the administrative image.
-   Second, the changes in the small update need to be propagated to the users.

**To apply a small update patch to an administrative image**

1.  Obtain the small update in the form of a [patch package](patch-packages.md). For example, the small update named Patch.msp.
2.  Obtain the path to the administrative image.
3.  From the command line use:

    **msiexec /a** *\[path to administrative image .msi file\]* **/p** *patch.msp*

4.  This updates the application files and the .msi file of the administrative image. For a list of the options that can be used with Msiexec.exe, see [Command Line Options](command-line-options.md). Windows Installer automatically determines whether the administrative image is using short file names and sets the [**SHORTFILENAMES**](shortfilenames.md) property.
5.  The resulting administrative image is the same as that produced by an administrative installation using a full product CD-ROM that includes the update. When new users install the application from this source they receive the updated application.

**To propagate the small update to the workgroup**

-   Members of the workgroup obtain the changes by reinstalling the application from the administrative image using the procedure described in [Applying Small Updates by Reinstalling the Product](applying-small-updates-by-reinstalling-the-product.md).

 

 



