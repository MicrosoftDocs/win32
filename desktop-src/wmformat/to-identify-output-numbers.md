---
title: To Identify Output Numbers
description: To Identify Output Numbers
ms.assetid: a2135a71-52e6-4f62-8be8-b9886be9b37c
keywords:
- Windows Media Format SDK,identifying output numbers
- Advanced Systems Format (ASF),identifying output numbers
- ASF (Advanced Systems Format),identifying output numbers
- Advanced Systems Format (ASF),output numbers and formats
- ASF (Advanced Systems Format),output numbers and formats
- output numbers and formats,identifying
ms.topic: article
ms.date: 05/31/2018
---

# To Identify Output Numbers

To identify the output numbers for a loaded file, perform the following steps. These procedures are identical for both the asynchronous reader and the synchronous reader. Where interface names vary, the synchronous reader methods are listed in parentheses after the methods of the asynchronous reader.

1.  Create a reader object and load a file for reading. For more information, see [To Create a Reader and Open a File](to-create-a-reader-and-open-a-file.md) (or [To Create a Synchronous Reader and Open a File](to-create-a-synchronous-reader-and-open-a-file.md)).
2.  Retrieve the total number of outputs for the file by calling [**IWMReader::GetOutputCount**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-getoutputcount) (or [**IWMSyncReader::GetOutputCount**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getoutputcount)).
3.  Loop through the outputs one at a time, performing the following steps for each:
    -   Retrieve the [**IWMOutputMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmoutputmediaprops) interface for the current output with a call to [**IWMReader::GetOutputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-getoutputprops) (or [**IWMSyncReader::GetOutputProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmsyncreader-getoutputprops)).
    -   Retrieve the [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type) structure for the output by making two calls to [**IWMMediaProps::GetMediaType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmediaprops-getmediatype). Make the first call to get the size of the structure, then allocate memory for it and pass a pointer to the allocated memory on the second call. Alternatively, you can call [**IWMMediaProps::GetType**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmmediaprops-gettype), which delivers the major type without requiring you to allocate memory for the **WM\_MEDIA\_TYPE** structure. You can skip outputs of the wrong major type.
    -   Retrieve the major media type and media subtype from the **WM\_MEDIA\_TYPE** structure. These values are stored in data members **majortype** and **subtype** respectively.
    -   Check the value of **WM\_MEDIA\_TYPE.formattype**. This specifies the type of structure contained in the buffer at **WM\_MEDIA\_TYPE.pbFormat**. For more information about format types, see [Media Types](media-types.md).
    -   Allocate memory to hold the structure of the type identified in the previous step. Copy the structure to your allocated memory. For audio and video, this structure gives you essential information about how the data should be rendered.

The synchronous reader also provides methods to retrieve associations between output numbers and stream numbers. For more information, see [To Find Stream Numbers and Output Numbers](to-find-stream-numbers-and-output-numbers.md).

## Related topics

<dl> <dt>

[**Inputs, Streams and Outputs**](inputs-streams-and-outputs.md)
</dt> <dt>

[**IWMMediaProps Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmediaprops)
</dt> <dt>

[**IWMOutputMediaProps Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmoutputmediaprops)
</dt> <dt>

[**IWMReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreader)
</dt> <dt>

[**IWMSyncReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmsyncreader)
</dt> <dt>

[**Working with Outputs**](working-with-outputs.md)
</dt> </dl>

 

 




