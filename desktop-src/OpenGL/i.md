---
title: I (OpenGL)
description: Definitions of OpenGL terms that begin with the letter I.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: '2c78efce-9aed-4bcd-a254-7bff053b0acd'
keywords:
- images
- image primitives
- immediate mode
- index
- IRIS GL
ms.topic: article
ms.date: 05/31/2018
---

# I (OpenGL)

[A](a.md) [B](b.md) [C](c.md) [D](d.md) [E](e.md) [F](f.md) [G](g.md) [H](h.md) I [J K](jk.md) [L](l.md) [M](m.md) [N](n.md) [O](o.md) [P](p.md) [Q](q.md) [R](r.md) [S](s.md) [T](t.md) [U V](u-v.md) [W](w.md) [X Y Z](x-y-z.md)

<dl> <dt>

<span id="opengl_image"></span><span id="OPENGL_IMAGE"></span>**image**
</dt> <dd>

A rectangular array of pixels, either in client memory or in the framebuffer.

</dd> <dt>

<span id="opengl_image_primitive"></span><span id="OPENGL_IMAGE_PRIMITIVE"></span>**image primitive** 
</dt> <dd>

A bitmap or an image.

</dd> <dt>

<span id="opengl_immediate_mode"></span><span id="OPENGL_IMMEDIATE_MODE"></span>**immediate mode**
</dt> <dd>

Mode in which an OpenGL command is called directly, rather than from a display list. No immediate-mode bit exists; the mode in immediate mode refers to usage of OpenGL, rather than to a specific bit of OpenGL state.

</dd> <dt>

<span id="opengl_index"></span><span id="OPENGL_INDEX"></span>**index**
</dt> <dd>

A single value that is interpreted as an absolute value, rather than as a normalized value in a specified range (as is a component). Color indexes are the names of colors, which are dereferenced by the display hardware using the color map. Indexes are typically masked, rather than clamped, when out of range. For example, the index 0xf7 is masked to 0x7 when written to a 4-bit buffer (color or stencil). Color indexes and stencil indexes are always treated as indexes, never as components.

</dd> <dt>

<span id="opengl_iris_gl"></span><span id="OPENGL_IRIS_GL"></span>**IRIS GL**
</dt> <dd>

Silicon Graphics' proprietary graphics library, developed from 1982 through 1992. OpenGL was designed with IRIS GL as a starting point.

</dd> </dl>

 

 




