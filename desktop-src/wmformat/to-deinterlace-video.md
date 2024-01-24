---
title: To Deinterlace Video
description: To Deinterlace Video
ms.assetid: 60e6af09-fde1-4e4a-b54c-4923c0549b6b
keywords:
- Windows Media Format SDK,deinterlaced video
- Windows Media Format SDK,inverse telecine
- Windows Media Format SDK,telecine
- Advanced Systems Format (ASF),deinterlaced video
- ASF (Advanced Systems Format),deinterlaced video
- Advanced Systems Format (ASF),inverse telecine
- ASF (Advanced Systems Format),inverse telecine
- Advanced Systems Format (ASF),telecine
- ASF (Advanced Systems Format),telecine
- deinterlaced video
- inverse telecine,about
- telecine,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# To Deinterlace Video

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Some sources of video, such as video capture cards, deliver video data for interlaced display. Each frame of interlaced video is made up of two fields. The top field contains the first line of video and every other line thereafter. The bottom field contains the second line of video and every other line thereafter. So one field contains all of the even numbered lines and the other contains all of the odd numbered lines. The fields that make up a frame represent slightly different presentation times so that, when interleaved, they do not form a static image.

When you want to display video on a computer monitor, each frame of the video should be displayed as one image (this method of displaying video one whole frame at a time is called *progressive* video.) If you display interlaced video progressively, the frames may not look right, because of the time difference between the two fields. The Windows Media Video codec and the Windows Media Video Advanced Profile codec both support a preprocessing feature that converts interlaced content into progressive frames.

To have the codec deinterlace input video, call the [**IWMWriterAdvanced2::SetInputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced2-setinputsetting) method. The setting to use is g\_wszDeinterlaceMode. Set the deinterlacing mode to one of the following values.




| Value | Description | 
|-------|-------------|
| WM_DM_NOTINTERLACED | Input is progressive. Use this setting to stop deinterlacing when you have previously set the deinterlacing mode to another value. | 
| WM_DM_DEINTERLACE_NORMAL | Select this mode to blend the even and odd fields of an interlaced frame (using a motion compensation mechanism).Benefits:<br /><ul><li>The interlace artifacts of the progressive display are significantly reduced.</li><li>The Windows Media Video codec produces higher quality compressed video.</li></ul> | 
| WM_DM_DEINTERLACE_HALFSIZE | Select this mode when the output resolution is half, or less, of the input resolution. For example, use this mode when the input video resolution is 640 x 480 pixels and the output video resolution is 320 x 240 pixels.Benefits:<br /><ul><li>The interlace artifacts of the progressive display are significantly reduced.</li></ul> | 
| WM_DM_DEINTERLACE_HALFSIZEDOUBLERATE | Select this mode when the output resolution is half, or less, of the input resolution and the output <a href="wmformat-glossary.md"><em>frame rate</em></a> is twice as high. For example, use this mode when the input video resolution is 640 x 480 pixels at 30 interlaced frames/sec and the output video resolution is 320 x 240 pixels at 60 frames/sec.Benefits:<br /><ul><li>This produces progressive frames of high quality, because each field is converted to a frame and so there is no need to blend any information.</li><li>The full motion of the interlaced fields is captured.</li></ul> | 
| WM_DM_DEINTERLACE_INVERSETELECINE | Select this mode to convert telecined 30 frames/sec video into the 24 frames/sec of the original film.Benefits:<br /><ul><li>The compression quality improves significantly because only 24 frames/sec instead of 30 frames/sec need to be encoded.</li><li>Because the result is progressive, the same compression and display benefits of deinterlacing are realized.</li></ul> | 
| WM_DM_DEINTERLACE_VERTICALHALFSIZEDOUBLERATE | Select this mode when the vertical output resolution is half, or less, of the input vertical resolution and the output <a href="wmformat-glossary.md"><em>frame rate</em></a> is twice as high. For example, the input vertical video resolution is 640 x 480 pixels at 30 interlaced frames/sec and the output vertical video resolution is 320 x 240 pixels at 60 frames/sec.Benefits:<br /><ul><li>This produces progressive frames of high quality, because each field is converted to a frame and so there is no need to blend any information.</li><li>The full motion of the interlaced fields is captured.</li></ul> | 




 

For mixed content, set the deinterlacing mode as needed before passing samples of a new type. For example, to start encoding with progressive input, you don't need to set any deinterlacing mode. If some samples then require normal deinterlacing, you must set the deinterlacing mode to WM\_DM\_DEINTERLACE\_NORMAL. To then process additional progressive samples you must set the deinterlacing mode to WM\_DM\_NOTINTERLACED.

## Inverse Telecine Settings

For a description of inverse telecine, see [To Use Inverse Telecine](to-use-inverse-telecine.md).

If you set the deinterlacing mode to WM\_DM\_DEINTERLACE\_INVERSETELECINE, you can specify the telecine pattern of the first input frame by calling the [**IWMWriterAdvanced2::SetInputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced2-setinputsetting). The setting to use is g\_wszInitialPatternForInverseTelecine. Set the initial pattern to one of the following values.



| Value                                              | Description                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WM\_DM\_IT\_DISABLE\_COHERENT\_MODE                | Specifies that the input media has gone through the telecine process but that the frames are no longer in a predictable pattern. This usually indicates that the media was edited after the telecine processing. When you use this setting, the codec attempts to reconstruct the original frames on its own. |
| WM\_DM\_IT\_FIRST\_FRAME\_IN\_CLIP\_IS\_AA\_TOP    | Specifies that the top field of the AA frame is the first sample.                                                                                                                                                                                                                                             |
| WM\_DM\_IT\_FIRST\_FRAME\_IN\_CLIP\_IS\_BB\_TOP    | Specifies that the top field of the BB frame is the first sample.                                                                                                                                                                                                                                             |
| WM\_DM\_IT\_FIRST\_FRAME\_IN\_CLIP\_IS\_BC\_TOP    | Specifies that the top field of the BC frame is the first sample.                                                                                                                                                                                                                                             |
| WM\_DM\_IT\_FIRST\_FRAME\_IN\_CLIP\_IS\_CD\_TOP    | Specifies that the top field of the CD frame is the first sample.                                                                                                                                                                                                                                             |
| WM\_DM\_IT\_FIRST\_FRAME\_IN\_CLIP\_IS\_DD\_TOP    | Specifies that the top field of the DD frame is the first sample.                                                                                                                                                                                                                                             |
| WM\_DM\_IT\_FIRST\_FRAME\_IN\_CLIP\_IS\_AA\_BOTTOM | Specifies that the bottom field of the AA frame is the first sample.                                                                                                                                                                                                                                          |
| WM\_DM\_IT\_FIRST\_FRAME\_IN\_CLIP\_IS\_BB\_BOTTOM | Specifies that the bottom field of the BB frame is the first sample.                                                                                                                                                                                                                                          |
| WM\_DM\_IT\_FIRST\_FRAME\_IN\_CLIP\_IS\_BC\_BOTTOM | Specifies that the bottom field of the BC frame is the first sample.                                                                                                                                                                                                                                          |
| WM\_DM\_IT\_FIRST\_FRAME\_IN\_CLIP\_IS\_CD\_BOTTOM | Specifies that the bottom field of the CD frame is the first sample.                                                                                                                                                                                                                                          |
| WM\_DM\_IT\_FIRST\_FRAME\_IN\_CLIP\_IS\_DD\_BOTTOM | Specifies that the bottom field of the DD frame is the first sample.                                                                                                                                                                                                                                          |



 

## Related topics

<dl> <dt>

[**Advanced Topics**](advanced-topics.md)
</dt> </dl>

 

 





