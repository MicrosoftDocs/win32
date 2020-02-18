---
title: To Seek By Time Using the Asynchronous Reader
description: To Seek By Time Using the Asynchronous Reader
ms.assetid: 731b0a6e-1472-45a7-998c-e395be86036f
keywords:
- Advanced Systems Format (ASF),seeking by time
- ASF (Advanced Systems Format),seeking by time
- Advanced Systems Format (ASF),asynchronous readers
- ASF (Advanced Systems Format),asynchronous readers
- asynchronous readers,seeking by time
ms.topic: article
ms.date: 05/31/2018
---

# To Seek By Time Using the Asynchronous Reader

If you want to seek to a specific presentation time in an ASF file, the file must be properly configured. You can seek in audio only files by default, but video files need to be indexed before seeking. If you are not sure about how a file has been created, you can check the g\_wszWMSeekable attribute in the header of the file by calling [**IWMHeaderInfo::GetAttributeByName**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmheaderinfo-getattributebyname).

To seek to data in an ASF file by presentation time using the asynchronous reader, call [**IWMReader::Start**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmreader-start), passing the desired time and duration of the part of the file you want to read as *cnsStart* and *cnsDuration* respectively.

## Related topics

<dl> <dt>

[**IWMReader Interface**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmreader)
</dt> <dt>

[**Reading Files with the Asynchronous Reader**](reading-files-with-the-asynchronous-reader.md)
</dt> <dt>

[**Reading Metadata at Playback**](reading-metadata-at-playback.md)
</dt> <dt>

[**Working with Indexes**](working-with-indexes.md)
</dt> </dl>

 

 




