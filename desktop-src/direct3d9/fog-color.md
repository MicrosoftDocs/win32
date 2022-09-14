---
description: Fog color for both pixel and vertex fog is set through the D3DRS\_FOGCOLOR render state. The render state values can be any RGB color, specified as an RGBA color. The alpha component is ignored.
ms.assetid: 76366496-553d-4dbf-868d-d58b5377d36a
title: Fog Color (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Fog Color (Direct3D 9)

Fog color for both pixel and vertex fog is set through the D3DRS\_FOGCOLOR render state. The render state values can be any RGB color, specified as an RGBA color. The alpha component is ignored.

The following C++ example sets the fog color to white.


```
/* For this example, the d3dDevice variable is
* a valid pointer to an IDirect3DDevice9 interface.
*/
HRESULT hr;
hr = d3dDevice->SetRenderState(
                    D3DRS_FOGCOLOR,
                    0x00FFFFFF); // Highest 8 bits are not used.
if(FAILED(hr))
    return hr;
```



Fog is applied differently by the fixed function pipeline and the programmable pipeline.

1.  If the driver supports D3DPMISCCAPS\_FOGANDSPECULARALPHA:
    -   If the fixed function pipeline is used and D3DRS\_FOGCOLOR is set, v1.w (in the pixel shader) equals the value set in fog renderstate.
    -   If the programmable pipeline is used, then v1.w (in the pixel shader) equals 0, even if oD1.w is explicitly written in a vertex shader.
2.  If the driver does NOT support D3DPMISCCAPS\_FOGANDSPECULARALPHA:
    -   If the fixed function pipeline is used and D3DRS\_FOGCOLOR is set, then v1.w (in the pixel shader) equals value set in fog renderstate.
    -   If oFog is explicitly written in a vertex shader, v1.w (in the pixel shader) equals oFog, clamped between 0 and 1.
    -   If neither of the above two cases applies, v1.w (in the pixel shader) equals 0, even if oD1.w is explicitly written in a vertex shader.

For more information, see [D3DPMISCCAPS](d3dpmisccaps.md).

## Related topics

<dl> <dt>

[Fog Types](fog-types.md)
</dt> </dl>

 

 



