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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Stream Configuration Object

A stream configuration object is used to specify the properties of a media stream in an ASF file. Stream configuration objects can be created for existing streams in a profile or can be created empty, ready to receive new data. Stream configuration objects cannot exist independently of a profile object. To save the contents of a stream configuration object, you must call either [**IWMProfile::AddStream**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-addstream) to add a new stream or [**IWMProfile::ReconfigStream**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-reconfigstream) to save changes made to an existing stream.

To create a stream configuration object, use one of the following methods.



| Method                                                                | Description                                                                                                                      |
|-----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**IWMProfile::CreateNewStream**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-createnewstream)     | Creates a stream configuration object without any data.                                                                          |
| [**IWMProfile::GetStream**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstream)                 | Creates a stream configuration object populated with data from a profile. Uses the stream index to identify the desired stream.  |
| [**IWMProfile::GetStreamByNumber**](/windows/desktop/api/Wmsdkidl/nf-wmsdkidl-iwmprofile-getstreambynumber) | Creates a stream configuration object populated with data from a profile. Uses the stream number to identify the desired stream. |



 

All of the methods in the preceding table set a pointer to an **IWMStreamConfig** interface. The other interfaces of the stream configuration object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the stream configuration object.



| Interface                                        | Description                                                                                                                  |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [**IWMMediaProps**](/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmmediaprops)           | Sets and retrieves the [**WM\_MEDIA\_TYPE**](/windows/desktop/api/Wmsdkidl/ns-wmsdkidl-_wmmediatype) structure for the stream.                                    |
| [**IWMPropertyVault**](/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmpropertyvault)     | Sets and retrieves properties that are not required for all streams, like variable bit rate (VBR) settings.                  |
| [**IWMStreamConfig**](/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig)       | Sets and retrieves all of the basic information about a stream.                                                              |
| [**IWMStreamConfig2**](/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig2)     | Configures the types of data unit extensions associated with the stream. Inherits all of the methods of **IWMStreamConfig**. |
| [**IWMStreamConfig3**](/windows/desktop/api/wmsdkidl/nn-wmsdkidl-iwmstreamconfig3)     | Sets and retrieves the language for the stream. Inherits all of the methods of **IWMStreamConfig** and **IWMStreamConfig2**. |
| [**IWMVideoMediaProps**](/windows/desktop/api/Wmsdkidl/nn-wmsdkidl-iwmvideomediaprops) | Manages the properties of a video stream. This is an optional interface, and is available only for video streams.            |



 

## Related topics

<dl> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Profile Manager Object**](profile-manager-object.md)
</dt> </dl>

 

 




