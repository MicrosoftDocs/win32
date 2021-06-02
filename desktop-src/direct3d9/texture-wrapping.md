---
description: In short, texture wrapping changes the basic way that Direct3D rasterizes textured polygons using the texture coordinates specified for each vertex.
ms.assetid: 00683d3f-3e3c-4ee4-9aec-a0d7fd9c8941
title: Texture Wrapping (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Texture Wrapping (Direct3D 9)

In short, texture wrapping changes the basic way that Direct3D rasterizes textured polygons using the texture coordinates specified for each vertex. While rasterizing a polygon, the system interpolates between the texture coordinates at each of the polygon's vertices to determine the texels that should be used for every pixel of the polygon. Normally, the system treats the texture as a 2D plane, interpolating new texels by taking the shortest route from point A within a texture to point B. If point A represents the u, v position (0.8, 0.1), and point B is at (0.1,0.1), the line of interpolation looks like the following diagram.

![diagram of a line of interpolation between two points](images/interp1.png)

Note that the shortest distance between A and B in this illustration runs roughly through the middle of the texture. Enabling u-texture or v-texture coordinate wrapping changes how Direct3D perceives the shortest route between texture coordinates in the u-direction and v-direction. By definition, texture wrapping causes the rasterizer to take the shortest route between texture coordinate sets, assuming that 0.0 and 1.0 are coincident. The last bit is the tricky part: You can imagine that enabling texture wrapping in one direction causes the system to treat a texture as though it were wrapped around a cylinder. For example, consider the following diagram.

![diagram of a texture and two points wrapped around a cylinder](images/interp2.png)

The preceding illustration shows how wrapping in the u - direction affects how the system interpolates texture coordinates. Using the same points as in the example for normal, or nonwrapped, textures, you can see that the shortest route between points A and B is no longer across the middle of the texture; it's now across the border where 0.0 and 1.0 exist together. Wrapping in the v-direction is similar, except that it wraps the texture around a cylinder that is lying on its side. Wrapping in both the u-direction and v-direction is more complex. In this situation, you can envision the texture as a torus, or doughnut.

The most common practical application for texture wrapping is to perform environment mapping. Usually, an object textured with an environment map appears very reflective, showing a mirrored image of the object's surroundings in the scene. For the sake of this discussion, picture a room with four walls, each one painted with a letter R, G, B, Y and the corresponding colors: red, green, blue, and yellow. The environment map for such a simple room might look like the following illustration.

![illustration of vertical stripes of red, green, blue, and yellow](images/envmap.png)

Imagine that the room's ceiling is held up by a perfectly reflective, four-sided, pillar. Mapping the environment map texture to the pillar is simple; making the pillar look as though it is reflecting the letters and colors is not as easy. The following diagram shows a wire frame of the pillar with the applicable texture coordinates listed near the top vertices. The seam where wrapping will cross the edges of the texture is shown with a dotted line.

![diagram of a rectangle with a bisecting dotted line](images/seam.png)

With wrapping enabled in the u-direction, the textured pillar shows the colors and symbols from the environment map appropriately and, at the seam in the front of the texture, the rasterizer properly chooses the shortest route between the texture coordinates, assuming that u-coordinates 0.0 and 1.0 share the same location. The textured pillar looks like the following illustration.

![illustration of a pillar that consists of red, green, blue, and yellow quadrants](images/tex-seam.png)

If texture wrapping isn't enabled, the rasterizer does not interpolate in the direction needed to generate a believable, reflected image. Rather, the area at the front of the pillar contains a horizontally compressed version of the texels between u-coordinates 0.175 and 0.875, as they pass through the center of the texture. The wrap effect is ruined.

## Using Texture Wrapping

To enable texture wrapping, call the [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate) method as shown in the code example below.


```
d3dDevice->SetRenderState(D3DRS_WRAP0, D3DWRAPCOORD_0);
```



The first parameter accepted by [**IDirect3DDevice9::SetRenderState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrenderstate) is a render state to set. Specify one of the D3DRS\_WRAP0 through D3DRS\_WRAP7 enumerated values which specify which texture level to set the wrapping for. Specify the D3DWRAPCOORD\_0 through D3DWRAPCOORD\_3 flags in the second parameter to enable texture wrapping in the corresponding direction, or combine them to enable wrapping in multiple directions. If you omit a flag, texture wrapping in the corresponding direction is disabled. To disable texture wrapping for a set of texture coordinates, set the value for the corresponding render state to 0.

Do not confuse texture wrapping with the similarly named texture addressing modes. Texture wrapping is performed before texture addressing. Be sure the texture wrapping data does not contain any texture coordinates outside of the range of \[0.0, 1.0\] because this will produce undefined results. For more information about texture addressing, see [Texture Addressing Modes (Direct3D 9)](texture-addressing-modes.md).

## Displacement Map Wrapping

Displacement maps are interpolated by the tesselation engine. Because the wrap mode cannot be specified for the tessellation engine, texture wrapping cannot be performed with displacement maps. An application is able to use a set of vertices that forces the interpolation to wrap in any direction. The application can also specify the interpolation to be done as a simple linear interpolation.

## Related topics

<dl> <dt>

[Direct3D Textures](direct3d-textures.md)
</dt> </dl>

 

 
