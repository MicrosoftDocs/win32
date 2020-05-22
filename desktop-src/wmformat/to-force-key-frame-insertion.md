---
title: To Force Key-Frame Insertion
description: To Force Key-Frame Insertion
ms.assetid: 456482da-aaa2-41f8-93f7-c0fa5abe7dd2
keywords:
- Advanced Systems Format (ASF),forcing key-frame insertions
- ASF (Advanced Systems Format),forcing key-frame insertions
- Advanced Systems Format (ASF),key-frame insertions
- ASF (Advanced Systems Format),key-frame insertions
- key frames
ms.topic: article
ms.date: 05/31/2018
---

# To Force Key-Frame Insertion

The Windows Media Video 9 codec supports forced key-frame insertion. When you pass a sample to the writer, you can specify that it must be encoded as a [*key frame*](wmformat-glossary.md).

To force key-frame insertion for a sample, perform the following steps.

1.  Allocate a buffer to hold the sample, and retrieve a pointer to the [**INSSBuffer**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer) interface containing the buffer by calling [**IWMWriter::AllocateSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-allocatesample).
2.  Retrieve the location and size of the buffer created in step 1 by calling [**INSSBuffer::GetBufferAndLength**](/previous-versions/windows/desktop/api/Wmsbuffer/nf-wmsbuffer-inssbuffer-getbufferandlength).
3.  Copy your sample data to the buffer location, making sure that the sample passed will fit in the allocated buffer. Depending upon the source of your samples, you can use a variety of functions to copy the data. For example, if you are copying a stream from an AVI file, you can use the AVI function, **AVIStreamRead**.
4.  Update the amount of data used in the buffer to reflect the actual size of the sample by calling [**INSSBuffer::SetLength**](/previous-versions/windows/desktop/api/Wmsbuffer/nf-wmsbuffer-inssbuffer-setlength).
5.  Obtain a pointer to the [**INSSBuffer3**](/previous-versions/windows/desktop/api/wmsbuffer/nn-wmsbuffer-inssbuffer3) interface by calling **INSSBuffer::QueryInterface**.
6.  Set the sample as a forced key frame by calling the [**INSSBuffer3::SetProperty**](/previous-versions/windows/desktop/api/Wmsbuffer/nf-wmsbuffer-inssbuffer3-setproperty) method to set the WM\_SampleExtensionGUID\_OutputCleanPoint property. This property is a Boolean value; set it to **TRUE**.
7.  Pass the buffer interface to the writer along with the input number and sample time by using the [**IWMWriter::WriteSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-writesample) method.

## Related topics

<dl> <dt>

[**IWMWriter::WriteSample**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmwriter-writesample)
</dt> <dt>

[**To Write Samples**](to-write-samples.md)
</dt> <dt>

[**Variable Bit Rate (VBR) Encoding**](variable-bit-rate--vbr--encoding.md)
</dt> <dt>

[**Writing ASF Files**](writing-asf-files.md)
</dt> </dl>

 

 




