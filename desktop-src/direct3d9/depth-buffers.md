---
description: A depth buffer, often called a z-buffer or a w-buffer, is a property of the device that stores depth information to be used by Direct3D.
ms.assetid: 'vs|directx_sdk|~\depth_buffers.htm'
title: Depth Buffers (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Depth Buffers (Direct3D 9)

A depth buffer, often called a z-buffer or a w-buffer, is a property of the device that stores depth information to be used by Direct3D. When Direct3D renders a scene to a target surface, it can use the memory in an associated depth-buffer surface as a workspace to determine how the pixels of rasterized polygons occlude one another. Direct3D uses an off-screen Direct3D surface as the target to which final color values are written. The depth-buffer surface that is associated with the render-target surface is used to store depth information that tells Direct3D how deep each visible pixel is in the scene.

When a scene is rasterized with depth buffering enabled, each point on the rendering surface is tested. The values in the depth buffer can be a point's z-coordinate or its homogeneous w-coordinate - from the point's (x,y,z,w) location in projection space. A depth buffer that uses z values is often called a z-buffer, and one that uses w values is called a w-buffer. Each type of depth buffer has advantages and disadvantages, which are discussed later.

At the beginning of the test, the depth value in the depth buffer is set to the largest possible value for the scene. The color value on the rendering surface is set to either the background color value or the color value of the background texture at that point. Each polygon in the scene is tested to see if it intersects with the current coordinate (x,y) on the rendering surface. If it does, the depth value - which will be the z coordinate in a z-buffer, and the w coordinate in a w-buffer - at the current point is tested to see if it is smaller than the depth value stored in the depth buffer. If the depth of the polygon value is smaller, it is stored in the depth buffer and the color value from the polygon is written to the current point on the rendering surface. If the depth value of the polygon at that point is larger, the next polygon in the list is tested. This process is shown in the following diagram.

![diagram of testing depth values](images/zbuffer.png)

> [!Note]  
> Although most applications don't use this feature, you can change the comparison that Direct3D uses to determine which values are placed in the depth buffer and subsequently the render-target surface. To do so, change the value for the D3DRS\_ZFUNC render state. On some hardware, changing the compare function may disable hierarchical z testing.

 

Nearly all accelerators on the market support z-buffering, making z-buffers the most common type of depth buffer today. However ubiquitous, z-buffers have their drawbacks. Due to the mathematics involved, the generated z values in a z-buffer tend not to be distributed evenly across the z-buffer range (typically 0.0 to 1.0, inclusive). Specifically, the ratio between the far and near clipping planes strongly affects how unevenly z values are distributed. Using a far-plane distance to near-plane distance ratio of 100, 90 percent of the depth buffer range is spent on the first 10 percent of the scene depth range. Typical applications for entertainment or visual simulations with exterior scenes often require far-plane/near-plane ratios of anywhere between 1,000 to 10,000. At a ratio of 1,000, 98 percent of the range is spent on the first 2 percent of the depth range, and the distribution becomes worse with higher ratios. This can cause hidden surface artifacts in distant objects, especially when using 16-bit depth buffers, the most commonly supported bit-depth.

A w-based depth buffer, on the other hand, is often more evenly distributed between the near and far clip planes than a z-buffer. The key benefit is that the ratio of distances for the far and near clipping planes is no longer an issue. This allows applications to support large maximum ranges, while still getting relatively accurate depth buffering close to the eye point. A w-based depth buffer isn't perfect, and can sometimes exhibit hidden surface artifacts for near objects. Another drawback to the w-buffered approach is related to hardware support: w-buffering isn't supported as widely in hardware as z-buffering.

Using a z-buffer requires overhead during rendering. Various techniques can be used to optimize rendering when using z-buffers. For details, see [Z-Buffer Performance](performance-optimizations.md).

> [!Note]  
> The actual interpretation of a depth value is specific to the renderer.

 

This section presents information about using depth buffers for hidden line and hidden surface removal.

-   [Querying for Depth Buffer Support (Direct3D 9)](querying-for-depth-buffer-support.md)
-   [Creating a Depth Buffer (Direct3D 9)](creating-a-depth-buffer.md)
-   [Enabling Depth Buffering (Direct3D 9)](enabling-depth-buffering.md)
-   [Retrieving a Depth Buffer (Direct3D 9)](retrieving-a-depth-buffer.md)
-   [Clearing Depth Buffers (Direct3D 9)](clearing-depth-buffers.md)
-   [Changing Depth Buffer Write Access (Direct3D 9)](changing-depth-buffer-write-access.md)
-   [Changing Depth Buffer Comparison Functions (Direct3D 9)](changing-depth-buffer-comparison-functions.md)

## Related topics

<dl> <dt>

[Direct3D Rendering](direct3d-rendering.md)
</dt> </dl>

 

 



