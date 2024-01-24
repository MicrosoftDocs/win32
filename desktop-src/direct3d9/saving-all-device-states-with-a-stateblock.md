---
description: A state block can be used to capture all device states (see State Blocks Save and Restore State (Direct3D 9)).
ms.assetid: e14077e4-1453-4aa3-b2de-4d3a829a819a
title: Saving All Device States with a StateBlock (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Saving All Device States with a StateBlock (Direct3D 9)

A state block can be used to capture all device states (see [State Blocks Save and Restore State (Direct3D 9)](state-blocks-save-and-restore-state.md)). The following state elements are included in the device state:

-   Vertex state (see [Saving Vertex States With a StateBlock (Direct3D 9)](saving-vertex-states-with-a-stateblock.md)).
-   Pixel state (see [Saving Pixel State With a StateBlock (Direct3D 9)](saving-pixel-states-with-a-stateblock.md)).
-   Each texture assigned to a sampler.
-   Each vertex texture.
-   Each displacement map texture.
-   The current texture palette.
-   For each vertex stream: a pointer to the vertex buffer, each argument from [**IDirect3DDevice9::SetStreamSource**](/windows/desktop/api), and the divider (if any) from [**IDirect3DDevice9::SetStreamSourceFreq**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setstreamsourcefreq).
-   A pointer to the index buffer.
-   The viewport.
-   The scissors rectangle.
-   The world, view, and projection matrices.
-   The texture transforms.
-   The clipping planes (if any).
-   The current material.

To capture all device states with a state block, specify D3DSBT\_ALL when calling [**IDirect3DDevice9::CreateStateBlock**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createstateblock).

## Related topics

<dl> <dt>

[State Blocks Save and Restore State](state-blocks-save-and-restore-state.md)
</dt> </dl>

 

 
