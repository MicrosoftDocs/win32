---
title: Stream Configuration Object
description: Stream Configuration Object
ms.assetid: 228e334c-9d9b-4604-a225-73af7af3255f
keywords:
- Windows Media Format SDK,stream configuration objects
- Advanced Systems Format (ASF),stream configuration objects
- ASF (Advanced Systems Format),stream configuration objects
- objects,stream configuration objects
- stream configuration objects
- streams,stream configuration objects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Stream Configuration Object

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A stream configuration object is used to specify the properties of a media stream in an ASF file. Stream configuration objects can be created for existing streams in a profile or can be created empty, ready to receive new data. Stream configuration objects cannot exist independently of a profile object. To save the contents of a stream configuration object, you must call either [**IWMProfile::AddStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-addstream) to add a new stream or [**IWMProfile::ReconfigStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-reconfigstream) to save changes made to an existing stream.

To create a stream configuration object, use one of the following methods.



| Method                                                                | Description                                                                                                                      |
|-----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**IWMProfile::CreateNewStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-createnewstream)     | Creates a stream configuration object without any data.                                                                          |
| [**IWMProfile::GetStream**](/previous-versions/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstream)                 | Creates a stream configuration object populated with data from a profile. Uses the stream index to identify the desired stream.  |
| [**IWMProfile::GetStreamByNumber**](/previous-versions/windows/desktop/api/wmsdkidl/nf-wmsdkidl-iwmprofile-getstreambynumber) | Creates a stream configuration object populated with data from a profile. Uses the stream number to identify the desired stream. |



 

All of the methods in the preceding table set a pointer to an **IWMStreamConfig** interface. The other interfaces of the stream configuration object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the stream configuration object.



| Interface                                        | Description                                                                                                                  |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [**IWMMediaProps**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmediaprops)           | Sets and retrieves the [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type) structure for the stream.                                    |
| [**IWMPropertyVault**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmpropertyvault)     | Sets and retrieves properties that are not required for all streams, like variable bit rate (VBR) settings.                  |
| [**IWMStreamConfig**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig)       | Sets and retrieves all of the basic information about a stream.                                                              |
| [**IWMStreamConfig2**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig2)     | Configures the types of data unit extensions associated with the stream. Inherits all of the methods of **IWMStreamConfig**. |
| [**IWMStreamConfig3**](/previous-versions/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig3)     | Sets and retrieves the language for the stream. Inherits all of the methods of **IWMStreamConfig** and **IWMStreamConfig2**. |
| [**IWMVideoMediaProps**](/previous-versions/windows/desktop/api/Wmsdkidl/nn-wmsdkidl-iwmvideomediaprops) | Manages the properties of a video stream. This is an optional interface, and is available only for video streams.            |



 

## Related topics

<dl> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Profile Manager Object**](profile-manager-object.md)
</dt> </dl>

 

 




