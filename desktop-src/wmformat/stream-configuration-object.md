---
title: Stream Configuration Object
description: Stream Configuration Object
ms.assetid: '228e334c-9d9b-4604-a225-73af7af3255f'
keywords: ["Windows Media Format SDK,stream configuration objects", "Advanced Systems Format (ASF),stream configuration objects", "ASF (Advanced Systems Format),stream configuration objects", "objects,stream configuration objects", "stream configuration objects", "streams,stream configuration objects"]
---

# Stream Configuration Object

A stream configuration object is used to specify the properties of a media stream in an ASF file. Stream configuration objects can be created for existing streams in a profile or can be created empty, ready to receive new data. Stream configuration objects cannot exist independently of a profile object. To save the contents of a stream configuration object, you must call either [**IWMProfile::AddStream**](iwmprofile-addstream.md) to add a new stream or [**IWMProfile::ReconfigStream**](iwmprofile-reconfigstream.md) to save changes made to an existing stream.

To create a stream configuration object, use one of the following methods.



| Method                                                                | Description                                                                                                                      |
|-----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**IWMProfile::CreateNewStream**](iwmprofile-createnewstream.md)     | Creates a stream configuration object without any data.                                                                          |
| [**IWMProfile::GetStream**](iwmprofile-getstream.md)                 | Creates a stream configuration object populated with data from a profile. Uses the stream index to identify the desired stream.  |
| [**IWMProfile::GetStreamByNumber**](iwmprofile-getstreambynumber.md) | Creates a stream configuration object populated with data from a profile. Uses the stream number to identify the desired stream. |



 

All of the methods in the preceding table set a pointer to an **IWMStreamConfig** interface. The other interfaces of the stream configuration object can be obtained by calling the **QueryInterface** method.

The following interfaces are supported by the stream configuration object.



| Interface                                        | Description                                                                                                                  |
|--------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| [**IWMMediaProps**](iwmmediaprops.md)           | Sets and retrieves the [**WM\_MEDIA\_TYPE**](wm-media-type.md) structure for the stream.                                    |
| [**IWMPropertyVault**](iwmpropertyvault.md)     | Sets and retrieves properties that are not required for all streams, like variable bit rate (VBR) settings.                  |
| [**IWMStreamConfig**](iwmstreamconfig.md)       | Sets and retrieves all of the basic information about a stream.                                                              |
| [**IWMStreamConfig2**](iwmstreamconfig2.md)     | Configures the types of data unit extensions associated with the stream. Inherits all of the methods of **IWMStreamConfig**. |
| [**IWMStreamConfig3**](iwmstreamconfig3.md)     | Sets and retrieves the language for the stream. Inherits all of the methods of **IWMStreamConfig** and **IWMStreamConfig2**. |
| [**IWMVideoMediaProps**](iwmvideomediaprops.md) | Manages the properties of a video stream. This is an optional interface, and is available only for video streams.            |



 

## Related topics

<dl> <dt>

[**Configuring Streams**](configuring-streams.md)
</dt> <dt>

[**Objects**](objects.md)
</dt> <dt>

[**Profile Manager Object**](profile-manager-object.md)
</dt> </dl>

 

 




