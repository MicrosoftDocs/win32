---
title: Direct2D Glossary
description: Describes terms commonly used by the Direct2D documentation.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 2e884390-56e4-45ae-b1c9-c58503d6f2dd
ms.topic: article
ms.date: 05/31/2018
---

# Direct2D Glossary

<dl> <dt>

<span id="direct2d.direct2d_glossary_a8_target"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_A8_TARGET"></span>**A8 target**
</dt> <dd>

A render target that uses a pixel format representing an alpha channel with eight bits. A8 targets are useful for drawing geometries as masks.

</dd> <dt>

<span id="direct2d.direct2d_glossary_aliasing"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_ALIASING"></span>**aliasing**
</dt> <dd>

In computer graphics, the jagged appearance of curves or diagonal lines. Aliasing is most visible at lower resolutions.

</dd> <dt>

<span id="direct2d.direct2d_glossary_antialiasing"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_ANTIALIASING"></span>**antialiasing**
</dt> <dd>

A technique for smoothing the jagged appearance of curved or diagonal lines. Methods of antialiasing include surrounding pixels with intermediate shades and manipulating the size and horizontal alignment of the pixels.

</dd> <dt>

<span id="direct2d.direct2d_glossary_batch"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_BATCH"></span>**batch**
</dt> <dd>

A set of requests or transactions that have been grouped together.

</dd> <dt>

<span id="direct2d.direct2d_glossary_bitmap"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_BITMAP"></span>**bitmap**
</dt> <dd>

A representation of characters or graphics by individual pixels. The pixels can be arranged horizontally, in rows, or vertically, in columns. Each pixel can be represented by one or more bits.

</dd> <dt>

<span id="direct2d.direct2d_glossary_bits_per_pixel__bpp_"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_BITS_PER_PIXEL__BPP_"></span>**bits per pixel (bpp)**
</dt> <dd>

The number of bits that are used to store and display the color data for a single pixel. This is the standard unit of measurement for bit depth (also called color depth). Common bit depths include 8, 16, and 32.

</dd> <dt>

<span id="direct2d.direct2d_glossary_brush"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_BRUSH"></span>**brush**
</dt> <dd>

A Direct2D resource that paints an infinite plane with a solid color, a gradient, or a bitmap. A brush is typically used to stroke and fill a geometry.

</dd> <dt>

<span id="direct2d.direct2d_glossary_cleartype"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_CLEARTYPE"></span>**ClearType**
</dt> <dd>

A font display technology that dramatically improves font display resolution, such that letters on the computer screen appear smooth, not jagged. ClearType improves text appearance on LCD monitors that have a digital interface, such as laptop monitors and high-quality flat-panel desktop monitors.

</dd> <dt>

<span id="direct2d.direct2d_glossary_dc"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_DC"></span>**DC**
</dt> <dd>

See definition for: device context.

</dd> <dt>

<span id="direct2d.direct2d_glossary_device_context__dc_"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_DEVICE_CONTEXT__DC_"></span>**device context (DC)**
</dt> <dd>

A GDI device context. See also: Graphics Device Interface.

</dd> <dt>

<span id="direct2d.direct2d_glossary_direct2d"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_DIRECT2D"></span>**Direct2D**
</dt> <dd>

A hardware-accelerated, immediate-mode 2-D rendering API.

</dd> <dt>

<span id="direct2d.direct2d_glossary_direct3d"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_DIRECT3D"></span>**Direct3D**
</dt> <dd>

The hardware acceleration platform and runtime for 3-D graphics in Windows.

</dd> <dt>

<span id="direct2d.direct2d_glossary_directwrite"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_DIRECTWRITE"></span>**DirectWrite**
</dt> <dd>

A text API that provides text rendering, font management, and text layout support that is independent of any specific rendering system.

</dd> <dt>

<span id="direct2d.direct2d_glossary_directx_graphics_infrastructure__dxgi_"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_DIRECTX_GRAPHICS_INFRASTRUCTURE__DXGI_"></span>**DirectX Graphics Infrastructure (DXGI)**
</dt> <dd>

The infrastructure that manages the low-level graphics-related tasks that are independent of the DirectX graphics runtime. DXGI provides a common framework for graphics components.

</dd> <dt>

<span id="direct2d.direct2d_glossary_dxgi"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_DXGI"></span>**DXGI**
</dt> <dd>

See definition for: DirectX Graphics Infrastructure (DXGI).

</dd> <dt>

<span id="direct2d.direct2d_glossary_figure"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_FIGURE"></span>**figure**
</dt> <dd>

An open or closed shape defined by a start point and a collection of segments.

</dd> <dt>

<span id="direct2d.direct2d_glossary_flatten"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_FLATTEN"></span>**flatten**
</dt> <dd>

To generate a polygonal approximation of a (potentially curved) geometry.

</dd> <dt>

<span id="direct2d.direct2d_glossary_gdi"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_GDI"></span>**GDI**
</dt> <dd>

See definition for: Graphics Device Interface (GDI).

</dd> <dt>

<span id="direct2d.direct2d_glossary_geometric_mask"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_GEOMETRIC_MASK"></span>**geometric mask**
</dt> <dd>

A clip or a cutout, defined by an ID2D1Geometry object, that masks a layer when it is drawn by a render target. A geometric mask can be either aliased or have sub-pixel edges.

</dd> <dt>

<span id="direct2d.direct2d_glossary_geometry_transform"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_GEOMETRY_TRANSFORM"></span>**geometry transform**
</dt> <dd>

A transform that is applied to a geometry before it is stroked or filled.

</dd> <dt>

<span id="direct2d.direct2d_glossary_glyph"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_GLYPH"></span>**glyph**
</dt> <dd>

A graphical representation of a character, part of a character, or sequence of characters.

</dd> <dt>

<span id="direct2d.direct2d_glossary_glyph_run"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_GLYPH_RUN"></span>**glyph run**
</dt> <dd>

A continuous run of glyphs that share a common format.

</dd> <dt>

<span id="direct2d.direct2d_glossary_gradient_brush"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_GRADIENT_BRUSH"></span>**gradient brush**
</dt> <dd>

A brush that paints an area in a gradual progression from one color to another or from one shade to another shade of the same color.

</dd> <dt>

<span id="direct2d.direct2d_glossary_gradient_stop"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_GRADIENT_STOP"></span>**gradient stop**
</dt> <dd>

A specific color that is defined for a location within the gradient region. Gradient stops are used to define the color at specific locations along the gradient path.

</dd> <dt>

<span id="direct2d.direct2d_glossary_grahics_primitive"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_GRAHICS_PRIMITIVE"></span>**grahics primitive**
</dt> <dd>

In computer graphics, a shape such as a line, circle, curve, or polygon that a graphics adapter can draw, store, and manipulate as a discrete entity.

</dd> <dt>

<span id="direct2d.direct2d_glossary_graphics_device_interface__gdi_"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_GRAPHICS_DEVICE_INTERFACE__GDI_"></span>**Graphics Device Interface (GDI)**
</dt> <dd>

A graphics API that enables applications to send graphics commands to a display or printing device, generally without consideration for its specifications or capabilities. A Microsoft Win32 GDI receives rendering requests from applications and passes those requests to the kernel-mode GDI.

</dd> <dt>

<span id="direct2d.direct2d_glossary_handle_to_a_device_context__hdc_"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_HANDLE_TO_A_DEVICE_CONTEXT__HDC_"></span>**handle to a device context (HDC)**
</dt> <dd>

A reference to a GDI device context.

</dd> <dt>

<span id="direct2d.direct2d_glossary_hdc"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_HDC"></span>**HDC**
</dt> <dd>

See definition for: handle to a device context.

</dd> <dt>

<span id="direct2d.direct2d_glossary_mesh"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_MESH"></span>**mesh**
</dt> <dd>

A collection of vertices that define a set of triangles that constitute a shape.

</dd> <dt>

<span id="direct2d.direct2d_glossary_multi-sample_anti-aliasing__msaa_"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_MULTI-SAMPLE_ANTI-ALIASING__MSAA_"></span>**Multi-Sample Anti-Aliasing (MSAA)**
</dt> <dd>

An antialiasing technique that processes an entire scene.

</dd> <dt>

<span id="direct2d.direct2d_glossary_opacity_mask"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_OPACITY_MASK"></span>**opacity mask**
</dt> <dd>

A mask, described by a brush or bitmap, that is applied to another object to make that object partially or completely transparent. An opacity mask uses alpha channel information to specify how the source pixels of the object are blended into the final destination target. The transparent portions of the mask indicate the areas where the underlying image is hidden, whereas the opaque portions of the mask indicate where the masked object is allowed.

</dd> <dt>

<span id="direct2d.direct2d_glossary_per_primitive_anti-aliasing__ppaa_"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_PER_PRIMITIVE_ANTI-ALIASING__PPAA_"></span>**Per Primitive Anti-Aliasing (PPAA)**
</dt> <dd>

An antialiasing technique that is applied to each individual graphics primitive rather than an entire scene.

</dd> <dt>

<span id="direct2d.direct2d_glossary_radial_gradient_brush"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_RADIAL_GRADIENT_BRUSH"></span>**radial gradient brush**
</dt> <dd>

A gradient where the start point is defined by a focal point and the end point is defined by a gradient.

</dd> <dt>

<span id="direct2d.direct2d_glossary_render_target"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_RENDER_TARGET"></span>**render target**
</dt> <dd>

A Direct2D resource that issues drawing commands. There are different types of render targets, each rendering to a different destination. For example, an ID2D1HwndRenderTarget renders to a window, and an ID2D1BitmapRenderTarget renders to a bitmap.

</dd> <dt>

<span id="direct2d.direct2d_glossary_segment"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_SEGMENT"></span>**segment**
</dt> <dd>

A portion of a geometric path, defined by the start and end points.

</dd> <dt>

<span id="direct2d.direct2d_glossary_tessellate"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_TESSELLATE"></span>**tessellate**
</dt> <dd>

To break a shape into a collection of triangles.

</dd> <dt>

<span id="direct2d.direct2d_glossary_transform"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_TRANSFORM"></span>**transform**
</dt> <dd>

A matrix that represents a linear mapping in a number of dimensions. Direct2D uses a 2-by-3 matrix, which limits the API to those deformations that are affine.

</dd> <dt>

<span id="direct2d.direct2d_glossary_translation"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_TRANSLATION"></span>**translation**
</dt> <dd>

The process of using a transformation matrix to move an object.

</dd> <dt>

<span id="direct2d.direct2d_glossary_vertex"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_VERTEX"></span>**vertex**
</dt> <dd>

The highest point of a curve, the point where a curve ends, or the point where two segments meet in a polygon or a freeform path.

</dd> <dt>

<span id="direct2d.direct2d_glossary_vertex_shader"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_VERTEX_SHADER"></span>**vertex shader**
</dt> <dd>

A type of programmable shader that contains a set of assembly instructions that are run on the GPU per vertex and per pixel for the current draw call. A vertex shader offloads intensive calculations from CPU to GPU.

</dd> <dt>

<span id="direct2d.direct2d_glossary_windows_imaging_component__wic_"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_WINDOWS_IMAGING_COMPONENT__WIC_"></span>**Windows Imaging Component (WIC)**
</dt> <dd>

An API that enables applications to (1) display and edit any image format for which a WIC-compliant CODEC is installed, and to (2) read and write metadata or image files.

</dd> <dt>

<span id="direct2d.direct2d_glossary_xml_paper_specification__xps_"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_XML_PAPER_SPECIFICATION__XPS_"></span>**XML Paper Specification (XPS)**
</dt> <dd>

A document format, described by the XML Paper Specification, that can be used to store documents, to process them for printing, and to print them.

</dd> <dt>

<span id="direct2d.direct2d_glossary_xps"></span><span id="DIRECT2D.DIRECT2D_GLOSSARY_XPS"></span>**XPS**
</dt> <dd>

See definition for: XML Paper Specification (XPS).

</dd> </dl>

 

 




