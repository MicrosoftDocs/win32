---
description: An application can opt out of the Default Ducking Experience handled by the system and replace it with a custom implementation.
ms.assetid: 18290d05-b114-476b-8365-6bbb5fe6cffc
title: Providing a Custom Ducking Behavior
ms.topic: article
ms.date: 05/31/2018
---

# Providing a Custom Ducking Behavior

An application can opt out of the [Default Ducking Experience](stream-attenuation.md) handled by the system and replace it with a custom implementation.

An application can provide a custom ducking experience. For example, Windows Media Player provides its own ducking experience by pausing the current media stream during a communication session and resuming playback when the session is closed. A sample media application that implements ducking is included with Windows SDK samples; for more information, see [DuckingMediaPlayer](duckingmediaplayer.md). To simulate the experience of opening and closing communication streams, and generating ducking events, see [DuckingCaptureSample](duckingcapturesample.md), which is also included with Windows SDK samples.

A media application that plays sounds to be attenuated must be aware of the communication streams, when they are opened and closed in the system. The custom implementation can be provided by using MediaFoundation, DirectShow, or DirectSound, which use the Core Audio APIs. A direct WASAPI client can also override the default handling if it knows when the communication session starts and ends.

**To provide a custom ducking experience, a WASAPI client must perform the following tasks:**

1.  Register to receive ducking events from the *ducking manager*—a component of the audio system that handles notifications related to communication stream changes. For more information, [Getting Ducking Events](handling-audio-ducking-events-from-communication-devices.md).
    > [!Note]  
    > If the client is gets registered to receive ducking notifications, the ducking manager disables the default behavior provided by the system. If the default behavior is disabled explictly (see [Disabling the Default Ducking Experience](disabling-the-ducking-experience.md)) and the client does not provide a substitute behavior, the application does not experience any ducking behavior.

     

2.  Listen for the duck event notifications sent by the ducking manager and perform the desired ducking behavior. For more information about implementing a ducking behavior, see [Implementation Considerations for Ducking Notifications](handling-audio-ducking-events-from-communication-devices.md).

## Related topics

<dl> <dt>

[Using a Communication Device](using-the-communication-device.md)
</dt> <dt>

[Default Ducking Experience](stream-attenuation.md)
</dt> <dt>

[Disabling the Default Ducking Experience](disabling-the-ducking-experience.md)
</dt> <dt>

[Implementation Considerations for Ducking Notifications](handling-audio-ducking-events-from-communication-devices.md)
</dt> <dt>

[Getting Ducking Events](getting-ducking-events-from-a-communication-device.md)
</dt> </dl>

 

 



