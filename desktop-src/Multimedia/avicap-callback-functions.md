---
title: AVICap Callback Functions
description: AVICap Callback Functions
ms.assetid: d238a238-9702-4ba6-92bd-5ef1605b4983
keywords:
- AVICap class,callback functions
- AVICap callback functions,about
- WM_CAP_SET_CALLBACK_CAPCONTROL message
- WM_CAP_SET_CALLBACK_ERROR message
- WM_CAP_SET_CALLBACK_FRAME message
- WM_CAP_SET_CALLBACK_STATUS message
- WM_CAP_SET_CALLBACK_VIDEOSTREAM message
- WM_CAP_SET_CALLBACK_WAVESTREAM message
- WM_CAP_SET_CALLBACK_YIELD message
- capSetCallbackOnCapControl macro
- capSetCallbackOnErrormacro
- capSetCallbackOnFrame macro
- capSetCallbackOnStatus macro
- capSetCallbackOnVideoStream macro
- capSetCallbackOnWaveStream macro
- capSetCallbackOnYield macro
ms.topic: article
ms.date: 05/31/2018
---

# AVICap Callback Functions

Your application can register callback functions with a capture window to have it notify your application when the status changes, when errors occur, when video frame and audio buffers become available, and to yield during streaming capture. The following messages set the callback function.



| Message                                                                        | Description                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_CAP\_SET\_CALLBACK\_CAPCONTROL**](wm-cap-set-callback-capcontrol.md)   | Specifies the callback function in the application called to give precise control over capture start and end. You can also use the [**capSetCallbackOnCapControl**](/windows/desktop/api/Vfw/nf-vfw-capsetcallbackoncapcontrol) macro to send this message.                   |
| [**WM\_CAP\_SET\_CALLBACK\_ERROR**](wm-cap-set-callback-error.md)             | Specifies the callback function in the application called when an error occurs. You can also use the [**capSetCallbackOnError**](/windows/desktop/api/Vfw/nf-vfw-capsetcallbackonerror) macro to send this message.                                                           |
| [**WM\_CAP\_SET\_CALLBACK\_FRAME**](wm-cap-set-callback-frame.md)             | Specifies the callback function in the application called when preview frames are captured. You can also use the [**capSetCallbackOnFrame**](/windows/desktop/api/Vfw/nf-vfw-capsetcallbackonframe) macro to send this message.                                               |
| [**WM\_CAP\_SET\_CALLBACK\_STATUS**](wm-cap-set-callback-status.md)           | Specifies the callback function in the application called when the status changes. You can also use the [**capSetCallbackOnStatus**](/windows/desktop/api/Vfw/nf-vfw-capsetcallbackonstatus) macro to send this message.                                                      |
| [**WM\_CAP\_SET\_CALLBACK\_VIDEOSTREAM**](wm-cap-set-callback-videostream.md) | Specifies the callback function in the application called during streaming capture when a new video buffer becomes available. You can also use the [**capSetCallbackOnVideoStream**](/windows/desktop/api/Vfw/nf-vfw-capsetcallbackonvideostream) macro to send this message. |
| [**WM\_CAP\_SET\_CALLBACK\_WAVESTREAM**](wm-cap-set-callback-wavestream.md)   | Specifies the callback function in the application called during streaming capture when a new audio buffer becomes available. You can also use the [**capSetCallbackOnWaveStream**](/windows/desktop/api/Vfw/nf-vfw-capsetcallbackonwavestream) macro to send this message.   |
| [**WM\_CAP\_SET\_CALLBACK\_YIELD**](wm-cap-set-callback-yield.md)             | Specifies the callback function in the application called when yielding during streaming capture. You can also use the [**capSetCallbackOnYield**](/windows/desktop/api/Vfw/nf-vfw-capsetcallbackonyield) macro to send this message.                                         |



 

The following topics describe the different callback functions, the notifications sent to the functions, and their uses.

 

 




