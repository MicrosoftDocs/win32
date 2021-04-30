---
title: D (OpenGL)
description: Definitions of OpenGL terms that begin with the letter D.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 'f97470e7-a500-47d7-84f0-b3045d04b8fc'
keywords:
- depth
- depth cueing
- display lists
- dithering
- double buffering
ms.topic: article
ms.date: 05/31/2018
---

# D (OpenGL)

[A](a.md) [B](b.md) [C](c.md) D [E](e.md) [F](f.md) [G](g.md) [H](h.md) [I](i.md) [J K](jk.md) [L](l.md) [M](m.md) [N](n.md) [O](o.md) [P](p.md) [Q](q.md) [R](r.md) [S](s.md) [T](t.md) [U V](u-v.md) [W](w.md) [X Y Z](x-y-z.md)

<dl> <dt>

<span id="opengl_depth"></span><span id="OPENGL_DEPTH"></span>**depth**
</dt> <dd>

Generally refers to the z window coordinate.

</dd> <dt>

<span id="opengl_depth_cueing"></span><span id="OPENGL_DEPTH_CUEING"></span>**depth cueing**
</dt> <dd>

A rendering technique that assigns color based on distance from the viewpoint.

</dd> <dt>

<span id="opengl_display_list"></span><span id="OPENGL_DISPLAY_LIST"></span>**display list**
</dt> <dd>

A named list of OpenGL commands. Display lists are always stored on the server, so display lists can be used to reduce the network traffic in client/server environments. The contents of a display list may be preprocessed, and might therefore execute more efficiently than the same set of OpenGL commands executed in immediate mode. Such preprocessing is especially important for computing intensive commands such as [**glTexImage**](glteximage1d.md).

</dd> <dt>

<span id="opengl_dithering"></span><span id="OPENGL_DITHERING"></span>**dithering**
</dt> <dd>

A technique for increasing the perceived range of colors in an image at the cost of spatial resolution. Adjacent pixels are assigned differing color values. When viewed from a distance, these colors seem to blend into a single intermediate color. The technique is similar to the half-toning used in black-and-white publications to achieve shades of gray.

</dd> <dt>

<span id="opengl_double_buffering"></span><span id="OPENGL_DOUBLE_BUFFERING"></span>**double buffering**
</dt> <dd>

Using OpenGL contexts in which both front and back color buffers are double-buffered. Smooth animation is accomplished by rendering into only the back buffer (which isn't displayed), then causing the front and back buffers to be swapped.

</dd> </dl>

 

 




