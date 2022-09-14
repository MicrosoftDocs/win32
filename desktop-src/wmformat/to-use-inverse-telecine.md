---
title: To Use Inverse Telecine
description: To Use Inverse Telecine
ms.assetid: 7752d1ac-34b1-446a-a69c-29463c9e10f7
keywords:
- Windows Media Format SDK,inverse telecine
- Windows Media Format SDK,telecine
- Advanced Systems Format (ASF),inverse telecine
- ASF (Advanced Systems Format),inverse telecine
- Advanced Systems Format (ASF),telecine
- ASF (Advanced Systems Format),telecine
- inverse telecine
- telecine
ms.topic: article
ms.date: 05/31/2018
---

# To Use Inverse Telecine

Telecine is the process of converting film, which has 24 frames per second, to video, which has 60 fields (half frames) per second. This process puts images from each film frame in multiple video fields.

When you digitally encode a video that was created from film by using telecine, the compression process can cause motion artifacts and other degradations in quality. To avoid affecting the quality of the digital output, the Windows Media Video 9 codec supports inverse telecine. When using inverse telecine, the codec reconstructs the original 24 film frames per second from the input video before encoding the content.

To use inverse telecine, you must:

-   Use a profile with a video stream set to 24 frames per second.
-   Know the field configuration of the input video.

To use inverse telecine for an input to the writer, perform the following steps.

1.  Set up the writer as usual. For more information, see [Writing ASF Files](writing-asf-files.md).
2.  Before beginning to write samples, obtain a pointer to the [**IWMWriterAdvanced2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriteradvanced2) interface by calling **IWMWriter::QueryInterface**.
3.  Identify the stream to be reconstructed by calling [**IWMWriterAdvanced2::SetInputSetting**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriteradvanced2-setinputsetting) for the desired input number. Pass g\_wszDeinterlaceMode as the setting and WM\_DM\_DEINTERLACE\_INVERSETELECINE as the value.
4.  Call **SetInputSetting** again to set g\_wszInitialPatternForInverseTelecine.
5.  Write the file as usual.

## Related topics

<dl> <dt>

[**Advanced Topics**](advanced-topics.md)
</dt> <dt>

[**IWMWriter Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriter)
</dt> <dt>

[**IWMWriterAdvanced2 Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmwriteradvanced2)
</dt> </dl>

 

 




