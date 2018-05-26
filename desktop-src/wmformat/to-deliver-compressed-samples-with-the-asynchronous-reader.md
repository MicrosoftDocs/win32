---
title: To Deliver Compressed Samples with the Asynchronous Reader
description: To Deliver Compressed Samples with the Asynchronous Reader
ms.assetid: 488baa3c-8863-4afc-89b2-fe55823e5db9
keywords:
- Advanced Systems Format (ASF),delivering compressed samples
- ASF (Advanced Systems Format),delivering compressed samples
- Advanced Systems Format (ASF),asynchronous readers
- ASF (Advanced Systems Format),asynchronous readers
- Advanced Systems Format (ASF),compressed samples
- ASF (Advanced Systems Format),compressed samples
- asynchronous readers,delivering compressed samples
- asynchronous readers,compressed samples
- compressed samples,delivering
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# To Deliver Compressed Samples with the Asynchronous Reader

The asynchronous reader can deliver compressed samples from streams in ASF files. Applications usually deliver compressed samples when copying a stream from one file to another. It is not advisable to recompress data that has been reconstructed from a compressed stream, because data is lost in the encoding process. Digital media that has been compressed more than once will have a noticeable decrease in quality.

The Windows Media Format SDK does not provide any methods for decoding data after it has been extracted from an ASF file. If you receive compressed samples and later want to decompress them, you will have to provide your own code to do so. One way to get around this limitation is to write the compressed samples to a new ASF file and then re-read them into normal, uncompressed samples.

To receive compressed samples with the asynchronous reader, perform the following steps.

1.  Implement the [**IWMReaderCallbackAdvanced::OnStreamSample**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmreadercallbackadvanced-onstreamsample?branch=master) callback. This callback is basically identical in function to [**IWMReaderCallback::OnSample**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmreadercallback-onsample?branch=master) except that it delivers samples by stream number and the samples are still compressed.
2.  Before starting playback, obtain a pointer to the [**IWMReaderAdvanced**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreaderadvanced?branch=master) interface of the reader object by calling **IWMReader::QueryInterface**.
3.  Configure the reader to deliver compressed samples for the desired stream by calling [**IWMReaderAdvanced::SetReceiveStreamSamples**](/windows/win32/Wmsdkidl/nf-wmsdkidl-iwmreaderadvanced-setreceivestreamsamples?branch=master).
4.  Repeat step 3 for each stream for which compressed sample delivery is desired.

> [!Note]  
> Image streams are not valid for compressed stream delivery. If you copy an image stream from one file to another, it will not work in the new file. To copy an image stream from file to file, retrieve the image stream samples by output number and include them in the new file as if including a new image stream.

 

## Related topics

<dl> <dt>

[**IWMReaderCallbackAdvanced Interface**](/windows/win32/wmsdkidl/nn-wmsdkidl-iwmreadercallbackadvanced?branch=master)
</dt> <dt>

[**Reading Files with the Asynchronous Reader**](reading-files-with-the-asynchronous-reader.md)
</dt> </dl>

 

 




