---
description: Fog blending refers to the application of the fog factor to the fog and object colors to produce the final color that appears in a scene, as discussed in Fog Formulas (Direct3D 9).
ms.assetid: b5b43f12-bbed-4464-aebc-02ad6dab1951
title: Fog Blending (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Fog Blending (Direct3D 9)

Fog blending refers to the application of the fog factor to the fog and object colors to produce the final color that appears in a scene, as discussed in [Fog Formulas (Direct3D 9)](fog-formulas.md). The D3DRS\_FOGENABLE render state controls fog blending. Set this render state to **TRUE** to enable fog blending as shown in the following example code. The default is **FALSE**.


```
// For this example, g_pDevice is a valid pointer
// to an IDirect3DDevice9 interface.
HRESULT hr;
hr = g_pDevice->SetRenderState(
                    D3DRS_FOGENABLE,
                    TRUE);
if FAILED(hr)
    return hr;
```



You must enable fog blending for both pixel fog and vertex fog. For information about using these types of fog, see [Pixel Fog (Direct3D 9)](pixel-fog.md) and [Vertex Fog (Direct3D 9)](vertex-fog.md).

## Related topics

<dl> <dt>

[Fog Types](fog-types.md)
</dt> </dl>

 

 



