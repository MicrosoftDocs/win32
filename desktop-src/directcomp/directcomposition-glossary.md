---
title: DirectComposition glossary
description: This topic defines Microsoft DirectComposition terms.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 3B9932EA-3182-41D0-B64A-7699EC98A714
ms.topic: article
ms.date: 05/31/2018
---

# DirectComposition glossary

> [!NOTE]
> For apps on Windows 10, we recommend using Windows.UI.Composition APIs instead of DirectComposition. For more info, see [Modernize your desktop app using the Visual layer](/windows/uwp/composition/visual-layer-in-desktop-apps).

This topic defines Microsoft DirectComposition terms.

<dl> <dt>

<span id="directcomp_glossary_animation_function"></span><span id="DIRECTCOMP_GLOSSARY_ANIMATION_FUNCTION"></span>**animation function**
</dt> <dd>

A construct that specifies how the value of a single object property changes over a period of time.

</dd> <dt>

<span id="directcomp_glossary_animation_object"></span><span id="DIRECTCOMP_GLOSSARY_ANIMATION_OBJECT"></span>**animation object**
</dt> <dd>

An object that represents a function for animating the properties of another object.

</dd> <dt>

<span id="directcomp_glossary_animation_primitive"></span><span id="DIRECTCOMP_GLOSSARY_ANIMATION_PRIMITIVE"></span>**animation segment**
</dt> <dd>

The fundamental timing definitions of an animation function; they are the primitives from which more complex and higher level animation functions are built.

</dd> <dt>

<span id="directcomp_glossary_back_buffer"></span><span id="DIRECTCOMP_GLOSSARY_BACK_BUFFER"></span>**back buffer**
</dt> <dd>

A rectangle of memory that an application can directly write to. The back buffer is never directly displayed on the monitor.

</dd> <dt>

<span id="directcomp_glossary_batch"></span><span id="DIRECTCOMP_GLOSSARY_BATCH"></span>**batch**
</dt> <dd>

A group of DirectComposition method calls that are processed atomically.

</dd> <dt>

<span id="directcomp_glossary_bitmap"></span><span id="DIRECTCOMP_GLOSSARY_BITMAP"></span>**bitmap**
</dt> <dd>

A color buffer, either with or without an alpha channel, that resides in system or video memory.

</dd> <dt>

<span id="directcomp_glossary_border_mode"></span><span id="DIRECTCOMP_GLOSSARY_BORDER_MODE"></span>**border mode**
</dt> <dd>

A property of a Microsoft DirectComposition visual that affects how the edges of a bitmap are composed when the bitmap is transformed such that the edges are not axis-aligned with integer coordinates. It also affects how content is clipped at the corners of a clip that has rounded corners, and at the edge of a clip that is transformed such that the edges are not axis-aligned with integer coordinates.

</dd> <dt>

<span id="directcomp_glossary_clip_object"></span><span id="DIRECTCOMP_GLOSSARY_CLIP_OBJECT"></span>**clip object**
</dt> <dd>

A object that represents a clip rectangle.

</dd> <dt>

<span id="directcomp_glossary_clip_rectangle"></span><span id="DIRECTCOMP_GLOSSARY_CLIP_RECTANGLE"></span>**clip rectangle**
</dt> <dd>

A set of coordinates that define the area of visual's bitmap content that is drawn on the screen when the bitmap is rendered.

</dd> <dt>

<span id="directcomp_glossary_cloak"></span><span id="DIRECTCOMP_GLOSSARY_CLOAK"></span>**cloak**
</dt> <dd>

To temporarily prevent Desktop Window Manager (DWM) from drawing a window to the display. Applications typically cloak a window while DirectComposition uses the window's bitmap in a composition.

</dd> <dt>

<span id="directcomp_glossary_commit"></span><span id="DIRECTCOMP_GLOSSARY_COMMIT"></span>**commit**
</dt> <dd>

To submit a batch of commands to DirectCompositionDirectComposition for processing.

</dd> <dt>

<span id="directcomp_glossary_composite_mode"></span><span id="DIRECTCOMP_GLOSSARY_COMPOSITE_MODE"></span>**composite mode**
</dt> <dd>

One of several ways of blending two bitmaps (a source and a destination) to achieve a particular effect.

</dd> <dt>

<span id="directcomp_glossary_composition"></span><span id="DIRECTCOMP_GLOSSARY_COMPOSITION"></span>**composition**
</dt> <dd>

A collection of bitmaps that are combined and manipulated by applying various transforms, effects, and animations to produce an intended visual result in an application UI.

</dd> <dt>

<span id="directcomp_glossary_composition_target_window"></span><span id="DIRECTCOMP_GLOSSARY_COMPOSITION_TARGET_WINDOW"></span>**composition target window**
</dt> <dd>

The window to which a visual tree is bound, and in which the resulting composition is drawn.

</dd> <dt>

<span id="directcomp_glossary_effect"></span><span id="DIRECTCOMP_GLOSSARY_EFFECT"></span>**effect**
</dt> <dd>

An operation that modifies how the bitmaps of a visual tree are rasterized, typically by applying a pixel shader.

</dd> <dt>

<span id="directcomp_glossary_effect_group"></span><span id="DIRECTCOMP_GLOSSARY_EFFECT_GROUP"></span>**effect group**
</dt> <dd>

A group of bitmap effects that are applied together to modify the rasterization of a visual’s sub-tree.

</dd> <dt>

<span id="directcomp_glossary_frame"></span><span id="DIRECTCOMP_GLOSSARY_FRAME"></span>**frame**
</dt> <dd>

An iteration of the composition engine that produces a rasterization of the visual tree.

</dd> <dt>

<span id="directcomp_glossary_front_buffer"></span><span id="DIRECTCOMP_GLOSSARY_FRONT_BUFFER"></span>**front buffer**
</dt> <dd>

A rectangle of memory that is translated by the graphics adapter and displayed on the monitor.

</dd> <dt>

<span id="directcomp_glossary_interpolation_mode"></span><span id="DIRECTCOMP_GLOSSARY_INTERPOLATION_MODE"></span>**interpolation mode**
</dt> <dd>

A property that determines how a bitmap is composed when it is transformed such that there is no one-to-one correspondence between pixels in the bitmap and pixels on the screen.

</dd> <dt>

<span id="directcomp_glossary_root_visual"></span><span id="DIRECTCOMP_GLOSSARY_ROOT_VISUAL"></span>**root visual**
</dt> <dd>

The visual from which all other visuals in a visual tree are descended.

</dd> <dt>

<span id="directcomp_glossary_swap_chain"></span><span id="DIRECTCOMP_GLOSSARY_SWAP_CHAIN"></span>**swap chain**
</dt> <dd>

A collection of one or more back buffers that can be serially presented to the front buffer

</dd> <dt>

<span id="directcomp_glossary_surface"></span><span id="DIRECTCOMP_GLOSSARY_SURFACE"></span>**surface**
</dt> <dd>

A representation of a linear area of display memory that usually resides in the display memory of the display card, although surfaces can exist in system memory.

</dd> <dt>

<span id="directcomp_glossary_transform"></span><span id="DIRECTCOMP_GLOSSARY_TRANSFORM"></span>**transform**
</dt> <dd>

A matrix that represents a coordinate transformation in either two-dimensional or three-dimensional space.

</dd> <dt>

<span id="directcomp_glossary_transform_group"></span><span id="DIRECTCOMP_GLOSSARY_TRANSFORM_GROUP"></span>**transform group**
</dt> <dd>

A collection of transforms whose matrices are multiplied together in the order in which they are specified in the collection before they are applied to a visual.

</dd> <dt>

<span id="directcomp_glossary_visual"></span><span id="DIRECTCOMP_GLOSSARY_VISUAL"></span>**visual**
</dt> <dd>

An object that contains an optional reference to a bitmap object, and a set of properties that determine where and how the bitmap is rendered to the screen.

</dd> <dt>

<span id="directcomp_glossary_visual_object"></span><span id="DIRECTCOMP_GLOSSARY_VISUAL_OBJECT"></span>**visual object**
</dt> <dd>

See [*visual*](/windows).

</dd> <dt>

<span id="directcomp_glossary_visual_subtree"></span><span id="DIRECTCOMP_GLOSSARY_VISUAL_SUBTREE"></span>**visual subtree**
</dt> <dd>

A portion of a visual tree consisting of a particular visual and all of its child and descendent visuals.

</dd> <dt>

<span id="directcomp_glossary_visual_tree"></span><span id="DIRECTCOMP_GLOSSARY_VISUAL_TREE"></span>**visual tree**
</dt> <dd>

A hierarchical collection of visuals used to create a composition.

</dd> <dt>

<span id="directcomp_glossary_windowless_swap_chain"></span><span id="DIRECTCOMP_GLOSSARY_WINDOWLESS_SWAP_CHAIN"></span>**windowless swap chain**
</dt> <dd>

A swap chain that is associated with a DirectComposition visual object instead of a window.

</dd> </dl>

 

 