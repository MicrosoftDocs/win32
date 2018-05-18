---
title: W
description: Definitions of OpenGL terms that begin with the letter W.
Robots: noindex, nofollow
ms.assetid: '59ac0414-a845-4f40-be9c-9962fd1585f6'
keywords: ["windows", "window-aligned", "window coordinates", "wireframe"]
---

# W

[A](a.md) [B](b.md) [C](c.md) [D](d.md) [E](e.md) [F](f.md) [G](g.md) [H](h.md) [I](i.md) [J K](jk.md) [L](l.md) [M](m.md) [N](n.md) [O](o.md) [P](p.md) [Q](q.md) [R](r.md) [S](s.md) [T](t.md) [U V](u-v.md) W [X Y Z](x-y-z.md)

<dl> <dt>

<span id="opengl_window"></span><span id="OPENGL_WINDOW"></span>**window**
</dt> <dd>

A subregion of the framebuffer, usually rectangular, whose pixels all have the same buffer configuration. An OpenGL context renders to one window at a time.

</dd> <dt>

<span id="opengl_window_aligned"></span><span id="OPENGL_WINDOW_ALIGNED"></span>**window-aligned**
</dt> <dd>

When referring to line segments or polygon edges, implies that these are parallel to the window boundaries. (In OpenGL, the window is rectangular, with horizontal and vertical edges). When referring to a polygon pattern, implies that the pattern is fixed relative to the window origin.

</dd> <dt>

<span id="opengl_window_coordinates"></span><span id="OPENGL_WINDOW_COORDINATES"></span>**window coordinates**
</dt> <dd>

The coordinate system of a window. It's important to distinguish between the names of pixels, which are discrete, and the window-coordinate system, which is continuous. For example, the pixel at the lower-left corner of a window is pixel (0, 0); the window coordinates of the center of this pixel are (0.5, 0.5, z). Note that window coordinates include a depth, or z, component, and that this component is continuous as well.

</dd> <dt>

<span id="opengl_wireframe"></span><span id="OPENGL_WIREFRAME"></span>**wireframe**
</dt> <dd>

A representation of an object that contains line segments only. Typically, the line segments indicate polygon edges.

</dd> </dl>

 

 




