---
description: Cloning and Sharing (Direct3D 9)
ms.assetid: 1dabe611-bf3b-49bf-99ab-dbdfd343f885
title: Cloning and Sharing (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Cloning and Sharing (Direct3D 9)

## Cloning Parameters

Cloning has the following restrictions.

-   Clones inherit the original effect's pool. See the Sharing Parameters section.
-   Clones inherit the original effect's techniques, passes, parameters, and annotations (including all annotations added with [**ID3DXEffect**](id3dxeffect.md)).
-   Clones inherit the original effect's dynamically added annotations.
-   Cloning onto a new device will fail if the original effect's pool was not **NULL** and the original effect contained a shared device-dependent parameter (such as a texture or shader).

## Sharing Parameters

A pool is a buffer that shares effect parameters between different effects. To add parameters to a pool, specify a shared usage when the effect is created.

A pool has the following restrictions.

-   A parameter is added to the pool the first time an effect containing that (shared) parameter is added to the pool.
-   A pool gets initial values from the first shared parameter; parameters shared subsequently get their values from the pool.
-   A parameter is deleted from the pool when all effect references to the shared parameter are released.
-   All effects in the pool that contain the same (shared) device-dependent parameter must have the same device.

**NULL** can be used to specify no pool, in which case no parameters are shared. This is almost equivalent to specifying a unique pool just for this effect. The single difference is that when the effect is cloned, the clone will not share its shared parameters with the original.

## Related topics

<dl> <dt>

[Effect Format](dx9-graphics-reference-effects-file-format.md)
</dt> </dl>

 

 



