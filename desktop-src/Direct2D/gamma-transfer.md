---
title: Gamma transfer effect
description: Use the gamma transfer effect to map the color intensities of an image using a gamma function created using an amplitude, exponent, and offset you provide for each channel.
ms.assetid: 0E0455CA-CFCA-4C4F-9DFA-1DB6A5205F6A
keywords:
- gamma transfer effect
ms.topic: article
ms.date: 05/31/2018
---

# Gamma transfer effect

Use the gamma transfer effect to map the color intensities of an image using a gamma function created using an amplitude, exponent, and offset you provide for each channel.

The CLSID for this effect is CLSID\_D2D1GammaTransfer. To use this effect, add dxguid.lib to the linker dependencies.

-   [Example image](#example-image)
-   [Effect properties](#effect-properties)
-   [Output bitmap](#output-bitmap)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example image



| Before                                                         |
|----------------------------------------------------------------|
| ![the image before the effect.](images/default-before.jpg)     |
| After                                                          |
| ![the image after the transform.](images/14-gammatransfer.png) |



 


```C++
ComPtr<ID2D1Effect> gammaTransferEffect;
m_d2dContext->CreateEffect(CLSID_D2D1GammaTransfer, &gammaTransferEffect);

gammaTransferEffect->SetInput(0, bitmap);

gammaTransferEffect->SetValue(D2D1_GAMMATRANSFER_PROP_RED_EXPONENT, 0.25f);
gammaTransferEffect->SetValue(D2D1_GAMMATRANSFER_PROP_GREEN_EXPONENT, 0.25f);
gammaTransferEffect->SetValue(D2D1_GAMMATRANSFER_PROP_BLUE_EXPONENT, 0.25f);

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(gammaTransferEffect.Get());
m_d2dContext->EndDraw();
```



This effect applies a gamma transfer function based on the equation here.

The input pixel intensity is represented as C and the output pixel intensity as C'. C' = Amplitude \* C<sup>Exponent</sup> + Offset

This effect works on straight and premultiplied alpha images. The effect outputs premultiplied alpha bitmaps.

## Effect properties

> [!Note]  
> For all channels of the gamma transfer properties:
>
> -   The amplitude value is not bounded and is unitless.
> -   The exponent value is not bounded and is unitless.
> -   The offset value is not bounded and is unitless.

 



| Display name and index enumeration                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RedAmplitude<br/> D2D1\_GAMMATRANSFER\_PROP\_RED\_AMPLITUDE<br/>     | The amplitude of the gamma transfer function for the Red channel. The type is FLOAT.<br/> The default value is 1.0f.<br/>                                                                                                                                                                                                                                                                                                                                                                                             |
| RedExponent<br/> D2D1\_GAMMATRANSFER\_PROP\_RED\_EXPONENT<br/>       | The exponent of the gamma transfer function for the Red channel. The type is FLOAT.<br/> The default value is 1.0f.<br/>                                                                                                                                                                                                                                                                                                                                                                                              |
| RedOffset<br/> D2D1\_GAMMATRANSFER\_PROP\_RED\_OFFSET<br/>           | The offset of the gamma transfer function for the Red channel. The type is FLOAT.<br/> The default value is 0.0f.<br/>                                                                                                                                                                                                                                                                                                                                                                                                |
| RedDisable<br/> D2D1\_GAMMATRANSFER\_PROP\_RED\_DISABLE<br/>         | If you set this to TRUE it does not apply the transfer function to the Red channel. An identity transfer function is used. If you set this to FALSE it applies the gamma transfer function to the Red channel. The type is BOOL.<br/> The default value is FALSE.<br/>                                                                                                                                                                                                                                                |
| GreenAmplitude<br/> D2D1\_GAMMATRANSFER\_PROP\_GREEN\_AMPLITUDE<br/> | The amplitude of the gamma transfer function for the Green channel. The type is FLOAT.<br/> The default value is 1.0f.<br/>                                                                                                                                                                                                                                                                                                                                                                                           |
| GreenExponent<br/> D2D1\_GAMMATRANSFER\_PROP\_GREEN\_EXPONENT<br/>   | The exponent of the gamma transfer function for the Green channel. The type is FLOAT.<br/> The default value is 1.0f.<br/>                                                                                                                                                                                                                                                                                                                                                                                            |
| GreenOffset<br/> D2D1\_GAMMATRANSFER\_PROP\_GREEN\_OFFSET<br/>       | The offset of the gamma transfer function for the Green channel. The type is FLOAT.<br/> The default value is 0.0f.<br/>                                                                                                                                                                                                                                                                                                                                                                                              |
| GreenDisable<br/> D2D1\_GAMMATRANSFER\_PROP\_GREEN\_DISABLE<br/>     | If you set this to TRUE it does not apply the transfer function to the Green channel. An identity transfer function is used. If you set this to FALSE it applies the gamma transfer function to the Green channel. The type is BOOL.<br/> The default value is FALSE.<br/>                                                                                                                                                                                                                                            |
| BlueAmplitude<br/> D2D1\_GAMMATRANSFER\_PROP\_BLUE\_AMPLITUDE<br/>   | The amplitude of the gamma transfer function for the Blue channel. The type is FLOAT.<br/> The default value is 1.0f.<br/>                                                                                                                                                                                                                                                                                                                                                                                            |
| BlueExponent<br/> D2D1\_GAMMATRANSFER\_PROP\_BLUE\_EXPONENT<br/>     | The exponent of the gamma transfer function for the Blue channel. The type is FLOAT.<br/> The default value is 1.0f.<br/>                                                                                                                                                                                                                                                                                                                                                                                             |
| BlueOffset<br/> D2D1\_GAMMATRANSFER\_PROP\_BLUE\_OFFSET<br/>         | The offset of the gamma transfer function for the Blue channel. The type is FLOAT.<br/> The default value is 0.0f.<br/>                                                                                                                                                                                                                                                                                                                                                                                               |
| BlueDisable<br/> D2D1\_GAMMATRANSFER\_PROP\_BLUE\_DISABLE<br/>       | If you set this to TRUE it does not apply the transfer function to the Blue channel. An identity transfer function is used. If you set this to FALSE it applies the gamma transfer function to the Blue channel. The type is BOOL.<br/> The default value is FALSE.<br/>                                                                                                                                                                                                                                              |
| AlphaAmplitude<br/> D2D1\_GAMMATRANSFER\_PROP\_ALPHA\_AMPLITUDE<br/> | The amplitude of the gamma transfer function for the alpha channel. The type is FLOAT.<br/> The default value is 1.0f.<br/>                                                                                                                                                                                                                                                                                                                                                                                           |
| AlphaExponent<br/> D2D1\_GAMMATRANSFER\_PROP\_ALPHA\_EXPONENT<br/>   | The exponent of the gamma transfer function for the alpha channel. The type is FLOAT.<br/> The default value is 1.0f.<br/>                                                                                                                                                                                                                                                                                                                                                                                            |
| AlphaOffset<br/> D2D1\_GAMMATRANSFER\_PROP\_ALPHA\_OFFSET<br/>       | The offset of the gamma transfer function for the alpha channel. The type is FLOAT.<br/> The default value is 0.0f.<br/>                                                                                                                                                                                                                                                                                                                                                                                              |
| AlphaDisable<br/> D2D1\_GAMMATRANSFER\_PROP\_ALPHA\_DISABLE<br/>     | If you set this to TRUE it does not apply the transfer function to the alpha channel. An identity transfer function is used. If you set this to FALSE it applies the gamma transfer function to the alpha channel. The type is BOOL.<br/> The default value is FALSE.<br/>                                                                                                                                                                                                                                            |
| ClampOutput<br/> D2D1\_GAMMATRANSFER\_PROP\_CLAMP\_OUTPUT<br/>       | Whether the effect clamps color values to between 0 and 1 before the effect passes the values to the next effect in the graph. The effect clamps the values before it premultiplies the alpha .<br/> If you set this to TRUE the effect will clamp the values. If you set this to FALSE, the effect will not clamp the color values, but other effects and the output surface may clamp the values if they are not of high enough precision.<br/> The type is BOOL.<br/> The default value is FALSE.<br/> |



 

## Output bitmap

The output bitmap size is the same as the input bitmap size.

## Requirements



| Requirement | Value |
|--------------------------|------------------------------------------------------------------------------------|
| Minimum supported client | Windows 8 and Platform Update for Windows 7 \[desktop apps \| Windows Store apps\] |
| Minimum supported server | Windows 8 and Platform Update for Windows 7 \[desktop apps \| Windows Store apps\] |
| Header                   | d2d1effects.h                                                                      |
| Library                  | d2d1.lib, dxguid.lib                                                               |



 

## Related topics

<dl> <dt>

[**ID2D1Effect**](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1effect)
</dt> </dl>

 

