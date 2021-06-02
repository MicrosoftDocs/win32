---
description: Alpha can also be supplied in a material. To enable material alpha, set the diffuse material render state so that the runtime will use the material diffuse color components rather than the vertex diffuse color components.
ms.assetid: fd477d8f-d838-4a08-a8c6-38678798e0b0
title: Material Alpha (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Material Alpha (Direct3D 9)

Alpha can also be supplied in a material. To enable material alpha, set the diffuse material render state so that the runtime will use the material diffuse color components rather than the vertex diffuse color components.


```
m_pd3dDevice->SetRenderState( D3DRS_DIFFUSEMATERIALSOURCE, D3DMCS_MATERIAL );
```



Initialize the material with an alpha value, and set the material before drawing.


```
D3DMATERIAL9 mtrl;
mtrl.Diffuse = mtrl.Ambient = mtrl.Specular = mtrl.Emissive = 
    D3DCOLORVALUE(255,0,0,0.5f)

m_pd3dDevice->SetMaterial(&mtrl);     
```



## Related topics

<dl> <dt>

[Alpha Blending](alpha-blending.md)
</dt> </dl>

 

 



