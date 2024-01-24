---
title: White tone map effect
description: This effect allows the white level of an image to be linearly scaled. This is especially helpful when you convert between display-referred luminance space and scene-referred luminance space, or vice versa.
ms.topic: article
ms.date: 02/01/2019
---

# White level adjustment effect

This effect allows the white level of an image to be linearly scaled. This is especially helpful when you convert between display-referred luminance space and scene-referred luminance space, or vice versa.

The properties for this effect are identified by the [**D2D1_WHITELEVELADJUSTMENT_PROP enumeration**](/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_whiteleveladjustment_prop), and the CLSID is **CLSID_D2D1WhiteLevelAdjustment**.

## Effect properties

| Display name and index enumeration | Type and default value | Description |
|-|-|-|
| InputWhiteLevel, D2D1_WHITELEVELADJUSTMENT_PROP_INPUT_WHITE_LEVEL | FLOAT | The white level of the input image, in nits. |
| OutputWhiteLevel, D2D1_WHITELEVELADJUSTMENT_PROP_OUTPUT_WHITE_LEVEL | FLOAT | The white level of the output image, in nits. |

## Remarks
This effect is intended to be combined with the [HDR tone map effect](hdr-tone-map-effect.md) to allow you to render HDR images in Direct2D with proper color management and tone mapping. See that topic's **Remarks** for more details. The effects are aimed at any framework that wants to provide a best-in-class HDR image viewing experience that handles all of the Windows HDR image formats, and adapts to the capabilities of the display (whether that's HDR or WCG/SDR).

On Windows, all SDR/WCG content is assumed to be in a display-referred luminance space, meaning that the white level of the content should be scaled up to the display's white level before it is ultimately presented. However, it's not always your application's responsibility to do this. In contrast, HDR content is assumed to be in a scene-referred luminance space, meaning that it shouldn't ultimately be scaled to match the display's white level. That said, your application may need to perform scaling in some circumstances when rendering HDR content to ensure that this is the net result.

When the Windows desktop is in SDR or WCG mode, the desktop is composed in a display-referred luminance space. But if the Windows desktop is in HDR mode, then desktop composition happens in scene-referred luminance space. That said, the Desktop Window Manager (DWM) itself performs luminance adjustments (often called SDRBoost) for 8-bit composition surfaces, and that simplifies your application for that case. Even so, the automatic boost means that your application's role in converting from one luminance space to another is dependent upon the composition format that your application is using to present its content.

The table below describes the cases when your application should and should not perform a white level adjustment, as well as what that adjustment should be. In general, the adjustment depends on three factors.

1. Input content colorspace. Whether your input content contains high dynamic range (HDR) luminance values or not. WCG content behaves the same as SDR for luminance behavior.
2. Composition format. The pixel format of the target surface that is presented to the DWM&mdash;for example, a [swap chain](/windows/desktop/api/dxgi/nn-dxgi-idxgiswapchain) or a [composition surface](/uwp/api/Windows.UI.Composition.ICompositionSurface). When rendering using Direct2D, this is either **UINT8** or **FP16**.
3. Desktop advanced color mode. Whether the DWM is running in SDR, WCG, or HDR mode for the current display. Obtain this information via [**DXGI_OUTPUT_DESC1::ColorSpace**](/windows/desktop/api/dxgi1_6/ns-dxgi1_6-dxgi_output_desc1) or [**AdvancedColorInfo.CurrentAdvancedColorKind**](/uwp/api/windows.graphics.display.advancedcolorinfo.currentadvancedcolorkind).

Based on these three factors, you should set the appropriate values for the `InputWhiteLevel` and `OutputWhiteLevel` properties.

|Input content|Composition format|Advanced color mode|InputWhiteLevel|OutputWhiteLevel|
|-|-|-|-|-|
|SDR/WCG|**UINT8**|Any|N/A|N/A|
|SDR/WCG|**FP16**|SDR/WCG|N/A|N/A|
|SDR/WCG|**FP16**|HDR|SDRWhite|80|
|HDR|Any|SDR/WCG|80|[**DXGI_OUTPUT_DESC1::MaxLuminance**](/windows/desktop/api/dxgi1_6/ns-dxgi1_6-dxgi_output_desc1)|
|HDR|**UINT8**|HDR|80|SDRWhite|
|HDR|**FP16**|HDR|N/A|N/A|

In the table, the value 80 is the reference white level, in nits, for sRGB or scRGB content. For this, you can use the constant [**D2D1_SCENE_REFERRED_SDR_WHITE_LEVEL**](/windows/desktop/direct2d/direct2d-constants), which is defined in `d2d1effects_2.h`. The value `SDRWhite` is the number of nits that the display should use to display white sRGB content. You can retrieve this value by accessing the [**AdvancedColorInfo.SdrWhiteLevelInNits**](/uwp/api/windows.graphics.display.advancedcolorinfo.sdrwhitelevelinnits) property. The value N/A means that white level adjustment is not used in this scenario; you can either remove the effect from your graph, or set values for a no-op.

Note that, in cases where a white level adjustment is not needed by the application, the DWM or the display may be handling the conversion from display-referred luminance space to scene-referred luminance space.

- In SDR/WCG mode, the conversion happens after DWM composition, and applies to all content presented to that display. The display implicitly performs this conversion.
- In HDR mode, the conversion is performed automatically by the DWM before composition, so long as your application's composition surface is SDR.

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows 10, version 1809 (10.0; Build 17763) \[desktop apps \| UWP apps\] |
| Header | d2d1effects\_2.h |
| Library | d2d1.lib, dxguid.lib |

## Related topics

* [ID2D1Effect interface](/windows/desktop/api/d2d1_1/nn-d2d1_1-id2d1effect)
* [D2D1_WHITELEVELADJUSTMENT_PROP enumeration](/windows/desktop/api/d2d1effects_2/ne-d2d1effects_2-d2d1_whiteleveladjustment_prop)
