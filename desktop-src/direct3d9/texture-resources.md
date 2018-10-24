---
Description: Texture resources are implemented in the IDirect3DTexture9 interface. To obtain a pointer to a texture interface, call the IDirect3DDevice9::CreateTexture method or any of the following D3DX functions.
ms.assetid: 'vs|directx_sdk|~\texture_resources.htm'
title: Texture Resources (Direct3D 9)
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Texture Resources (Direct3D 9)

Texture resources are implemented in the [**IDirect3DTexture9**](https://msdn.microsoft.com/library/Bb205909(v=VS.85).aspx) interface. To obtain a pointer to a texture interface, call the [**IDirect3DDevice9::CreateTexture**](https://msdn.microsoft.com/library/Bb174363(v=VS.85).aspx) method or any of the following D3DX functions.

-   [**D3DXCreateTexture**](d3dxcreatetexture.md)
-   [**D3DXCreateTextureFromFile**](d3dxcreatetexturefromfile.md)
-   [**D3DXCreateTextureFromFileEx**](d3dxcreatetexturefromfileex.md)
-   [**D3DXCreateTextureFromFileInMemory**](d3dxcreatetexturefromfileinmemory.md)
-   [**D3DXCreateTextureFromFileInMemoryEx**](d3dxcreatetexturefromfileinmemoryex.md)
-   [**D3DXCreateTextureFromResource**](d3dxcreatetexturefromresource.md)
-   [**D3DXCreateTextureFromResourceEx**](d3dxcreatetexturefromresourceex.md)

The following code example uses [**D3DXCreateTextureFromFile**](d3dxcreatetexturefromfile.md) to load a texture from Tiger.bmp.


```
// The following code example assumes that D3dDevice
// is a valid pointer to an IDirect3DDevice9 interface.

LPDIRECT3DTEXTURE9 pTexture;

D3DXCreateTextureFromFile( d3dDevice, "tiger.bmp", &pTexture);
```



The first parameter that [**D3DXCreateTextureFromFile**](d3dxcreatetexturefromfile.md) accepts is a pointer to an [**IDirect3DDevice9**](/windows/desktop/api) interface. The second parameter tells Direct3D the name of the file from which to load the texture. The third parameter takes the address of a pointer to an [**IDirect3DTexture9**](https://msdn.microsoft.com/library/Bb205909(v=VS.85).aspx) interface, representing the created texture object.

## Rendering with Texture Resources

Direct3D supports multiple texture blending through the concept of texture stages. Each texture stage contains a texture and operations that can be performed on the texture. The textures in the texture stages form the set of current textures. For more information, see [Texture Blending (Direct3D 9)](texture-blending.md). The state of each texture is encapsulated in its texture stage.

In a C++ application, the state of each texture must be set with the [**IDirect3DDevice9::SetTextureStageState**](/windows/desktop/api) method. Pass the stage number (0-7) as the value of the first parameter. Set the value of the second parameter to a member of the [**D3DTEXTURESTAGESTATETYPE**](https://msdn.microsoft.com/en-us/library/Bb172617(v=VS.85).aspx) enumerated type. The final parameter is the state value for the particular texture state.

Using texture interface pointers, your application can render a blend of up to eight textures. Set the current textures by invoking the [**IDirect3DDevice9::SetTexture**](https://msdn.microsoft.com/library/Bb174461(v=VS.85).aspx) method. Direct3D blends all current textures onto the primitives that it renders.

> [!Note]  
> The [**IDirect3DDevice9::SetTexture**](https://msdn.microsoft.com/library/Bb174461(v=VS.85).aspx) method increments the reference count of the texture surface being assigned. When the texture is no longer needed, you should set the texture at the appropriate stage to **NULL**. If you fail to do this, the surface will not be released, resulting in a memory leak.

 

Your application can set the texture wrapping state for the current textures by calling the [**IDirect3DDevice9::SetRenderState**](https://msdn.microsoft.com/library/Bb174454(v=VS.85).aspx) method. Pass a value from D3DRS\_WRAP0 through D3DRS\_WRAP7 as the value of the first parameter, and use a combination of the D3DWRAPCOORD\_0, D3DWRAPCOORD\_1, D3DWRAPCOORD\_2, and D3DWRAPCOORD\_3 flags to enable wrapping in the u, v, or w directions.

Your application can also set the texture perspective and texture filtering states. See [Texture Filtering (Direct3D 9)](texture-filtering.md).

## Related topics

<dl> <dt>

[Direct3D Textures](direct3d-textures.md)
</dt> </dl>

 

 



