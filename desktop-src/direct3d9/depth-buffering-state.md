---
description: Depth buffering is a method of removing hidden lines and surfaces. By default, Direct3D does not use depth buffering.
ms.assetid: 03795e4e-1daa-48e3-8724-8dd4b5187edc
title: Depth Buffering State (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Depth Buffering State (Direct3D 9)

Depth buffering is a method of removing hidden lines and surfaces. By default, Direct3D does not use depth buffering.

For a conceptual overview of depth buffers, see [Depth Buffers (Direct3D 9)](depth-buffers.md).

C++ applications update the depth-buffering state with the D3DRS\_ZENABLE render state, using a member of the [**D3DZBUFFERTYPE**](./d3dzbuffertype.md) enumeration to specify the new state value.

If your application needs to prevent Direct3D from writing to the depth buffer, it can use the D3DRS\_ZWRITEENABLE enumerated value, specifying D3DZB\_FALSE as the second parameter for the call to [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate).

The following code example shows how the depth-buffer state is set to enable z-buffering.


```
// This code example assumes that d3dDevice is a 
// valid pointer to an IDirect3DDevice9 interface.
// Enable z-buffering.
d3dDevice->SetRenderState(D3DRS_ZENABLE, D3DZB_TRUE);
```



Your application can also use the D3DRS\_ZFUNC render state to control the comparison function that Direct3D uses when performing depth buffering.

Z-biasing is a method of displaying one surface in front of another, even if their depth values are the same. You can use this technique for a variety of effects. A common example is rendering shadows on walls. Both the shadow and the wall have the same depth value. However, you want your application to show the shadow on the wall. Giving a z-bias to the shadow makes Direct3D display them properly (see D3DRS\_DEPTHBIAS).

## Related topics

<dl> <dt>

[Render States](render-states.md)
</dt> </dl>

 

 
