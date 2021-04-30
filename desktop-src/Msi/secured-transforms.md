---
description: Secured transforms are sometimes necessary for security reasons.
ms.assetid: c6019b28-b0a7-4104-9d78-b4b4228635b8
title: Secured Transforms
ms.topic: article
ms.date: 05/31/2018
---

# Secured Transforms

Secured transforms are sometimes necessary for security reasons. Secured transforms are stored locally on the user's computer in a location where, on a secure file system, the user does not have write access. Such transforms are cached in this location during the installation or advertisement of the package. Only administrators and local system have write access to this location. A non-admin user would not be able to modify the transform file. During subsequent [installation-on-demand](installation-on-demand.md) or [maintenance installations](maintenance-installation.md) of the package, the installer uses the cached transforms.

To specify secured transform storage, set the [TransformsSecure policy](transformssecure-policy.md), set the [**TRANSFORMSSECURE**](transformssecure.md) property, or pass the @ or \| symbol in the transforms list. Note that you cannot include secured and unsecured transforms in the same transforms list. See [Applying Transforms](applying-transforms.md).

The removal of the product by any user removes all secured transforms for that product from the user's computer.

If the installer finds that a secured transform is not locally available, it then attempts to restore the transform cache from a source. Secure transforms can be secure-at-source or secure-full-path:

-   [Secure-at-source transforms](secure-at-source-transforms.md) that are missing from the local transform cache are restored from the root of the source of the .msi file.
-   [Secure-full-path transforms](secure-full-path-transforms.md) that are missing from the local transform cache are restored from the original full path specified by the transforms list.

 

 



