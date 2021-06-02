---
description: Locking a resource means granting CPU access to its storage.
ms.assetid: b17d8262-e514-4b9c-9237-653a4258a14e
title: Locking Resources (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Locking Resources (Direct3D 9)

Locking a resource means granting CPU access to its storage. The following locking options are defined for resources:

-   D3DLOCK\_DISCARD
-   D3DLOCK\_READONLY
-   D3DLOCK\_NOOVERWRITE
-   D3DLOCK\_NOSYSLOCK
-   D3DLOCK\_NO\_DIRTY\_UPDATE

For details on locking flags and how they relate to specific resources, see the reference pages on the individual resource locking methods. Application developers should note that the D3DLOCK\_DISCARD, D3DLOCK\_READONLY, and D3DLOCK\_NOOVERWRITE flags are only hints. The run time does not check that applications are following the functionality specified by these flags. An application that specifies D3DLOCK\_READONLY but then writes to the resource should expect undefined results. In general, working against locking flags, including the locking usage flags, is not guaranteed to work in later releases and may incur a significant performance penalty.

A lock operation is followed by an unlock operation. For example, after locking a texture, the application subsequently relinquishes direct access to locked textures by unlocking them. In addition to granting processor access, any other operations involving that resource are serialized for the duration of a lock. Only a single lock for a resource is allowed, even for non-overlapping regions, and no accelerator operations on a surface can be ongoing while a lock operation is outstanding on that surface.

Each resource interface has methods for locking the contained buffers. Each texture resource can also lock a sub-portion of that resource. 2D resources (surfaces) allow the locking of sub-rectangles, and volume resources allow the locking of sub-volumes or boxes. Each lock method returns a structure that contains a pointer to the storage backing the resource and values representing the distances between rows or planes of data, depending on the resource type. For details, see the method lists for the resource interfaces. The returned pointer always points to the top-left byte in the locked sub-regions.

When working with index and vertex buffers, you can make multiple lock calls; however, you must ensure that the number of lock calls matches the number of unlock calls.

The DXTn store pixels in encoded 4x4 blocks, and can only be locked on 4x4 boundaries.

## Related topics

<dl> <dt>

[Direct3D Resources](direct3d-resources.md)
</dt> </dl>

 

 



