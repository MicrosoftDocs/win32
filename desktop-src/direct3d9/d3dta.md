---
description: 'Texture argument constants are used as values for the following members of the D3DTEXTURESTAGESTATETYPE enumerated type:'
ms.assetid: 36b2b715-5ced-4246-840e-8ea343521ef4
title: D3DTA
ms.topic: article
ms.date: 05/31/2018
---

# D3DTA

Texture argument constants are used as values for the following members of the [**D3DTEXTURESTAGESTATETYPE**](./d3dtexturestagestatetype.md) enumerated type:

-   D3DTSS\_ALPHAARG0
-   D3DTSS\_ALPHAARG1
-   D3DTSS\_ALPHAARG2
-   D3DTSS\_COLORARG0
-   D3DTSS\_COLORARG1
-   D3DTSS\_COLORARG2
-   D3DTSS\_RESULTARG

Set and retrieve texture arguments by calling the [**SetTextureStageState**](/windows/desktop/api) and [**GetTextureStageState**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-gettexturestagestate) methods.

Argument flags

You can combine an argument flag with a modifier, but two argument flags cannot be combined.



| \#define          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| D3DTA\_CONSTANT   | Select a constant from a texture stage. The default value is 0xffffffff.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| D3DTA\_CURRENT    | The texture argument is the result of the previous blending stage. In the first texture stage (stage 0), this argument is equivalent to D3DTA\_DIFFUSE. If the previous blending stage uses a bump-map texture (the D3DTOP\_BUMPENVMAP operation), the system chooses the texture from the stage before the bump-map texture. If s represents the current texture stage and s - 1 contains a bump-map texture, this argument becomes the result output by texture stage s - 2. Permissions are read/write. |
| D3DTA\_DIFFUSE    | The texture argument is the diffuse color interpolated from vertex components during Gouraud shading. If the vertex does not contain a diffuse color, the default color is 0xffffffff. Permissions are read-only.                                                                                                                                                                                                                                                                                          |
| D3DTA\_SELECTMASK | Mask value for all arguments; not used when setting texture arguments.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| D3DTA\_SPECULAR   | The texture argument is the specular color interpolated from vertex components during Gouraud shading. If the vertex does not contain a specular color, the default color is 0xffffffff. Permissions are read-only.                                                                                                                                                                                                                                                                                        |
| D3DTA\_TEMP       | The texture argument is a temporary register color for read or write. D3DTA\_TEMP is supported if the [D3DPMISCCAPS\_TSSARGTEMP](d3dpmisccaps.md) device capability is present. The default value for the register is (0.0, 0.0, 0.0, 0.0). Permissions are read/write.                                                                                                                                                                                                                                   |
| D3DTA\_TEXTURE    | The texture argument is the texture color for this texture stage. Permissions are read-only.                                                                                                                                                                                                                                                                                                                                                                                                               |
| D3DTA\_TFACTOR    | The texture argument is the texture factor set in a previous call to the [**SetRenderState**](/windows/desktop/api) with the [**D3DRS\_TEXTUREFACTOR**](./d3drenderstatetype.md) render-state value. Permissions are read-only.                                                                                                                                                                                                                                                       |



 

Modifier flags

An argument flag may be combined with one of the following modifier flags.



| \#define              | Description                                                                                                    |
|-----------------------|----------------------------------------------------------------------------------------------------------------|
| D3DTA\_ALPHAREPLICATE | Replicate the alpha information to all color channels before the operation completes. This is a read modifier. |
| D3DTA\_COMPLEMENT     | Take the complement of the argument x, (1.0 - x). This is a read modifier.                                     |



 

## Constant Information



|   Requirement                       |  Value           |
|--------------------------|-------------|
| Header                   | d3d9types.h |
| Minimum operating system | Windows 98  |



 

## Related topics

<dl> <dt>

[Direct3D Constants](dx9-graphics-reference-d3d-constants.md)
</dt> </dl>

 

 
