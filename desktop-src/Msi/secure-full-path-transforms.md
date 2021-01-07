---
description: Secure-full-path transforms must have a source located at the full path specified in the TRANSFORMS property.
ms.assetid: 9c1cd6c5-d246-49d8-a632-991274bb4511
title: Secure-Full-Path Transforms
ms.topic: article
ms.date: 05/31/2018
---

# Secure-Full-Path Transforms

Secure-full-path transforms must have a source located at the full path specified in the [**TRANSFORMS**](transforms.md) property. When the package is installed or advertised, the installer saves the transforms in a cache where, on a secure file system, the user does not have write access. If the local copy of the transform becomes unavailable, it may only restore the cache using the specified path. The removal of a product by any user removes all secure transforms for that product from the user's computer.

To apply secure-full-paths transforms at the installation of a package, set the [TransformsSecure policy](transformssecure-policy.md) or the [**TRANSFORMSSECURE**](transformssecure.md) property or make \| the first character passed in the transform list. The full paths to the source of each transform must be passed in the transforms string. If any relative paths are in the list, the installation fails. The transform source does not have to be located with the source of the package.

 

 



