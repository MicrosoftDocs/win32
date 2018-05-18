---
Description: 'After beginning preview of a video stream, call the IWiaVideo::TakePicture method of the IWiaVideo interface to capture a still image from the streaming video.'
ms.assetid: '2b8c465b-0dbf-4741-a701-200862cc3de3'
title: Capturing a Still Image from a Video Stream
---

# Capturing a Still Image from a Video Stream

After beginning preview of a video stream, call the [**IWiaVideo::TakePicture**](-wia-iwiavideo-takepicture.md) method of the [**IWiaVideo**](-wia-iwiavideo.md) interface to capture a still image from the streaming video. For instructions on how to get an **IWiaVideo** pointer and begin previewing streaming video, see [Previewing Video](-wia-previewing-video.md).

When the [**IWiaVideo::TakePicture**](-wia-iwiavideo-takepicture.md) method returns, the *pbstrNewImageFilename* parameter contains the full path and filename of the resulting image file. The file is in JPEG format. The directory in which the file is created is specified by the value of the [**IWiaVideo::ImagesDirectory**](-wia-iwiavideo-imagesdirectory.md) property of the [**IWiaVideo**](-wia-iwiavideo.md) interface.

> [!Note]  
> Windows Image Acquisition (WIA) does not support video devices in Windows Server 2003, Windows Vista, or later. For those versions of the Windows, use [DirectShow](http://msdn.microsoft.com/en-us/library/ms783323(VS.85).aspx) to acquire images from video.

 

 

 



