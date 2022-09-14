---
description: Current hardware does not necessarily implement all the functionality that the Direct3D interface enables. Your application must test user hardware and adjust its rendering strategies accordingly.
ms.assetid: 7b5f586c-616c-4351-b6b9-5c0179db5d8b
title: Hardware Considerations for Texturing (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Hardware Considerations for Texturing (Direct3D 9)

Current hardware does not necessarily implement all the functionality that the Direct3D interface enables. Your application must test user hardware and adjust its rendering strategies accordingly.

Many 3D accelerator cards do not support diffuse iterated values as arguments to blending units. However, your application can introduce iterated color data when it performs texture blending.

Some 3D hardware may not have a blending stage associated with the first texture. On these adapters, your application must perform blending in the second and third texture stages in the set of current textures.

Because of limitations in much of today's hardware, few display adapters can perform trilinear mipmap interpolation through the multiple texture blending interface offered by [**IDirect3DDevice9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9). Your application can use multipass texture blending to achieve the same effects, or degrade to the D3DTEXF\_POINT mipmap filter mode, which is widely supported.

## Related topics

<dl> <dt>

[Direct3D Textures](direct3d-textures.md)
</dt> </dl>

 

 
