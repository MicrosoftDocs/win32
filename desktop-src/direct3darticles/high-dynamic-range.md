---
title: Using DirectX with High Dynamic Range Displays and Advanced Color
description: This topic provides a technical overview of rendering high dynamic range Direct3D 11 and Direct3D 12 content to an HDR10 display using Windows 10 advanced color support.
ms.assetid: 
ms.topic: article
ms.date: 04/23/2020
---

# Using DirectX with High Dynamic Range Displays and Advanced Color

This topic provides a technical overview of outputting high dynamic range Direct3D 11 and Direct3D 12 content to an HDR10 display using Windows 10 advanced color support. It summarizes some key conceptual differences between outputting to HDR10 displays vs. traditional standard dynamic range (SDR) displays. It also covers the key technical requirements for your app to properly support Windows advanced color, as well as recommendations and best practices.

## Introduction

Windows advanced color refers to several related technologies, first introduced with Windows 10 version 1703, that provide support for displays that exceed the color capabilities of traditional standard dynamic range (SDR) displays. The three major extended capabilities are described below. The most common type of advanced color display, HDR10, supports all three extended capabilities.

### High Dynamic Range

Dynamic range refers to the difference between the maximum and minimum luminance in a scene; this is often measured in nits (candelas per square centimeter). Real world scenes, such as this sunset, often have dynamic ranges of 10 orders of magnitude of luminance; the human eye can discern an even greater range after adaptation.

![picture of a sunset with brightness and darkest points in the scene labeled](images/HDR-HDR.jpg)

Ever since Direct3D 9, graphics engines have been able to internally render their scenes with this level of physically accurate fidelity. However, a typical standard dynamic range display can only reproduce a little more than 3 orders of magnitude of luminance, and therefore any HDR rendered content had to be tonemapped (compressed) into the limited range of the display. New HDR displays, including those that comply with the HDR10 (BT.2100) standard, break through this limitation.

### Wide Color Gamut with Automatic System Color Management

Color gamut refers to the range and saturation of hues that a display can reproduce. The most saturated natural color the human eye can perceive is pure, monochromatic light such as what is produced by a laser. However, mainstream consumer displays often can only reproduce colors within the sRGB gamut, which only represents about 35% of all human-perceivable colors. The below diagram is a representation of the human "spectral locus" or all perceivable colors (at a given luminance level), where the smaller triangle is the sRGB gamut.

![diagram of the human spectral locus and sRGB gamut](images/HDR-WCG.jpg)

High end, professional PC displays have long supported color gamuts that are significantly wider than sRGB, such as Adobe RGB and D65-P3, and these wide gamut displays are becoming more common. However, prior to advanced color, Windows did not perform any system-level color management for applications. This meant that if a DirectX app rendered, for example, a pure red or RGB(1.0, 0.0, 0.0) to its swap chain, Windows would simply scanout the most saturated red that the display could reproduce, regardless of what the actual color gamut of the display was.

Apps that needed high color accuracy could query the color capabilities of the display (for example, using ICC profiles) and perform their own in-process color management to correctly target the display's color gamut. However, the vast majority of apps and visual content assume the display is sRGB, and rely on the operating system to fulfill this assumption.

Windows advanced color adds automatic system-level color management. The Desktop Window Manager (DWM) is Windows' compositor. When advanced color is enabled, the DWM performs an explicit color conversion from the app visual content's colorspace to a canonical composition color space, which is scRGB. Windows then color converts the composed framebuffer content to the display's native color space. In this way, traditional sRGB content automatically gets color accurate behavior, while advanced color-aware apps can take advantage of the full color capabilities of the display.

### Deep Precision/Bit Depth

Numerical precision or bit depth refers to represent/distinguish between similar but distinct colors without banding or artifacts. Mainstream PC displays support 8 bits per color channel, while the human eye requires at least 10-12 bits of precision to avoid perceivable distortions, without resorting to techniques like dithering and depending on viewing conditions.

![picture of windmills at a simulated 2 bits per color channel vs. 8 bits per channel](images/HDR-bitdepth.jpg)

Prior to advanced color, the DWM restricted windowed apps to only output content at 8 bits per color channel, even if the display supported a higher bit depth. When advanced color is enabled, the DWM performs its composition using IEEE half precision floating point (FP16), eliminating any bottlenecks and allowing the full precision of the display to be used.

## System Requirements

### Operating System

Advanced color support first shipped with Windows 10 version 1703 and has been significantly improved with each update. This topic assumes that your app is targeting Windows 10 version 1903.

### Display

To take advantage of high dynamic range, you must have a display that supports the HDR10 standard. Windows works best with displays that are [VESA DisplayHDR certified](www.displayhdr.org).

### Graphics Processor (GPU)

A recent GPU is required. To support HDR10 displays, Windows 10 requires one of the following:

* Nvidia GeForce 1000 series (Pascal) and newer
* AMD Radeon RX 400 series (Polaris) and newer
* Selected Intel Core 7 series (Kabylake) and newer

Note that additional hardware requirements apply depending on the scenarios, including hardware codec acceleration (10 bit HEVC, 10 bit VP9, etc) and PlayReady support (SL3000). Contact your GPU vendor for more specific information.

### Graphics driver (WDDM)

The latest available graphics driver is strongly recommended, either from Windows Update or from the GPU vendor or PC manufacturer's website. For Windows 10 version 1903, we recommend drivers that support at least Windows Display Driver Model (WDDM) version 2.6.

## Supported rendering APIs

Windows 10 supports a wide variety of rendering APIs and frameworks. Advanced color support fundamentally relies on your app being able to perform modern presentation using either DXGI or the Visual Layer APIs:

* [DirectX Graphics Infrastructure (DXGI)](../direct3ddxgi/dx-graphics-dxgi.md)
* [Visual Layer (Windows.UI.Composition)](https://docs.microsoft.com/windows/uwp/composition/visual-layer)

Therefore, any rendering API that can output to one of these presentations methods can support advanced color. This includes but is not limited to:

* [Direct3D 11](../Direct3D11/atoc-dx-graphics-direct3d-11.md)
* [Direct3D 12](../Direct3D12/direct3d-12-graphics.md)
* [Direct2D](../Direct2D/direct2d-portal.md)
* [Win2D](https://github.com/Microsoft/Win2D)
  * Requires using the lower level CanvasSwapChain or CanvasSwapChainPanel APIs.
* [Windows.UI.Input.Inking](https://docs.microsoft.com/uwp/api/Windows.UI.Input.Inking)
  * Supports custom dry ink rendering using DirectX
* [XAML](https://docs.microsoft.com/windows/uwp/xaml-platform/)
  * Supports playback of HDR videos using MediaPlayerElement
  * Supports decode of JPEG XR images using Image element
  * Supports DirectX interop using SwapChainPanel

## Handling Dynamic Display Capabilities

Windows 10 supports an enormous range of advanced color-capable displays, from power efficient integrated panels to high end gaming monitors and TVs. Windows users expect that your app will seamlessly handle all of these variations including ubiquitous existing SDR displays.

Windows 10 provides control over HDR and advanced color capabilities to the user. Your app must detect the current display's configuration, and respond dynamically to any changes in capability. This could occur for many reasons, for example because the user enabled or disabled a feature, moved the app between different displays, or the system's power state changed.

### Universal Windows Platform (UWP) apps

If you are writing a UWP app, regardless of the graphics rendering API you are using, use [AdvancedColorInfo](https://docs.microsoft.com/uwp/api/windows.graphics.display.advancedcolorinfo) to get display capabilities. Obtain an instance of AdvancedColorInfo from [DisplayInformation::GetAdvancedColorInfo](https://docs.microsoft.com/uwp/api/windows.graphics.display.displayinformation.getadvancedcolorinfo).

To check what advanced color kind is currently active, use the [CurrentAdvancedColorKind](https://docs.microsoft.com/uwp/api/windows.graphics.display.advancedcolorinfo.currentadvancedcolorkind) property. In Windows 10 1903 this returns one of three possible values: SDR, WCG, or HDR. This is the most important property to check and you should configure your render and presentation pipeline in response to the active kind.

To check what advanced color kinds are supported but not necessarily active, call [IsAdvancedColorKindAvailable](https://docs.microsoft.com/uwp/api/windows.graphics.display.advancedcolorinfo.isadvancedcolorkindavailable). You could use this information, for example, to prompt the user to navigate the Settings app so they can enable HDR or WCG.

The other members of AdvancedColorInfo provide quantitative information about the panel’s physical color volume (luminance and chrominance), corresponding to SMPTE ST.2086 static HDR metadata. You should use this information to configure your app's HDR tonemapping and gamut mapping.

To handle changes in advanced color capabilities, register for the [AdvancedColorInfoChanged](https://docs.microsoft.com/uwp/api/windows.graphics.display.displayinformation.advancedcolorinfochanged) event. This event fires if any parameter of the display’s advanced color capabilities has changed for any reason.

Respond to this event by obtaining a new instance of AdvancedColorInfo and checking which values have changed.

### Desktop (Win32) DirectX apps

If you are writing a Win32 app and using DirectX to render, use [DXGI_OUTPUT_DESC1](https://docs.microsoft.com/windows/desktop/api/DXGI1_6/ns-dxgi1_6-dxgi_output_desc1) to get display capabilities. Obtain an instance of this struct via [IDXGIOutput6::GetDesc1](https://docs.microsoft.com/windows/win32/api/dxgi1_6/nf-dxgi1_6-idxgioutput6-getdesc1).

To check what advanced color kind is currently active, use the ColorSpace property, which is of type [DXGI_COLOR_SPACE_TYPE](https://docs.microsoft.com/windows/win32/api/dxgicommon/ne-dxgicommon-dxgi_color_space_type) and contains one of the following values:

* DXGI_COLOR_SPACE_RGB_FULL_G22_NONE_P709: SDR
* DXGI_COLOR_SPACE_RGB_FULL_G2048_NONE_P2020: HDR

> [!Note]
> Other advanced color kinds such as WCG are treated as SDR by DXGI. You can’t use DXGI to identify a WCG display.

> [!Note]
> DXGI does not let you check what advanced color kinds are supported but not active at the moment.

Most of the other members of DXGI_OUTPUT_DESC1 provide quantitative information about the panel’s physical color volume (luminance and chrominance), corresponding to SMPTE ST.2086 static HDR metadata. You should use this information to configure your app's HDR tonemapping and gamut mapping.

Win32 apps don’t have a native mechanism to respond to advanced color capability changes. Instead, if your app uses a render loop you should query [IDXGIFactory1::IsCurrent](https://docs.microsoft.com/windows/desktop/api/DXGI/nf-dxgi-idxgifactory1-iscurrent) with each frame. If it reports FALSE then you should obtain a new DXGI_OUTPUT_DESC1 and check which values have changed.

In addition, your Win32 message pump should handle the [WM_SIZE](https://docs.microsoft.com/windows/win32/winmsg/wm-size) message which is indicates that your app may have moved between different displays.

> [!Note]
> To obtain a new DXGI_OUTPUT_DESC1 you must obtain the current display. However, you should not call IDXGISwapChain::GetContainingOutput. This is because swap chains will return a stale DXGI output once DXGIFactory::IsCurrent is false, and recreating the swap chain to get a current output results in a temporary black screen. Instead, we recommend that you enumerate through the bounds of all DXGI outputs and determine which one has the greatest intersection with your app window’s bounds.

The following code sample comes from the [DirectX-Graphics-Samples repository](https://github.com/Microsoft/DirectX-Graphics-Samples/tree/master/Samples/Desktop/D3D12HDR).

```C++
// Retrieve the current default adapter.
ComPtr<IDXGIAdapter1> dxgiAdapter;
ThrowIfFailed(m_dxgiFactory->EnumAdapters1(0, &dxgiAdapter));

// Iterate through the DXGI outputs associated with the DXGI adapter,
// and find the output whose bounds have the greatest overlap with the
// app window (i.e. the output for which the intersection area is the
// greatest).

UINT i = 0;
ComPtr<IDXGIOutput> currentOutput;
ComPtr<IDXGIOutput> bestOutput;
float bestIntersectArea = -1;

while (dxgiAdapter->EnumOutputs(i, &currentOutput) != DXGI_ERROR_NOT_FOUND)
{
    // Get the retangle bounds of the app window
    int ax1 = m_windowBounds.left;
    int ay1 = m_windowBounds.top;
    int ax2 = m_windowBounds.right;
    int ay2 = m_windowBounds.bottom;

    // Get the rectangle bounds of current output
    DXGI_OUTPUT_DESC desc;
    ThrowIfFailed(currentOutput->GetDesc(&desc));
    RECT r = desc.DesktopCoordinates;
    int bx1 = r.left;
    int by1 = r.top;
    int bx2 = r.right;
    int by2 = r.bottom;

    // Compute the intersection
    int intersectArea = ComputeIntersectionArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2);
    if (intersectArea > bestIntersectArea)
    {
        bestOutput = currentOutput;
        bestIntersectArea = static_cast<float>(intersectArea);
    }

    i++;
}

// Having determined the output (display) upon which the app is primarily being 
// rendered, retrieve the HDR capabilities of that display by checking the color space.
ComPtr<IDXGIOutput6> output6;
ThrowIfFailed(bestOutput.As(&output6));

DXGI_OUTPUT_DESC1 desc1;
ThrowIfFailed(output6->GetDesc1(&desc1));
```

## Setting up Your DirectX Swap Chain

Once you have determined that the display currently supports advanced color capabilities, configure your swap chain as follows.

### Use a Flip Model Presentation Effect

When creating your swap chain using the CreateSwapChainForHwnd/Composition/CoreWindow methods, you must use the DXGI flip model by selecting either the DXGI_SWAP_EFFECT_FLIP_SEQUENTIAL or DXGI_SWAP_EFFECT_FLIP_DISCARD option, which makes your swap chain eligible for advanced color processing from DWM and various fullscreen optimizations. For more information, refer to the following topic: [For best performance, use DXGI flip model](../direct3ddxgi/for-best-performance--use-dxgi-flip-model.md).

### Option 1: Use FP16 Pixel Format and scRGB Color Space

Windows 10 supports two main combinations of pixel format and color space for advanced color. Select one based on your app’s specific requirements.

For general purpose apps, we recommend specifying [DXGI_FORMAT_R16G16B16A16_FLOAT](https://docs.microsoft.com/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format) a.k.a. FP16 in your [DXGI_SWAP_CHAIN_DESC1](https://docs.microsoft.com/windows/win32/api/dxgi1_2/ns-dxgi1_2-dxgi_swap_chain_desc1) when creating your swap chain. By default, a swap chain created with a float point pixel format is treated as if it uses the [DXGI_COLOR_SPACE_RGB_FULL_G10_NONE_P709](https://docs.microsoft.com/windows/win32/api/dxgicommon/ne-dxgicommon-dxgi_color_space_type) color space a.k.a. scRGB.

This combination provides you with the numeric range and precision to specify almost any physically possible color and perform arbitrary processing including blending. In addition, if you are using Direct2D, Win2D or Windows.UI.Composition, this is the only supported combination for any swap chain or intermediate target that contains advanced color content. 

The main tradeoff of this option is that it consumes 64 bits per pixel which doubles GPU bandwidth and memory consumption versus the traditional UINT8 SDR pixel formats. In addition, scRGB uses numeric values that are outside the normalized [0, 1] range to represent colors that are outside the sRGB gamut and/or greater than 80 nits of luminance. For example, scRGB (1.0, 1.0, 1.0) encodes the standard D65 white at 80 nits; but scRGB (12.5, 12.5, 12.5) encodes the same D65 white at a much brighter 1000 nits. Some graphics operations require a normalized numeric range, and you must either modify the operation or re-normalize color values.

### Option 2: Use UINT10/RGB10 Pixel Format and HDR10/BT.2100 Color Space

For apps that consume HDR10-encoded content such as media players, or apps that are expected to mainly be used in fullscreen scenarios such as games, you should consider specifying [DXGI_FORMAT_R10G10B10A2_UNORM](https://docs.microsoft.com/windows/win32/api/dxgiformat/ne-dxgiformat-dxgi_format) in [DXGI_SWAP_CHAIN_DESC1](https://docs.microsoft.com/windows/win32/api/dxgi1_2/ns-dxgi1_2-dxgi_swap_chain_desc1) when creating your swap chain. By default, this is treated as using the sRGB color space; therefore, you must explicitly call [IDXGISwapChain3::SetColorSpace1](https://docs.microsoft.com/windows/win32/api/dxgi1_4/nf-dxgi1_4-idxgiswapchain3-setcolorspace1) and set [DXGI_COLOR_SPACE_RGB_FULL_G2084_NONE_P2020](https://docs.microsoft.com/windows/win32/api/dxgicommon/ne-dxgicommon-dxgi_color_space_type) a.k.a. HDR10/BT.2100 as your color space.

This combination has more stringent restrictions than FP16. You can only use this with Direct3D 11 or Direct3D 12. In addition, UINT10/HDR10 has limitations as an intermediate format because it uses the ST.2084 EOTF (“gamma” function) which is highly nonlinear and optimized as a wire format, and because it only offers 2 bits of alpha.

However, this combination can offer powerful performance optimizations when used in your app's final output. It consumes the same 32 bits per pixel as traditional UINT8 SDR pixel formats. In addition, in certain fullscreen scenarios the OS can optimize performance by directly scanning out the HDR10 surface.

## Correctly Render SDR Content with SDR Reference White Level

In many scenarios, your app will want to render both SDR and HDR content; for example rendering subtitles or transport controls over HDR video, or UI into a game scene. It is important to understand the concept of _SDR reference white level_ to ensure your SDR content looks correct on an HDR display.

Windows treats HDR content as _scene-referred_, meaning that a particular color value should be displayed at a specific luminance level; for example, scRGB (1.0, 1.0, 1.0) and HDR10 (497, 497, 497) both encode exactly D65 white at 80 nits luminance. Meanwhile, SDR content traditionally has been _output-referred_ (or display-referred), meaning that its luminance is left up to the user or the device; for example sRGB (1.0, 1.0, 1.0) encodes D65 white as in the HDR examples, but at whatever maximum luminance the display is configured for. Windows allows the user to adjust the _SDR reference white level_ to their preference; this is the luminance that Windows will render sRGB (1.0, 1.0, 1.0) at. On desktop HDR monitors, SDR reference white levels are typically set to around 200 nits.

> [!Note]
> On displays that support brightness control, such as on laptops, Windows will adjust the luminance of HDR (scene-referred) content to fit the user's desired brightness level, but this is mostly invisible to the app.

If your app always renders SDR and HDR to separate surfaces and relies on OS composition, then Windows will automatically perform the correct adjustment to boost SDR content to the desired white level. For example, if your app uses XAML and renders HDR content to its own SwapChainPanel.

However, if your app performs its own composition of SDR and HDR content into a single surface, then you are responsible for performing the SDR reference white level adjustment yourself. Otherwise the SDR content may appear too dim assuming typical desktop viewing conditions. First, you must obtain the current SDR reference white level, and then you must adjust the color values of any SDR content you are rendering.

### Obtain the Current SDR Reference White Level

Currently, only UWP apps can obtain the current SDR reference white level via [AdvancedColorInfo.SdrWhiteLevelInNits](https://docs.microsoft.com/uwp/api/windows.graphics.display.advancedcolorinfo.sdrwhitelevelinnits). This API requires a [CoreWindow](https://docs.microsoft.com/uwp/api/Windows.UI.Core.CoreWindow).

### Adjust Color Values of SDR Content

Windows defines the nominal, or default, reference white level at 80 nits; therefore if you were to render a standard sRGB (1.0, 1.0, 1.0) white to an FP16 swap chain, it would be reproduced at 80 nits luminance. In order to match the actual user-defined reference white level, you must adjust SDR content from 80 nits to the level specified via AdvancedColorInfo.SdrWhiteLevelInNits.

If you are rendering using FP16 and scRGB, or any color space that uses linear (1.0) gamma, then you can simply multiply the SDR color value by _AdvancedColorInfo.SdrWhiteLevelInNits_ / _80_.

```
float4 output;

```

## Additional Resources

* [Direct2D advanced color images SDK sample](https://github.com/Microsoft/Windows-universal-samples/tree/master/Samples/D2DAdvancedColorImages): UWP SDK sample implementing an advanced color-aware HDR and WCG image viewer using Direct2D.
* [Direct3D 12 HDR desktop sample](https://github.com/microsoft/DirectX-Graphics-Samples/tree/master/Samples/Desktop/D3D12HDR): Desktop SDK sample implementing a basic Direct3D 12 HDR scene
* [Direct3D 12 HDR UWP sample](https://github.com/microsoft/DirectX-Graphics-Samples/tree/master/Samples/UWP/D3D12HDR): UWP equivalent of the above sample
* [Xbox ATG SimpleHDR PC sample](https://github.com/microsoft/Xbox-ATG-Samples/tree/master/PCSamples/Graphics/SimpleHDR_PC): Desktop SDK sample implementing a basic Direct3D 11 HDR scene

## Conclusion

Windows 10 supports HDR and other advanced color displays, which provide significantly higher color fidelity than traditional SDR displays. You can use Direct3D, Direct2D and other graphics APIs to render HDR content to a capable display.