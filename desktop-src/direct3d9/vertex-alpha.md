---
description: Alpha data can be supplied in the vertex data. To enable vertex alpha, set the D3DRS\_DIFFUSEMATERIALSOURCE to D3DMCS\_COLOR1 so that the Direct3D runtime takes the diffuse value from the diffuse color rather than the material.
ms.assetid: 2b0d842d-ee7d-4633-846d-96697153adc7
title: Vertex Alpha (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Vertex Alpha (Direct3D 9)

Alpha data can be supplied in the vertex data. To enable vertex alpha, set the D3DRS\_DIFFUSEMATERIALSOURCE to D3DMCS\_COLOR1 so that the Direct3D runtime takes the diffuse value from the diffuse color rather than the material.


```
m_pd3dDevice->SetRenderState( D3DRS_DIFFUSEMATERIALSOURCE,  
                                D3DMCS_COLOR1 );
```



Then, provide alpha values in the diffuse color. The AddAlphaToASphere function, adds alpha to the vertices of a sphere. Here's an example of how to provide the alpha information to the function.


```
AddAlphaToASphere( m_pObstacleVertices, 12,  
                    D3DRGBA(light.dcvDiffuse.r, light.dcvDiffuse.g, 
                            light.dcvDiffuse.b, vAlpha ));
```



This is what the function looks like.


```
 
void AddAlphaToASphere(D3DLVERTEX* pVertices, DWORD dwNumRings, D3DCOLOR lightcolor)
{
    WORD x, y;
    // rings around
    for( y=0; y < dwNumRings; y++ )
        for( x=0; x < (dwNumRings*2)+1; x++ )
            (pVertices++)->color = lightcolor;

    // top and bottom
    (pVertices++)->color = lightcolor;
    (pVertices++)->color = lightcolor;
}
```



AddAlphaToASphere simply modifies the color member of each vertex, which are of type D3DLVERTEX, to include the alpha information.

D3DLVERTEX looks like this.


```
 
// Lit vertex
typedef struct {
    D3DVALUE x, y, z;
    DWORD dwReserved;
    D3DCOLOR color, specular;
    D3DVALUE tu, tv;
} D3DLVERTEX, *LPD3DLVERTEX;
```



Drawing the sphere,


```
#define D3DFVF_LVERTEX ( D3DFVF_XYZ | D3DFVF_DIFFUSE | D3DFVF_SPECULAR | \
                        D3DFVF_TEX0 )

//...

// Draw the lit sphere
m_pd3dDevice->DrawIndexedPrimitive( D3DPT_TRIANGLELIST, D3DFVF_LVERTEX,
                                    m_pObstacleVertices, m_dwNumObstacleVertices,
                                    m_pObstacleIndices,  m_dwNumObstacleIndices, 0 );
```



results in a transparent sphere using vertex alpha.

## Related topics

<dl> <dt>

[Alpha Blending](alpha-blending.md)
</dt> </dl>

 

 



