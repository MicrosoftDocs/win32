---
description: Embedded transforms are stored inside the .msi file of the package. This guarantees to users that the transform is always available when the installation package is available. Alternatively, transforms may be provided to users as standalone .mst files.
ms.assetid: f7b265df-4b34-44ea-85ab-8dbca4797517
title: Embedded Transforms
ms.topic: article
ms.date: 05/31/2018
---

# Embedded Transforms

Embedded transforms are stored inside the .msi file of the package. This guarantees to users that the transform is always available when the installation package is available. Alternatively, transforms may be provided to users as standalone .mst files.

To add an embedded transform to the transforms list, add a colon (:) prefix to the file name. Because the installer can always obtain the transform from storage in the .msi file, embedded transforms are not cached on the user's computer. Embedded transforms may be used in combination with [secured transforms](secured-transforms.md) or [unsecured transforms](unsecured-transforms.md). For more information, see [Applying Transforms](applying-transforms.md).

 

 



