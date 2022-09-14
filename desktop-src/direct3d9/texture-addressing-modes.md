---
description: Your Direct3D application can assign texture coordinates to any vertex of any primitive.
ms.assetid: 2e23bcb3-9eba-49d9-93ce-0a4fbb15f746
title: Texture Addressing Modes (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Texture Addressing Modes (Direct3D 9)

Your Direct3D application can assign texture coordinates to any vertex of any primitive. For details, see [Texture Coordinates (Direct3D 9)](texture-coordinates.md). Typically, the u- and v-texture coordinates that you assign to a vertex are in the range of 0.0 to 1.0 inclusive. However, by assigning texture coordinates outside that range, you can create certain special texturing effects.

You control what Direct3D does with texture coordinates that are outside the \[0.0, 1.0\] range by setting the texture addressing mode. For instance, you can have your application set the texture addressing mode so that a texture is tiled across a primitive.

Direct3D enables applications to perform texture wrapping. It is important to note that setting the texture addressing mode to D3DTADDRESS\_WRAP is not the same as performing texture wrapping. Setting the texture addressing mode to D3DTADDRESS\_WRAP results in multiple copies of the source texture being applied to the current primitive, and enabling texture wrapping changes how the system rasterizes textured polygons. For details, see [Texture Wrapping (Direct3D 9)](texture-wrapping.md).

Enabling texture wrapping effectively makes texture coordinates outside the \[0.0, 1.0\] range invalid, and the behavior for rasterizing such delinquent texture coordinates is undefined in this case. When texture wrapping is enabled, texture addressing modes are not used. Take care that your application does not specify texture coordinates lower than 0.0 or higher than 1.0 when texture wrapping is enabled.

## Setting the Addressing Mode

You can set texture addressing modes for individual texture stages by calling the [**IDirect3DDevice9::SetSamplerState**](/windows/desktop/api) method. Specify the desired texture stage identifier in the *Sampler* parameter. Set the *Type* parameter to D3DSAMP\_ADDRESSU, D3DSAMP\_ADDRESSV, or D3DSAMP\_ADDRESSW values to update the u-, v-, or w-addressing modes individually. The *Value* parameter determines which mode is being set. This can be any member of the [**D3DTEXTUREADDRESS**](./d3dtextureaddress.md) enumerated type. To retrieve the current texture address mode for a texture stage, call [**IDirect3DDevice9::GetSamplerState**](/windows/desktop/api), using the D3DSAMP\_ADDRESSU, D3DSAMP\_ADDRESSV, or D3DSAMP\_ADDRESSW members of the [**D3DSAMPLERSTATETYPE**](./d3dsamplerstatetype.md) enumeration to identify the address mode about which you want information.

## Device Limitations

Although the system generally allows texture coordinates outside the range of 0.0 and 1.0, inclusive, hardware limitations often affect how far outside that range texture coordinates can be. A rendering device communicates this limit in the **MaxTextureRepeat** member of the [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) structure when you retrieve device capabilities. The value in this member describes the full range of texture coordinates allowed by the device. For instance, if this value is 128, then the input texture coordinates must be kept in the range -128.0 to +128.0. Passing vertices with texture coordinates outside this range is invalid. The same restriction applies to the texture coordinates generated as a result of automatic texture coordinate generation and texture coordinate transformations.

The interpretation of **MaxTextureRepeat** is also affected by the D3DPTEXTURECAPS\_TEXREPEATNOTSCALEDBYSIZE capability bit. When this bit is set, the value in the **MaxTextureRepeat** member is used precisely as described. However, when D3DPTEXTURECAPS\_TEXREPEATNOTSCALEDBYSIZE is not set, texture repeating limitations depend on the size of the texture indexed by the texture coordinates. In this case, **MaxTextureRepeat** must be scaled by the current texture size at the largest level of detail to compute the valid texture coordinate range. For example, given a texture dimension of 32 and **MaxTextureRepeat** of 512, the actual valid texture coordinate range is 512/32 = 16, so the texture coordinates for this device must be within the range of -16.0 to +16.0.

Additional information about the texture addressing modes is contained in the following topics.

-   [Wrap Texture Address Mode (Direct3D 9)](wrap-texture-address-mode.md)
-   [Mirror Texture Address Mode (Direct3D 9)](mirror-texture-address-mode.md)
-   [Clamp Texture Address Mode (Direct3D 9)](clamp-texture-address-mode.md)
-   [Border Color Texture Address Mode (Direct3D 9)](border-color-texture-address-mode.md)

## Related topics

<dl> <dt>

[Basic Texturing Concepts](basic-texturing-concepts.md)
</dt> </dl>

 

 
