---
description: You create a cubic environment map texture by calling the CreateCubeTexture method. Cubic environment map textures must be square, with dimensions that are a power of two.
ms.assetid: 3879d215-064b-4d7d-afae-2ed46569c8bf
title: Creating Cubic Environment Map Surfaces (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Creating Cubic Environment Map Surfaces (Direct3D 9)

You create a cubic environment map texture by calling the [**CreateCubeTexture**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-createcubetexture) method. Cubic environment map textures must be square, with dimensions that are a power of two.

The following code example shows how your C++ application might create a simple cubic environment map.


```
// Init m_d3dDevice to point to an IDirect3DDevice9 interface

LPDIRECT3DCUBETEXTURE9 m_pCubeMap;

m_d3dDevice->CreateCubeTexture(256, 1, D3DUSAGE_RENDERTARGET, D3DFMT_R8G8B8,
                                D3DPOOL_DEFAULT, &m_pCubeMap);
```



## Accessing Cubic Environment Map Faces

You can navigate between faces of a cubic environment map by using the [**GetCubeMapSurface**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dcubetexture9-getcubemapsurface) method.

The following code example uses [**GetCubeMapSurface**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dcubetexture9-getcubemapsurface) to retrieve the cube-map surface used for the positive y-face (face 2).


```
// Init m_pCubeMap to point to an IDirect3DCubeTexture9 interface

LPDIRECT3DSURFACE9 pFace2;
m_pCubeMap->GetCubeMapSurface(D3DCUBEMAP_FACE_POSITIVE_Y, 0, &pFace2);
```



The first parameter that [**GetCubeMapSurface**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dcubetexture9-getcubemapsurface) accepts is a [**D3DCUBEMAP\_FACES**](./d3dcubemap-faces.md) enumerated value that describes the attached surface that the method should retrieve. The second parameter tells Direct3D which level of a mipmapped cube texture to retrieve. The third parameter accepted is the address of the [**IDirect3DSurface9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dsurface9) interface, representing the returned cube texture surface. Because this cube-map is not mipmapped, 0 is used here.

> [!Note]
>
> After calling this method, the internal reference count on the [**IDirect3DSurface9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3dsurface9) interface is increased. When you are done using this surface, be sure to call the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) method on this **IDirect3DSurface9** interface or you will have a memory leak.

 

## Rendering to Cubic Environment Maps

You can copy images to the individual faces of the cube map just like you would any other texture or surface object. The most important thing to do before rendering to a face is set the transformation matrices so that the camera is positioned properly and points in the proper direction for that face: forward (+z), backward (-z), left (-x), right (+x), up (+y), or down (-y).

The following C++ code example prepares and sets a view matrix according to the face being rendered.


```
// Init pCubeMap to point to an IDirect3DCubeTexture9 interface
// Init d3dDevice to point to an IDirect3DDevice9 interface

void RenderFaces()
{
    // Save transformation matrices of the device
    D3DXMATRIX matProjSave, matViewSave;
    d3dDevice->GetTransform(D3DTS_VIEW,       &matViewSave ;
    d3dDevice->GetTransform(D3DTS_PROJECTION, &matProjSave);

    // Store the current back buffer and z-buffer
    LPDIRECT3DSURFACE9 pBackBuffer, pZBuffer;
    d3dDevice->GetRenderTarget(&pBackBuffer);
    d3dDevice->GetDepthStencilSurface(&pZBuffer);
```



Remember, each face of a cubic environment map represents a 90-degree field of view. Unless your application requires a different field of view angle - for special effects, for example - take care to set the projection matrix accordingly.

This code example creates and sets a projection matrix for the most common case.


```
    // Use 90-degree field of view in the projection
    D3DMATRIX matProj;
    D3DXMatrixPerspectiveFovLH(matProj, D3DX_PI/2, 1.0f, 0.5f, 1000.0f);
    d3dDevice->SetTransform(D3DTS_PROJECTION, &matProj);

    // Loop through the six faces of the cube map
    for(DWORD i=0; i<6; i++)
    {
        // Standard view that will be overridden below
        D3DVECTOR vEnvEyePt = D3DVECTOR(0.0f, 0.0f, 0.0f);
        D3DVECTOR vLookatPt, vUpVec;

        switch(i)
        {
            case D3DCUBEMAP_FACE_POSITIVE_X:
                vLookatPt = D3DVECTOR(1.0f, 0.0f, 0.0f);
                vUpVec    = D3DVECTOR(0.0f, 1.0f, 0.0f);
                break;
            case D3DCUBEMAP_FACE_NEGATIVE_X:
                vLookatPt = D3DVECTOR(-1.0f, 0.0f, 0.0f);
                vUpVec    = D3DVECTOR( 0.0f, 1.0f, 0.0f);
                break;
            case D3DCUBEMAP_FACE_POSITIVE_Y:
                vLookatPt = D3DVECTOR(0.0f, 1.0f, 0.0f);
                vUpVec    = D3DVECTOR(0.0f, 0.0f,-1.0f);
                break;
            case D3DCUBEMAP_FACE_NEGATIVE_Y:
                vLookatPt = D3DVECTOR(0.0f,-1.0f, 0.0f);
                vUpVec    = D3DVECTOR(0.0f, 0.0f, 1.0f);
                break;
            case D3DCUBEMAP_FACE_POSITIVE_Z:
                vLookatPt = D3DVECTOR( 0.0f, 0.0f, 1.0f);
                vUpVec    = D3DVECTOR( 0.0f, 1.0f, 0.0f);
                break;
            case D3DCUBEMAP_FACE_NEGATIVE_Z:
                vLookatPt = D3DVECTOR(0.0f, 0.0f,-1.0f);
                vUpVec    = D3DVECTOR(0.0f, 1.0f, 0.0f);
                break;
        }

         D3DMATRIX matView;
         D3DXMatrixLookAtLH(matView, vEnvEyePt, vLookatPt, vUpVec);
         d3dDevice->SetTransform(D3DTS_VIEW, &matView);
```



When the camera is in position and the projection matrix set, you can render the scene. Each object in the scene should be positioned as you would normally position them. The following code example, provided for completeness, outlines this task.


```
        // Get pointer to surface in order to render to it
        LPDIRECT3DSURFACE9 pFace;
        pCubeMap->GetCubeMapSurface((D3DCUBEMAP_FACES)i, 0, &pFace);
        d3dDevice->SetRenderTarget (pFace , pZBuffer);
        SAFE_RELEASE(pFace);

        d3dDevice->BeginScene();
        // Render scene here
        ...
        d3dDevice->EndScene();
    }

    // Change the render target back to the main back buffer.
    d3dDevice->SetRenderTarget(pBackBuffer, pZBuffer);
    SAFE_RELEASE(pBackBuffer);
    SAFE_RELEASE(pZBuffer);

    // Restore the original transformation matrices
    d3dDevice->SetTransform(D3DTS_VIEW,       &matViewSave);
    d3dDevice->SetTransform(D3DTS_PROJECTION, &matProjSave);
}
```



Note the call to the [**SetRenderTarget**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setrendertarget) method. When rendering to the cube map faces, you must assign the face as the current render-target surface. Applications that use depth buffers can explicitly create a depth-buffer for the render-target, or reassign an existing depth-buffer to the render-target surface. The code sample above uses the latter approach.

## Related topics

<dl> <dt>

[Cubic Environment Mapping](cubic-environment-mapping.md)
</dt> </dl>

 

 
