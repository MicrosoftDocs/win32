---
description: Transforms that have not been secured as described in Secured Transforms are unsecured transforms by default.
ms.assetid: feace6c3-7828-44d0-8d2b-482a02e8e0c0
title: Unsecured Transforms
ms.topic: article
ms.date: 05/31/2018
---

# Unsecured Transforms

Transforms that have not been secured as described in [Secured Transforms](secured-transforms.md) are unsecured transforms by default.

To apply an unsecured transform when installing a package, pass the transform file names in the [**TRANSFORMS**](transforms.md) property or command line string. Do not begin the string with the @ or \| characters or set the [TransformsSecure policy](transformssecure-policy.md) or the [**TRANSFORMSSECURE**](transformssecure.md) property. Note that you cannot combine unsecured transforms and [secured transforms](secured-transforms.md) in the same transforms list.

If the package is installed or advertised in the per-user [installation context](installation-context.md), and has unsecured transforms, the installer saves the transform source in the Application Data folder in the user's profile. This enables a user to maintain their customization of a product while moving between computers.

If the package is installed or advertised in the per-machine [installation context](installation-context.md), and uses unsecured transforms, the installer saves the transform source in the %windir%\\Installer folder.

During a first-time installation of the package, the installer first searches for the transform at the source supplied by the [**TRANSFORMS**](transforms.md) property or command line string. If this source is unavailable, the installer then searches for the transform at the source of the package next to the .msi file.

During a [maintenance installation](maintenance-installation.md), the installer searches for the transform at the cache location. If the cached copy of the transform becomes unavailable, the installer searches for the transform at the source of the package next to the .msi file.

For more information, see [Applying Transforms](applying-transforms.md) and [Source Resiliency](source-resiliency.md).

 

 



