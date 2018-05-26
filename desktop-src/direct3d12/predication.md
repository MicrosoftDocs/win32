---
title: Predication
description: Predication is a feature that enables the GPU rather than the CPU to determine to not draw, copy or dispatch an object.
ms.assetid: 21526012-A675-40E8-A11C-4CBA5C12B9CF
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Predication can be set based on the value of 64-bits within a buffer (refer to [**D3D12\_PREDICATION\_OP**](/windows/win32/D3D12/ne-d3d12-d3d12_predication_op?branch=master)).

When the GPU executes a [**SetPredication**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-setpredication?branch=master) command it snaps the value in the buffer. Future changes to the data in the buffer do not retroactively affect the predication state.

If the input parameter Buffer is NULL, then predication is disabled.

Predication hints are not present in the D3D12 API, and predication is allowed on direct and compute command lists. The source buffer can be in any heap type (default, upload, readback).

The core runtime will validate the following:

-   *AlignedBufferOffset* is a multiple of 8 bytes
-   The resource is a buffer
-   The operation is a valid member of the enumeration
-   [**SetPredication**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-setpredication?branch=master) cannot be called from within a bundle
-   The command list type supports predication
-   The offset does not exceed the buffer size

The debug layer will issue an error if the source buffer is not in the D3D12\_RESOURCE\_STATE\_VERTEX\_AND\_CONSTANT\_BUFFER state.

The set of operations which can be predicated are:

-   [**DrawInstanced**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-drawinstanced?branch=master)
-   [**DrawIndexedInstanced**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-drawindexedinstanced?branch=master)
-   [**Dispatch**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-dispatch?branch=master)
-   [**CopyTextureRegion**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-copytextureregion?branch=master)
-   [**CopyBufferRegion**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-copybufferregion?branch=master)
-   [**CopyResource**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-copyresource?branch=master)
-   [**CopyTiles**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-copytiles?branch=master)
-   [**ResolveSubresource**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-resolvesubresource?branch=master)
-   [**ClearDepthStencilView**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-cleardepthstencilview?branch=master)
-   [**ClearRenderTargetView**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-clearrendertargetview?branch=master)
-   [**ClearUnorderedAccessViewUint**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-clearunorderedaccessviewuint?branch=master)
-   [**ClearUnorderedAccessViewFloat**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-clearunorderedaccessviewfloat?branch=master)
-   [**ExecuteIndirect**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-executeindirect?branch=master)

[**ExecuteBundle**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-executebundle?branch=master) is not predicated itself. Instead, individual operations from the list above which are contained in side of the bundle are predicated.

The ID3D12GraphicsCommandList methods [**ResolveQueryData**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-resolvequerydata?branch=master), [**BeginQuery**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-beginquery?branch=master) and [**EndQuery**](/windows/win32/d3d12/nf-d3d12-id3d12graphicscommandlist-endquery?branch=master) are not predicated.

## Related topics

<dl> <dt>

[Counters and Queries](counters-and-queries.md)
</dt> <dt>

[Performance Measurement](performance-measurement.md)
</dt> <dt>

[Predication queries walk-through](predication-queries.md)
</dt> </dl>

 

 




