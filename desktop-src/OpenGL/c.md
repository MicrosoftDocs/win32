---
title: C (OpenGL)
description: Definitions of OpenGL terms that begin with the letter C.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 037c39b1-b728-41d3-a664-c0aa6c487103
keywords:
- client computers
- client memory
- clip coordinates
- clipping
- color index
- color-index mode
- color maps
- components
- contexts
- convex
- convex hull
- coordinate system
- culling
- current matrix
- current raster position
ms.topic: article
ms.date: 05/31/2018
---

# C (OpenGL)

[A](a.md) [B](b.md) C [D](d.md) [E](e.md) [F](f.md) [G](g.md) [H](h.md) [I](i.md) [J K](jk.md) [L](l.md) [M](m.md) [N](n.md) [O](o.md) [P](p.md) [Q](q.md) [R](r.md) [S](s.md) [T](t.md) [U V](u-v.md) [W](w.md) [X Y Z](x-y-z.md)

<dl> <dt>

<span id="opengl_client_computer"></span><span id="OPENGL_CLIENT_COMPUTER"></span>**client computer**
</dt> <dd>

The computer from which OpenGL commands are issued. The computer that issues OpenGL commands can be connected through a network to a different computer that executes the commands, or commands can be issued and executed on the same computer. See also [server](s.md).

</dd> <dt>

<span id="opengl_client_memory"></span><span id="OPENGL_CLIENT_MEMORY"></span>**client memory**
</dt> <dd>

The main memory (where program variables are stored) of the client computer.

</dd> <dt>

<span id="opengl_clip_coordinates"></span><span id="OPENGL_CLIP_COORDINATES"></span>**clip coordinates**
</dt> <dd>

The coordinate system that follows transformation by the projection matrix and precedes perspective division. View-volume clipping is done in clip coordinates, but application-specific clipping is not. See also [application-specific clipping](a.md).

</dd> <dt>

<span id="opengl_clipping"></span><span id="OPENGL_CLIPPING"></span>**clipping**
</dt> <dd>

Eliminating the portion of a geometric primitive that is outside the half-space defined by a clipping plane. Points are simply rejected if outside. The portion of a line or of a polygon that is outside the half-space is eliminated, and additional vertices are generated as necessary to complete the primitive within the clipping half-space. Geometric primitives and the current raster position (when specified) are always clipped against the six half-spaces defined by the left, right, bottom, top, near, and far planes of the view volume. Applications can specify optional application-specific clipping planes to be applied in eye coordinates.

</dd> <dt>

<span id="opengl_color_index"></span><span id="OPENGL_COLOR_INDEX"></span>**color index**
</dt> <dd>

A single value that represents a color by name, rather than by value. OpenGL color indexes are treated as continuous values (for example, floating-point numbers) while operations such as interpolation and dithering are performed on them. Color indexes stored in the frame buffer are always integer values, however. Floating-point indexes are converted to integers by rounding to the nearest integer value.

</dd> <dt>

<span id="opengl_color_index_mode"></span><span id="OPENGL_COLOR_INDEX_MODE"></span>**color-index mode**
</dt> <dd>

Mode of an OpenGL context in which its color buffers store color indexes, rather than red, green, blue, and alpha color components.

</dd> <dt>

<span id="opengl_color_map"></span><span id="OPENGL_COLOR_MAP"></span>**color map**
</dt> <dd>

A table of index-to-RGB mappings that is accessed by the display hardware. Each color index is read from the color buffer, converted to an RGB triple by lookup in the color map, and sent to the monitor.

</dd> <dt>

<span id="opengl_component"></span><span id="OPENGL_COMPONENT"></span>**component**
</dt> <dd>

A single, continuous (for example, floating-point) value that represents an intensity or quantity. Usually, a component value of zero represents the minimum value or intensity, and a component value of one represents the maximum value or intensity, though other normalizations are sometimes used. Because component values are interpreted in a normalized range, they are specified independently of actual resolution. For example, the RGB triple (1, 1, 1) is white, regardless of whether the color buffers store 4, 8, or 12 bits each. Out-of-range components are typically clamped to the normalized range, not truncated or otherwise interpreted. For example, the RGB triple (1.4, 1.5, 0.9) is clamped to (1.0, 1.0, 0.9) before it's used to update the color buffer. Red, green, blue, alpha, and depth are always treated as components, never as indexes.

</dd> <dt>

<span id="opengl_context"></span><span id="OPENGL_CONTEXT"></span>**context**
</dt> <dd>

A complete set of OpenGL state variables. Note that framebuffer contents are not part of the OpenGL state, but that the configuration of the framebuffer is.

</dd> <dt>

<span id="opengl_convex"></span><span id="OPENGL_CONVEX"></span>**convex**
</dt> <dd>

Condition of a polygon in which no straight line in the plane of the polygon intersects the polygon more than twice.

</dd> <dt>

<span id="opengl_convex_hull"></span><span id="OPENGL_CONVEX_HULL"></span>**convex hull**
</dt> <dd>

The smallest convex region enclosing a specified group of points. In two dimensions, the convex hull is found conceptually by stretching a rubber band around the points so that all of the points lie within the band.

</dd> <dt>

<span id="opengl_coordinate_system"></span><span id="OPENGL_COORDINATE_SYSTEM"></span>**coordinate system**
</dt> <dd>

In n-dimensional space, a set of n linearly independent vectors anchored to a point (called the origin). A group of coordinates specifies a point in spaceIn n-dimensional space, a set of n linearly independent vectors anchored to a point (called the origin). A group of coordinates specifies a point in space (or a vector from the origin) by indicating how far to travel along each vector to reach the point (or tip of the vector). (or a vector from the origin) by indicating how far to travel along each vector to reach the point (or tip of the vector).

</dd> <dt>

<span id="opengl_culling"></span><span id="OPENGL_CULLING"></span>**culling**
</dt> <dd>

The process of eliminating a front face or back face of a polygon so that the face isn't drawn.

</dd> <dt>

<span id="opengl_current_matrix"></span><span id="OPENGL_CURRENT_MATRIX"></span>**current matrix**
</dt> <dd>

A matrix that transforms coordinates in one coordinate system to coordinates of another system. There are three current matrices in OpenGL: the modelview matrix, which transforms object coordinates (coordinates specified by the programmer) to eye coordinates; the perspective matrix, which transforms eye coordinates to clip coordinates; and the texture matrix, which transforms specified or generated texture coordinates as described by the matrix. Each current matrix is the top element on a stack of matrices. Each of the three stacks can be manipulated with OpenGL matrix-manipulation commands.

</dd> <dt>

<span id="opengl_current_raster_position"></span><span id="OPENGL_CURRENT_RASTER_POSITION"></span>**current raster position**
</dt> <dd>

A window coordinate position that specifies the placement of an image primitive when it's rasterized. The current raster position, and other current raster parameters, are updated when glRasterpos is called.

</dd> </dl>

 

 




