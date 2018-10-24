---
title: Readback Data Through Buffers
description: Reading back data from the GPU, such as capturing a screen shot, involves the use of the Readback heap.
ms.assetid: 2F515B2C-3317-4AA8-81E1-7762ED895F77
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Readback Data Through Buffers

Reading back data from the GPU, such as capturing a screen shot, involves the use of the Readback heap.

-   [Read Back Data via Buffers](#read-back-data-via-buffers)
-   [Related topics](#related-topics)

## Read Back Data via Buffers

Reading back data via buffers is similar to uploading data via buffers as shown before, with a few differences:

-   Applications need to create a heap with the [**D3D12\_HEAP\_TYPE**](/windows/desktop/api/D3D12/ne-d3d12-d3d12_heap_type) set to D3D12\_HEAP\_TYPE\_READBACK instead of D3D12\_HEAP\_TYPE\_UPLOAD.
-   Applications need to use fences to detect when the GPU completes processing a frame and when the writing of data back to the buffer is complete. The [**Map**](/windows/desktop/api/D3D12/nf-d3d12-id3d12resource-map) method no longer synchronizes with the GPU, as it did in D3D11. All D3D12 **Map** calls now behave as if you called D3D11 Map with the NO\_OVERWRITE flag.
-   After the data is ready, applications must call [**Map**](/windows/desktop/api/D3D12/nf-d3d12-id3d12resource-map) to see the results.

## Related topics

<dl> <dt>

[Suballocation Within Buffers](large-buffers.md)
</dt> </dl>

 

 




