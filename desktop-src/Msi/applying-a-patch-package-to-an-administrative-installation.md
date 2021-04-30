---
description: You may apply the small update to an administrative source image of MNP2000.msi by installing the sample patch MNP2000.msp created in Generating a Patch Package.
ms.assetid: 24ae9cd6-2057-4345-90ec-943da7620cb0
title: Applying a Patch Package to an Administrative Installation
ms.topic: article
ms.date: 05/31/2018
---

# Applying a Patch Package to an Administrative Installation

You may apply the small update to an administrative source image of MNP2000.msi by installing the sample patch MNP2000.msp created in [Generating a Patch Package](generating-a-patch-package.md). The update can then be propagated to users by requesting that they reinstall the application from the new administrative source image.

An administrator can use the following command line to update the administrative source image located at //server/MNP2000.msi to a new source image that is the same as would be produced by an administrative installation from a fully updated CD-ROM.

**msiexec /a //server/MNP2000.msi /p MNP2000.msp**

Members of the workgroup using MNP2000 then must reinstall the application from the new administrative source image to receive the update.

To completely reinstall the applications and cache the updated .msi file on the user's computer, users may enter either of the following commands.

**msiexec /fvomus //server/MNP2000.msi**

**msiexec /I //server/MNP2000.msi REINSTALL=ALL REINSTALLMODE=vomus**

To reinstall only the updated Concert feature and cache the updated .msi file on the user's computer, users may enter the following command.

**msiexec /I //server/MNP2000.msi REINSTALL=Concert REINSTALLMODE=vomus**

## Next example

[A Localization Example](a-localization-example.md)

 

 



