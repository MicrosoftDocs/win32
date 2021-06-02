---
description: Alpha Blending
ms.assetid: 56618e74-32cc-48f8-83b6-4fc31ab6fc36
title: Alpha Blending (DirectShow)
ms.topic: article
ms.date: 05/31/2018
---

# Alpha Blending (DirectShow)

\[This API is not supported and may be altered or unavailable in the future.\]

This article describes alpha blending in [DirectShow Editing Services](directshow-editing-services.md) (DES).

Alpha measures the transparency of a pixel or image. In 32-bit uncompressed RGB video, four components define each pixel: an alpha channel (A) and three color components (RGB). A pixel with an alpha value of zero is completely transparent. A pixel with an alpha value of 255 is opaque. Between these values, the pixel has various degrees of transparency.

DirectShow defines two media types for 32-bit RGB video:

-   **MEDIASUBTYPE\_ARGB32**: The video is 32-bit RGB with a valid alpha channel.
-   **MEDIASUBTYPE\_RGB32**: Pixels are 32 bits, but the alpha channel is not necessarily valid.

To perform alpha blending in DES, set the video group's uncompressed media type to MEDIASUBTYPE\_ARGB32. In C++, call the [**IAMTimelineGroup::SetMediaType**](iamtimelinegroup-setmediatype.md) method. In the XTL format, setting the [**bitdepth**](bitdepth-attribute.md) attribute of the [**group**](group-element.md) element to 32 accomplishes this as well.

Next, you need video data that contains an alpha channel. There are several options:

-   You can use an AVI file that already has 32-bit RGB video with alpha data. Currently, alpha is not supported for MPEG or Microsoft Windows Media Format (WMF) source files.
-   DES supports 32-bit bitmap (.bmp) and Targa (.tga) files with alpha data.
-   You can write a custom source filter that creates 32-bit RGB data with alpha. The output media type must be **MEDIASUBTYPE\_ARGB32**. Use the filter as the subobject in a timeline source object.

If your video source does not have alpha, you can use an effect that creates alpha data. The [Alpha Setter Effect](alpha-setter-effect.md) sets the alpha channel for the entire image to a constant value. To vary the alpha over time, use the [**IPropertySetter**](ipropertysetter.md) interface with the Alpha Setter Effect. The original source does not have to be 32 bits, as long as the group's uncompressed media type is **MEDIASUBTYPE\_ARGB32**.

Finally, pass the video to an effect or transition that performs alpha blending. The [Compositor Transition](compositor-transition.md) performs alpha blending, and the [Key Transition](key-transition.md) can key by alpha value.

The following sample XTL project performs alpha blending:


```C++
<timeline>
<group type="video" bitdepth="32" width="320" height="240">
<track>
  <clip start="0" stop="6" src="c:\Example.avi" />
</track>
<track>
  <clip start="0" stop="6" src="c:\Example2.avi">
    <!-- Alpha Setter effect. -->
    <effect clsid="{506D89AE-909A-44f7-9444-ABD575896E35}" start="0" stop="6">
      <param name="alpha" value="255">
        <linear time="6" value="0" />
      </param>
    </effect>
  </clip>
  <!-- Key transition, with alpha keying. -->
  <transition clsid="{C5B19592-145E-11d3-9F04-006008039E37}" start="0" stop="6">
    <param name="KeyType" value="3" />  
  </transition>
</track>
</group>
</timeline>
```



## Related topics

<dl> <dt>

[Using DirectShow Editing Services](using-directshow-editing-services.md)
</dt> </dl>

 

 



