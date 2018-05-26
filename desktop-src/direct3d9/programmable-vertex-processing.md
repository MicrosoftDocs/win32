---
Description: When using a programmed vertex shader, the elements updated in the destination vertex buffer are controlled by the shader function program.
ms.assetid: c75564ef-528b-4af5-9ed7-a32b9120bf6a
title: Programmable Vertex Processing (Direct3D 9)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Programmable Vertex Processing (Direct3D 9)

When using a programmed vertex shader, the elements updated in the destination vertex buffer are controlled by the shader function program. When the application writes to one of the destination vertex registers, the corresponding element within each vertex of the destination vertex buffer is updated. Elements in the destination vertex buffer that are not written to by the application are not modified. [**IDirect3DDevice9::ProcessVertices**](/windows/win32/d3d9helper/nf-d3d9-idirect3ddevice9-processvertices?branch=master) will fail if the application writes to elements that are not present in the destination vertex buffer.

## Related topics

<dl> <dt>

[Vertex Buffers](vertex-buffers.md)
</dt> </dl>

 

 



