---
title: Color management effect
description: Use the color management effect to transform an image from one ICC (International Color Consortium) color profile to another. The effect transforms the image according to the ICC specification.
ms.assetid: 7351C4B4-F289-4236-BB42-1B3BD8753248
keywords:
- color management effect
ms.topic: article
ms.date: 02/05/2019
---

# Color management effect

Use the color management effect to transform an image from one ICC (International Color Consortium) color profile to another. The effect transforms the image according to the [ICC specification](https://www.color.org).

The CLSID for this effect is CLSID\_D2D1ColorManagement.

- [Effect properties](#effect-properties)
- [Rendering intent modes](#rendering-intent-modes)
- [Input image alpha modes](#input-image-alpha-modes)
- [Compliance with ICC specification](#compliance-with-icc-specification)
- [Alpha channel behavior](#alpha-channel-behavior)
- [Quality modes](#quality-modes)
- [Sample code](#sample-code)
- [Requirements](#requirements)
- [Related topics](#related-topics)

## Effect properties

| Display name and index enumeration | Description |
|-|-|
| SourceContext<br/> D2D1\_COLORMANAGEMENT\_PROP\_SOURCE\_COLOR\_CONTEXT<br/> | The source color space information. The type is [**ID2D1ColorContext**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1colorcontext).<br/> The default value is NULL.<br/> |
| SourceIntent<br/> D2D1\_COLORMANAGEMENT\_PROP\_SOURCE\_RENDERING\_INTENT<br/> | Which ICC rendering intent to use. The type is D2D1\_COLORMANAGEMENT\_RENDERING\_INTENT.<br/> The default value is D2D1\_COLORMANAGEMENT\_RENDERING\_INTENT\_PERCEPTUAL.<br/> |
| DestinationContext<br/> D2D1\_COLORMANAGEMENT\_PROP\_DESTINATION\_COLOR\_CONTEXT<br/> | The destination color space information. The type is [**ID2D1ColorContext**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1colorcontext).<br/> The default value is NULL.<br/> |
| DestinationIntent<br/> D2D1\_COLORMANAGEMENT\_PROP\_DESTINATION\_RENDERING\_INTENT<br/> | Which ICC rendering intent to use. The type is D2D1\_COLORMANAGEMENT\_RENDERING\_INTENT.<br/> The default value is D2D1\_COLORMANAGEMENT\_RENDERING\_INTENT\_PERCEPTUAL.<br/> |
| AlphaMode<br/> D2D1\_COLORMANAGEMENT\_PROP\_ALPHA\_MODE<br/> | How to interpret alpha data that is contained in the input image. The type is D2D1\_COLORMANAGEMENT\_ALPHA\_MODE.<br/> The default value is D2D1\_COLORMANAGEMENT\_ALPHA\_MODE\_PREMULTIPLIED.<br/> |
| Quality<br/> D2D1\_COLORMANAGEMENT\_PROP\_QUALITY<br/> | The quality level of the transform. The type is D2D1\_COLORMANAGEMENT\_QUALITY.<br/> The default value is D2D1\_COLORMANAGEMENT\_QUALITY\_NORMAL.<br/> |

## Rendering intent modes

| Enumeration | Description |
|-|-|
| D2D1\_COLORMANAGEMENT\_RENDERING\_INTENT\_PERCEPTUAL | The effect compresses or expands the full color gamut of the image to fill the color gamut of the device, to produce a perceptually pleasing output that preserves color details but may sacrifice colorimetric accuracy. It is useful for general reproduction of real life content such as photos. |
| D2D1\_COLORMANAGEMENT\_RENDERING\_INTENT\_RELATIVE\_COLORIMETRIC | The effect adjusts any colors that fall outside the gamut that the output device can render to the closest color that can be rendered. It does not preserve the white point. |
| D2D1\_COLORMANAGEMENT\_RENDERING\_INTENT\_SATURATION | The effect preserves the saturation of pure colors in the image at the possible expense of hue and lightness. It is useful for graphics like charts and diagrams. |
| D2D1\_COLORMANAGEMENT\_RENDERING\_INTENT\_ABSOLUTE\_COLORIMETRIC | The effect adjusts any colors that fall outside the gamut that the output device can render to the closest color that can be rendered. The effect does not change the in-gamut colors and preserves the white point. |

## Input image alpha modes

| Enumeration | Description |
|-|-|
| D2D1\_COLORMANAGEMENT\_ALPHA\_MODE\_PREMULTIPLIED | The effect assumes the alpha mode is premultiplied. |
| D2D1\_COLORMANAGEMENT\_ALPHA\_MODE\_STRAIGHT | The effect assumes the alpha mode is straight. |

## D2D1_GAMMA1_G2084 behavior changes
	
If your application uses the [D2D1_GAMMA1_G2084](/windows/desktop/api/d2d1_3/ne-d2d1_3-d2d1_gamma1) space, or one of the [DXGI_COLOR_SPACE_TYPE](/windows/desktop/api/dxgicommon/ne-dxgicommon-dxgi_color_space_type) enumeration values that use the SMPTE ST.2084 (Perceptual Quantizer) color space, then the application intends to work with HDR data.

The [**ID2D1DeviceContext5::CreateColorContextFromSimpleColorProfile**](/windows/desktop/api/d2d1_3/nf-d2d1_3-id2d1devicecontext5-createcolorcontextfromsimplecolorprofile(constd2d1_simple_color_profile__id2d1colorcontext1)) and [**ID2D1DeviceContext5::CreateColorContextFromDxgiColorSpace**](/windows/desktop/api/d2d1_3/nf-d2d1_3-id2d1devicecontext5-createcolorcontextfromdxgicolorspace) APIs don't account for that; rather, the HDR content is scaled to fit in the 0-1 range during the G2084 DeGamma operation.

In practice, content that is encoded in this gamma space uses a reference WhiteLevel of 10,000 Nits, which would normally be represented in CCCS as 10,000 / 80 = 125.0. So, to better facilitate your app, it's simplest for this gamma conversion to also scale the luminance by a factor of 125. As of Windows 10, version 1809 (10.0; Build 17763), the behavior of the color management effect is such that it applies this scaling. That means that you, as the developer, don't have to apply a second [White level adjustment effect](white-level-adjustment-effect.md) into the pipeline.

## Compliance with ICC specification

The color management effect is compliant with the ICC v4.3 specification, with these limitations:

- The effect supports 1, 3, and 4 channel color spaces.
- The effect doesn't support ColorSpace or Named Color profiles.

## Alpha channel behavior

In general, the effect sets alpha to 1 (opaque) if there is no alpha data in the source image and the alpha data is discarded if there is no room in the destination image. The table here describes the alpha behavior.

<table>
<thead>
<tr class="header">
<th>Source colorspace, pixel format</th>
<th>Destination colorspace, pixel format</th>
<th>Alpha behavior</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="4">1 channel, R pixel format<br />
</td>
<td>1 channel, R pixel format</td>
<td>(No alpha data)</td>
</tr>
<tr class="even">
<td>1 channel, RGBA pixel format</td>
<td>Alpha data is set to 1 (opaque)</td>

</tr>
<tr class="odd">
<td>3 channel, RGBA pixel format</td>
<td>Alpha data is set to 1 (opaque)</td>

</tr>
<tr class="even">
<td>4 channel, RGBA pixel format</td>
<td>(No alpha data)</td>

</tr>
<tr class="odd">
<td rowspan="4">1 channel, RGBA pixel format<br />
</td>
<td>1 channel, R pixel format</td>
<td>Alpha data is discarded</td>
</tr>
<tr class="even">
<td>1 channel, RGBA pixel format</td>
<td>Alpha data is passed through</td>

</tr>
<tr class="odd">
<td>3 channel, RGBA pixel format</td>
<td>Alpha data is passed through</td>

</tr>
<tr class="even">
<td>4 channel, RGBA pixel format</td>
<td>Alpha data is discarded</td>

</tr>
<tr class="odd">
<td rowspan="4">3 channel, RGBA pixel format<br />
</td>
<td>1 channel, R pixel format</td>
<td>Alpha data is discarded</td>
</tr>
<tr class="even">
<td>1 channel, RGBA pixel format</td>
<td>Alpha data is passed through</td>

</tr>
<tr class="odd">
<td>3 channel, RGBA pixel format</td>
<td>Alpha data is passed through</td>

</tr>
<tr class="even">
<td>4 channel, RGBA pixel format</td>
<td>Alpha data is discarded</td>

</tr>
<tr class="odd">
<td rowspan="4">4 channel, RGBA pixel format<br />
</td>
<td>1 channel, R pixel format</td>
<td>(No alpha data)</td>
</tr>
<tr class="even">
<td>1 channel, RGBA pixel format</td>
<td>Alpha data is set to 1 (opaque)</td>

</tr>
<tr class="odd">
<td>3 channel, RGBA pixel format</td>
<td>Alpha data is set to 1 (opaque)</td>

</tr>
<tr class="even">
<td>4 channel, RGBA pixel format</td>
<td>(No alpha data)</td>

</tr>
</tbody>
</table>

## Quality modes

| Mode | Description |
|-|-|
| D2D1\_COLORMANAGEMENT\_QUALITY\_PROOF | The lowest quality mode. This mode requires feature level 9\_1 or above. |
| D2D1\_COLORMANAGEMENT\_QUALITY\_NORMAL | Normal quality mode. This mode requires feature level 9\_1 or above. |
| D2D1\_COLORMANAGEMENT\_QUALITY\_BEST | The best quality mode. This mode requires feature level 10\_0 or above, as well as floating point precision buffers. This mode supports floating point precision as well as extended range as defined in the ICC v4.3 specification. |

The color management effect fails when drawing if the application requests a quality mode that is not supported by the hardware. You can determine the feature level when you call [**D3D11CreateDevice**](/windows/desktop/api/d3d11/nf-d3d11-d3d11createdevice). You can check for floating point buffer support by calling [**ID2D1EffectContext::IsBufferPrecisionSupported**](/windows/win32/api/d2d1_1/nf-d2d1_1-id2d1devicecontext-isbufferprecisionsupported) with the value [**D2D1\_BUFFER\_PRECISION\_32BPC\_FLOAT**](/windows/desktop/api/D2d1_1/ne-d2d1_1-d2d1_buffer_precision).

## Sample code

For an example of this effect, download the [Direct2D effects photo adjustment sample](https://github.com/microsoft/Windows-universal-samples/tree/master/Samples/D2DPhotoAdjustment), and see Lesson 4 of the sample.

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows 8 and Platform Update for Windows 7 \[desktop apps \| Windows Store apps\] |
| Minimum supported server | Windows 8 and Platform Update for Windows 7 \[desktop apps \| Windows Store apps\] |
| Header | d2d1effects.h |
| Library | d2d1.lib, dxguid.lib |

## Related topics

* [ID2D1Effect interface](/windows/desktop/api/d2d1_1/nn-d2d1_1-id2d1effect)
