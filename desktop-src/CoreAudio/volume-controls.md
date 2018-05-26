---
Description: Volume Controls
ms.assetid: 3b1adef5-40e9-4527-aa79-5a71f201fdfc
title: Volume Controls
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Volume Controls

Clients that manage shared-mode streams typically use the [**ISimpleAudioVolume**](/windows/win32/Audioclient/nn-audioclient-isimpleaudiovolume?branch=master) and [**IAudioSessionEvents**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessionevents?branch=master) interfaces in [WASAPI](wasapi.md) to control and monitor the stream volume levels. Through the methods in the **ISimpleAudioVolume** interface, the client can get and set the volume levels of the [audio sessions](audio-sessions.md) that the shared-mode streams belong to. If Sndvol or another application changes the session volume level, the client can receive notification of the change through the **IAudioSessionEvents** interface.

Clients that manage exclusive-mode streams typically use the [**IAudioEndpointVolume**](/windows/win32/Endpointvolume/nn-endpointvolume-iaudioendpointvolume?branch=master) and [**IAudioEndpointVolumeCallback**](/windows/win32/Endpointvolume/nn-endpointvolume-iaudioendpointvolumecallback?branch=master) interfaces in the [EndpointVolume API](endpointvolume-api.md) to control and monitor the stream volume levels. Through the methods in the **IAudioEndpointVolume** interface, the client can get and set the volume level of an [audio endpoint device](audio-endpoint-devices.md). If Sndvol or another application changes the volume level of the endpoint device, the client can receive notification of the change through the **IAudioEndpointVolumeCallback** interface.

As explained in [Audio Sessions](audio-sessions.md), Sndvol is the system volume-control program. It displays volume controls for the audio-rendering endpoint devices in the system. (Currently, it does not display the volume controls for audio-capture endpoint devices.) To view the volume controls for a particular device, click **Device** in the menu bar and select a device name from the list of available devices.

The Sndvol window separates the volume controls for a device into two groups. The group box on the left side of the window is labeled **Device**. The **Device** box contains a single volume control that is controlled by the [**IAudioEndpointVolume**](/windows/win32/Endpointvolume/nn-endpointvolume-iaudioendpointvolume?branch=master) interface. Changes that the user makes to this volume control can be monitored through the [**IAudioEndpointVolumeCallback**](/windows/win32/Endpointvolume/nn-endpointvolume-iaudioendpointvolumecallback?branch=master) interface.

The group box on the right side of the Sndvol window is labeled **Applications**. The **Applications** box contains the volume controls for the applications that currently share the device. For applications that use the device in shared mode, the volume controls represent the volume levels that are controlled by the [**ISimpleAudioVolume**](/windows/win32/Audioclient/nn-audioclient-isimpleaudiovolume?branch=master) interface. Changes that the user makes to these volume controls can be monitored through the [**IAudioSessionEvents**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessionevents?branch=master) interface.

Although a shared-mode application can use its [**IAudioSessionEvents**](/windows/win32/Audiopolicy/nn-audiopolicy-iaudiosessionevents?branch=master) interface to monitor changes that the user makes to the application's volume control in the **Applications** box in the Sndvol window, the application cannot monitor changes to the volume controls of other, unrelated applications. Similarly, an application can change the volume levels of its audio sessions through the [**ISimpleAudioVolume**](/windows/win32/Audioclient/nn-audioclient-isimpleaudiovolume?branch=master) interface, but it cannot change the volume levels of sessions that belong to other, unrelated applications.

However, two or more related applications (or instances of the same application) can share the same volume control in the **Applications** box in the Sndvol window either by assigning their audio streams to the same cross-process session or by associating their respective sessions with the same grouping parameter. For more information, see [Audio Sessions](audio-sessions.md) and [Grouping Parameters](grouping-parameters.md).

WASAPI provides two additional interfaces, [**IChannelAudioVolume**](/windows/win32/Audioclient/nn-audioclient-ichannelaudiovolume?branch=master) and [**IAudioStreamVolume**](/windows/win32/Audioclient/nn-audioclient-iaudiostreamvolume?branch=master), to control the volume levels of shared-mode streams. These interfaces are mainly used by specialized clients that require control over the volume levels of either individual channels in a session or individual streams in a session.

The [DeviceTopology API](devicetopology-api.md) enables clients to access the volume controls in the topologies of audio adapters. However, clients that manage exclusive-mode streams typically use the EndpointVolume API instead of the DeviceTopology API to control the stream volume levels. The EndpointVolume API simplifies control of the volume of an endpoint device in two ways. First, if an endpoint device implements a hardware volume control, the DeviceTopology API requires the client to traverse the device topology in search of the hardware control. In contrast, the EndpointVolume API automatically finds the hardware volume control for the client. Second, if the endpoint device does not implement a hardware volume control, a DeviceTopology client must implement a volume control in software. In contrast, the EndpointVolume API automatically substitutes a software volume control for the missing hardware control.

The following sections describe volume controls for audio sessions and for audio endpoint devices:

-   [Session Volume Controls](session-volume-controls.md)
-   [Endpoint Volume Controls](endpoint-volume-controls.md)
-   [EndpointVolume API](endpointvolume-api.md)
-   [Audio-Tapered Volume Controls](audio-tapered-volume-controls.md)
-   [Peak Meters](peak-meters.md)

## Related topics

<dl> <dt>

[Programming Guide](programming-guide.md)
</dt> </dl>

 

 



