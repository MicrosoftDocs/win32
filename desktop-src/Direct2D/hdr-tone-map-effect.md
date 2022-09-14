---
title: HDR tone map effect
description: This effect adjusts the dynamic range of an image to better suit its content to the capability of the output display.
ms.topic: article
ms.date: 02/01/2019
---

# HDR tone map effect

This effect adjusts the dynamic range of an image to better suit its content to the capability of the output display.

The properties for this effect are identified by the [**D2D1_HDRTONEMAP_PROP enumeration**](/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_hdrtonemap_prop), and the CLSID is **CLSID_D2D1HdrToneMap**.

## Effect properties

| Display name and index enumeration | Type and default value | Description |
|-|-|-|
| InputMaxLuminance, D2D1_HDRTONEMAP_PROP_INPUT_MAX_LUMINANCE | FLOAT | The maximum light level (or MaxCLL) of the image, in nits. |
| OutputMaxLuminance, D2D1_HDRTONEMAP_PROP_OUTPUT_MAX_LUMINANCE | FLOAT | The MaxCLL supported by the output target, in nits&mdash;typically set to the MaxCLL of the display. |
| DisplayMode, D2D1_HDRTONEMAP_PROP_DISPLAY_MODE | [**D2D1_HDRTONEMAP_DISPLAY_MODE**](/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_hdrtonemap_display_mode) | When set to **_HDR**, the tone mapping curve is adjusted to better fit the fit the behavior of common HDR displays. |

## Remarks
The value for `InputMaxLuminance` is typically derived from the image metadata. For cases where the metadata is not present, you can use the **D2DAdvancedColorImagesRenderer::ComputeHdrMetadata** function (in the [Direct2D advanced color image rendering sample](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/D2DAdvancedColorImages)) to compute the maximum light level (MaxCLL) of an image, in nits.

The value for `OutputMaxLuminance` is designed to be derived from the display, using [**DXGI_OUTPUT_DESC1::MaxLuminance**](/windows/desktop/api/dxgi1_6/ns-dxgi1_6-dxgi_output_desc1).

The HDR tone map effect has different tone map curves depending on whether the display is an HDR display or an SDR/WCG display.

This effect is intended to be combined with the [White level adjustment effect](white-level-adjustment-effect.md) to allow you to render HDR images in Direct2D with proper color management and tone mapping. It's aimed at any framework that wants to provide a best-in-class HDR image viewing experience that handles all of the Windows HDR image formats, and adapts to the capabilities of the display (whether that's HDR or WCG/SDR). The effects are intended to be chained together in sequence, as described below.

- Take the input image, whose color space defined by its codec. Metadata may specify whitePoint. Metadata may specify input luminance level.
- Apply the color management effect. Convert to scRGB (CCCS) space.
- Apply the HDR tone map effect. Lower the light level of the image to the desired level.
- Apply the white level adjustment effect. Scale the white level of the image to the white level required by the swap chain.
- Apply the color management effect again. If rendering to 8bpc, then convert to sRGB.

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows 10, version 1809 (10.0; Build 17763) \[desktop apps \| UWP apps\] |
| Header | d2d1effects\_2.h |
| Library | d2d1.lib, dxguid.lib |

## Related topics

* [ID2D1Effect interface](/windows/desktop/api/d2d1_1/nn-d2d1_1-id2d1effect)
* [D2D1_HDRTONEMAP_PROP enumeration](/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_hdrtonemap_prop)
