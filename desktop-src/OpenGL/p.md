---
title: P (OpenGL)
description: Definitions of OpenGL terms that begin with the letter P.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 'bc7b0c93-af06-44a4-8bb8-adc0c6fedb6e'
keywords:
- parameters
- perspective division
- pixels
- points
- polygons
- primitives
- projection matrices
ms.topic: article
ms.date: 05/31/2018
---

# P (OpenGL)

[A](a.md) [B](b.md) [C](c.md) [D](d.md) [E](e.md) [F](f.md) [G](g.md) [H](h.md) [I](i.md) [J K](jk.md) [L](l.md) [M](m.md) [N](n.md) [O](o.md) P [Q](q.md) [R](r.md) [S](s.md) [T](t.md) [U V](u-v.md) [W](w.md) [X Y Z](x-y-z.md)

<dl> <dt>

<span id="opengl_parameter"></span><span id="OPENGL_PARAMETER"></span>**parameter**
</dt> <dd>

A value passed as an argument to an OpenGL command. Sometimes one of the values passed by reference to an OpenGL command.

</dd> <dt>

<span id="opengl_perspective_division"></span><span id="OPENGL_PERSPECTIVE_DIVISION"></span>**perspective division**
</dt> <dd>

The division of x, y, and z by w, carried out in clip coordinates. See also [clip coordinates](c.md).

</dd> <dt>

<span id="opengl_pixel"></span><span id="OPENGL_PIXEL"></span>**pixel**
</dt> <dd>

Picture element. The bits at location (x, y) of all the bitplanes in the framebuffer constitute the single pixel (x, y). In an image in client memory, a pixel is one group of elements. In OpenGL window coordinates, each pixel corresponds to a 1.0x1.0 screen area. The coordinates of the lower-left corner of the pixel names x, y are (x, y), and the upper-right corner are (x+1, y+1).

</dd> <dt>

<span id="opengl_point"></span><span id="OPENGL_POINT"></span>**point**
</dt> <dd>

An exact location in space, which is rendered as a finite-diameter dot.

</dd> <dt>

<span id="opengl_polygon"></span><span id="OPENGL_POLYGON"></span>**polygon**
</dt> <dd>

A near-planar surface bounded by edges specified by vertices. Each triangle of a triangle mesh is a polygon, as is each quadrilateral of a quadrilateral mesh. The rectangle specified by glRect is also a polygon.

</dd> <dt>

<span id="opengl_primitive"></span><span id="OPENGL_PRIMITIVE"></span>**primitive**
</dt> <dd>

A shape (such as a point, line, polygon, bitmap, or image) that can be drawn, stored, and manipulated as a discrete entity; elements from which large graphic designs are created.

</dd> <dt>

<span id="opengl_projection_matrix"></span><span id="OPENGL_PROJECTION_MATRIX"></span>**projection matrix**
</dt> <dd>

The 4x4 matrix that transforms points, lines, polygons, and raster positions from eye coordinates to clip coordinates.

</dd> </dl>

 

 




