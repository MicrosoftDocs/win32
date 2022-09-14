---
title: Writing Video Image Samples
description: Writing Video Image Samples
ms.assetid: 1d375186-230a-4a18-a995-b331c72a76e7
keywords:
- Advanced Systems Format (ASF),writing video image samples
- ASF (Advanced Systems Format),writing video image samples
- video images,writing samples
- streams,writing video image samples
- codecs,writing video image samples
ms.topic: article
ms.date: 05/31/2018
---

# Writing Video Image Samples

A Video Image stream is a video that contains a series of still images. The images can move within the frame, and each image can blend into the next. Video Image streams are encoded using the Windows Media Video 9 Image v2 codec. The output video is similar to that created by the Windows Media Video 9 codec.

To create a profile that contains a Video Image stream, start by enumerating the video codecs as described in [Getting Stream Configuration Information from Codecs](getting-stream-configuration-information-from-codecs.md). Search for the codec that supports the WMMEDIASUBTYPE\_WVP2 subtype.

After you set the profile on the writer object, call [**IWMWriter::GetInputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-getinputprops) to get the media properties for the Video Image input stream. Get the media type from the media properties object, by calling [**IWMMediaProps::GetMediaType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmediaprops-getmediatype), and change the subtype to WMMEDIASUBTYPE\_VIDEOIMAGE. You should set the video width and height to the maximum dimensions needed to encompass the images you will add to the stream. Then call [**IWMMediaProps::SetMediaType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmediaprops-setmediatype) with the modified input type. Now you are ready to begin sending samples to the writer object.

Each sample must begin with a **WMT\_VIDEOIMAGE\_SAMPLE2** structure. Additionally, samples may contain bitmap images. An image is only attached to a sample for the first frame in which it appears. All additional frames using that image need only information in the structure. Input bitmaps must be formatted as RGB, 24 bits per pixel.

Bitmap files store the image data so that the data for each row of the image takes a number of bytes divisible by four. (This is called the stride of the bitmap.) This forces the beginning of every row of video to a **DWORD** boundary, which makes copying more efficient. If the image rows are not evenly divisible by four, the row is padded to the next highest multiple of four bytes. When you attach image data, you must remove any padding that exists at the end of the data for each row.

The Windows Media Video 9 Image v2 codec maintains up to two images in memory at a time. These images are called the previous image and the current image. Each image has a set of members in the **WMT\_VIDEOIMAGE\_SAMPLE2** structure, which dictate how the image is presented in the frame. You can add an image by setting the dwControlFlags member of **WMT\_VIDEOIMAGE\_SAMPLE2** to WMT\_VIDEOIMAGE\_SAMPLE\_INPUT\_FRAME. When you pass an input frame to the codec, that image becomes the current image. The image that was the current image in the previous sample usually becomes the previous image, and the image that was the previous image in the previous sample is discarded. You can configure the codec to retain the old previous image by setting the **bKeepPrevImage** member to **TRUE**. In that case, the image that was the current image in the previous sample is discarded.

The basic composition of a Video Image frame is determined by two factors for each image: region of interest and blend coefficient. The region of interest for an image is defined by an origin point, width, and height. The part of an image described by the region of interest fills the output frame. If the region of interest is a different size than the output frame, the codec resizes it. The blend coefficient of the image determines the blending of the two images. The blend coefficients for the current and previous images must total 1.0. For example, if **fCurrBlendCoef** is set to 0.5 and **fPrevBlendCoef** is set to 0.5, then the output frame is composed of an equal blend of the regions of interest from both images.

By manipulating the region of interest for an image, you can create pan and zoom effects. The blend coefficients enable you to cross-fade (dissolve) between images. In addition to these effects, you can use one of the predefined transitions to create more complex frames. The available transitions are described in the [Video Image Transitions](video-image-transitions.md) section of this documentation. When using a transition, you must configure each frame. The easiest way to do this is to create a function that incrementally changes members of the **WMT\_VIDEOIMAGE\_SAMPLE2** structure for a complete effect.

For more information about the values to set for deformations, see [**WMT\_VIDEOIMAGE\_SAMPLE2**](/previous-versions/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-wmt_videoimage_sample2).

**Note** If you want to include audio in a file with a Video Image stream, you must use uncompressed audio input. To combine a Video Image stream with an existing compressed audio stream, you must decompress the audio and pass the samples in uncompressed. If you pass compressed samples to the writer when writing a Video Image stream, an error will occur, resulting in samples being dropped from the video.

Also, compressed Video Image files with no audio streams can contain several very small, highly compressed video frames in a single ASF packet, which can result in a poor playback experience on previous versions of Windows Media Player. To avoid this problem, the best solution is to insert a silent audio stream into the file, although this will also increase the file size.

## Related topics

<dl> <dt>

[**Video Image**](video-image.md)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




