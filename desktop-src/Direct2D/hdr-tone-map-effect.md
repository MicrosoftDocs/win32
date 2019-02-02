---
title: HDR tone map effect
description: This effect adjusts the dynamic range of an image to better suit its content to the capability of the output display.
ms.topic: article
ms.date: 02/01/2019
---

# HDR tone map effect

This effect adjusts the dynamic range of an image to better suit its content to the capability of the output display.

The CLSID for this effect is CLSID_D2D1HdrToneMap.

## Effect properties

| Display name and index enumeration | Type and default value | Description |
|-|-|-|
| InputMaxLuminance, D2D1_HDRTONEMAP_PROP_INPUT_MAX_LUMINANCE | FLOAT | The maximum light level (or MaxCLL) of the image, in nits. |
| OutputMaxLuminance, D2D1_HDRTONEMAP_PROP_OUTPUT_MAX_LUMINANCE | FLOAT | The MaxCLL supported by the output target, in nits&mdash;typically set to the MaxCLL of the display. |
| DisplayMode, D2D1_HDRTONEMAP_PROP_DISPLAY_MODE | [**D2D1_HDRTONEMAP_DISPLAY_MODE**](/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_hdrtonemap_display_mode) | When set to **D2D1_HDRTONEMAP_DISPLAY_MODE_HDR**, the tone mapping curve is adjusted to better fit the fit the behavior of common HDR displays. |

## Remarks
The value for `InputMaxLuminance` is typically derived from the image metadata.

The value for `OutputMaxLuminance` is designed to be derived from the display, using [**DXGI_OUTPUT_DESC1::MaxLuminance**](/windows/desktop/api/dxgi1_6/ns-dxgi1_6-dxgi_output_desc1).

The HDR tone map effect has different tone map curves depending on whether the display is an HDR display or an SDR/WCG display.

## Requirements

| | |
|-|-|
| Minimum supported client | Windows 10, version 1809 (10.0; Build 17763) \[desktop apps \| UWP apps\] |
| Header | d2d1effects\_2.h |
| Library | d2d1.lib, dxguid.lib |

## Related topics

* [ID2D1Effect interface](/windows/desktop/api/d2d1_1/nn-d2d1_1-id2d1effect)
