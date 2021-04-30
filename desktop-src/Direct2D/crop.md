---
title: Crop effect
description: Use the crop effect to output a specified region of an image.
ms.assetid: DFB7DE20-F202-4E7F-AE63-94BF817B6E30
keywords:
- crop effect
ms.topic: article
ms.date: 05/31/2018
---

# Crop effect

Use the crop effect to output a specified region of an image.

The CLSID for this effect is CLSID\_D2D1Crop.

-   [Example image](#example-image)
-   [Effect properties](#effect-properties)
-   [Output bitmap](#output-bitmap)
-   [Requirements](#requirements)
-   [Related topics](#related-topics)

## Example image



| Before                                                     |
|------------------------------------------------------------|
| ![the image before the effect.](images/default-before.jpg) |
| After                                                      |
| ![the image after the transform.](images/8-crop.png)       |



 


```C++
ComPtr<ID2D1Effect> cropEffect;
m_d2dContext->CreateEffect(CLSID_D2D1Crop, &cropEffect);

cropEffect->SetInput(0, bitmap);
cropEffect->SetValue(D2D1_CROP_PROP_RECT, D2D1::RectF(0.0f, 0.0f, 256.0f, 192.0f));

m_d2dContext->BeginDraw();
m_d2dContext->DrawImage(cropEffect.Get());
m_d2dContext->EndDraw();
```



## Effect properties



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Display name and index enumeration</th>
<th>Type and default value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Rect<br/></td>
<td>D2D1_VECTOR_4F<br/></td>
<td>The region to be cropped specified as a vector in the form (left, top, width, height).<br/></td>
</tr>
<tr class="even">
<td>D2D1_CROP_PROP_RECT<br/></td>
<td>{-FLT_MAX, -FLT_MAX, FLT_MAX, FLT_MAX}<br/></td>
<td>The units are in DIPs. <br/>
<blockquote>
<p>[!Note]</p>
<p>The Rect will be truncated if it overlaps the edge boundaries of the input image.<br/></p>
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>D2D1_CROP_PROP_BORDER_MODE<br/></td>
<td>D2D1_BORDER_MODE <br/> D2D1_BORDER_MODE_SOFT <br/></td>
<td><ul>
<li>D2D1_BORDER_MODE_SOFT : If the crop rectangle falls on fractional pixel coordinates, the effect applies antialiasing which results in a soft edge.</li>
<li>D2D1_BORDER_MODE_HARD : If the crop rectangle falls on fractional pixel coordinates, the effect clamps which results in a hard edge.</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Output bitmap

The output of this effect is the size of the Rect property. The length and width are calc

ulated using the equations here: <dl> Output length in Pixels=(Rect.Right-Rect.Left)\*(User's DPI/96)  
Output height in pixels=(Rect.Bottom-Rect.Top)\*(User's DPI/96)  
</dl>

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

 

