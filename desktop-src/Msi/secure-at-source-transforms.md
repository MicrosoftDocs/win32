---
description: Secure-at-source transforms must have a source located at the root of the source for the package.
ms.assetid: b5355053-9922-444f-a117-f6af461ef9e9
title: Secure-At-Source Transforms
ms.topic: article
ms.date: 05/31/2018
---

# Secure-At-Source Transforms

Secure-at-source transforms must have a source located at the root of the source for the package. When the package is installed or advertised, the installer saves the transforms in a cache where, on a secure file system, the user does not have write access. If the local copy of the transform becomes unavailable, the installer searches for a source to restore the cache. The method is the same as searching the source list for an .msi file. For more information, see [Source Resiliency](source-resiliency.md). The removal of a product by any user removes all secure transforms for that product from the user's computer.

To apply secure-at-source transforms at the installation of a package, set the [TransformsSecure policy](transformssecure-policy.md) or the [**TRANSFORMSSECURE**](transformssecure.md) property, or make @ the first character passed in the transform list. Each transform must be indicated by a file name and must be located at the root of the source for the package. If any of the transforms are not located at the root of the package source, the installation fails. For more information, see [Applying Transforms](applying-transforms.md).

 

 



