---
description: Defines a coordinate frame, or &\#0034;frame of reference.&\#0034; The Frame template is open and can contain any object. The D3DX mesh-loading functions recognize Mesh, FrameTransformMatrix, and Frame template instances as child objects when loading a Frame instance.
ms.assetid: 'vs|directx_sdk|~\frame.htm'
title: Frame (Direct3D 9 Graphics)
ms.topic: article
ms.date: 05/31/2018
---

# Frame (Direct3D 9 Graphics)

Defines a coordinate frame, or "frame of reference." The Frame template is open and can contain any object. The D3DX mesh-loading functions recognize [**Mesh**](mesh.md), [**FrameTransformMatrix**](frametransformmatrix.md), and **Frame** template instances as child objects when loading a **Frame** instance.

``` syntax
template Frame
{
    < 3D82AB46-62DA-11CF-AB39-0020AF71E433 >
    [...]           
} 
```

The frame template recognizes child **Frame** and [**Mesh**](mesh.md) nodes inside a frame and can recognize user-defined templates through a callback function.

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



