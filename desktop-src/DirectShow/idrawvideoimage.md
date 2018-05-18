---
Description: 'Note  This interface has been deprecated.'
ms.assetid: 'ff412213-60e5-43d8-8cb1-e7ae8b3ca1bc'
title: IDrawVideoImage interface
---

# IDrawVideoImage interface

> [!Note]  
> This interface has been deprecated. New applications should not use it.

 

The `IDrawVideoImage` interface enables an application to draw the same video image in multiple places simultaneously on the screen. The [Video Renderer](video-renderer-filter.md) filter exposes this interface. The Video Mixing Renderer (VMR) filter provides a better way to accomplish the same effect, through the use of multiple input streams.

To use this interface, call **DrawVideoImageBegin** to put the Video Renderer into GDI mode. Then the application can call the **DrawVideoImageDraw** method as often as necessary. The renderer simply takes the current video frame and draws it to the specified rectangle. This process is asynchronous to the delivery of frames to the renderer on the filter graph thread. The application is responsible for the frame rate at which it renders images; this rate will never be the same as the rate of the frames being delivered to the filter. In other words, calling this method is like taking a periodic shapshot of the video and putting it into a device context of your choosing at a rate of your choosing.

## Members

The **IDrawVideoImage** interface inherits from the [**IUnknown**](com.iunknown) interface. **IDrawVideoImage** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDrawVideoImage** interface has these methods.



| Method                                                             | Description                                                                                                                    |
|:-------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------|
| [**DrawVideoImageBegin**](idrawvideoimage-drawvideoimagebegin.md) | Turns off DirectDraw in preparation for a call to [**DrawVideoImageDraw**](idrawvideoimage-drawvideoimagedraw.md).<br/> |
| [**DrawVideoImageDraw**](idrawvideoimage-drawvideoimagedraw.md)   | Draws the specified source rectangle to the specified destination rectangle in the specified GDI device context.<br/>    |
| [**DrawVideoImageEnd**](idrawvideoimage-drawvideoimageend.md)     | Turns DirectDraw back on after drawing has been performed.<br/>                                                          |



 

## See also

<dl> <dt>

[Deprecated Interfaces](deprecated-interfaces.md)
</dt> </dl>

 

 




