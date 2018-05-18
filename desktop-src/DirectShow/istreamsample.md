---
Description: 'Note  This interface is deprecated.'
ms.assetid: '57818d7d-3290-46f7-a3fd-8585cdd64ec3'
title: IStreamSample interface
---

# IStreamSample interface

> [!Note]  
> This interface is deprecated. New applications should not use it.

 

The `IStreamSample` interface provides control over the behavior of stream samples. You can retrieve the media stream that created the sample, set or retrieve sample start and stop times, check the sample's completion status, and perform a developer-specified function on the sample itself.

Implement this interface when you implement a media stream for a new media type. The interface is exposed on sample objects created by media streams.

Use this interface when you want to control data samples created by [**IMediaStream**](imediastream.md) or its derived interfaces.

In addition to the methods inherited from **IUnknown**, the `IStreamSample` interface exposes the following methods.

## Members

The **IStreamSample** interface inherits from the [**IUnknown**](com.iunknown) interface. **IStreamSample** also has these types of members:

-   [Methods](#methods)

### Methods

The **IStreamSample** interface has these methods.



| Method                                                     | Description                                                                                                                                     |
|:-----------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CompletionStatus**](istreamsample-completionstatus.md) | Retrieves the status of the current sample's latest asynchronous update. If the update isn't complete, you can force it to complete.<br/> |
| [**GetMediaStream**](istreamsample-getmediastream.md)     | Retrieves a pointer to the media stream object that created the current sample.<br/>                                                      |
| [**GetSampleTimes**](istreamsample-getsampletimes.md)     | Retrieves the current sample's start and end times.<br/>                                                                                  |
| [**SetSampleTimes**](istreamsample-setsampletimes.md)     | Sets the current sample's start and end times.<br/>                                                                                       |
| [**Update**](istreamsample-update.md)                     | Performs a synchronous or an asynchronous update on the current sample.<br/>                                                              |



 

 

 




