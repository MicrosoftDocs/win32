---
description: Direct3D enables one shading mode to be selected at a time.
ms.assetid: 9531947d-4cd8-43c3-8825-4c48a0d69395
title: Setting the Shading Mode (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Setting the Shading Mode (Direct3D 9)

Direct3D enables one shading mode to be selected at a time. By default, Gouraud shading is selected. In C++, you can change the shading mode by calling the [**IDirect3DDevice9::SetRenderState**](/windows/desktop/api) method. Set the *State* parameter to D3DRS\_SHADEMODE. The *State* parameter must be set to a member of the [**D3DSHADEMODE**](./d3dshademode.md) enumeration. The following sample code examples illustrate how the current shading mode of a Direct3D application can be set to flat or Gouraud shading mode.


```
// Set to flat shading.
// This code example assumes that pDev is a valid pointer to 
// an IDirect3DDevice9 interface.
hr = pDev->SetRenderState(D3DRS_SHADEMODE, D3DSHADE_FLAT);
if(FAILED(hr))
{
    // Code to handle the error goes here.
}

// Set to Gouraud shading. This is the default for Direct3D.
hr = pDev->SetRenderState(D3DRS_SHADEMODE,
                            D3DSHADE_GOURAUD);
if(FAILED(hr))
{
    // Code to handle the error goes here.
}
```



## Related topics

<dl> <dt>

[Shading](shading.md)
</dt> </dl>

 

 
