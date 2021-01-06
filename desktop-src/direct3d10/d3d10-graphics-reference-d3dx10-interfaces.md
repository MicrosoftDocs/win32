---
description: This section contains reference information for the component object model (COM) interfaces provided by the D3DX utility library. The following interfaces are used with the D3DX utility library.
ms.assetid: c57d9c39-3f30-4205-9b0a-665fe53f2b14
title: D3DX Interfaces (Direct3D 10 Graphics)
ms.topic: article
ms.date: 05/31/2018
---

# D3DX Interfaces (Direct3D 10 Graphics)

This section contains reference information for the component object model (COM) interfaces provided by the D3DX utility library. The following interfaces are used with the D3DX utility library.



| Interfaces                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ID3DX10DataLoader Interface**](id3dx10dataloader.md)       | Data loading object used by [**ID3DX10ThreadPump Interface**](id3dx10threadpump.md) for loading data asynchronously.<br/>                                                                                                                                                                                                                                                                                                   |
| [**ID3DX10DataProcessor Interface**](id3dx10dataprocessor.md) | Data processing object used by [**ID3DX10ThreadPump Interface**](id3dx10threadpump.md) for processing loaded data asynchronously.<br/>                                                                                                                                                                                                                                                                                      |
| [**ID3DX10Font Interface**](id3dx10font.md)                   | The ID3DX10Font interface encapsulates the textures and resources needed to render a specific font on a specific device.<br/>                                                                                                                                                                                                                                                                                                |
| [**ID3DX10Mesh Interface**](id3dx10mesh.md)                   | Applications use the methods of the ID3DX10Mesh interface to manipulate mesh objects.<br/>                                                                                                                                                                                                                                                                                                                                   |
| [**ID3DX10MeshBuffer Interface**](id3dx10meshbuffer.md)       |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [**ID3DX10SkinInfo Interface**](id3dx10skininfo.md)           | ID3DX10SkinInfo allows you to optimize, process, and manually set the relationship between bones and vertices in your meshes (see [Skeletal Animation on Wikipedia](https://en.wikipedia.org/wiki/Skeletal_animation)). It is most useful for making .x files exported by DCC Apps (such as 3DS Max and Maya) more hardware-friendly, and for improving the render speed of your skinned meshes in software render mode.<br/> |
| [**ID3DX10Sprite Interface**](id3dx10sprite.md)               | The ID3DX10Sprite interface provides a set of methods that simplify the process of drawing sprites using Microsoft Direct3D.<br/>                                                                                                                                                                                                                                                                                            |
| [**ID3DX10ThreadPump Interface**](id3dx10threadpump.md)       | Used to execute tasks asynchronously. This object takes up a substantial amount of resources, so generally only one should be created per application.<br/>                                                                                                                                                                                                                                                                  |
| [**ID3DXMatrixStack Interface**](d3d10-id3dxmatrixstack.md)   | Applications use the methods of the ID3DXMATRIXStack interface to manipulate a matrix stack.<br/>                                                                                                                                                                                                                                                                                                                            |



 

## Related topics

<dl> <dt>

[D3DX Reference](d3d10-graphics-reference-d3dx10.md)
</dt> </dl>

 

 




