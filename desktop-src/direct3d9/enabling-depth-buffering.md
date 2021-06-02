---
description: After you create a depth buffer, as described in Creating a Depth Buffer (Direct3D 9), you enable depth buffering by calling the IDirect3DDevice9::SetRenderState method.
ms.assetid: a3c972dd-3630-4d21-a22b-64a68e9acd19
title: Enabling Depth Buffering (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Enabling Depth Buffering (Direct3D 9)

After you create a depth buffer, as described in [Creating a Depth Buffer (Direct3D 9)](creating-a-depth-buffer.md), you enable depth buffering by calling the [**IDirect3DDevice9::SetRenderState**](/windows/desktop/api) method. Set the D3DRS\_ZENABLE render state to enable depth-buffering. Use the D3DZB\_TRUE member of the [**D3DZBUFFERTYPE**](./d3dzbuffertype.md) enumerated type (or **TRUE**) to enable z-buffering, D3DZB\_USEW to enable w-buffering, or D3DZB\_FALSE (or **FALSE**) to disable depth buffering.

> [!Note]  
> To use w-buffering, your application must set a compliant projection matrix even if it doesn't use the Direct3D transformation pipeline. For information about providing an appropriate projection matrix, see [A W-Friendly Projection Matrix](projection-transform.md)

 

## Related topics

<dl> <dt>

[Depth Buffers](depth-buffers.md)
</dt> </dl>

 

 
