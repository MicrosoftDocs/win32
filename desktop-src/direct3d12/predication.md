---
title: Predication
description: Predication is a feature that enables the GPU rather than the CPU to determine to not draw, copy or dispatch an object.
ms.assetid: '21526012-A675-40E8-A11C-4CBA5C12B9CF'
---

# Predication

Predication is a feature that enables the GPU rather than the CPU to determine to not draw, copy or dispatch an object.

-   [Overview](#overview)
-   [SetPredication](#setpredication)
-   [Related topics](#related-topics)

## Overview

The typical use of predication is with occlusion; if a bounding box is drawn and is occluded, there is obviously no point in drawing the object itself. In this situation the drawing of the object can be "predicated" , enabling its removal from actual rendering by the GPU.

Unlike Direct3D 11, predication is decoupled from queries, and is expanded in Direct3D 12 to enable an application to predicate objects based on any reasoning the app developer may decide on (not just occlusion).

## SetPredication

Predication can be set based on the value of 64-bits within a buffer (refer to [**D3D12\_PREDICATION\_OP**](d3d12-predication-op.md)).

When the GPU executes a [**SetPredication**](id3d12graphicscommandlist-setpredication.md) command it snaps the value in the buffer. Future changes to the data in the buffer do not retroactively affect the predication state.

If the input parameter Buffer is NULL, then predication is disabled.

Predication hints are not present in the D3D12 API, and predication is allowed on direct and compute command lists. The source buffer can be in any heap type (default, upload, readback).

The core runtime will validate the following:

-   *AlignedBufferOffset* is a multiple of 8 bytes
-   The resource is a buffer
-   The operation is a valid member of the enumeration
-   [**SetPredication**](id3d12graphicscommandlist-setpredication.md) cannot be called from within a bundle
-   The command list type supports predication
-   The offset does not exceed the buffer size

The debug layer will issue an error if the source buffer is not in the D3D12\_RESOURCE\_STATE\_VERTEX\_AND\_CONSTANT\_BUFFER state.

The set of operations which can be predicated are:

-   [**DrawInstanced**](id3d12graphicscommandlist-drawinstanced.md)
-   [**DrawIndexedInstanced**](id3d12graphicscommandlist-drawindexedinstanced.md)
-   [**Dispatch**](id3d12graphicscommandlist-dispatch.md)
-   [**CopyTextureRegion**](id3d12graphicscommandlist-copytextureregion.md)
-   [**CopyBufferRegion**](id3d12graphicscommandlist-copybufferregion.md)
-   [**CopyResource**](id3d12graphicscommandlist-copyresource.md)
-   [**CopyTiles**](id3d12graphicscommandlist-copytiles.md)
-   [**ResolveSubresource**](id3d12graphicscommandlist-resolvesubresource.md)
-   [**ClearDepthStencilView**](id3d12graphicscommandlist-cleardepthstencilview.md)
-   [**ClearRenderTargetView**](id3d12graphicscommandlist-clearrendertargetview.md)
-   [**ClearUnorderedAccessViewUint**](id3d12graphicscommandlist-clearunorderedaccessviewuint.md)
-   [**ClearUnorderedAccessViewFloat**](id3d12graphicscommandlist-clearunorderedaccessviewfloat.md)
-   [**ExecuteIndirect**](id3d12graphicscommandlist-executeindirect.md)

[**ExecuteBundle**](id3d12graphicscommandlist-executebundle.md) is not predicated itself. Instead, individual operations from the list above which are contained in side of the bundle are predicated.

The ID3D12GraphicsCommandList methods [**ResolveQueryData**](id3d12graphicscommandlist-resolvequerydata.md), [**BeginQuery**](id3d12graphicscommandlist-beginquery.md) and [**EndQuery**](id3d12graphicscommandlist-endquery.md) are not predicated.

## Related topics

<dl> <dt>

[Counters and Queries](counters-and-queries.md)
</dt> <dt>

[Performance Measurement](performance-measurement.md)
</dt> <dt>

[Predication queries walk-through](predication-queries.md)
</dt> </dl>

 

 




