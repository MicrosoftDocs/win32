---
description: The clip epecifies a media source.
ms.assetid: 40323e64-ad5f-4646-bad7-2a4e7d0ddcf6
title: clip Element
ms.topic: reference
ms.date: 05/31/2018
---

# clip Element

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `clip` epecifies a media source.

## Attributes

[**clsid**](clsid-attribute.md), [**framerate**](framerate-attribute.md), [**lock**](lock-attribute.md), [**mlength**](mlength-attribute.md), [**mstart**](mstart-attribute.md), [**mstop**](mstop-attribute.md), [**mute**](mute-attribute.md), [**src**](src-attribute.md), [**start**](start-attribute.md), [**stop**](stop-attribute.md), [**stream**](stream-attribute.md), [**stretchmode**](stretchmode-attribute.md), [**userdata**](userdata-attribute.md), [**userid**](userid-attribute.md), [**username**](username-attribute.md)

## Parent/Child Information



| Label | Value |
|----------|----------------------------------|
| Parent   | [**track**](track-element.md)   |
| Children | [**effect**](effect-element.md) |



 

## Remarks

The **clsid** attribute specifies the CLSID of a source filter to use as the source. Do not specify the **src** and **clsid** attributes within the same `clip` element.

Specify at least one start-time attribute (**start** or **mstart**) and one stop-time attribute (**stop** or **mstop**). If one of the start-time attributes is unspecified, it defaults to 0 (the beginning of the timeline for **start**, or the beginning of the clip for **mstart**). If one of the stop-time attributes is unspecified, DES assumes a normal playback rate and calculates the unspecified stop time accordingly. If both stop times are specified, playback is faster or slower than normal, if necessary.

In the following example, the timeline duration is seven seconds (**stop** minus **start**). Normal playback rate is assumed, so the media stop time defaults to 10 seconds (the duration plus **mstart**).


```
<clip start="2" stop="9" mstart="3" />
```



In the next example, the media start time defaults to 0, forcing the media duration to be 10 seconds. The timeline duration is five seconds, so the clip plays back at twice the normal rate.


```
<clip start="5" stop="10" mstop="10" />  
```



If the **src** attribute specifies a still image, DES attempts to load a series of still images to create an animation. For example, if the **src** attribute is IMAGE001.BMP, DES looks for IMAGE002.BMP, IMAGE003.BMP, IMAGE004.BMP, and so on. Assuming they exist, they are displayed in sequential numerical order, at the rate specified by the **framerate** attribute.

## Examples


```XML
<clip src="sample.avi" start="1:05" stop="1:42.5" mstart="30" />
```



## See also

<dl> <dt>

[XTL Elements](xtl-elements.md)
</dt> </dl>

 

 



