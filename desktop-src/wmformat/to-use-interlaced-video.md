---
title: To Use Interlaced Video
description: To Use Interlaced Video
ms.assetid: cb77bac7-bea8-4f1b-8302-fee9a43d4815
keywords:
- Windows Media Format SDK,interlaced video
- Windows Media Format SDK,video encoding interlaced
- Windows Media Format SDK,encoding interlaced video
- Windows Media Format SDK,decoding interlaced video
- Windows Media Format SDK,field order
- Advanced Systems Format (ASF),interlaced video
- ASF (Advanced Systems Format),interlaced video
- Advanced Systems Format (ASF),video encoding interlaced
- ASF (Advanced Systems Format),video encoding interlaced
- Advanced Systems Format (ASF),encoding interlaced video
- ASF (Advanced Systems Format),encoding interlaced video
- Advanced Systems Format (ASF),decoding interlaced video
- ASF (Advanced Systems Format),decoding interlaced video
- Advanced Systems Format (ASF),field order
- ASF (Advanced Systems Format),field order
- interlaced video,about
- interlaced video,encoding
- interlaced video,decoding
- interlaced video,field order
ms.topic: article
ms.date: 05/31/2018
---

# To Use Interlaced Video

There are two basic types of video encoding: progressive and interlaced. In progressive encoding, each frame is an encoded representation of one frame of video. In interlaced encoding, each frame is an encoded representation of either all of the even rows of pixels in the video, or all of the odd rows. Each interlaced frame is called a *field*, so there are odd fields and even fields. An interlaced display (like a television) renders the fields one at a time, alternating fields. A progressive display renders frames all at once.

The Windows Media Video 9 Advanced Profile codec provides support for maintaining interlacing in compressed streams.

## When to Use Interlaced Video

Encoding interlaced video is useful only when the content is displayed on an interlaced device. Content that is intended to be viewed on a television (through a set-top box or other device) may need to be interlaced. Content that is intended to be viewed exclusively on a computer display should not be encoded as interlaced.

To encode interlaced video as progressive video, you must configure input settings. For more information, see [To Deinterlace Video](to-deinterlace-video.md).

## Field Order

Most sources of interlaced video, such as video capture cards, deliver video samples that include both fields interleaved with each other. The result is like a complete frame of video, except that the odd and even lines are shifted slightly in time. There is no universal standard as to which field in the interleaved video sample occurs first in time.

You should enable users to specify field order when passing interlaced samples to your application.

## Encoding Interlaced Video

To use interlaced encoding, perform the following steps:

1.  Configure the video stream in the profile to use the content type data unit extension by calling the [**IWMStreamConfig2::AddDataUnitExtension**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmstreamconfig2-adddataunitextension) method. The sample extension GUID for the content type extension is WM\_SampleExtensionsGUID\_ContentType.
2.  Set the stream in the profile and configure the writer with the profile as normal.
3.  Before passing interlaced samples to the writer, call the [**IWMWriterAdvanced2::SetInputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced2-setinputsetting) method to set the g\_wszInterlacedCoding input setting to **TRUE**.
4.  For every interlaced sample that you pass to the writer, call the [**INSSBuffer3::SetProperty**](/previous-versions/windows/desktop/api/Wmsbuffer/nf-wmsbuffer-inssbuffer3-setproperty) method to set the content type. Content type values are combinations of the flags in the following table.



| Flag                         | Description                                                                                                                                                                                                                                                                                                                                                      |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WM\_CT\_INTERLACED           | Always set this flag when encoding interlaced content. If you use this flag without setting a field-order flag (WM\_CT\_BOTTOM\_FIELD\_FIRST or WM\_CT\_TOP\_FIELD\_FIRST) the codec will assume that the top field is first. If the codec uses the wrong field order, there should be no impact on image quality, but the encoding efficiency will be affected. |
| WM\_CT\_BOTTOM\_FIELD\_FIRST | When combined with the WM\_CT\_INTERLACED flag, this flag indicates that the bottom field (the field starting with the second line in the sample) occurs first in time.                                                                                                                                                                                          |
| WM\_CT\_TOP\_FIELD\_FIRST    | When combined with the WM\_CT\_INTERLACED flag, this flag indicates that the top field (the field starting with the first line in the sample) occurs first in time.                                                                                                                                                                                              |
| WM\_CT\_REPEAT\_FIRST\_FIELD | Indicates that the first field in the sample should be repeated on playback. This flag is used for video that has created from film by the telecine process.If no field-order flag is set in conjunction with this flag, the top field is assumed to occur first in time.<br/>                                                                             |



 

> [!Note]  
> If the WM\_CT\_INTERLACED flag is not set, the sample is assumed to contain a progressive video frame.

 

## Decoding Interlaced Video

When decoding interlaced video, you must set the g\_wszAllowInterlacedOutput setting to **TRUE** using the [**IWMReaderAdvanced2::SetOutputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced2-setoutputsetting) method. Otherwise the codec will deliver progressive frames.

The content type data unit extension is maintained on the output samples. You should pass the field orientation to the rendering device to ensure proper playback.

## Related topics

<dl> <dt>

[**Advanced Topics**](advanced-topics.md)
</dt> </dl>

 

 





