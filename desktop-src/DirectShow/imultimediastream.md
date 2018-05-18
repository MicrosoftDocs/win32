---
Description: 'Note  This interface is deprecated.'
ms.assetid: '8be6c74f-9290-48b4-ad66-8d7d7cc94174'
title: IMultiMediaStream interface
---

# IMultiMediaStream interface

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

The `IMultiMediaStream` interface is exposed by the AMMultimediaStream object. It contains methods for enumerating the media streams, retrieving information about them, and running and stopping them.

## Members

The **IMultiMediaStream** interface inherits from the [**IUnknown**](com.iunknown) interface. **IMultiMediaStream** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMultiMediaStream** interface has these methods.



| Method                                                                           | Description                                                                                   |
|:---------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| [**EnumMediaStreams**](imultimediastream-enummediastreams.md)                   | Retrieves a media stream, specified by index.<br/>                                      |
| [**GetDuration**](imultimediastream-getduration.md)                             | Retrieves the duration of the multimedia stream.<br/>                                   |
| [**GetEndOfStreamEventHandle**](imultimediastream-getendofstreameventhandle.md) | Retrieves an event that is signaled when the multimedia stream completes playback.<br/> |
| [**GetInformation**](imultimediastream-getinformation.md)                       | Retrieves the capabilities of the multimedia stream object.<br/>                        |
| [**GetMediaStream**](imultimediastream-getmediastream.md)                       | Retrieves a media stream, specified by purpose ID.<br/>                                 |
| [**GetState**](imultimediastream-getstate.md)                                   | Retrieves the current state of the multimedia stream object.<br/>                       |
| [**GetTime**](imultimediastream-gettime.md)                                     | Retrieves the current stream time.<br/>                                                 |
| [**Seek**](imultimediastream-seek.md)                                           | Seeks all of the media streams to a new position.<br/>                                  |
| [**SetState**](imultimediastream-setstate.md)                                   | Runs or stops the multimedia stream object.<br/>                                        |



 

## See also

<dl> <dt>

[**IAMMultiMediaStream Interface**](iammultimediastream.md)
</dt> </dl>

 

 




