---
description: A texture resource is a structured collection of data.
ms.assetid: 4c716be8-044e-4ed4-aeca-4379440826bd
title: Creating Texture Resources (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Creating Texture Resources (Direct3D 10)

A [texture](d3d10-graphics-programming-guide-resources-types.md) resource is a structured collection of data. Typically, color values are stored in textures and accessed during rendering by the [pipeline](d3d10-graphics-programming-guide-pipeline-stages.md) at various stages for both input and output. Creating textures and defining how they will be used is an important part of rendering interesting-looking scenes in Direct3D 10.

Even though textures typically contain color information, creating textures using different [**DXGI\_FORMAT**](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format) enables them to store different kinds of data. This data can then be leveraged by the Direct3D 10 pipeline in non-traditional ways.

All textures have limits on how much memory they consume, and how many texels they contain. These limits are specified by [resource constants](d3d10-graphics-reference-resource-constants.md).

-   [Create a Texture from a File](#create-a-texture-from-a-file)
    -   [Create Texture and View Separately](#create-texture-and-view-separately)
    -   [Create Texture and View Simultaneously](#create-texture-and-view-simultaneously)
-   [Creating Empty Textures](#creating-empty-textures)
    -   [Rendering to a texture](#rendering-to-a-texture)
    -   [Filling Textures Manually](#filling-textures-manually)
-   [Multiple Rendertargets](#multiple-rendertargets)
-   [Related topics](#related-topics)

## Create a Texture from a File

> [!Note]  
> The [D3DX utility library](d3d10-graphics-reference-d3dx10.md) is deprecated for Windows 8 and is not supported for Windows Store apps.

 

When you create a texture in Direct3D 10, you also need to create a [view](d3d10-graphics-programming-guide-resources-access-views.md). A view is an object that tells the device how a texture should be accessed during rendering. The most common way to access a texture is to read from it using a [shader](../direct3dhlsl/dx-graphics-hlsl.md). A shader-resource view will tell a shader how to read from a texture during rendering. The kind of view a texture will use must be specified when you create it.

Creating a texture and loading its initial data can be done in two different ways: create a texture and view separately, or create both the texture and the view at the same time. The API provides both techniques so you can choose which better suits your needs.

### Create Texture and View Separately

The easiest way to create a texture is to load it from an image file. To create the texture, just fill in one structure and provide the texture's name to [**D3DX10CreateTextureFromFile**](d3dx10createtexturefromfile.md).


```
ID3D10Device *pDevice = NULL;
// Initialize D3D10 device...

D3DX10_IMAGE_LOAD_INFO loadInfo;
ZeroMemory( &loadInfo, sizeof(D3DX10_IMAGE_LOAD_INFO) );
loadInfo.BindFlags = D3D10_BIND_SHADER_RESOURCE;

ID3D10Resource *pTexture = NULL;
D3DX10CreateTextureFromFile( pDevice, L"sample.bmp", &loadInfo, NULL, &pTexture, NULL );
```



The D3DX function [**D3DX10CreateTextureFromFile**](d3dx10createtexturefromfile.md) does three things: first, it creates a Direct3D 10 texture object; second, it reads the input image file; third, it stores the image data in the texture object. In the sample above, a BMP file is loaded, but the function can load a variety of file types.

The bind flag indicates the texture will be created as a shader resource which allows a shader stage to read from the texture during rendering.

The above example does not specify all of the loading parameters. In fact, it's often beneficial to simply zero out the loading parameters as this enables D3DX to choose appropriate values based on the input image. If you want the input image to determine all of the parameters the texture is created with, simply specify **NULL** for the **loadInfo** parameter like this:


```
D3DX10CreateTextureFromFile( pDevice, L"sample.bmp", NULL, NULL, &pTexture, NULL );
```



Specifying **NULL** for the loading information is a simple yet powerful shortcut.

Now that a texture has been created, you need to create a shader-resource view so that the texture can be bound as an input to a shader. Since [**D3DX10CreateTextureFromFile**](d3dx10createtexturefromfile.md) returns a pointer to a resource and not a pointer to a texture, you have to determine the exact type of resource that was loaded, and then you can create a shader-resource view using [**CreateShaderResourceView**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-createshaderresourceview).


```
D3D10_SHADER_RESOURCE_VIEW_DESC srvDesc;
D3D10_RESOURCE_DIMENSION type;
pTexture->GetType( &type );
switch( type )
{
    case D3D10_RESOURCE_DIMENSION_BUFFER:
    //...
    break;
    case D3D10_RESOURCE_DIMENSION_TEXTURE1D:
    //...
    break;
    case D3D10_RESOURCE_DIMENSION_TEXTURE2D:
    {
        D3D10_TEXTURE2D_DESC desc;
        ID3D10Texture2D *pTexture2D = (ID3D10Texture2D*)pTexture;
        pTexture2D->GetDesc( &desc );
        
        srvDesc.Format = desc.Format;
        srvDesc.ViewDimension = D3D10_SRV_DIMENSION_TEXTURE2D;
        srvDesc.Texture2D.MipLevels = desc.MipLevels;
        srvDesc.Texture2D.MostDetailedMip = desc.MipLevels -1;

    }
    break;
    case D3D10_RESOURCE_DIMENSION_TEXTURE3D:
    //...
    break;
    default:
    //...
    break;
}

ID3D10ShaderResourceView *pSRView = NULL;
pDevice->CreateShaderResourceView( pTexture, &srvDesc, &pSRView );
```



Although the above sample creates a 2D shader-resource view, the code to create other shader-resource view types is very similar. Any shader stage can now use this texture as an input.

Using [**D3DX10CreateTextureFromFile**](d3dx10createtexturefromfile.md) and [**CreateShaderResourceView**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-createshaderresourceview) to create a texture and its associated view is one way to prepare a texture to be bound to a shader stage. Another way to do so is to create both the texture and its view at the same time, which is discussed in the next section.

### Create Texture and View Simultaneously

Direct3D 10 requires both a texture and a shader-resource view to read from a texture during runtime. Since the creation of a texture and a shader-resource view is such a common task, D3DX provides the [**D3DX10CreateShaderResourceViewFromFile**](d3dx10createshaderresourceviewfromfile.md) to do it for you.


```
D3DX10_IMAGE_LOAD_INFO loadInfo;
ZeroMemory( &loadInfo, sizeof(D3DX10_IMAGE_LOAD_INFO) );
loadInfo.BindFlags = D3D10_BIND_SHADER_RESOURCE;
loadInfo.Format = DXGI_FORMAT_BC1_UNORM;

ID3D10ShaderResourceView *pSRView = NULL;
D3DX10CreateShaderResourceViewFromFile( pDevice, L"sample.bmp", &loadInfo, NULL, &pSRView, NULL );
```



With a single D3DX call, both the texture and shader-resource view are created. The functionality of the **loadInfo** parameter is unchanged; you can use it to customize how the texture is created, or derive the necessary parameters from the input file by specifying **NULL** for the **loadInfo** parameter.

The [**ID3D10ShaderResourceView**](/windows/desktop/api/d3d10/nn-d3d10-id3d10shaderresourceview) object returned by the [**D3DX10CreateShaderResourceViewFromFile**](d3dx10createshaderresourceviewfromfile.md) function can later be used to retrieve the original [**ID3D10Resource**](/windows/desktop/api/D3D10/nn-d3d10-id3d10resource) interface if it is needed. This can be done by calling the [**GetResource**](/windows/desktop/api/D3D10/nf-d3d10-id3d10view-getresource) method.

D3DX provides a single function to create a texture and shader-resource view as a convienience; it is up to you to decide which method of creating a texture and view best suits the needs of your application.

Now that you know how to create a texture and its shader-resource view, the next section will show you how you can sample (read) from that texture using a shader.

## Creating Empty Textures

Sometimes applications will want to create a texture and compute the data to be stored in the texture, or use the graphics [pipeline](d3d10-graphics-programming-guide-pipeline-stages.md) to render to this texture and later use the results in other processing. These textures could be updated by the graphics pipeline or by the application itself, depending on what kind of [**usage**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_usage) was specified for the texture when it was created.

### Rendering to a texture

The most common case of creating an empty texture to be filled with data during runtime is the case where an application wants to render to a texture and then use the results of the rendering operation in a subsequent pass. Textures created with this purpose should specify default [**usage**](/windows/desktop/api/D3D10/ne-d3d10-d3d10_usage).

The following code sample creates an empty texture that the pipeline can render to and subsequently use as an input to a [shader](../direct3dhlsl/dx-graphics-hlsl-using-shaders-10.md).


```
// Create the render target texture
D3D10_TEXTURE2D_DESC desc;
ZeroMemory( &desc, sizeof(desc) );
desc.Width = 256;
desc.Height = 256;
desc.MipLevels = 1;
desc.ArraySize = 1;
desc.Format = DXGI_FORMAT_R32G32B32A32_FLOAT;
desc.SampleDesc.Count = 1;
desc.Usage = D3D10_USAGE_DEFAULT;
desc.BindFlags = D3D10_BIND_RENDER_TARGET | D3D10_BIND_SHADER_RESOURCE;

ID3D10Texture2D *pRenderTarget = NULL;
pDevice->CreateTexture2D( &desc, NULL, &pRenderTarget );
```



Creating the texture requires the application to specify some information about the properties the texture will have. The width and height of the texture in texels is set to 256. For this render target, a single mipmap level is all we need. Only one render target is required so the array size is set to 1. Each texel contains four 32-bit floating point values, which can be used to store very precise information (see [**DXGI\_FORMAT**](/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format)). One sample per pixel is all that will be needed. The usage is set to default because this allows for the most efficient placement of the render target in memory. Finally, the fact that the texture will be bound as a render target and a shader resource at different points in time is specified.

Textures cannot be bound for rendering to the pipeline directly; use a render-target view as shown in the following code sample.


```
D3D10_RENDER_TARGET_VIEW_DESC rtDesc;
rtDesc.Format = desc.Format;
rtDesc.ViewDimension = D3D10_RTV_DIMENSION_TEXTURE2D;
rtDesc.Texture2D.MipSlice = 0;

ID3D10RenderTargetView *pRenderTargetView = NULL;
pDevice->CreateRenderTargetView( pRenderTarget, &rtDesc, &pRenderTargetView );
```



The format of the render-target view is simply set to the format of the original texture. The information in the resource should be interpreted as a 2D texture, and we only want to use the first mipmap level of the render target.

Similarly to how a render-target view must be created so that the render target can be bound for output to the pipeline, a shader-resource view must be created so that the render target can be bound to the pipeline as an input. The following code sample demonstrates this.


```
// Create the shader-resource view
D3D10_SHADER_RESOURCE_VIEW_DESC srDesc;
srDesc.Format = desc.Format;
srDesc.ViewDimension = D3D10_SRV_DIMENSION_TEXTURE2D;
srDesc.Texture2D.MostDetailedMip = 0;
srDesc.Texture2D.MipLevels = 1;

ID3D10ShaderResourceView *pShaderResView = NULL;
pDevice->CreateShaderResourceView( pRenderTarget, &srDesc, &pShaderResView );
```



The parameters of shader-resource view descriptions are very similar to those of render-target view descriptions and were chosen for the same reasons.

### Filling Textures Manually

Sometimes applications would like to compute values at runtime, put them into a texture manually and then have the graphics [pipeline](d3d10-graphics-programming-guide-pipeline-stages.md) use this texture in later rendering operations. To do this, the application must create an empty texture in such a way to allow the CPU to access the underlying memory. This is done by creating a dynamic texture and gaining access to the underlying memory by calling a particular method. The following code sample demonstrates how to do this.


```
D3D10_TEXTURE2D_DESC desc;
desc.Width = 256;
desc.Height = 256;
desc.MipLevels = desc.ArraySize = 1;
desc.Format = DXGI_FORMAT_R8G8B8A8_UNORM;
desc.SampleDesc.Count = 1;
desc.Usage = D3D10_USAGE_DYNAMIC;
desc.BindFlags = D3D10_BIND_SHADER_RESOURCE;
desc.CPUAccessFlags = D3D10_CPU_ACCESS_WRITE;
ID3D10Texture2D *pTexture = NULL;
pd3dDevice->CreateTexture2D( &desc, NULL, &pTexture );
```



Note that the format is set to a 32 bits per pixel where each component is defined by 8 bits. The usage parameter is set to dynamic while the bind flags are set to specify the texture will be accessed by a shader. The rest of the texture description is similar to creating a render target.

Calling [**Map**](/windows/desktop/api/D3D10/nf-d3d10-id3d10texture2d-map) enables the application to access the underlying memory of the texture. The pointer retrieved is then used to fill the texture with data. This can be seen in the following code sample.


```
D3D10_MAPPED_TEXTURE2D mappedTex;
pTexture->Map( D3D10CalcSubresource(0, 0, 1), D3D10_MAP_WRITE_DISCARD, 0, &mappedTex );

UCHAR* pTexels = (UCHAR*)mappedTex.pData;
for( UINT row = 0; row < desc.Height; row++ )
{
    UINT rowStart = row * mappedTex.RowPitch;
    for( UINT col = 0; col < desc.Width; col++ )
    {
        UINT colStart = col * 4;
        pTexels[rowStart + colStart + 0] = 255; // Red
        pTexels[rowStart + colStart + 1] = 128; // Green
        pTexels[rowStart + colStart + 2] = 64;  // Blue
        pTexels[rowStart + colStart + 3] = 32;  // Alpha
    }
}

pTexture->Unmap( D3D10CalcSubresource(0, 0, 1) );
```



## Multiple Rendertargets

Up to eight render-target views can be bound to the pipeline at a time (with [**OMSetRenderTargets**](/windows/desktop/api/D3D10/nf-d3d10-id3d10device-omsetrendertargets)). For each pixel (or each sample if multisampling is enabled), blending is done independently for each render-target view. Two of the blend state variables - BlendEnable and RenderTargetWriteMask - are arrays of eight, each array member corresponds to a render-target view. When using multiple render targets, each render target must be the same [resource type](d3d10-graphics-programming-guide-resources-types.md) (buffer, 1D texture, 2D texture array, etc.) and must have the same dimension (width, height, depth for 3D textures, and array size for texture arrays). If the render targets are multisampled, then they must all have the same number of samples per pixel.

There can only be one depth-stencil buffer active, regardless of how many render targets are active. When using texture arrays as render targets, all view dimensions must match. The render targets do not need to have the same texture format.

## Related topics

<dl> <dt>

[Resources (Direct3D 10)](d3d10-graphics-programming-guide-resources.md)
</dt> </dl>

 

 
