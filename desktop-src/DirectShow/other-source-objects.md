---
description: Other Source Objects
ms.assetid: 67482227-9df6-4e89-b16f-160a0bae6609
title: Other Source Objects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Other Source Objects

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

In addition to video and audio sources, [DirectShow Editing Services](directshow-editing-services.md) (DES) supports the following source objects.

**Still Images**

DES supports the following file formats for still images:

-   Bitmap (.bmp)
-   GIF (Graphics Interchange Format)
-   JPEG (Joint Photographic Experts Group)
-   Targa or Truevision Graphics Adapter (.tga): Mode 2 (uncompressed RGB) in 16-bit, 24,-bit, or 32-bit format.

These files can be used as still images or to create animations. For bitmap, JPEG, and Targa files, if you are using the file as a still image, call the [**IAMTimelineSrc::SetDefaultFPS**](iamtimelinesrc-setdefaultfps.md) method to set the frame rate to zero.

**DIB Sequences**

Given a series of bitmap, JPEG, or Targa files, the render engine can construct a DIB sequence. To create a DIB sequence, give the files numerically sequential names, such as Image001.bmp, Image002.bmp, Image003.bmp, and so on. Use the first file in the sequence as the source. Set the frame rate for the sequence by calling [**IAMTimelineSrc::SetDefaultFPS**](iamtimelinesrc-setdefaultfps.md). The render engine cycles through the images in the sequence at the specified frame rate.

If the sequence is too short to fill the duration, given the frame rate, the rest of the duration is solid black. No error occurs during rendering.

**GIF Sources**

DES supports GIF sources, including animated and transparent GIFs, using the GIF89a specification. With an animated GIF, unlike the other file types, you do not need to set the frame rate. The GIF file specifies the delay between each image in the animation.

To support transparent GIFs, DES converts transparent regions in the image to the RGB triplet RGB(0,0,0). You can then use the [Key Transition](key-transition.md) to key on RGB(0,0,0).

DES also converts any black regions that fall within the range RGB(0–7,0–7,0–7) to the value RGB(8,8,8)—except for the transparency index, if it falls in that range. This conversion is not detectable to the eye.

**Video Color Source**

The [Video Color Source](video-color-source.md) object creates a continuous video image of a solid color. One use for this object is to make it a layer in a transition. For example, use it in a video fade-in or fade-out.

**Custom Source Filters**

DES can use a DirectShow source filter as a timeline source, if the filter meets the following conditions:

-   It supports seeking
-   It produces a format that DES supports. The format can be compressed as long as the user's system has a DirectShow filter capable of decoding it.

To use a custom source, specify the CLSID of the filter as the subobject GUID of the source object. For more information, see [Subobjects](subobjects.md). To support custom properties, implement them as **IDispatch** "put" properties. Only static properties are supported on source objects; dynamic properties are not supported.

## Related topics

<dl> <dt>

[Working with Sources](working-with-sources.md)
</dt> </dl>

 

 



