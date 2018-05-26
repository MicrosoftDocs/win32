---
title: WPF Bitmap Effects
description: Bitmap effects enable designers and developers to apply visual effects to rendered Windows Presentation Foundation (WPF) content.
ms.assetid: cec30833-b3e7-4b6a-88ca-a6fe7d1e7a7b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WPF Bitmap Effects

Bitmap effects enable designers and developers to apply visual effects to rendered Windows Presentation Foundation (WPF) content. For example, bitmap effects allow you to easily apply a DropShadowBitmapEffect effect or a blur effect to an image or a button. The unmanaged APIs provide an extensible framework for independent hardware vendors (IHVs) to develop custom effects to use in WPF applications.

Bitmap effects ([**IMILBitmapEffect**](/windows/previous-versions/Mileffects/nn-mileffects-imilbitmapeffect?branch=master) object) are simple pixel processing operations. A bitmap effect takes a [IWICBitmapSource Interface](http://msdn.microsoft.com/library/ms736175(VS.85).aspx) as an input and produces a new IWICBitmapSource Interface after applying the effect, such as a blur or drop shadow.

-   [Native Bitmap Effects](#native-bitmap-effects)
-   [Custom BitmapEffects](#custom-bitmapeffects)
-   [Related topics](#related-topics)

## Native Bitmap Effects

There are 5 built in bitmap effects available in WPF. 

| Effect     | Description                                                                                                              | Effect CLSID                     |
|------------|--------------------------------------------------------------------------------------------------------------------------|----------------------------------|
| Blur       | Simulates looking at an object through an out-of-focus lens.                                                             | CLSID\_MILBitmapEffectBlur       |
| DropShadow | Applies a shadow behind a visual object at a slight offset.                                                              | CLSID\_MILBitmapEffectDropShadow |
| OuterGlow  | Creates a halo of color around objects or areas of color.                                                                | CLSID\_MILBitmapEffectOuterGlow  |
| Bevel      | Creates a bevel which raises the surface of the image according to a specified curve.                                    | CLSID\_MILBitmapEffectBevel      |
| Emboss     | Creates a bump mapping of the visual object to give the impression of depth and texture from an artificial light source. | CLSID\_MILBitmapEffectEmboss     |



 

## Custom BitmapEffects

Custom effects are created by implemented the unmanaged APIs to create an effect library that can be used in a managed WPF application.

For an example of a custom bitmap effect, see [Custom RGBFilter Effect in WPF](http://go.microsoft.com/fwlink/p/?linkid=181556).

## Related topics

<dl> <dt>

[Custom RGBFilter Effect in WPF](http://go.microsoft.com/fwlink/p/?linkid=181556)
</dt> <dt>

[**IMILBitmapEffect**](/windows/previous-versions/Mileffects/nn-mileffects-imilbitmapeffect?branch=master)
</dt> </dl>

 

 




