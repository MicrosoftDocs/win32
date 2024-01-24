---
title: Linear transfer effect
description: Use the linear transfer effect to map the color intensities of an image using a linear function created from a list of values you provide for each channel.
ms.assetid: 22DC496E-2958-4726-A74D-B3DE934F507C
keywords:
- linear transfer effect
ms.topic: article
ms.date: 05/31/2018
---

# Linear transfer effect

Use the linear transfer effect to map the color intensities of an image using a linear function created from a list of values you provide for each channel.

The CLSID for this effect is CLSID\_D2D1LinearTransfer.

-   [Example image](#example-image)
-   [Effect properties](#effect-properties)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example image



| Before                                                          |
|-----------------------------------------------------------------|
| ![the image before the effect.](images/default-before.jpg)      |
| After                                                           |
| ![the image after the transform.](images/13-lineartransfer.png) |



 


```C++
ComPtr<ID2D1Effect> linearTransferEffect;
m_d2dContext->CreateEffect(CLSID_D2D1LinearTransfer, &linearTransferEffect);

linearTransferEffect->SetInput(0, bitmap);

linearTransferEffect->SetValue(D2D1_LINEARTRANSFER_PROP_RED_Y_INTERCEPT, -1.0f);
linearTransferEffect->SetValue(D2D1_LINEARTRANSFER_PROP_RED_SLOPE, 2.5f);
linearTransferEffect->SetValue(D2D1_LINEARTRANSFER_PROP_GREEN_Y_INTERCEPT, -1.0f);
linearTransferEffect->SetValue(D2D1_LINEARTRANSFER_PROP_GREEN_SLOPE, 5.0f);

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(linearTransferEffect.Get());
m_d2dContext->EndDraw();
```



The linear transfer function is created based on the slope and y-intercept for each channel that you specify. The output pixel intensity C  is calculated with the equation: C' = mC + B, where m is the slope of the linear function and B is the Y-intercept of the linear function.

This effect works on straight and premultiplied alpha images. The effect outputs premultiplied alpha bitmaps.

## Effect properties

> [!Note]  
> For all channels of the linear transfer properties:
>
> -   The Y-intercept is not bounded and is unitless.
> -   The slope is not bounded and is unitless.

 



| Display name and index enumeration                                                    | Type and default value           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RedYIntercept<br/> D2D1\_LINEARTRANSFER\_PROP\_RED\_Y\_INTERCEPT<br/>     | FLOAT<br/> 0.0f<br/> | The Y-intercept of the linear function for the Red channel.                                                                                                                                                                                                                                                                                                                                                                                                   |
| RedSlope<br/> D2D1\_LINEARTRANSFER\_PROP\_RED\_SLOPE<br/>                 | FLOAT<br/> 1.0f<br/> | The slope of the linear function for the Red channel.                                                                                                                                                                                                                                                                                                                                                                                                         |
| RedDisable<br/> D2D1\_LINEARTRANSFER\_PROP\_RED\_DISABLE<br/>             | BOOL<br/> FALSE<br/> | If you set this to TRUE the effect does not apply the transfer function to the Red channel. If you set this to FALSE the effect applies the RedLinearTransfer function to the Red channel.                                                                                                                                                                                                                                                                    |
| GreenYIntercept<br/> D2D1\_LINEARTRANSFER\_PROP\_GREEN\_Y\_INTERCEPT<br/> | FLOAT<br/> 0.0f<br/> | The Y-intercept of the linear function for the Green channel.                                                                                                                                                                                                                                                                                                                                                                                                 |
| GreenSlope<br/> D2D1\_LINEARTRANSFER\_PROP\_GREEN\_SLOPE<br/>             | FLOAT<br/> 1.0f<br/> | The slope of the linear function for the Green channel.                                                                                                                                                                                                                                                                                                                                                                                                       |
| GreenDisable<br/> D2D1\_LINEARTRANSFER\_PROP\_GREEN\_DISABLE<br/>         | BOOL<br/> FALSE<br/> | If you set this to TRUE the effect does not apply the transfer function to the Green channel. If you set this to FALSE it applies the GreenLinearTransfer function to the Green channel.                                                                                                                                                                                                                                                                      |
| BlueYIntercept<br/> D2D1\_LINEARTRANSFER\_PROP\_BLUE\_Y\_INTERCEPT<br/>   | FLOAT<br/> 0.0f<br/> | The Y-intercept of the linear function for the Blue channel.                                                                                                                                                                                                                                                                                                                                                                                                  |
| BlueSlope<br/> D2D1\_LINEARTRANSFER\_PROP\_BLUE\_SLOPE<br/>               | FLOAT<br/> 1.0f<br/> | The slope of the linear function for the Blue channel.                                                                                                                                                                                                                                                                                                                                                                                                        |
| BlueDisable<br/> D2D1\_LINEARTRANSFER\_PROP\_BLUE\_DISABLE<br/>           | BOOL<br/> FALSE<br/> | If you set this to TRUE the effect does not apply the transfer function to the Blue channel. If you set this to FALSE it applies the BlueLinearTransfer function to the Blue channel.                                                                                                                                                                                                                                                                         |
| AlphaYIntercept<br/> D2D1\_LINEARTRANSFER\_PROP\_ALPHA\_Y\_INTERCEPT<br/> | FLOAT<br/> 0.0f<br/> | The Y-intercept of the linear function for the Alpha channel.                                                                                                                                                                                                                                                                                                                                                                                                 |
| AlphaSlope<br/> D2D1\_LINEARTRANSFER\_PROP\_ALPHA\_SLOPE<br/>             | FLOAT<br/> 0.0f<br/> | The slope of the linear function for the Alpha channel.                                                                                                                                                                                                                                                                                                                                                                                                       |
| AlphaDisable<br/> D2D1\_LINEARTRANSFER\_PROP\_ALPHA\_DISABLE<br/>         | BOOL<br/> FALSE<br/> | If you set this to TRUE the effect does not apply the transfer function to the Alpha channel. If you set this to FALSE it applies the AlphaLinearTransfer function to the Alpha channel.                                                                                                                                                                                                                                                                      |
| ClampOutput<br/> D2D1\_LINEARTRANSFER\_PROP\_CLAMP\_OUTPUT<br/>           | BOOL<br/> FALSE<br/> | Whether the effect clamps color values to between 0 and 1 before the effect passes the values to the next effect in the graph. The effect clamps the values before it premultiplies the alpha .<br/> If you set this to TRUE the effect will clamp the values. If you set this to FALSE, the effect will not clamp the color values, but other effects and the output surface may clamp the values if they are not of high enough precision.<br/> |



 

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

 

