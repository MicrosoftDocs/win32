---
title: Input Media Properties Object
description: Input Media Properties Object
ms.assetid: e7aa6c99-b6b3-4e5b-869d-3387f70dad87
keywords:
- Windows Media Format SDK,input media properties objects
- Advanced Systems Format (ASF),input media properties objects
- ASF (Advanced Systems Format),input media properties objects
- objects,input media properties objects
- input media properties objects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Input Media Properties Object

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

An input media properties object created by the writer object supports the following interfaces. These interfaces are accessed by a call to **QueryInterface** on one of the interfaces of the writer object.



| Interface                                        | Description                                                                                                |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**IWMInputMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwminputmediaprops) | Retrieves the properties of an input stream.                                                               |
| [**IWMMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmediaprops)           | Used as the base interface for the other media-property interfaces (input, output, and video).             |
| [**IWMVideoMediaProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nn-wmsdkidl-iwmvideomediaprops) | Manages the properties of a video stream. This is an optional interface, available only for video streams. |



 

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Writer Object**](writer-object.md)
</dt> </dl>

 

 




