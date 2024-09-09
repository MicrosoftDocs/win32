---
title: Stream Prioritization Object
description: Stream Prioritization Object
ms.assetid: cb0345ce-6847-435b-8cbb-f8b93856af9f
keywords:
- Windows Media Format SDK,stream prioritization objects
- Advanced Systems Format (ASF),stream prioritization objects
- ASF (Advanced Systems Format),stream prioritization objects
- objects,stream prioritization objects
- stream prioritization objects
- streams,stream prioritization objects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Stream Prioritization Object

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A stream prioritization object is used to specify an order of importance for the streams in a profile. When full playback is not possible due to bit-rate limitations, the lowest priority streams will be the first to be dropped.

Stream prioritization objects can be created for existing stream prioritization data in a profile or can be created empty, ready to receive new data. Stream prioritization objects cannot exist independently of a profile object. To save the contents of a stream prioritization object, you must call [**IWMProfile3::SetStreamPrioritization**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile3-setstreamprioritization). To create a stream prioritization object, use one of the following methods.



| Method                                                                                          | Description                                                                  |
|-------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| [**IWMProfile3::CreateNewStreamPrioritization**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile3-createnewstreamprioritization) | Creates a stream prioritization object without any data.                     |
| [**IWMProfile3::GetStreamPrioritization**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile3-getstreamprioritization)             | Creates a stream prioritization object populated with data from the profile. |



 

Both methods in the preceding table set a pointer to an **IWMStreamPrioritization** interface. This is the only interface supported by the stream prioritization object.



| Interface                                                  | Description                                                          |
|------------------------------------------------------------|----------------------------------------------------------------------|
| [**IWMStreamPrioritization**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamprioritization) | Manages the list of streams within the stream prioritization object. |



 

## Remarks

Only one stream prioritization can exist for a given profile. If you create a new stream prioritization for a profile that already contains a stream prioritization, the old one will be deleted.

## Related topics

<dl> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Profile Object**](profile-object.md)
</dt> <dt>

[**Using Stream Prioritization**](using-stream-prioritization.md)
</dt> </dl>

 

 




