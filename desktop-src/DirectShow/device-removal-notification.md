---
description: Device Removal Notification
ms.assetid: 0b96231a-f990-4c1c-8d00-cafeb3985ab3
title: Device Removal Notification
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Device Removal Notification

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

If the user removes a Plug and Play device that the graph was using, the filter graph manager posts an [**EC\_DEVICE\_LOST**](ec-device-lost.md) event. If the device becomes available again, the filter graph manager posts another **EC\_DEVICE\_LOST** event. However, the previous state of the capture filter is no longer valid. The application must rebuild the graph to use the device.

DirectShow does not send any event when a new device is plugged in. To learn when a new device is available, the application can monitor WM\_DEVICECHANGE window messages. For more information, see "Device Management" in the Platform SDK documentation.

## Related topics

<dl> <dt>

[Event Notification in DirectShow](event-notification-in-directshow.md)
</dt> </dl>

 

 



