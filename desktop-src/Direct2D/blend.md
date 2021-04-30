---
title: Blend effect
description: Use the blend effect to combine 2 images. This effect has 26 blend modes.
ms.assetid: 39D8BAA3-8FF3-4F10-99A0-B26FCA3018AE
keywords:
- blend effect
ms.topic: article
ms.date: 05/31/2018
---

# Blend effect

Use the blend effect to combine 2 images. This effect has 26 blend modes.

The CLSID for this effect is CLSID\_D2D1Blend.

-   [Blending examples](#blending-examples)
-   [Effect properties](#effect-properties)
-   [Blend modes](#blend-modes)
-   [HSL color space conversions](#hsl-color-space-conversions)
    -   [Converting from RGB to HSL](#converting-from-rgb-to-hsl)
    -   [Converting from HSL to RGB](#converting-from-hsl-to-rgb)
-   [Output bitmap](#output-bitmap)
-   [Sample code](#sample-code)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Blending examples

Here is an example image of every blend mode of the blend effect. A full list of the blend modes and the corresponding mode properties are in the next section

![effect example screenshot of all the available blend modes.](images/blend-modes.png)

Here is another example using the exclusion mode.



| Before image 1                                                             |
|----------------------------------------------------------------------------|
| ![the first source image before the effect.](images/default-before.jpg)    |
| Before image 2                                                             |
| ![the second image before the effect.](images/4-arthimetic-composite2.jpg) |
| After                                                                      |
| ![the image after the transform.](images/5-blend.png)                      |



 


```C++
ComPtr<ID2D1Effect> blendEffect;
m_d2dContext->CreateEffect(CLSID_D2D1Blend, &blendEffect);

blendEffect->SetInput(0, bitmap);
blendEffect->SetInput(1, bitmapTwo);
blendEffect->SetValue(D2D1_BLEND_PROP_MODE, D2D1_BLEND_MODE_EXCLUSION);

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(blendEffect.Get());
m_d2dContext->EndDraw();
```



## Effect properties



| Display name and index enumeration                 | Description                                                                                                                                                                               |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mode<br/> D2D1\_BLEND\_PROP\_MODE<br/> | The blend mode used for the effect. See [Blend modes](#blend-modes) for more info. The type is D2D1\_BLEND\_MODE.<br/> The default value is D2D1\_BLEND\_MODE\_MULTIPLY.<br/> |



 

## Blend modes

The table here shows all the blend modes of this effect. The helper functions necessary to compute the output of the effect are in the next section.

Color: O<sub>PRGB</sub> = *f*(F<sub>RGB</sub>, B<sub>RGB</sub>) \* F<sub>A</sub> \* B<sub>A</sub> + F<sub>RGB</sub> \* F<sub>A</sub> \* (1 - B<sub>A</sub>) + B<sub>RGB</sub> \* B<sub>A</sub> \* (1 - F<sub>A</sub>)

Alpha: O<sub>A</sub> = F<sub>A</sub> \* (1 - B<sub>A</sub>) + B<sub>A</sub>

Where:

-   O<sub>PRGB</sub> is the pre-multiplied output color
-   O<sub>A</sub> is Output Alpha
-   B<sub>RGB</sub> is the un-pre-multiplied destination color
-   B<sub>A</sub> is destination alpha
-   F<sub>RGB</sub> is the un-pre-multiplied source color
-   F<sub>A</sub> is source alpha
-   *f*(S<sub>RGB</sub>, D<sub>RGB</sub>) is a blend function that varies per-blend-mode

Some of the blend modes require conversion to and from the hue, saturation, luminosity (HSL) color space to RGB.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Enumeration</th>
<th>Equation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>D2D1_BLEND_MODE_DARKEN</td>
<td>Basic blend formula for alpha only. <img src="images/blend-mode-darken-1.png" alt="mathematical formula for a darken effect." /></td>
</tr>
<tr class="even">
<td>D2D1_BLEND_MODE_MULTIPLY</td>
<td>Basic blend formula for alpha only. <img src="images/blend-mode-multiply-1.png" alt="Mathematical formula for a mutiply effect." /></td>
</tr>
<tr class="odd">
<td>D2D1_BLEND_MODE_COLOR_BURN</td>
<td>Basic blend formulas with <em>f</em>(F<sub>RGB</sub>, B<sub>RGB</sub>) = <img src="images/blend-mode-colorburn-1.png" alt="Mathematical formula for a coor burn effect." /></td>
</tr>
<tr class="even">
<td>D2D1_BLEND_MODE_LINEAR_BURN</td>
<td>Basic blend formulas with <em>f</em>(F<sub>RGB</sub>, B<sub>RGB</sub>) = <img src="images/blend-mode-linearburn-1.png" alt="Mathematical formula for a linear burn effect." /></td>
</tr>
<tr class="odd">
<td>D2D1_BLEND_MODE_DARKER_COLOR</td>
<td>Basic blend formula for alpha only. <img src="images/blend-mode-darkencolor-1.png" alt="Mathematical formla for a darken color effect." /></td>
</tr>
<tr class="even">
<td>D2D1_BLEND_MODE_LIGHTEN</td>
<td>Basic blend formula for alpha only. <img src="images/blend-mode-lighten-1.png" alt="Mathematical formula for a lighten effect." /></td>
</tr>
<tr class="odd">
<td>D2D1_BLEND_MODE_SCREEN</td>
<td>Basic blend formula for alpha only. <img src="images/blend-mode-screen-1.png" alt="Mathematical formula for a screen effect." /></td>
</tr>
<tr class="even">
<td>D2D1_BLEND_MODE_COLOR_DODGE</td>
<td>Basic blend formulas with <em>f</em>(F<sub>RGB</sub>, B<sub>RGB</sub>) = <img src="images/blend-mode-colordodge-1.png" alt="Mathematical formula for a color dodge effect." /></td>
</tr>
<tr class="odd">
<td>D2D1_BLEND_MODE_LINEAR_DODGE</td>
<td>Basic blend formulas with <em>f</em>(F<sub>RGB</sub>, B<sub>RGB</sub>) = <img src="images/blend-mode-lineardodge-1.png" alt="Mathematical formula for a linear dodge effect." /></td>
</tr>
<tr class="even">
<td>D2D1_BLEND_MODE_LIGHTER_COLOR</td>
<td>Basic blend formula for alpha only. <img src="images/blend-mode-lightercolor-1.png" alt="Mathematical formula for a lighter color effect." /></td>
</tr>
<tr class="odd">
<td>D2D1_BLEND_MODE_OVERLAY</td>
<td>Basic blend formulas with <em>f</em>(F<sub>RGB</sub>, B<sub>RGB</sub>) = <img src="images/blend-mode-overlay-1.png" alt="Mathematical formula for an overlay effect." /></td>
</tr>
<tr class="even">
<td>D2D1_BLEND_MODE_SOFT_LIGHT</td>
<td>Basic blend formulas with <em>f</em>(F<sub>RGB</sub>, B<sub>RGB</sub>) = <img src="images/blend-mode-softlight-1.png" alt="Mathematical formula for a soft light effect." /></td>
</tr>
<tr class="odd">
<td>D2D1_BLEND_MODE_HARD_LIGHT</td>
<td>Basic blend formulas with <em>f</em>(F<sub>RGB</sub>, B<sub>RGB</sub>) = <img src="images/blend-mode-hardlight-1.png" alt="Mathematical formula for a hard light effect." /></td>
</tr>
<tr class="even">
<td>D2D1_BLEND_MODE_VIVID_LIGHT</td>
<td>Basic blend formulas with <em>f</em>(F<sub>RGB</sub>, B<sub>RGB</sub>) = <img src="images/blend-mode-vividlight-1.png" alt="Mathematical formula for a vivid light effect." /></td>
</tr>
<tr class="odd">
<td>D2D1_BLEND_MODE_LINEAR_LIGHT</td>
<td>Basic blend formulas with <em>f</em>(F<sub>RGB</sub>, B<sub>RGB</sub>) = <img src="images/blend-mode-linearlight-1.png" alt="Mathematical formula for a linear light effect." /></td>
</tr>
<tr class="even">
<td>D2D1_BLEND_MODE_PIN_LIGHT</td>
<td>Basic blend formulas with <em>f</em>(F<sub>RGB</sub>, B<sub>RGB</sub>) = <img src="images/blend-mode-pinlight-1.png" alt="Mathematical formula for a pin light effect." /></td>
</tr>
<tr class="odd">
<td>D2D1_BLEND_MODE_HARD_MIX</td>
<td>Basic blend formulas with <em>f</em>(F<sub>RGB</sub>, B<sub>RGB</sub>) = <img src="images/blend-mode-hardmix-1.png" alt="Mathematical formula for a hard mix effect." /></td>
</tr>
<tr class="even">
<td>D2D1_BLEND_MODE_DIFFERENCE</td>
<td>Basic blend formulas with <em>f</em>(F<sub>RGB</sub>, B<sub>RGB</sub>) = abs(F<sub>RGB</sub> - B<sub>RGB</sub>)</td>
</tr>
<tr class="odd">
<td>D2D1_BLEND_MODE_EXCLUSION</td>
<td>Basic blend formulas with <em>f</em>(F<sub>RGB</sub>, B<sub>RGB</sub>) = F<sub>RGB</sub> + B<sub>RGB</sub>   2 * F<sub>RGB</sub> * B<sub>RGB</sub></td>
</tr>
<tr class="even">
<td>D2D1_BLEND_MODE_HUE</td>
<td>Basic blend formula for alpha only. <img src="images/blend-mode-hue-1.png" alt="Mathematical formula for a hue blend effect." /></td>
</tr>
<tr class="odd">
<td>D2D1_BLEND_MODE_SATURATION</td>
<td>Basic blend formula for alpha only. <img src="images/blend-mode-saturation-1.png" alt="Mathematical formula for a sturation blend effect." /></td>
</tr>
<tr class="even">
<td>D2D1_BLEND_MODE_COLOR</td>
<td>Basic blend formula for alpha only. <img src="images/blend-mode-color-1.png" alt="Mathematical formula for a color blend effect." /></td>
</tr>
<tr class="odd">
<td>D2D1_BLEND_MODE_LUMINOSITY</td>
<td>Basic blend formula for alpha only. <img src="images/blend-mode-luminosity-1.png" alt="Mathematical formula for a luminosity blend effect." /></td>
</tr>
<tr class="even">
<td>D2D1_BLEND_MODE_DISSOLVE</td>
<td>Given:
<ul>
<li>A scene coordinate XY for the current pixel</li>
<li>A deterministic pseudo-random number generator rand(XY) based on seed coordinate XY, with unbiased distribution of values from [0, 1]</li>
</ul>
<br/> <img src="images/blend-mode-dissolve-1.png" alt="Mathematical formula for a dissolve blend effect." /><br/></td>
</tr>
<tr class="odd">
<td>D2D1_BLEND_MODE_SUBTRACT</td>
<td>Basic blend formula for alpha only. <img src="images/blend-mode-subtract-1.png" alt="Mathematical formula for a subtract blend effect." /></td>
</tr>
<tr class="even">
<td>D2D1_BLEND_MODE_DIVISION</td>
<td>Basic blend formula for alpha only. <img src="images/blend-mode-division-1.png" alt="Mathematical formula for a division blend effect." /></td>
</tr>
</tbody>
</table>



 

> [!Note]  
> For all Blend modes, the output value is premultiplied and clamped to the range \[0, 1\].

 

## HSL color space conversions

The luminosity component is computed using the RGB weights here:

-   *k*<sub>R</sub> = 0.30
-   *k*<sub>G</sub> = 0.59
-   *k*<sub>B</sub> = 0.11

### Converting from RGB to HSL

![mathematical formula describing the transformation from rgb color to hsl color.](images/blend-rgb-to-hsl-1.png)

This places *S* and *L* in the range \[0.0, 1.0\] and *H* in the range \[-1.0, 5.0\].

### Converting from HSL to RGB

To convert the other way we use the inverse of the previous calculations.

If *S* = 0 then *R* = *G* = *B* = *L*

Otherwise there are six hue-dependant cases:

If *H* is greater than 0, the values are in the red/magenta sector where *R* > *B* > *G*.

![mathematical equaiton step one of six converting hsl color to rgb.](images/blend-hsl-to-rgb-1rm.png)

If *H* is greater than or equal to 0 and less than 1, the values are in the red/yellow sector where *R* > *G* > *B*.

![mathematical equaiton step two of six converting hsl color to rgb.](images/blend-hsl-to-rgb-1ry.png)

If *H* is greater than or equal to 1 and less than 2, the values are in the yellow/green sector where *G* > *R* > *B*.

![mathematical equaiton step three of six converting hsl color to rgb.](images/blend-hsl-to-rgb-1yg.png)

If *H* is greater than or equal to 2 and less than 3, the values are in the green/cyan sector where *G* > *B* > *R*.

![mathematical equaiton step four of six converting hsl color to rgb.](images/blend-hsl-to-rgb-1gc.png)

If *H* is greater than or equal to 3 and less than 4, the values are in the cyan/blue sector where *B* > *G* > *R*.

![mathematical equaiton step five of six converting hsl color to rgb.](images/blend-hsl-to-rgb-1cb.png)

If *H* is greater than or equal to 4, the values are in the blue/magenta sector where *B* > *R* > *G*.

![mathematical equaiton step six of six converting hsl color to rgb.](images/blend-hsl-to-rgb-1bm.png)

Because the blending modes make arbitrary combinations of HSL components from two different colors, it is common for the converted RGB value to be out-of-gamut, that is, one or more channel components may be outside the legal range of \[0.0, 1.0\]. These colors are brought back into gamut by minimally reducing the saturation, while preserving both hue and luminosity:

![mathematical formula describing the corrections required for out of gamut instances.](images/blend-gamut-correction.png)

## Output bitmap

The output bitmap for this effect is always the size of the union of the two input images.

## Sample code

For an example of this effect, download the [Direct2D composite effect modes sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Direct2D%20composite%20effect%20modes%20sample).

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

 

