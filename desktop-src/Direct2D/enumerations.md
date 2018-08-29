---
title: Enumerations
description: Direct2D defines the following enumerations.
ms.assetid: 1491f241-5b67-4883-9ee9-d934a3a66e73
keywords:
- Direct2D,enumerations
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enumerations

Direct2D defines the following enumerations.

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_2daffinetransform_interpolation_mode"><strong>D2D1_2DAFFINETRANSFORM_INTERPOLATION_MODE</strong></a><br/></td>
<td>The interpolation mode to be used with the 2D affine transform effect to scale the image. There are 6 scale modes that range in quality and speed.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_2daffinetransform_prop"><strong>D2D1_2DAFFINETRANSFORM_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="2d-affine-transform">2D affine transform effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_3dperspectivetransform_interpolation_mode"><strong>D2D1_3DPERSPECTIVETRANSFORM_INTERPOLATION_MODE</strong></a><br/></td>
<td>The interpolation mode the <a href="3d-perspective-transform">3D perspective transform effect</a> uses on the image. There are 5 scale modes that range in quality and speed. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_3dperspectivetransform_prop"><strong>D2D1_3DPERSPECTIVETRANSFORM_PROP</strong></a><br/></td>
<td>Identifiers for the properties of the <a href="3d-perspective-transform">3D perspective transform effect</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_3dtransform_interpolation_mode"><strong>D2D1_3DTRANSFORM_INTERPOLATION_MODE</strong></a><br/></td>
<td>The interpolation mode the <a href="3d-transform">3D transform effect</a> uses on the image. There are 5 scale modes that range in quality and speed. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_3dtransform_prop"><strong>D2D1_3DTRANSFORM_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="3d-transform">3D transform effect</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/dcommon/ne-dcommon-d2d1_alpha_mode"><strong>D2D1_ALPHA_MODE</strong></a><br/></td>
<td>Specifies how the alpha value of a bitmap or render target should be treated.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_antialias_mode"><strong>D2D1_ANTIALIAS_MODE</strong></a><br/></td>
<td>Specifies how the edges of nontext primitives are rendered.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_arc_size"><strong>D2D1_ARC_SIZE</strong></a><br/></td>
<td>Specifies whether an arc should be greater than 180 degrees.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_arithmeticcomposite_prop"><strong>D2D1_ARITHMETICCOMPOSITE_PROP</strong></a><br/></td>
<td>Identifiers for the properties of the <a href="arithmetic-composite">Arithmetic composite effect</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_atlas_prop"><strong>D2D1_ATLAS_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="atlas">Atlas effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_bitmapsource_alpha_mode"><strong>D2D1_BITMAPSOURCE_ALPHA_MODE</strong></a><br/></td>
<td>Specifies the alpha mode of the output of the <a href="bitmap-source">Bitmap source effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_bitmapsource_interpolation_mode"><strong>D2D1_BITMAPSOURCE_INTERPOLATION_MODE</strong></a><br/></td>
<td>The interpolation mode used to scale the image in the <a href="bitmap-source">Bitmap source effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_bitmapsource_orientation"><strong>D2D1_BITMAPSOURCE_ORIENTATION</strong></a><br/></td>
<td>Speficies whether a flip and/or rotation operation should be performed by the <a href="bitmap-source">Bitmap source effect</a><br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_bitmapsource_prop"><strong>D2D1_BITMAPSOURCE_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="bitmap-source">Bitmap source effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_bitmap_interpolation_mode"><strong>D2D1_BITMAP_INTERPOLATION_MODE</strong></a><br/></td>
<td>Specifies the algorithm that is used when images are scaled or rotated.<br/>
<blockquote>
[!Note]<br />
Starting in Windows 8, more interpolations modes are available. See <a href="https://msdn.microsoft.com/library/windows/desktop/hh447004"><strong>D2D1_INTERPOLATION_MODE</strong></a> for more info.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/D2d1_1/ne-d2d1_1-d2d1_bitmap_options"><strong>D2D1_BITMAP_OPTIONS</strong></a><br/></td>
<td>Specifies how a bitmap can be used.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effectauthor/ne-d2d1effectauthor-d2d1_blend"><strong>D2D1_BLEND</strong></a><br/></td>
<td>Specifies how one of the color sources is to be derived and optionally specifies a preblend operation on the color source.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_blend_mode"><strong>D2D1_BLEND_MODE</strong></a><br/></td>
<td>The blend mode used for the <a href="blend">Blend effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/D2d1effectauthor/ne-d2d1effectauthor-d2d1_blend_operation"><strong>D2D1_BLEND_OPERATION</strong></a><br/></td>
<td>Specifies the blend operation on two color sources.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_blend_prop"><strong>D2D1_BLEND_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="blend">Blend effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_border_edge_mode"><strong>D2D1_BORDER_EDGE_MODE</strong></a><br/></td>
<td>The edge mode for the <a href="border">Border effect</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_border_mode"><strong>D2D1_BORDER_MODE</strong></a><br/></td>
<td>Specifies how the <a href="crop">Crop effect</a> handles the crop rectangle falling on fractional pixel coordinates. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_border_prop"><strong>D2D1_BORDER_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="border">Border effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_brightness_prop"><strong>D2D1_BRIGHTNESS_PROP</strong></a><br/></td>
<td>Identifiers for the properties of the <a href="brightness">Brightness effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/D2d1_1/ne-d2d1_1-d2d1_buffer_precision"><strong>D2D1_BUFFER_PRECISION</strong></a><br/></td>
<td>Represents the bit depth of the imaging pipeline in Direct2D.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_cap_style"><strong>D2D1_CAP_STYLE</strong></a><br/></td>
<td>Describes the shape at the end of a line or segment.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/D2d1effectauthor/ne-d2d1effectauthor-d2d1_change_type"><strong>D2D1_CHANGE_TYPE</strong></a><br/></td>
<td>Describes flags that influence how the renderer interacts with a custom vertex shader.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effectauthor/ne-d2d1effectauthor-d2d1_channel_depth"><strong>D2D1_CHANNEL_DEPTH</strong></a><br/></td>
<td>Allows a caller to control the channel depth of a stage in the rendering pipeline.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_channel_selector"><strong>D2D1_CHANNEL_SELECTOR</strong></a><br/></td>
<td>Specifies the color channel the <a href="displacement-map">Displacement map effect</a> extracts the intensity from and uses it to spatially displace the image in the X or Y direction.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_chromakey_prop"><strong>D2D1_CHROMAKEY_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="chromakey-effect">Chroma-key effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_colormanagement_alpha_mode"><strong>D2D1_COLORMANAGEMENT_ALPHA_MODE</strong></a><br/></td>
<td>Indicates how the <a href="color-management">Color management effect</a> should interpret alpha data that is contained in the input image. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_colormanagement_prop"><strong>D2D1_COLORMANAGEMENT_PROP</strong></a><br/></td>
<td>Identifiers for the properties of the <a href="color-management">Color management effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_colormanagement_quality"><strong>D2D1_COLORMANAGEMENT_QUALITY</strong></a><br/></td>
<td>The quality level of the transform for the <a href="color-management">Color management effect</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_colormanagement_rendering_intent"><strong>D2D1_COLORMANAGEMENT_RENDERING_INTENT</strong></a><br/></td>
<td>Specifies which ICC rendering intent the <a href="color-management">Color management effect</a> should use.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_colormatrix_alpha_mode"><strong>D2D1_COLORMATRIX_ALPHA_MODE</strong></a><br/></td>
<td>The alpha mode of the output of the <a href="color-matrix">Color matrix effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_colormatrix_prop"><strong>D2D1_COLORMATRIX_PROP</strong></a><br/></td>
<td>Identifiers for the properties of the <a href="color-matrix">Color matrix effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1_3/ne-d2d1_3-d2d1_color_bitmap_glyph_snap_option"><strong>D2D1_COLOR_BITMAP_GLYPH_SNAP_OPTION</strong></a><br/></td>
<td>Specifies the pixel snapping policy when rendering color bitmap glyphs.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1_3/ne-d2d1_3-d2d1_color_context_type"><strong>D2D1_COLOR_CONTEXT_TYPE</strong></a><br/></td>
<td>Specifies which way a color profile is defined.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/D2d1_1/ne-d2d1_1-d2d1_color_space"><strong>D2D1_COLOR_SPACE</strong></a><br/></td>
<td>Defines options that should be applied to the color space.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1_1/ne-d2d1_1-d2d1_color_interpolation_mode"><strong>D2D1_COLOR_INTERPOLATION_MODE</strong></a><br/></td>
<td>Defines how to interpolate between colors.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_combine_mode"><strong>D2D1_COMBINE_MODE</strong></a><br/></td>
<td>Specifies the different methods by which two geometries can be combined.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_compatible_render_target_options"><strong>D2D1_COMPATIBLE_RENDER_TARGET_OPTIONS</strong></a><br/></td>
<td>Specifies additional features supportable by a compatible render target when it is created. This enumeration allows a bitwise combination of its member values.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/D2d1_1/ne-d2d1_1-d2d1_composite_mode"><strong>D2D1_COMPOSITE_MODE</strong></a><br/></td>
<td>Used to specify the blend mode for all of the Direct2D blending operations.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_composite_prop"><strong>D2D1_COMPOSITE_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="composite">Composite effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_contrast_prop"><strong>D2D1_CONTRAST_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="contrast-effect">Contrast effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_convolvematrix_prop"><strong>D2D1_CONVOLVEMATRIX_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="convolve-matrix">Convolve matrix effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_convolvematrix_scale_mode"><strong>D2D1_CONVOLVEMATRIX_SCALE_MODE</strong></a><br/></td>
<td>The interpolation mode the <a href="convolve-matrix">Convolve matrix effect</a> uses to scale the image to the corresponding kernel unit length. There are six scale modes that range in quality and speed.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_crop_prop"><strong>D2D1_CROP_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="crop">Crop effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_dash_style"><strong>D2D1_DASH_STYLE</strong></a><br/></td>
<td>Describes the sequence of dashes and gaps in a stroke. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_dc_initialize_mode"><strong>D2D1_DC_INITIALIZE_MODE</strong></a><br/></td>
<td>Specifies how a device context is initialized for GDI rendering when it is retrieved from the render target.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_debug_level"><strong>D2D1_DEBUG_LEVEL</strong></a><br/></td>
<td>Indicates the type of information provided by the <a href="direct2ddebuglayer-overview">Direct2D Debug Layer</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/D2d1_1/ne-d2d1_1-d2d1_device_context_options"><strong>D2D1_DEVICE_CONTEXT_OPTIONS</strong></a><br/></td>
<td>This specifies options that apply to the device context for its lifetime.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_directionalblur_optimization"><strong>D2D1_DIRECTIONALBLUR_OPTIMIZATION</strong></a><br/></td>
<td>Specifies the optimization mode for the <a href="directional-blur">Directional blur effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_directionalblur_prop"><strong>D2D1_DIRECTIONALBLUR_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="directional-blur">Directional blur effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_discretetransfer_prop"><strong>D2D1_DISCRETETRANSFER_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="discrete-transfer">Discrete transfer effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_displacementmap_prop"><strong>D2D1_DISPLACEMENTMAP_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="displacement-map">Displacement map effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_distantdiffuse_prop"><strong>D2D1_DISTANTDIFFUSE_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="distant-diffuse">Distant-diffuse lighting effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_distantdiffuse_scale_mode"><strong>D2D1_DISTANTDIFFUSE_SCALE_MODE</strong></a><br/></td>
<td>The interpolation mode the effect uses to scale the image to the corresponding kernel unit length. There are six scale modes that range in quality and speed.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_distantspecular_prop"><strong>D2D1_DISTANTSPECULAR_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="distant-specular">Distant-specular lighting effect</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_distantspecular_scale_mode"><strong>D2D1_DISTANTSPECULAR_SCALE_MODE</strong></a><br/></td>
<td>The interpolation mode the <a href="distant-specular">Distant-specular lighting effect</a> uses to scale the image to the corresponding kernel unit length. There are six scale modes that range in quality and speed.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_dpicompensation_interpolation_mode"><strong>D2D1_DPICOMPENSATION_INTERPOLATION_MODE</strong></a><br/></td>
<td>The interpolation mode the <a href="dpi-compensation">DPI compensation effect</a> uses to scale the image. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_dpicompensation_prop"><strong>D2D1_DPICOMPENSATION_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="dpi-compensation">DPI compensation effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_draw_text_options"><strong>D2D1_DRAW_TEXT_OPTIONS</strong></a><br/></td>
<td>Specifies whether text snapping is suppressed or clipping to the layout rectangle is enabled. This enumeration allows a bitwise combination of its member values.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_edgedetection_mode"><strong>D2D1_EDGEDETECTION_MODE</strong></a><br/></td>
<td>Values for the <a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_edgedetection_prop"><strong>D2D1_EDGEDETECTION_PROP_MODE</strong></a> property of the <a href="edge-detection-effect">Edge Detection effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_edgedetection_prop"><strong>D2D1_EDGEDETECTION_PROP</strong></a><br/></td>
<td>Identifiers for properties of the Edge Detection effect.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_emboss_prop"><strong>D2D1_EMBOSS_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="emboss-effect">Emboss effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_exposure_prop"><strong>D2D1_EXPOSURE_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="exposure-effect">Exposure effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_extend_mode"><strong>D2D1_EXTEND_MODE</strong></a><br/></td>
<td>Specifies how a brush paints areas outside of its normal content area.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_factory_type"><strong>D2D1_FACTORY_TYPE</strong></a><br/></td>
<td>Specifies whether Direct2D provides synchronization for an <a href="https://msdn.microsoft.com/en-us/library/Dd371246(v=VS.85).aspx"><strong>ID2D1Factory</strong></a> and the resources it creates, so that they may be safely accessed from multiple threads. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/D2d1effectauthor/ne-d2d1effectauthor-d2d1_feature"><strong>D2D1_FEATURE</strong></a><br/></td>
<td>Defines capabilities of the underlying Direct3D device which may be queried using <a href="https://msdn.microsoft.com/en-us/library/Hh871455(v=VS.85).aspx"><strong>ID2D1EffectContext::CheckFeatureSupport</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_feature_level"><strong>D2D1_FEATURE_LEVEL</strong></a><br/></td>
<td>Describes the minimum DirectX support required for hardware rendering by a render target.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_figure_begin"><strong>D2D1_FIGURE_BEGIN</strong></a><br/></td>
<td>Indicates whether a specific <a href="https://msdn.microsoft.com/en-us/library/Dd316919(v=VS.85).aspx"><strong>ID2D1SimplifiedGeometrySink</strong></a> figure is filled or hollow. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_figure_end"><strong>D2D1_FIGURE_END</strong></a><br/></td>
<td>Indicates whether a specific <a href="https://msdn.microsoft.com/en-us/library/Dd316919(v=VS.85).aspx"><strong>ID2D1SimplifiedGeometrySink</strong></a> figure is open or closed. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_fill_mode"><strong>D2D1_FILL_MODE</strong></a><br/></td>
<td>Specifies how the intersecting areas of geometries or figures are combined to form the area of the composite geometry. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/D2d1effectauthor/ne-d2d1effectauthor-d2d1_filter"><strong>D2D1_FILTER</strong></a><br/></td>
<td>Represents filtering modes that a transform may select to use on input textures.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_flood_prop"><strong>D2D1_FLOOD_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="flood">Flood effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_gamma"><strong>D2D1_GAMMA</strong></a><br/></td>
<td>Specifies which gamma is used for interpolation.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1_3/ne-d2d1_3-d2d1_gamma1"><strong>D2D1_GAMMA1</strong></a><br/></td>
<td>Determines what gamma is used for interpolation and blending.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_gammatransfer_prop"><strong>D2D1_GAMMATRANSFER_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="gamma-transfer">Gamma transfer effect</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_gaussianblur_optimization"><strong>D2D1_GAUSSIANBLUR_OPTIMIZATION</strong></a><br/></td>
<td>The optimization mode for the <a href="gaussian-blur">Gaussian blur effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_gaussianblur_prop"><strong>D2D1_GAUSSIANBLUR_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="gaussian-blur">Gaussian blur effect</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/en-us/library/Hh447002(v=VS.85).aspx"><strong>D2D1_GAMMA_CONVERSION</strong></a><br/></td>
<td>Defines the conversion between color spaces.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_geometry_relation"><strong>D2D1_GEOMETRY_RELATION</strong></a><br/></td>
<td>Describes how one geometry object is spatially related to another geometry object. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_geometry_simplification_option"><strong>D2D1_GEOMETRY_SIMPLIFICATION_OPTION</strong></a><br/></td>
<td>Specifies how a geometry is simplified to an <a href="https://msdn.microsoft.com/en-us/library/Dd316919(v=VS.85).aspx"><strong>ID2D1SimplifiedGeometrySink</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_highlightsandshadows_input_gamma"><strong>D2D1_HIGHLIGHTSANDSHADOWS_INPUT_GAMMA</strong></a><br/></td>
<td>Values for the <a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_highlightsandshadows_prop"><strong>D2D1_HIGHLIGHTSANDSHADOWS_PROP_INPUT_GAMMA</strong></a> property of the <a href="highlights-and-shadows-effect">Highlights and Shadows effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_highlightsandshadows_prop"><strong>D2D1_HIGHLIGHTSANDSHADOWS_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="highlights-and-shadows-effect">Highlights and Shadows effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_histogram_prop"><strong>D2D1_HISTOGRAM_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="histogram">Histogram effect</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_huerotation_prop"><strong>D2D1_HUEROTATION_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="hue-rotate">Hue rotate effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_huetorgb_input_color_space"><strong>D2D1_HUETORGB_INPUT_COLOR_SPACE</strong></a><br/></td>
<td>Values for the <a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_huetorgb_prop"><strong>D2D1_HUETORGB_PROP_INPUT_COLOR_SPACE</strong></a> property of the <a href="hue-to-rgb-effect">Hue to RGB effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_huetorgb_prop"><strong>D2D1_HUETORGB_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="hue-to-rgb-effect">Hue to RGB effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1_3/ne-d2d1_3-d2d1_image_source_from_dxgi_options"><strong>D2D1_IMAGE_SOURCE_FROM_DXGI_OPTIONS</strong></a><br/></td>
<td>Option flags controlling primary conversion performed by <a href="https://msdn.microsoft.com/en-us/library/Dn890791(v=VS.85).aspx"><strong>CreateImageSourceFromDxgi</strong></a>, if any.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1_3/ne-d2d1_3-d2d1_image_source_loading_options"><strong>D2D1_IMAGE_SOURCE_LOADING_OPTIONS</strong></a><br/></td>
<td>Controls option flags for a new ID2D1ImageSource when it is created.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1_3/ne-d2d1_3-d2d1_ink_nib_shape"><strong>D2D1_INK_NIB_SHAPE</strong></a><br/></td>
<td>Specifies the appearance of the ink nib (pen tip) as part of an <a href="/windows/desktop/api/d2d1_3/ns-d2d1_3-d2d1_ink_style_properties"><strong>D2D1_INK_STYLE_PROPERTIES</strong></a> structure. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/D2d1_1/ne-d2d1_1-d2d1_interpolation_mode"><strong>D2D1_INTERPOLATION_MODE</strong></a><br/></td>
<td>This is used to specify the quality of image scaling with <a href="https://msdn.microsoft.com/en-us/library/Hh404511(v=VS.85).aspx"><strong>ID2D1DeviceContext::DrawImage</strong></a> and with the <a href="2d-affine-transform">2D affine transform effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_layer_options"><strong>D2D1_LAYER_OPTIONS</strong></a><br/></td>
<td>Specifies options that can be applied when a layer resource is applied to create a layer. <br/>
<blockquote>
[!Note]<br />
Starting in Windows 8, the <strong>D2D1_LAYER_OPTIONS_INITIALIZE_FOR_CLEARTYPE</strong> option is no longer supported. See <a href="/windows/desktop/api/d2d1_1/ne-d2d1_1-d2d1_layer_options1"><strong>D2D1_LAYER_OPTIONS1</strong></a> for Windows 8 layer options.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1_1/ne-d2d1_1-d2d1_layer_options1"><strong>D2D1_LAYER_OPTIONS1</strong></a><br/></td>
<td>Specifies how the layer contents should be prepared. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_lineartransfer_prop"><strong>D2D1_LINEARTRANSFER_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="linear-transfer">Linear transfer effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_line_join"><strong>D2D1_LINE_JOIN</strong></a><br/></td>
<td>Describes the shape that joins two lines or segments. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_lookuptable3d_prop"><strong>D2D1_LOOKUPTABLE3D_PROP</strong></a><br/></td>
<td>Identifiers for the properties of the 3D Lookup Table effect.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_morphology_mode"><strong>D2D1_MORPHOLOGY_MODE</strong></a><br/></td>
<td>The mode for the <a href="morphology">Morphology effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_morphology_prop"><strong>D2D1_MORPHOLOGY_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="morphology">Morphology effect</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/D2d1_1/ne-d2d1_1-d2d1_map_options"><strong>D2D1_MAP_OPTIONS</strong></a><br/></td>
<td>Specifies how the memory to be mapped from the corresponding <a href="https://msdn.microsoft.com/en-us/library/Hh404349(v=VS.85).aspx"><strong>ID2D1Bitmap1</strong></a> should be treated.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_opacitymetadata_prop"><strong>D2D1_OPACITYMETADATA_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="opacity-metadata-effect">Opacity metadata effect</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_opacity_mask_content"><strong>D2D1_OPACITY_MASK_CONTENT</strong></a><br/></td>
<td>Describes whether an opacity mask contains graphics or text. Direct2D uses this information to determine which gamma space to use when blending the opacity mask.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1_3/ne-d2d1_3-d2d1_orientation"><strong>D2D1_ORIENTATION</strong></a><br/></td>
<td>Specifies the flip and rotation at which an image appears.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1_3/ne-d2d1_3-d2d1_patch_edge_mode"><strong>D2D1_PATCH_EDGE_MODE</strong></a><br/></td>
<td>Specifies how to render gradient mesh edges.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_path_segment"><strong>D2D1_PATH_SEGMENT</strong></a><br/></td>
<td>Indicates whether a segment should be stroked and whether the join between this segment and the previous one should be smooth. This enumeration allows a bitwise combination of its member values. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/D2d1effectauthor/ne-d2d1effectauthor-d2d1_pixel_options"><strong>D2D1_PIXEL_OPTIONS</strong></a><br/></td>
<td>Indicates how pixel shader sampling will be restricted.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_pointdiffuse_prop"><strong>D2D1_POINTDIFFUSE_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="point-diffuse-lighting">Point-diffuse lighting effect</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_pointdiffuse_scale_mode"><strong>D2D1_POINTDIFFUSE_SCALE_MODE</strong></a><br/></td>
<td>The interpolation mode the <a href="point-diffuse-lighting">Point-diffuse lighting effect</a> uses to scale the image to the corresponding kernel unit length. There are six scale modes that range in quality and speed<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_pointspecular_prop"><strong>D2D1_POINTSPECULAR_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="point-specular">Point-specular lighting effect</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_pointspecular_scale_mode"><strong>D2D1_POINTSPECULAR_SCALE_MODE</strong></a><br/></td>
<td>The interpolation mode the <a href="point-specular">Point-specular lighting effect</a> uses to scale the image to the corresponding kernel unit length. There are six scale modes that range in quality and speed.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_posterize_prop"><strong>D2D1_POSTERIZE_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="posterize-effect">Posterize effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_present_options"><strong>D2D1_PRESENT_OPTIONS</strong></a><br/></td>
<td>Describes how a render target behaves when it presents its content. This enumeration allows a bitwise combination of its member values.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/D2d1_1/ne-d2d1_1-d2d1_primitive_blend"><strong>D2D1_PRIMITIVE_BLEND</strong></a><br/></td>
<td>Used to specify the geometric blend mode for all Direct2D primitives. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1_1/ne-d2d1_1-d2d1_print_font_subset_mode"><strong>D2D1_PRINT_FONT_SUBSET_MODE</strong></a><br/></td>
<td>Defines when font resources should be subset during printing.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/D2d1_1/ne-d2d1_1-d2d1_property_type"><strong>D2D1_PROPERTY_TYPE</strong></a><br/></td>
<td>Specifies the types of properties supported by the Direct2D property interface. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/D2d1_1/ne-d2d1_1-d2d1_property"><strong>D2D1_PROPERTY</strong></a><br/></td>
<td>Specifies the indices of the system properties present on the <a href="https://msdn.microsoft.com/en-us/library/Hh446854(v=VS.85).aspx"><strong>ID2D1Properties</strong></a> interface for an <a href="https://msdn.microsoft.com/en-us/library/Hh404566(v=VS.85).aspx"><strong>ID2D1Effect</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/D2D1_2/ne-d2d1_2-d2d1_rendering_priority"><strong>D2D1_RENDERING_PRIORITY</strong></a><br/></td>
<td>The rendering priority affects the extent to which <a href="direct2d-portal">Direct2D</a> will throttle its rendering workload.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_render_target_type"><strong>D2D1_RENDER_TARGET_TYPE</strong></a><br/></td>
<td>Describes whether a render target uses hardware or software rendering, or if Direct2D should select the rendering mode.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_render_target_usage"><strong>D2D1_RENDER_TARGET_USAGE</strong></a><br/></td>
<td>Describes how a render target is remoted and whether it should be GDI-compatible. This enumeration allows a bitwise combination of its member values.<br/></td>
</tr>
<tr class="odd">
<td><a href="https://msdn.microsoft.com/en-us/library/Hh447014(v=VS.85).aspx"><strong>D2D1_RESOURCE_TYPE</strong></a><br/></td>
<td>Specifies which kinds of resources should be released when <a href="https://msdn.microsoft.com/en-us/library/Hh404542(v=VS.85).aspx"><strong>ID2D1Device::ClearResources</strong></a> is invoked. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_rgbtohue_output_color_space"><strong>D2D1_RGBTOHUE_OUTPUT_COLOR_SPACE</strong></a><br/></td>
<td>Values for the <a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_rgbtohue_prop"><strong>D2D1_RGBTOHUE_PROP_OUTPUT_COLOR_SPACE</strong></a> property of the <a href="rgb-to-hue-effect">RGB to Hue effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_rgbtohue_prop"><strong>D2D1_RGBTOHUE_PROP</strong></a><br/></td>
<td>Indentifiers for properties of the <a href="rgb-to-hue-effect">RGB to Hue effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_saturation_prop"><strong>D2D1_SATURATION_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="saturation">Saturation effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_scale_interpolation_mode"><strong>D2D1_SCALE_INTERPOLATION_MODE</strong></a><br/></td>
<td>The interpolation mode the <a href="high-quality-scale">Scale effect</a> uses to scale the image. There are 6 scale modes that range in quality and speed. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_scale_prop"><strong>D2D1_SCALE_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="high-quality-scale">Scale effect</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_sepia_prop"><strong>D2D1_SEPIA_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="sepia-effect">Sepia effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_shadow_optimization"><strong>D2D1_SHADOW_OPTIMIZATION</strong></a><br/></td>
<td>The level of performance optimization for the <a href="drop-shadow">Shadow effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_shadow_prop"><strong>D2D1_SHADOW_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="drop-shadow">Shadow effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_sharpen_prop"><strong>D2D1_SHARPEN_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="sharpen-effect">Sharpen effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_spotdiffuse_prop"><strong>D2D1_SPOTDIFFUSE_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="diffuse-lighting">Spot-diffuse lighting effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_spotdiffuse_scale_mode"><strong>D2D1_SPOTDIFFUSE_SCALE_MODE</strong></a><br/></td>
<td>The interpolation mode the <a href="diffuse-lighting">Spot-diffuse lighting effect</a> uses to scale the image to the corresponding kernel unit length. There are six scale modes that range in quality and speed.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_spotspecular_prop"><strong>D2D1_SPOTSPECULAR_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="specular-lighting">Spot-specular lighting effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_spotspecular_scale_mode"><strong>D2D1_SPOTSPECULAR_SCALE_MODE</strong></a><br/></td>
<td>The interpolation mode the <a href="specular-lighting">Spot-specular lighting effect</a> uses to scale the image to the corresponding kernel unit length. There are six scale modes that range in quality and speed.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1_3/ne-d2d1_3-d2d1_sprite_options"><strong>D2D1_SPRITE_OPTIONS</strong></a><br/></td>
<td>Specifies additional aspects of how a sprite batch is to be drawn, as part of a call to <a href="/windows/desktop/api/d2d1_3/nf-d2d1_3-drawspritebatch"><strong>ID2D1DeviceContext3::DrawSpriteBatch</strong></a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_straighten_prop"><strong>D2D1_STRAIGHTEN_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="straighten-effect">Straighten effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_straighten_scale_mode"><strong>D2D1_STRAIGHTEN_SCALE_MODE</strong></a><br/></td>
<td>Values for the <a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_straighten_prop"><strong>D2D1_STRAIGHTEN_PROP_SCALE_MODE</strong></a> property of the <a href="straighten-effect">Straighten effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/D2d1_1/ne-d2d1_1-d2d1_stroke_transform_type"><strong>D2D1_STROKE_TRANSFORM_TYPE</strong></a><br/></td>
<td>Defines how the world transform, dots per inch (dpi), and stroke width affect the shape of the pen used to stroke a primitive.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/D2d1_1/ne-d2d1_1-d2d1_subproperty"><strong>D2D1_SUBPROPERTY</strong></a><br/></td>
<td>Specifies the indices of the system sub-properties that may be present in any property.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1svg/ne-d2d1svg-d2d1_svg_aspect_align"><strong>D2D1_SVG_ASPECT_ALIGN</strong></a><br/></td>
<td>The alignment portion of the SVG preserveAspectRatio attribute.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1svg/ne-d2d1svg-d2d1_svg_aspect_scaling"><strong>D2D1_SVG_ASPECT_SCALING</strong></a><br/></td>
<td>The meetOrSlice portion of the SVG preserveAspectRatio attribute.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1svg/ne-d2d1svg-d2d1_svg_attribute_pod_type"><strong>D2D1_SVG_ATTRIBUTE_POD_TYPE</strong></a><br/></td>
<td>Defines the type of SVG POD attribute to set or get.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1svg/ne-d2d1svg-d2d1_svg_attribute_string_type"><strong>D2D1_SVG_ATTRIBUTE_STRING_TYPE</strong></a><br/></td>
<td>Defines the type of SVG string attribute to set or get.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1svg/ne-d2d1svg-d2d1_svg_display"><strong>D2D1_SVG_DISPLAY</strong></a><br/></td>
<td>Specifies a value for the SVG display property.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1svg/ne-d2d1svg-d2d1_svg_length_units"><strong>D2D1_SVG_LENGTH_UNITS</strong></a><br/></td>
<td>Specifies the units for an SVG length.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1svg/ne-d2d1svg-d2d1_svg_line_cap"><strong>D2D1_SVG_LINE_CAP</strong></a><br/></td>
<td>Specifies a value for the SVG stroke-linecap property.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1svg/ne-d2d1svg-d2d1_svg_line_join"><strong>D2D1_SVG_LINE_JOIN</strong></a><br/></td>
<td>Specifies a value for the SVG stroke-linejoin property.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1svg/ne-d2d1svg-d2d1_svg_overflow"><strong>D2D1_SVG_OVERFLOW</strong></a><br/></td>
<td>Specifies a value for the SVG overflow property.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1svg/ne-d2d1svg-d2d1_svg_paint_type"><strong>D2D1_SVG_PAINT_TYPE</strong></a><br/></td>
<td>Specifies the paint type for an SVG fill or stroke.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1svg/ne-d2d1svg-d2d1_svg_path_command"><strong>D2D1_SVG_PATH_COMMAND</strong></a><br/></td>
<td>Represents a path commmand. Each command may reference floats from the segment data. Commands ending in _ABSOLUTE interpret data as absolute coordinate. Commands ending in _RELATIVE interpret data as being relative to the previous point.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1svg/ne-d2d1svg-d2d1_svg_unit_type"><strong>D2D1_SVG_UNIT_TYPE</strong></a><br/></td>
<td>Defines the coordinate system used for SVG gradient or clipPath elements.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1svg/ne-d2d1svg-d2d1_svg_visibility"><strong>D2D1_SVG_VISIBILITY</strong></a><br/></td>
<td>Specifies a value for the SVG visibility property.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_sweep_direction"><strong>D2D1_SWEEP_DIRECTION</strong></a><br/></td>
<td>Defines the direction that an elliptical arc is drawn. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_tabletransfer_prop"><strong>D2D1_TABLETRANSFER_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="table-transfer">Table transfer effect</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_temperatureandtint_prop"><strong>D2D1_TEMPERATUREANDTINT_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="temperature-and-tint-effect">Temperature and Tint effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_text_antialias_mode"><strong>D2D1_TEXT_ANTIALIAS_MODE</strong></a><br/></td>
<td>Describes the antialiasing mode used for drawing text. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1_1/ne-d2d1_1-d2d1_threading_mode"><strong>D2D1_THREADING_MODE</strong></a><br/></td>
<td>Specifies the threading mode used while simultaneously creating the device, factory, and device context. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_tile_prop"><strong>D2D1_TILE_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="tile">Tile effect</a>. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1_3/ne-d2d1_3-d2d1_transformed_image_source_options"><strong>D2D1_TRANSFORMED_IMAGE_SOURCE_OPTIONS</strong></a><br/></td>
<td>Option flags for transformed image sources.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_turbulence_noise"><strong>D2D1_TURBULENCE_NOISE</strong></a><br/></td>
<td>The turbulence noise mode for the <a href="turbulence">Turbulence effect</a>. Indicates whether to generate a bitmap based on Fractal Noise or the Turbulence function. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects/ne-d2d1effects-d2d1_turbulence_prop"><strong>D2D1_TURBULENCE_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="turbulence">Turbulence effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/D2d1_1/ne-d2d1_1-d2d1_unit_mode"><strong>D2D1_UNIT_MODE</strong></a><br/></td>
<td>Specifies how units in Direct2D will be interpreted.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/D2d1effectauthor/ne-d2d1effectauthor-d2d1_vertex_options"><strong>D2D1_VERTEX_OPTIONS</strong></a><br/></td>
<td>Describes flags that influence how the renderer interacts with a custom vertex shader.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/D2d1effectauthor/ne-d2d1effectauthor-d2d1_vertex_usage"><strong>D2D1_VERTEX_USAGE</strong></a><br/></td>
<td>Indicates whether the vertex buffer changes infrequently or frequently.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_vignette_prop"><strong>D2D1_VIGNETTE_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="vignette-effect">Vignette effect</a>.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1/ne-d2d1-d2d1_window_state"><strong>D2D1_WINDOW_STATE</strong></a><br/></td>
<td>Describes whether a window is occluded. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects_1/ne-d2d1effects_1-d2d1_ycbcr_chroma_subsampling"><strong>D2D1_YCBCR_CHROMA_SUBSAMPLING</strong></a><br/></td>
<td>Specifies the chroma subsampling of the input chroma image used by the <a href="ycbcr-effect">YCbCr effect</a>. <br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/d2d1effects_1/ne-d2d1effects_1-d2d1_ycbcr_interpolation_mode"><strong>D2D1_YCBCR_INTERPOLATION_MODE</strong></a><br/></td>
<td>Specifies the interpolation mode for the <a href="ycbcr-effect">YCbCr effect</a>.<br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/d2d1effects_1/ne-d2d1effects_1-d2d1_ycbcr_prop"><strong>D2D1_YCBCR_PROP</strong></a><br/></td>
<td>Identifiers for properties of the <a href="ycbcr-effect">YCbCr effect</a>. <br/></td>
</tr>
</tbody>
</table>



 

 

 





