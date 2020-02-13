---
title: To Seek By Frame Number Using the Asynchronous Reader
description: To Seek By Frame Number Using the Asynchronous Reader
ms.assetid: faab6344-3afc-47ff-9107-d2ce36c0a2b8
keywords:
- Advanced Systems Format (ASF),seeking by frame numbers
- ASF (Advanced Systems Format),seeking by frame numbers
- Advanced Systems Format (ASF),asynchronous readers
- ASF (Advanced Systems Format),asynchronous readers
- asynchronous readers,seeking by frame numbers
- video streams,seeking by frame numbers
- video streams,asynchronous readers
ms.topic: article
ms.date: 05/31/2018
---

# To Seek By Frame Number Using the Asynchronous Reader

The asynchronous reader object can be used to seek to the frame numbers of video streams in an ASF file. To use frame-based seeking, the file loaded in the reader must be indexed by frame. Each individual video stream can be indexed. To determine whether a stream has been indexed by frame, you can check the g\_wszWMNumberOfFrames attribute in the header of the file by calling [**IWMHeaderInfo::GetAttributeByName**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo-getattributebyname).

To seek data in an ASF file by frame number using the asynchronous reader, perform the following steps.

1.  Obtain a pointer to the [**IWMReaderAdvanced3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced3) interface of the reader object by calling **IWMReader::QueryInterface**.
2.  Set the starting frame number and duration by calling [**IWMReaderAdvanced3::StartAtPosition**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced3-startatposition). You must specify the stream number of a frame-indexed video stream. The reader will synchronize the rest of the outputs to the presentation time of the specified frame of the specified stream and begin delivering output samples.
3.  Handle the samples as you normally would in your implementation of the **IWMReaderCallback::OnSample** method.

## Related topics

<dl> <dt>

[**Reading Files with the Asynchronous Reader**](reading-files-with-the-asynchronous-reader.md)
</dt> <dt>

[**Reading Metadata at Playback**](reading-metadata-at-playback.md)
</dt> <dt>

[**Working with Indexes**](working-with-indexes.md)
</dt> </dl>

 

 




