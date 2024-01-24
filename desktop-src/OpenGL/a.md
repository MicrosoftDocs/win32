---
title: A (OpenGL)
description: Definitions of OpenGL terms that begin with the letter A.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: e583610f-37da-47bb-bbd6-41d353b88244
keywords:
- aliasing
- alpha
- animation
- antialiasing
- application-specific clipping
ms.topic: article
ms.date: 05/31/2018
---

# A (OpenGL)

A [B](b.md) [C](c.md) [D](d.md) [E](e.md) [F](f.md) [G](g.md) [H](h.md) [I](i.md) [J K](jk.md) [L](l.md) [M](m.md) [N](n.md) [O](o.md) [P](p.md) [Q](q.md) [R](r.md) [S](s.md) [T](t.md) [U V](u-v.md) [W](w.md) [X Y Z](x-y-z.md)

<dl> <dt>

<span id="opengl_aliasing"></span><span id="OPENGL_ALIASING"></span>**aliasing**
</dt> <dd>

A rendering technique that assigns to pixels the color of the primitive being rendered, whether that primitive covers all or part of the pixel's area. Aliasing results in jagged edges, or jaggies. See also [jaggies](jk.md).

</dd> <dt>

<span id="opengl_alpha"></span><span id="OPENGL_ALPHA"></span>**alpha**
</dt> <dd>

A fourth color component typically used to control color blending. The alpha component is never displayed directly. By convention, OpenGL alpha indicates opacity and transparency on a scale of 0.0 to 1.0. An alpha value of 1.0 implies complete opacity, an alpha value of 0.0 implies complete transparency.

</dd> <dt>

<span id="opengl_animation"></span><span id="OPENGL_ANIMATION"></span>**animation**
</dt> <dd>

The generation of repeated renderings of a scene quickly enough, with smoothly changing viewpoint or object positions, that the illusion of motion is achieved. OpenGL animation almost always uses double-buffering.

</dd> <dt>

<span id="opengl_antialiasing"></span><span id="OPENGL_ANTIALIASING"></span>**antialiasing**
</dt> <dd>

A rendering technique that assigns colors to pixels based on the fraction of the pixel area that is covered by the primitive being rendered. Antialiased rendering reduces or eliminates the jaggies that result from aliased rendering. See also [jaggies](jk.md), [rendering](r.md).

</dd> <dt>

<span id="opengl_application_specific_clipping"></span><span id="OPENGL_APPLICATION_SPECIFIC_CLIPPING"></span>**application-specific clipping** 
</dt> <dd>

Clipping of primitives against planes in eye coordinates. The planes are specified by the application using [**glClipPlane**](glclipplane.md). See also [eye coordinates](e.md).

</dd> </dl>

 

 




