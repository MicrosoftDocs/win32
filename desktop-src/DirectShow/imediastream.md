---
Description: 'Note  This interface is deprecated.'
ms.assetid: 'c842b841-a4dc-47c8-8186-347aff2c4ac3'
title: IMediaStream interface
---

# IMediaStream interface

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

The **IMediaStream** interface provides access to the characteristics of a media stream, such as the stream's media type and purpose ID. It also has methods that create data samples.

For sample code that implements the multimedia streaming interfaces, see [Multimedia Streaming Sample Code](multimedia-streaming-sample-code.md).

Implement this interface when you want to add media type-specific functionality to your media stream. This interface is implemented on multimedia stream objects. **IMediaStream** provides generic sample-creation methods, but you usually want to write a more powerful version of these methods that will take advantage of your media type's specific characteristics.

Use this interface when your application needs to access a stream's media type information and create data samples.

## Members

The **IMediaStream** interface inherits from the [**IUnknown**](com.iunknown) interface. **IMediaStream** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMediaStream** interface has these methods.



| Method                                                          | Description                                                                                                  |
|:----------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------|
| [**AllocateSample**](imediastream-allocatesample.md)           | Allocates a new stream sample object for the current media stream.<br/>                                |
| [**CreateSharedSample**](imediastream-createsharedsample.md)   | Creates a new stream sample that shares the same backing object as the existing sample.<br/>           |
| [**GetInformation**](imediastream-getinformation.md)           | Retrieves the stream's purpose ID and media type.<br/>                                                 |
| [**GetMultiMediaStream**](imediastream-getmultimediastream.md) | Retrieves a pointer to the multimedia stream that contains the specified media stream.<br/>            |
| [**SendEndOfStream**](imediastream-sendendofstream.md)         | Forces the current stream to end. If the current stream isn't writable, this method does nothing.<br/> |
| [**SetSameFormat**](imediastream-setsameformat.md)             | Sets the media stream to the same format as a previous stream.<br/>                                    |



 

 

 




