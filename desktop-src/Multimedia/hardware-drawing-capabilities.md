---
title: Hardware Drawing Capabilities
description: Hardware Drawing Capabilities
ms.assetid: 3a26de73-cb9e-41a0-8c33-a7cca7d6058e
keywords:
- video compression manager (VCM),drawing
- VCM (video compression manager),drawing
- ICGetInfo function
ms.topic: article
ms.date: 05/31/2018
---

# Hardware Drawing Capabilities

Some renderers can draw directly to video hardware as they decompress video frames. These renderers return the VIDCF\_DRAW flag in response to the [**ICGetInfo**](/windows/desktop/api/Vfw/nf-vfw-icgetinfo) function. When using this type of renderer, your application does not have to handle the decompressed data. It lets the renderer retain the decompressed data for drawing.

If your application uses a renderer with drawing capabilities, it must handle the following tasks:

-   Select a renderer.
-   Specify image formats.
-   Initialize the renderer.
-   Draw the data.
-   Control drawing parameters.

## Renderer Selection

The [**ICDrawOpen**](/windows/desktop/api/Vfw/nf-vfw-icdrawopen) macro opens a renderer that can draw images with the specified format. It returns a handle of a renderer if it is successful, or zero otherwise. This macro uses the [**ICLocate**](/windows/desktop/api/Vfw/nf-vfw-iclocate) function to open the renderer.

## Specifying Image Formats

Because your application does not need to draw the decompressed data, it does not require a specific output format. It must, however, ensure that the renderer can draw using the input format by using the [**ICM\_DRAW\_QUERY**](icm-draw-query.md) message (or use the [**ICDrawQuery**](/windows/desktop/api/Vfw/nf-vfw-icdrawquery) macro). This message cannot determine if a renderer can draw a bitmap. If your application must determine if the renderer can draw the bitmap, use this message with the [**ICDrawBegin**](/windows/desktop/api/Vfw/nf-vfw-icdrawbegin) function.

Your application can have a renderer suggest an input format by using the [**ICDrawSuggestFormat**](/windows/desktop/api/Vfw/nf-vfw-icdrawsuggestformat) function. This function is used when a renderer separates the drawing capabilities from the decompressing capabilities. Most applications using the drawing functions will not need to determine the output format.

## Renderer Initialization

The [**ICDrawBegin**](/windows/desktop/api/Vfw/nf-vfw-icdrawbegin) function initializes a renderer and tells it the drawing destination. This function can also perform the following tasks:

-   Determine whether the renderer supports a specific input format.
-   Specify whether the drawing operation occupies a window or the entire screen.
-   Specify the part of the image to display using the source rectangle.
-   Define the playback rate of the image sequence.

Some renderers buffer the compressed data to operate more efficiently. Your application can send the [**ICM\_GETBUFFERSWANTED**](icm-getbufferswanted.md) message (or use the [**ICGetBuffersWanted**](/windows/desktop/api/Vfw/nf-vfw-icgetbufferswanted) macro) to determine the number of buffers the renderer requests. Your application should preload these buffers and send them to the renderer before drawing.

## Drawing the Data

You can use the [**ICDraw**](/windows/desktop/api/Vfw/nf-vfw-icdraw) function to decompress the data for drawing. The renderer, however, does not start drawing data until your application sends the [**ICM\_DRAW\_START**](icm-draw-start.md) message (or uses the [**ICDrawStart**](/windows/desktop/api/Vfw/nf-vfw-icdrawstart) macro). When your application calls this function, the renderer begins to draw the frames at the rate specified by the *dwRate* parameter divided by the *dwScale* parameter; these parameters were supplied when the application initialized the renderer by using the [**ICDrawBegin**](/windows/desktop/api/Vfw/nf-vfw-icdrawbegin) function. Drawing continues until your application sends the [**ICM\_DRAW\_STOP**](icm-draw-stop.md) message (or uses the [**ICDrawStop**](/windows/desktop/api/Vfw/nf-vfw-icdrawstop) macro).

> [!Note]  
> If a renderer buffers the data before drawing, your application should not use the **ICDrawStart** macro until it has sent the number of frames the renderer returned for the **ICGetBuffersWanted** macro.

 

The *lTime* parameter of [**ICDraw**](/windows/desktop/api/Vfw/nf-vfw-icdraw) specifies the time to draw a frame. The renderer divides this integer by the time scale specified with [**ICDrawBegin**](/windows/desktop/api/Vfw/nf-vfw-icdrawbegin) to obtain the actual time. Times for **ICDraw** functions are relative to **ICDrawStart**. **ICDrawStart** sets the clock to zero. For example, if your application specifies 1000 for the time scale and 75 for *lTime*, the renderer draws the frame 75 milliseconds into the sequence.

## Controlling Drawing Parameters

You can monitor the clock of a renderer by sending the [**ICM\_DRAW\_GETTIME**](icm-draw-gettime.md) message (or use the [**ICDrawGetTime**](/windows/desktop/api/Vfw/nf-vfw-icdrawgettime) macro), and you can set the clock of a renderer that can draw data by sending the [**ICM\_DRAW\_SETTIME**](icm-draw-settime.md) message (or use the [**ICDrawSetTime**](/windows/desktop/api/Vfw/nf-vfw-icdrawsettime) macro).

To change the current position while a renderer is drawing, your application can send the [**ICM\_DRAW\_WINDOW**](icm-draw-window.md) message (or use the [**ICDrawWindow**](/windows/desktop/api/Vfw/nf-vfw-icdrawwindow) macro) for repositioning the window. Applications typically use this message whenever the window changes.

If the playback window gets a realize-palette message, your application must send the [**ICM\_DRAW\_REALIZE**](icm-draw-realize.md) message (or use the [**ICDrawRealize**](/windows/desktop/api/Vfw/nf-vfw-icdrawrealize) macro) to have the renderer realize the palette again for playback. Applications can change the palette by sending the [**ICM\_DRAW\_CHANGEPALETTE**](icm-draw-changepalette.md) message (or use the [**ICDrawChangePalette**](/windows/desktop/api/Vfw/nf-vfw-icdrawchangepalette) macro) and obtain the current palette by sending the [**ICM\_DRAW\_GET\_PALETTE**](icm-draw-get-palette.md) message.

Some renderers must be specifically instructed to display frames passed to them. Sending the [**ICM\_DRAW\_RENDERBUFFER**](icm-draw-renderbuffer.md) message (or use the [**ICDrawRenderBuffer**](/windows/desktop/api/Vfw/nf-vfw-icdrawrenderbuffer) macro) causes these renderers to draw the frame.

 

 




