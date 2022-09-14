---
title: Apply a Technique (Direct3D 11)
description: Learn how to set the effect state in the device for Direct3D 11 after the constants, textures, and shader state are declared and initialized.
ms.assetid: 16001913-7ae2-4629-a625-eb850e29fc77
ms.topic: article
ms.date: 05/31/2018
---

# Apply a Technique (Direct3D 11)

With the constants, textures, and shader state declared and initialized, the only thing left to do is to set the effect state in the device.

## Set Non-Shader State in the Device

Some pipeline state is not set by an effect. For example clearing a render target prepares the render target for data. Before setting the effect state in the device, here is an example of clearing output buffers.


```
    // Clear the render target and depth stencil
    float ClearColor[4] = { 0.0f, 0.25f, 0.25f, 0.55f };
    ID3D11RenderTargetView* pRTV = DXUTGetD3D11RenderTargetView();
    pD3DDevice->ClearRenderTargetView( pRTV, ClearColor );
    ID3D11DepthStencilView* pDSV = DXUTGetD3D11DepthStencilView();
    pD3DDevice->ClearDepthStencilView( pDSV, D3D11_CLEAR_DEPTH, 1.0, 0 );
```



## Set Effect State in the Device

Setting effect state is done by applying the effect state within the render loop. This is done from the outside in. That is, select a technique, and then set the state for each of the passes (depending on your desired result).


```
    D3D11_TECHNIQUE_DESC techDesc;
    pRenderTechnique->GetDesc( &techDesc );
    for( UINT p = 0; p < techDesc.Passes; ++p )
    {
        }
            ....
            pRenderTechnique->GetPassByIndex( p )->Apply(0);
            pd3dDevice->DrawIndexed( (UINT)pSubset->IndexCount, 0,  
                 (UINT)pSubset->VertexStart );
        }
    }
```



An effect doesn't render anything, it simply sets effect state to the device. The rendering code is called after the effect state updates device state. In this example, the DrawIndexed call performs the rendering.

## Related topics

<dl> <dt>

[Rendering an Effect (Direct3D 11)](d3d11-graphics-programming-guide-effects-render.md)
</dt> </dl>

 

 




