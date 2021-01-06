---
description: The IDirect3DDevice9 interface supports vertex processing in both software and hardware.
ms.assetid: c1ac0382-1701-40e4-967a-d400ada96533
title: Processing Vertex Data (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Processing Vertex Data (Direct3D 9)

The [**IDirect3DDevice9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9) interface supports vertex processing in both software and hardware. In general, the device capabilities for software and hardware vertex processing are not identical. Hardware capabilities are variable, depending on the display adapter and driver, while software capabilities are fixed.

The following flags control vertex processing behavior for the hardware abstraction layer (HAL) and reference devices.

-   D3DCREATE\_SOFTWARE\_VERTEXPROCESSING
-   D3DCREATE\_HARDWARE\_VERTEXPROCESSING
-   D3DCREATE\_MIXED\_VERTEXPROCESSING

Specify one of the vertex processing behavior flags when calling [**IDirect3D9::CreateDevice**](/windows/win32/api/d3d9/nf-d3d9-idirect3d9-createdevice). The mixed-mode flag enables the device to perform both software and hardware vertex processing. Only one vertex processing flag may be set for a device at any one time. Note that the D3DCREATE\_HARDWARE\_VERTEXPROCESSING flag is required to be set when creating a pure device (D3DCREATE\_PUREDEVICE).

To avoid dual vertex processing capabilities on a single device, only the hardware vertex processing capabilities can be queried at run time. Software vertex processing capabilities are fixed and cannot be queried at run time.

The VertexProcessingCaps member of the [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) structure determines the hardware vertex processing capabilities of the device.

For software vertex processing the following capabilities are supported.

-   the D3DVTXPCAPS\_DIRECTIONALLIGHTS member of [D3DVTXPCAPS](d3dvtxpcaps.md)
-   the D3DVTXPCAPS\_LOCALVIEWER member of [D3DVTXPCAPS](d3dvtxpcaps.md)
-   the D3DVTXPCAPS\_MATERIALSOURCE7 member of [D3DVTXPCAPS](d3dvtxpcaps.md)
-   the D3DVTXPCAPS\_POSITIONALLIGHTS member of [D3DVTXPCAPS](d3dvtxpcaps.md)
-   the D3DVTXPCAPS\_TEXGEN member of [D3DVTXPCAPS](d3dvtxpcaps.md)
-   the D3DVTXPCAPS\_TWEENING member of [D3DVTXPCAPS](d3dvtxpcaps.md)

In addition, the following table lists the values that are set for members of the [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) structure for a device in software vertex processing mode.



| Member                 | Software vertex processing capabilities |
|------------------------|-----------------------------------------|
| MaxActiveLights        | Unlimited                               |
| MaxUserClipPlanes      | 6                                       |
| MaxVertexBlendMatrices | 4                                       |
| MaxStreams             | 16                                      |
| MaxVertexIndex         | 0xFFFFFFFF                              |



 

In general, any application that is vertex processing bound should use a HAL device. Software vertex processing provides a guaranteed set of vertex processing capabilities, including an unbounded number of lights and full support for programmable vertex shaders. You can toggle between software and hardware vertex processing at any time when using the HAL device (which is the only device type that supports both hardware and software vertex processing). The only requirement is that vertex buffers used for software vertex processing must be allocated in system memory.

## Related topics

<dl> <dt>

[Direct3D Devices](direct3d-devices.md)
</dt> </dl>

 

 
