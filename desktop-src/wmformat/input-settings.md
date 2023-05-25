---
title: Input Settings
description: Input Settings
ms.assetid: 23adbb64-5733-4198-8f2b-d02052ddb848
keywords:
- Windows Media Format SDK,global constants
- Advanced Systems Format (ASF),global constants
- ASF (Advanced Systems Format),global constants
- global constants,list of
- Windows Media Format SDK,constants
- Advanced Systems Format (ASF),constants
- ASF (Advanced Systems Format),constants
- constants,list of
- Windows Media Format SDK,input settings
- Advanced Systems Format (ASF),input settings
- ASF (Advanced Systems Format),input settings
- input settings
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Input Settings

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following global constants are used to identify input settings for the writer.



| Global constant                        | WMT\_ATTR\_DATATYPE                                                                                                                       | Description of *pValue*                                                                                                                                                                                                                                                 |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| g\_wszDeinterlaceMode                  | **WMT\_TYPE\_DWORD** set to one of the values in the mode table in the topic [To Deinterlace Video](to-deinterlace-video.md).            | When set, specifies the type of interlaced content of the input. For more information, see [To Deinterlace Video](to-deinterlace-video.md).                                                                                                                            |
| g\_wszFixedFrameRate                   | **WMT\_TYPE\_BOOL**                                                                                                                       | When set to True, instructs the codec not to drop any frames during encoding. This will cause the [*frame rate*](wmformat-glossary.md) of the output video stream to be constant. The frame rate of the input stream does not need to be constant. |
| g\_wszInitialPatternForInverseTelecine | **WMT\_TYPE\_DWORD** set to one of the values in the initial pattern table in the topic [To Deinterlace Video](to-deinterlace-video.md). | When the deinterlace mode is set to WM\_DM\_DEINTERLACE\_INVERSETELECINE, this can be set to specify the pattern of the [*telecine*](wmformat-glossary.md) input. For more information, see [To Deinterlace Video](to-deinterlace-video.md).        |
| g\_wszInterlacedCoding                 | **WMT\_TYPE\_BOOL**                                                                                                                       | When set to True, specifies that that the codec should encode the stream as interlaced content. For more information, see [To Use Interlaced Video](to-use-interlaced-video.md).                                                                                       |
| g\_wszJPEGCompressionQuality           | **WMT\_TYPE\_DWORD**                                                                                                                      | Specifies the JPEG quality level (from 1 to 100) to be used on the input.                                                                                                                                                                                               |
| g\_wszWatermarkCLSID                   | **WMT\_TYPE\_GUID**                                                                                                                       | The value is set to the watermark GUID.                                                                                                                                                                                                                                 |
| g\_wszWatermarkConfig                  | **WMT\_TYPE\_STRING**                                                                                                                     | The value is set to the watermark configuration. This value will vary depending upon the watermarking DMO. Consult the documentation of the watermarking system for more information.                                                                                   |



 

> [!Note]  
> The input settings configured for a stream are not persisted in the written file. If you want your custom reader to have access to these encoding parameters, you must create custom attributes to store them in the file header.

 

## Related topics

<dl> <dt>

[**IWMWriterAdvanced2::GetInputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced2-getinputsetting)
</dt> <dt>

[**IWMWriterAdvanced2::SetInputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced2-setinputsetting)
</dt> </dl>

 

 




